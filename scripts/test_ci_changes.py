import json
import shutil
from pathlib import Path
import subprocess
import tempfile
import unittest
import ci_changes as ci


class ChangesTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.git('init', '-q', '-b', 'main')
        self.git('config', 'user.name', 'CI')
        self.git('config', 'user.email', 'ci@example.test')
        self.write(ci.CONFIG, json.dumps({'files': ['README.md', 'NOTES.txt'], 'directories': ['docs/']}))
        self.write('README.md', 'old')
        self.write('app.py', 'old')
        self.commit()
        self.base = self.git('rev-parse', 'HEAD').strip()
        self.git('update-ref', 'refs/remotes/origin/main', self.base)

    def git(self, *args):
        return ci.git(self.root, *args).decode()

    def write(self, name, text):
        target = self.root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text)

    def commit(self):
        self.git('add', '.')
        self.git('commit', '-qm', 'test')

    def test_docs_skip_local_pr_and_push(self):
        self.write('README.md', 'new')
        self.write('docs/note with space.txt', 'note')
        self.commit()
        self.assertFalse(ci.local_required(self.root))
        self.assertFalse(ci.github_required(self.root, 'push', {'before': self.base}, 'HEAD'))
        self.assertFalse(ci.github_required(self.root, 'pull_request', {'pull_request': {'base': {'sha': self.base}}}, 'HEAD'))

    def test_runtime_text_and_unknown_paths_require_ci(self):
        for name in ['requirements.txt', 'robots.txt', 'public-content/privacy.md', '_posts/post.md', 'content/page.md', 'docs/check.py', '.github/ci-docs.json']:
            with self.subTest(name=name):
                self.git('reset', '--hard', self.base)
                self.git('clean', '-fd')
                self.write(name, 'changed')
                self.commit()
                self.assertTrue(ci.required(self.root, self.base))

    def test_mixed_and_multiple_commits_require_ci(self):
        self.write('app.py', 'code')
        self.commit()
        self.write('README.md', 'new')
        self.commit()
        self.assertTrue(ci.local_required(self.root))
        self.assertTrue(ci.required(self.root, self.base))

    def test_rename_delete_permissions_and_symlink(self):
        (self.root / 'docs').mkdir()
        self.git('mv', 'app.py', 'docs/old.txt')
        self.commit()
        self.assertTrue(ci.required(self.root, self.base))
        self.git('reset', '--hard', self.base)
        self.git('rm', 'README.md')
        self.commit()
        self.assertFalse(ci.required(self.root, self.base))
        self.git('reset', '--hard', self.base)
        (self.root / 'README.md').chmod(0o755)
        self.commit()
        self.assertTrue(ci.required(self.root, self.base))
        self.git('reset', '--hard', self.base)
        (self.root / 'README.md').unlink()
        (self.root / 'README.md').symlink_to('app.py')
        self.commit()
        self.assertTrue(ci.required(self.root, self.base))

    def test_unknown_base_empty_dirty_and_manual_require_ci(self):
        self.assertTrue(ci.required(self.root, 'missing'))
        self.assertTrue(ci.required(self.root, '0' * 40))
        self.assertTrue(ci.required(self.root, self.base))
        self.write('README.md', 'dirty')
        self.assertTrue(ci.local_required(self.root))
        self.assertTrue(ci.github_required(self.root, 'workflow_dispatch', {}, 'HEAD'))
        self.assertTrue(ci.github_required(self.root, 'schedule', {}, 'HEAD'))

    def test_shell_skips_runner_only_for_docs(self):
        source = Path(__file__).resolve().parents[1]
        if not (source / 'scripts/ci.sh').exists():
            return
        self.write('.gitignore', 'build/\n')
        self.write('scripts/local_ci.py', "from pathlib import Path;Path(__file__).with_name('called').write_text('yes')\n")
        self.write('scripts/test_ci_changes.py', '')
        shutil.copyfile(source / 'scripts/ci.sh', self.root / 'scripts/ci.sh')
        shutil.copyfile(source / 'scripts/ci_changes.py', self.root / 'scripts/ci_changes.py')
        self.commit()
        self.git('update-ref', 'refs/remotes/origin/main', 'HEAD')
        self.write('README.md', 'new')
        self.commit()
        subprocess.run(['bash', 'scripts/ci.sh', 'run', '--publish'], cwd=self.root, check=True, capture_output=True)
        self.assertFalse((self.root / 'scripts/called').exists())
        self.write('app.py', 'code')
        self.commit()
        subprocess.run(['bash', 'scripts/ci.sh', 'run', '--publish'], cwd=self.root, check=True, capture_output=True)
        self.assertTrue((self.root / 'scripts/called').exists())

    def test_main_compares_previous_commit_and_missing_origin_fails_closed(self):
        self.write('README.md', 'new')
        self.commit()
        self.git('update-ref', 'refs/remotes/origin/main', 'HEAD')
        self.assertFalse(ci.local_required(self.root))
        self.git('update-ref', '-d', 'refs/remotes/origin/main')
        self.assertTrue(ci.local_required(self.root))


if __name__ == '__main__':
    unittest.main()
