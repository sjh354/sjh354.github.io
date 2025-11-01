---
layout: post
title: 블로그 도메인을 바꿔보자!
date: 2024-02-09 23:59:59+0900
description: 블로그 도메인을 바꿔보자!
tags: 정보 삽질 문제해결
categories: Development
---

## 1. 서론
지금 블로그를 sjh354.github.io에서 깃허브 페이지로 호스팅 하고 있었다. 근데 약간 기분 나빠서 그냥 하고 싶어서 미리 사놨던 caffeineoverdose.life 도메인에서 서브도메인 하나 파서 호스팅 하려고 한다. <br> 

## 2. 본론
지금 호스팅케이알에서 caffeineoverdose.life 도메인을 사놨다. 
지금 깃헙 페이지에서 호스팅하고 있는 지킬 블로그를 blog.caffeineoverdose.life에서 호스팅 해보자.

1. 호스팅케이알에서 DNS레코드 관리 - 새 레코드 추가 에서 A레코드 4개랑 CNAME레코드 1개를 추가한다.
A 레코드에는 이름은 서브도메인 이름으로(나는 *blog*)으로 했고 값 란에는 아래의 4 개의 IPv4를 추가한다
> 185.199.108.153 / 185.199.109.153 / 185.199.110.153 / 185.199.111.153 

CNAME 레코드에는 www.blog를 이름으로 넣고 값 란에는 <username>.github.io(나의 경우 sjh354.github.io)로 추가해 주었다.

{% include figure.liquid loading="eager" path="assets/img/blog/2402/2.png" class="img-fluid rounded z-depth-1" %}

{% include figure.liquid loading="eager" path="assets/img/blog/2402/3.png" class="img-fluid rounded z-depth-1" %}

2. github에서 호스팅 중인 레포지토리로 들어와서 Settings - Pages 에서 Custom Domain란의 주소에 내 블로그의 새 주소를 넣어주었다.(나의 경우 blog.caffeineoverdose.life)

3. 그럼 끗~~~~~~~!!
결과는 요로케 뜬다

{% include figure.liquid loading="eager" path="assets/img/blog/2402/4.png" class="img-fluid rounded z-depth-1" %}

## 3. 결론
블로그는 사 드세요..제발 <br>
농담이고 아주 맘에 든다.<br>
(대충 네이버 블로그 킹받는 이모티콘)
