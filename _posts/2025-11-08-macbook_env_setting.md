---
layout: post
title: 맥북 환경 설정
date: 2025-11-08 20:30:00+0900
description:
tags: 정보
categories: Development
---

## 맥북을 초기화하고 처음부터 설정해 보자.

<br />
22년도 봄에 사서 계속 쓰던 M1 맥북이 있는데 군대 갔다 오니까 어떻게 썼는지 기억도 안난다.  

그런 김에 다음에 기변할 때 도움도 받을 겸 초기 세팅을 어떻게 하는지 기록해 두려고 한다.  

<br />


우선 깨끗히 초기화 된 맥북을 준비한다.  
초기화는 [여기](https://19-97.tistory.com/142)를 참고했다.


<br />
<br />


먼저 화면 하단의 Dock을 싹다 날려줬다.  
나는 애초에 Windows를 써도 작업 표시줄에 딱 크롬만 남기고 다 날리는 스타일이고, 특히 맥은 단축키로 Spotlight 검색이 가능하기 때문에 필요를 못 느껴 다 지우고 있다.  
그리고 웬만해선 안쓰는 앱들도 다 지우는데 맥북의 기본 앱들을 지우기에는 골아픈 경우가 생기기 때문에 그냥 두겠다.  
<s>체스는 진자 지우고 싶은데....</s>
{% include figure.liquid loading="eager" path="assets/img/blog/2511/13.png" class="img-fluid rounded z-depth-1" %}

<br />

가장 먼저 Rosseta2를 설치해 주겠다.  
로제타는 애플 실리콘에서 인텔 프로세서의 프로그램을 원활하게 실행하게 해 준다.  
아래 명령어로 설치할 수 있다.  
```bash
/usr/sbin/softwareupdate --install-rosetta --agree-to-license
```


<br />

그 다음은 Homebrew를 설치해 주겠다.  
Homebrew는 Mac용 패키지 관리자로, 여러가지 프로그램을 터미널에서 설치·관리할 수 있게 하는 프로그램이다.  
[Homebrew 홈페이지](brew.sh)에 접속해 설치 명령어를 터미널에 그대로 복사 붙여넣기 하면 설치가 진행된다.  
설치를 진행하고 난 이후에는 <span class="text-info"> ==> Next Steps:</span>로 몇 개의 명령어를 치라고 나오는데, 그대로 복붙해서 입력하면 PATH에 brew 명령어가 추가된다.  

<br />

Homebrew에는 주요 설치 방법으로 Formulae와 Cask가 있다.  
간단히 말해서 Formulae는 CLI(Command Line Interface) 애플리케이션, Cask는 GUI(Graphical User Interface) 애플리케이션을 설치하기 위한 방법이라 보면 되고,  
Formulae는 소스 코드를 다운로드하여 컴파일 후 설치하는 방식이고, Cask는 애플리케이션의 바이너리를 다운로드하여 설치하는 방식으로 조금의 차이가 있으나,  
결론적으로 CLI 환경에서 앱을 설치하고 관리하는 도구라 보면 되겠다.  

무튼 brew를 이용하여 'Visual Studio Code', 'Google Chrome', 'Iterm2' 등의 앱을 설치할 것이다.  
```bash
brew install --cask visual-studio-code google-chrome iterm2 tiles 
```

<br />

특히 Iterm2가 설치된 이후에는 기본으로 들어있는 Terminal 대신 Iterm2를 사용할 것이다.  
먼저 Iterm의 몇 가지 설정을 만져주자.  
- iterm > Settings > appearance > theme=minimal
- Iterm > Settings > Profiles > sessions > status bar enabled, configure에서 배터리, cpu, 메모리, 네트워크, 색깔
- [Iterm2colorschemes.com](http://iterm2colorschemes.com/)에서 Github Dark파일 다운로드, 확장자(txt) 지우고 파일 열면 iterm으로 열림, Iterm > Settings > profiles > colors > color palets에서 GithubDark 선택
- Oh my zsh 설치 : [Oh my zsh](ohmyz.sh)에서 설치 커맨드 복붙
- [Powerlevel10k](https://github.com/romkatv/powerlevel10k?tab=readme-ov-file#oh-my-zsh)의 설치 커맨드 복붙
- 위 링크의 2번 항목에 따라 `~/.zshrc`를 열고 수정한 후, Iterm2를 종료했다 다시 시작하면 powerlevel10k설치 뜨는데 폰트 설치하고 아이콘 보이는지 테스트 하고 스타일 설정하면 된다.  

<br />

슬슬 Iterm도 설정 다 됐으니까 이제 쓸만한 앱들 설치하면 된다.  
나는 주로 많이 쓰는 앱들을 설치할 수 있게 아래 명령어로 정리해 뒀다.  


```bash
brew install python3 go nvm gh docker docker-compose miniconda
brew install --cask docker postman scroll-reverser miniconda notion slack zoom discord
```

이후에 nvm 설치할때 뜨는 export NVM_DIR뭐시기부터 커맨드 좀 복사해서 code ~/.zshrc열고 밑에 붙여넣고 저장, 터미널 재시작 하면 nvm 커맨드가 설정된다.  
터미널에서 nvm ls-remote -> 리스트 뜨는거에서 최신 버전 설치(nvm install 24.11.0 등)해서 최신 버전을 설치해 준다.  
gh auth login해서 github로그인도 진행해 준다.  
이후에 Docker 애플리케이션을 한번 실행해서 이것저것 수락 해 주면서 한번 실행 해 줘야 한다.  
```bash
docker info
docker run hello-world
```
등의 명령어로 Docker가 잘 돌아가고 있는지 확인할 수 있다.  

<br />

이 다음에는 VSCode 설정을 진행한다.  
- extestions : C/C++ python3 go Korean language materialIconTheme preiiter Jupyter comunityMeterialTheme 등 필요한거 다 설치한다.
- Setting > (Terminal > Integrated: Font Family) 에다가 MesloLGS NF 저장해 글꼴을 설정한다.  
- 또 [링크](https://code.visualstudio.com/docs/cpp/config-clang-mac)에서 C나 C++ 코드의 빌드 및 디버깅을 위한 환경을 설정하기 위해 샘플 환경을 하나 구축해 두겠다.  


<br />

이외에도 앱스토어에서 카카오톡, Runcat, Hidden Bar, Goodnotes, Excel, Word, Powerpoint를 설치하고 설정하고,
[반디집X](https://kr.bandisoft.com/bandizip/x/), [LogiOptions+](https://www.logitech.com/ko-kr/software/logi-options-plus.html) 를 인터넷에서 설치하고 설정해 준다.


<br />


일단 이정도로 마무리 하겠다.  
뭔가 새로운게 생기면 이 페이지를 수정할 예정이다.  
Last Modified : 2025.11.08

<br />
<br />


## 마치며...
M1 맥북의 개발 환경을 세팅해 보았다.  
