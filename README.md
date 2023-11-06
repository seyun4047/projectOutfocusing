나의 취미는 사진 촬영이다.

어느날 문득 이런 생각을 갖게된다.

아웃포커싱 내가 프로그래밍으로 구현 가능할지도?

하지만 내가 할 줄 아는건 파이썬 깔짝, openCV깔짝, 코딩 깔짝...

일단 하자.

--------------------------------------------------------

**1. 아웃포커싱이란?**
--------------

https://namu.wiki/w/아웃포커싱

즉, 배경(전경)을 흐리고 피사체를 강조하는 촬영 기법을 말함.

**2. needs**

아웃포커싱 + 원본JPEG보다 적은 용량의 파일

**3. HOW?**

--------------------------------------------------------

**아웃포커싱 예시**
-----------
<img width="1295" alt="needs" src="https://github.com/seyun4047/projectOutfocusing/assets/73819780/152d1343-0a56-4521-94eb-957719b1ded7">


--------------------------------------------------------
**CHAPTER 1**
---------
OpenCV를 이용한 간단 제작

구현 방법 :

1. 피사체-관심영역 설정
2. 
-> 바이너리화 후 배경과 피사체 분리
   
3. 배경 다운스케일
   
4. 구분된 영역 정리(sanding)

OpenCV를 이용한 간단 제작

--------------------------------------------------------
**CHAPTER 2**
-------------

선택영역의 색상의 Edge 변화로 피사체의 심도를 확인하고, 피사체만 마스킹하기

-> 단일 이미지 심도 파악 알고리즘 부재로 인한 미해결

--------------------------------------------------------
**CHAPTER 3**
-------------

자유도를 가진 선택영역 설정 후, 그 선택영역 제외부분 블러처리

->마우스왼쪽클릭 : 영역마스킹처리

->마우스오른쪽클릭 : 영역마스킹해제처리

--------------------------------------------------------
**CHAPTER 4**
-------------

fill ver1 매커니즘 구현

toggle Btn :
'q' = quit,

'f' = fill on,

'g' = fill off,

-> 추후 threshold 함수와 연계하여 피사체 자동 분석가능하도록 연계예정

-> 한계 : ty(topY), dy(downY) 탐색 알고리즘의 부정확성으로 인한 fill 끊김 발생

--------------------------------------------------------
**CHAPTER 4-1**
-------------

fill ver2 매커니즘 구현

-> Chapter 4의 fill 끊김 현상을 BFS 알고리즘을 통해 극복

-> 한계 : 너무 느림
