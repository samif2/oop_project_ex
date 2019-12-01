# 2019-2 객체지향 프로그래밍 프로젝트 - **{SAram}**
구성원: 2-1 이주호 | 2-3 이소이 | 2-3 이정수 

## 1. 주제
원하는 사람의 위치를 추측하는 프로그램

## 2. 동기
친구와 조별과제를 진행해야 할 때, 친구에게 할 이야기가 있을 때, 선생님이 친구를 찾을 때 등 학교에 있을 때 친구를 찾아야 할 경우는 생각보다 많다.
하지만 학교가 워낙 넓다보니 모든 강의실을 돌며 친구를 찾는 일은 몹시 비효율적이다. 또한, 우리 학교는 달빛학사 시스템을 통해 어느 정도 학생들의 움직임을 예측할 수 있다는 사실을 알게 되었다.
따라서 우리는 사용자가 현재 시각, 혹은 사람을 찾고자 하는 시가을 입력하고 찾고 싶은 사람에 대한 
정보 일부를 제공하면 그 사람의 위치를 추측하여 제시하는 프로그램을 만들어보기로 하였다.

## 3. 프로그램 사용 대상
교내 학생 및 교사의 위치를 알고자 하는 우리 학교 사람들

## 4. 목적
사람을 찾으러 돌아다니기에는 다소 넓은 세종과학예술영재학교에서 사람을 보다 효율적이고 쉽게 찾을 수 있도록 돕는다

## 5. 주요기능
  a. 다양한 입력
  
  사용자를 A, 사용자가 찾고자 하는 사람을 B라 하자.
  프로그램이 B의 위치를 추측하기 위해서는 B에 대한 몇가지 정보가 필요하다.
  이 때, 정보를 다양한 방향으로 받을 수 있도록 한다.
  예를 들어, B의 반 정보를 받을 때, A가 B의 반을 알지 못한다면, B의 담임선생님이나 같은 반 친구의 이름을 받을 수 있도록 한다.
  
  b. 위치 추측
  
  프로그램의 핵심기능이다. 
  A가 B를 찾기 위한 필수적인 정보(B의 이름 혹은 학번, 찾고자 하는 시각)를 입력하고
  B에 대해 알고있는 몇가지 정보만 더 제시한다면 B가 있을만한 장소, 즉 찾으러 가볼 장소를 추천받을 수 있다.
  
## 6. 프로젝트 핵심
프로그램은 달빛학사에 접속한 후, 미리 입력된 로그인 정보를 활용하여 달빛학사에 로그인하여
공강시간 검색 기능을 통해 찾고자 하는 시각에 B가 공강인지 여부를 따져 공강이라면 도서관과 공강실을 추천한다.
만약 5시 10분이 넘어간 시각이라면 기숙사를 추천한다.

만약 공강이 아니라면 ...

(i) 1학년일 경우
1학년은 반 단위로 움직이기 때문에 입력받은 정보를 토대로 (혹은 이름 정보를 통해), B가 몇반인지 알아낸 뒤, 그 반이 수업중인 강의실을 출력한다 

(ii) 2, 3학년일 경우 ...
시간표 검색을 통해 해당 시각에 열리는 수업에 대한 정보를 가져오고, 강의명을 통해 과목을 분리한다.
A가 입력한 정보 중에서 B의 전공과목, 혹은 B가 듣지 않을 만한 과목등을 활용해 B가 들을만한 강의를 추려내어 해당 강의의 강의실 위치를 출력해낸다.

만약 입력 시각이 쉬는시간이라면 앞, 뒤 시간에 대해 같은 방법으로 분석하여 2군데 이상의 강의실을 추천한다
만약 A가 제공한 정보가 너무 부족하다면 정보를 더 요구하고, 아는 정보가 없다면 "화이팅!!"을 출력한다

## 7. 구현에 필요한 라이브러리나 기술
웹크롤링과 웹파싱. beautifulsoup4, selenium 라이브러리를 이용하여 달빛학사에 접속하여 강의 정보를 얻는다.

## 8. **분업 계획**
웹 조작하는 함수/클래스 제작하기

새 창 열기 및 달빛학사 접속하여 자동 로그인 - 이정수

강의를 과목별로 분리 - 이소이

공강 검색 기능을 통한 공강 여부 확인 - 이주호
시간표 보기 창에서 시간표 긁어오기 - 이주호

>> 정보를 추려서 출력하기 - 위 사항이 모두 완료되면 함께

## 9. 기타
더 추가할 수 있는 기능이 있다면 추가할 예정이다

## 10. 프로그램 실행 방법
main.py 파일을 실행한다.

<hr>

#### readme 작성관련 참고하기 [바로가기](https://heropy.blog/2017/09/30/markdown/)

#### 예시 계획서 [[예시 1]](https://docs.google.com/document/d/1hcuGhTtmiTUxuBtr3O6ffrSMahKNhEj33woE02V-84U/edit?usp=sharing) | [[예시 2]](https://docs.google.com/document/d/1FmxTZvmrroOW4uZ34Xfyyk9ejrQNx6gtsB6k7zOvHYE/edit?usp=sharing) | [[예시 3]](https://github.com/goldmango328/2018-OOP-Python-Light) | [[예시4]](https://github.com/ssy05468/2018-OOP-Python-lightbulb) | [[모두보기]](https://github.com/kadragon/oop_project_ex/network/members)
