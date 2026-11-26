"""문서 전용 변경은 CI·이미지 게시·자동 배포에서 제외한다."""
import argparse
import json
import logging
import os
from pathlib import Path, PurePosixPath
import subprocess

CONFIG = '.github/ci-docs.json'
EXTENSIONS = {'.md', '.txt', '.rst', '.adoc'}


def git(root, *args):
    return subprocess.check_output(['git', *args], cwd=root, stderr=subprocess.PIPE, timeout=60)


def required(root, base, head='HEAD'):
    try:
        if not base or set(base) == {'0'}:
            return True
        config = json.loads(git(root, 'show', f'{head}:{CONFIG}'))
        # --no-renames는 문서→코드 이동의 양쪽 경로를 모두 검사한다.
        paths = git(root, 'diff', '--name-only', '--no-renames', '-z', base, head).split(b'\0')
        paths = [os.fsdecode(p) for p in paths if p]
        if not paths:
            return True
        for name in paths:
            path = PurePosixPath(name)
            if (path.suffix.lower() not in EXTENSIONS or
                    not (name in config['files'] or any(name.startswith(d) for d in config['directories']))):
                return True
        for commit in (base, head):
            for entry in git(root, 'ls-tree', '-rz', commit).split(b'\0'):
                if entry and os.fsdecode(entry.split(b'\t', 1)[1]) in paths:
                    if not entry.startswith(b'100644 blob '):
                        return True
        return False
    except (subprocess.SubprocessError, OSError, ValueError, KeyError, TypeError):
        logging.warning('변경 범위를 확인할 수 없어 전체 CI를 실행합니다.')
        return True


def local_required(root):
    try:
        if git(root, 'status', '--porcelain').strip():
            return True
        head = git(root, 'rev-parse', 'HEAD').strip()
        main = git(root, 'rev-parse', 'refs/remotes/origin/main').strip()
        base = 'HEAD^' if head == main else git(root, 'merge-base', 'HEAD', 'refs/remotes/origin/main').decode().strip()
        return required(root, base)
    except (subprocess.SubprocessError, OSError):
        logging.warning('로컬 기준 커밋을 확인할 수 없어 전체 CI를 실행합니다.')
        return True


def github_required(root, event_name, event, head):
    if event_name == 'pull_request':
        return required(root, event['pull_request']['base']['sha'], head)
    if event_name == 'push':
        return required(root, event.get('before'), head)
    # 수동 실행과 정기 보안 검사는 명시적인 실행 요청이다.
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--github', action='store_true')
    parser.add_argument('--base')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    if args.github:
        try:
            value = github_required(root, os.environ['GITHUB_EVENT_NAME'],
                                    json.loads(Path(os.environ['GITHUB_EVENT_PATH']).read_text()),
                                    os.environ['GITHUB_SHA'])
        except (OSError, ValueError, KeyError, TypeError):
            logging.warning('이벤트를 확인할 수 없어 전체 CI를 실행합니다.')
            value = True
        with open(os.environ['GITHUB_OUTPUT'], 'a') as output:
            output.write(f'required={str(value).lower()}\n')
    else:
        value = required(root, args.base) if args.base else local_required(root)
    print(str(value).lower())


if __name__ == '__main__':
    main()
