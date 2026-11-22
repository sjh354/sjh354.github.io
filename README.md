# Homepage

- Theme : Jekyll - al-folio
- Github Pages로 배포중
- Github action 여러개 돌아가는데 뭐 버전 이미 닫힌것도있고 그렇긴 한데 걍 쓰자

## 로컬에 설치 및 실행

```bash
brew install rbenv ruby-build

echo 'eval "$(rbenv init - zsh)"' >> ~/.zshrc
source ~/.zshrc

rbenv install 3.3.0
rbenv global 3.3.0

ruby -v

gem install jekyll bundler

bundle install

bundle exec jekyll serve
```

## 사용법

- 설정 같은건 \_config.yml 파일 수정
- 블로그 글은 \_pages/ 폴더 안에 탬플릿 써놓은거 갖고 갖다쓰기

## 문서만 변경한 경우의 CI

문서 전용 변경은 `.github/ci-docs.json`에 지정한 안내 파일과 문서 디렉터리의
`.md`, `.txt`, `.rst`, `.adoc` 파일만 바뀐 경우입니다. `scripts/ci_changes.py`가
변경 범위를 먼저 확인하며, 문서만 바뀌면 로컬 CI·이미지 게시·자동 배포를 생략합니다.
GitHub에서는 가벼운 변경 분류만 실행합니다. 코드와 섞인 변경, 실행 권한·심볼릭 링크 변경,
기준 커밋을 확인할 수 없는 변경은 전체 CI를 실행합니다. 정책 게시 원고·블로그 글·
`requirements.txt`·`robots.txt` 등 실행·게시 입력은 문서 제외 목록에 넣지 않습니다.
수동 workflow 실행과 정기 보안 검사는 그대로 실행합니다.
