Fork & PR 실습
--------------
* https://github.com/ 계정 만들기
* git/github 설치 
  * [Git 다운로드](https://git-scm.com/)
  * [Github DeskTop](https://desktop.github.com/)
  * [sourcetree](https://www.sourcetreeapp.com/)
* [github 강의 저장소 fork 하기](https://github.com/kakaotrack/opensource-class)
* 자기소개서 작성하기: `github-2023` 폴더에 `학번-이름.md` 파일
  - 관심 저장소 fork 2개 이상 포함 
* PR 보내기
* (참고)
  - [opensource-class 저장소](https://github.com/kakaotrack/opensource-class)에서 [나의 원격 저장소](https://github.com/나의깃헙아이디/opensource-class )로 **Fork**
  - Git Bash 실행 (윈도우용 Git이 설치된 상태)
  - [원격 저장소](https://github.com/나의깃헙아이디/opensource-class)에서 로컬 저장소(opensource-class 디렉토리)로 가져오기: `git clone https://github.com/깃헙사용자아이디/opensource-class.git`
  - `cd opensource-class`
  - vi 실행하고 파일 새로만들기/열기: `vi github-2023/학번.md`
  - [초간단 vi 편집기 사용법](http://kklyoon.tistory.com/100)
  - 편집한 파일 저장하고 vi 종료 `:wq`
  - 버전 관리 대상으로 추가: `git add github-2023/학번.md`
  - 로컬 저장소에 커밋: `git commit -m '아무개 자기소개서 추가'`
  - [나의 원격 저장소](https://github.com/나의깃헙아이디/opensource-class)에 올리기: `git push`
  - [나의 원격 저장소 웹 페이지](https://github.com/나의깃헙아이디/opensource-class/pulls)에서 [원본 저장소](https://github.com/kakaotrack/opensource-class)로 **Pull Request** 보내기

Markdown
--------
* [Github Markdown](https://guides.github.com/features/mastering-markdown/)
//test Commit changes
