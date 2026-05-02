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
- 설정 같은건 _config.yml 파일 수정
- 블로그 글은 _pages/ 폴더 안에 탬플릿 써놓은거 갖고 갖다쓰기