---
layout: post
title: 티케팅 환경에서 서버시간에 딱 맞게 새로고침하는 방법
date: 2025-11-17 20:30:00+0900
description:
tags: 정보
categories: Development
---

## 티케팅을 해보자

<br />
최근들어 티켓팅이 더더 힘들어지고 있는 것 같다.  

이것저것 프로그램을 써보는 것도 좋지만 가볍게 해결해 보자.

<br />

```javascript

function getTime() {
  console.log(Date.now());

  var xmlHttp;
  var ServerTime =
    "https://www.musinsa.com/campaign/mujinjangsale/special#limited";
  xmlHttp = new XMLHttpRequest();

  //XML 전송 INIT
  xmlHttp.open("HEAD", ServerTime, false);
  xmlHttp.setRequestHeader("ContentType", "text/html");
  xmlHttp.send("");

  //XML형식으로 서버의 시간을 가져옵니다
  var serverDate = xmlHttp.getResponseHeader("Date");
  var date = new Date(serverDate);

  // UTC 시간 계산
  var utc = date.getTime() + date.getTimezoneOffset() * 60 * 1000;
  console.log(utc);

  // UTC to KST (UTC + 9시간)
  // var KR_TIME = 9 * 60 * 60 * 1000;
  // var now = new Date(utc + KR_TIME);
  console.log(Date.now());

  alert(now);
}
getTime();

const pivot = new Date(2025, 10, 17, 19, 23, 30, 0);
setInterval(() => {
  if (Date.now() > pivot) location.reload();
}, 0.01);

```

일단 이정도로 해당 서버 시간을 가져오고 어쩌고 저쩌고 할 수 있겠다.

내일 이어서 써야징


<br />

