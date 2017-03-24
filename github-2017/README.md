Markdown 
--------
* [소개](https://docs.google.com/presentation/d/1TJzzz5gIDBGRa5MaVsmoAG4jEPkk1za13V2z5vLuFFg/edit?usp=sharing)
* [markdown 실습](http://www.markdowntutorial.com/lesson/1/)

Gitub
-----
* [try Git  실습](https://try.github.io/levels/1/challenges/1)

Fork & PR 실습
--------------
* github 계정 만들기
* [윈도우용 Git 다운로드](https://git-for-windows.github.io/)
* [github 강의 저장소 fork 하기](https://github.com/daumkakaotrack/opensource-class)
* 자기소개서 작성하기: `github-2017` 폴더에 `학번.md` 파일
  - 관심 저장소 fork 2개 이상 포함 
* PR 보내기
* 힌트
  - [github 강의 저장소](https://github.com/daumkakaotrack/opensource-class)에서 [나의 원격 저장소](https://github.com/나의깃헙아이디/opensource-class )로 **Fork**
  - Git Bash 실행 (윈도우용 Git이 설치된 상태)
  - [원격 저장소](https://github.com/나의깃헙아이디/opensource-class)에서 로컬 저장소(opensource-class 디렉토리)로 가져오기: `git clone https://github.com/깃헙사용자아이디/opensource-class.git`
  - `cd opensource-class`
  - vi 실행하고 파일 새로만들기/열기: `vi github-2017/학번.md`
  - [초간단 vi 편집기 사용법](http://kklyoon.tistory.com/100)
  - 편집한 파일 저장하고 vi 종료 `:wq`
  - 버전 관리 대상으로 추가: `git add github-2017/학번.md`
  - 로컬 저장소에 커밋: `git commit -m '아무개 자기소개서 추가'`
  - [나의 원격 저장소](https://github.com/나의깃헙아이디/opensource-class)에 올리기: `git push`
  - [나의 원격 저장소 웹 페이지](https://github.com/나의깃헙아이디/opensource-class/pulls)에서 [원본 저장소](https://github.com/daumkakaotrack/opensource-class)로 **Pull Request** 하기
