---
layout: post
title: 블로그 도메인 바꾸기
date: 2025-11-08 15:30:00+0900
description:
tags: 정보
categories: Development
---

## 블로그의 도메인을 바꿔보고자 한다.

<br />

지금은 깃허브 pages에서 이 페이지를 호스팅 하고 있다.  
근데 좀 뽀대(?)가 안나니까 마침 또 싸게 팔고있는 도메인 하나를 사서 여기다 달아볼까 한다.  

<br />

먼저 [호스팅케이알](https://www.hosting.kr/)에서 할인하고 있는 도메인 하나를 구매했다.

<br />

도메인은 일반적으로 'www.example.com'과 같이 .(점)으로 구분된 여러 부분으로 구분되는데,   
그 중에서도 마지막 부분을 '최상위 도메인(TLD, Top-Level Domain)'이라 하고 .com, .co.kr 등이 있다.  
그 바로 앞은 '2단계 도메인(SLD, Second-Level Domain)' 이라 하며 위의 예에서 example 부분이 해당한다.  

<br />

내가 갖고 싶은 도메인 주소(특히 SLD)를 검색해서 다른 주인이 없으면 살 수 있다.  
같은 SLD를 갖더라도 여러 가지의 TLD를 붙일 수 있는데, 이 것들의 수요에 따라 가격이 다 다르다.


<br />

예를 들어 내가 쓰고 있는 SLD인 'sjh354'를 검색했을 때 아래와 같이 주인이 있는(내가 샀다 저건) 도메인을 제외하고는 구매할 수 있다.
{% include figure.liquid loading="eager" path="assets/img/blog/2511/7.jpg" class="img-fluid rounded z-depth-1" %}
<div class="caption">
    호스팅케이알에서 'sjh354'로 검색했을 때
</div>


반면 'google'을 검색하면 아래와 같이 주인이 있다고 나온다.  
저런건 요즘 사기꾼들이 원체 많아 기업에서 싹쓸이 한 것으로 보인다.  
{% include figure.liquid loading="eager" path="assets/img/blog/2511/8.jpg" class="img-fluid rounded z-depth-1" %}
<div class="caption">
    호스팅케이알에서 'google'로 검색했을 때
</div>

<br />


무튼 도메인을 샀으면 이걸 내 페이지를 서비스 하고 있는 깃허브 페이지에 연결하면 된다.  


<br />

그 전에 이 도메인을 통째로 연결할 건지 서브 도메인을 사용할 것인지 결정해야 한다.  
루트 도메인을 사용할 거라면 바로 'sjh354.xyz'가 연결 될 것이고,   
서브 도메인을 사용할 거라면 앞에 경로를 추가로 붙여서 예를 들어 'blog.sjh354.xyz'와 같이 연결할 수 있다.  
나는 루트 도메인을 바로 연결할 것이다.  


<br />

먼저 GitHub Pages에서 방금 산 커스텀 도메인을 연결하자.  
내 페이지가 들어있는 레포지토리의 'Settings' 탭에 들어가면 'Pages'가 있는데 여기 들어가면 Custom domain이라고 세팅할 수 있는 란이 있다.  
여기에 연결할 도메인을 입력한다.  
그럼 아래와 같이 <span class="text-warning">DNS check unsuccessful</span>이라고 뜰 것인데 이제 도메인 등록 업체에서 DNS 레코드를 설정해 주면 된다.  
{% include figure.liquid loading="eager" path="assets/img/blog/2511/9.jpg" class="img-fluid rounded z-depth-1" %}

<br />


호스팅케이알의 [나의 도메인](https://app.hosting.kr/domains/portfolio/owned)에 들어가면 방금 산 도메인이 있다.  
내가 산 도메인에 들어가서 '네임서버/DNS' 설정의 'DNS 레코드 관리'를 살펴보자.  

<br />

먼저 A레코드를 추가할 건데 우리의 도메인을 Github Pages의 IP주소 4개에 각각 연결해 준다.  
GitHub Pages에 대한 IP 주소는 다음 4개이다. ([출처](https://docs.github.com/ko/enterprise-cloud@latest/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site))
```
> 185.199.108.153
> 185.199.109.153
> 185.199.110.153
> 185.199.111.153
```

추가로 CNAME 유형 레코드를 사용해 그냥  www 서브 도메인에 대해서 원래 깃허브에서 제공하는 주소로 연결한다.  

{% include figure.liquid loading="eager" path="assets/img/blog/2511/10.jpg" class="img-fluid rounded z-depth-1" %}


<br />

그런데 나는 이런 에러가 떴다.  
{% include figure.liquid loading="eager" path="assets/img/blog/2511/11.jpg" class="img-fluid rounded z-depth-1" %}
<div class="caption">
    Domain's DNS record could not be retrieved.
</div>


그런데 한 1시간 기다리니까 다음과 같이 <span class="text-primary">DNS check successful</span>를 받았다.

{% include figure.liquid loading="eager" path="assets/img/blog/2511/12.jpg" class="img-fluid rounded z-depth-1" %}

원래 DNS라는게 전 세계로 퍼질 때 까지 시간이 좀 걸리므로 마음 편히 먹고 좀 기다리면 된다.  
최대 48시간 정도까지도 걸린다고 하니 DNS 설정을 잘 했다면 느긋한 마음을 갖고 오래 기다려 보자.  

<br />


이후에 그 아래의 Enforce HTTPS를 켜주면 끝~~

<br />
<br />


## 마치며...
깃허브 블로그에 커스텀 도메인을 붙여 보았다.  
아무래도 가장 중요한 것은 느긋한 마음인 것 같다.