# 장고 연습용 레포지토리 (Django Practice Repository)
이 레포지토리는 장고(Django) 연습을 위해 만들어진 레포지토리입니다. 이 레포지토리를 통해 장고의 기본 개념과 개발 방법을 익히고, 각 작업일마다 어떤 이론을 학습하고 어떤 실습을 진행했는지에 대한 내용을 상세하게 담고 있습니다. 

## 6월 20일
오늘은 Django 개발 세팅을 완료하고, 프로젝트를 생성하고 앱을 생성했습니다. 또한, 기능 정리, 데이터베이스 모델 작성, URLs 설정, Views 작성까지 진행했습니다.
### 오늘은 Django 개발 세팅을 진행했습니다.
1. Python과 Django를 설치하고 가상환경을 구축했습니다.
2. Django 프로젝트를 생성했습니다.
3. Django 앱을 생성했습니다.

### 또한, Django 개발 순서에 따라 작업을 진행했습니다.
#### 1. 기능 정리: 블로그 기능들을 정리 했습니다.

|blog|request|method|
|---|---|---|
|1. 글쓰기|/posts/write|post|
|2. 게시판(목록)|/posts/board|get|
|3. 글 수정|/posts/edit|put/post|
|4. 글 삭제|/posts/delete|delete/post|
|5. 댓글 쓰기|/comment/write|post|
|6. 댓글 삭제|/comment/delete|delete/post|
|7. 태그(달기)|/tag|post|


#### 2. Models(데이터베이스) 작성: 관계형 데이터베이스를 구성하기 위해 데이터 모델을 작성했습니다.
   - 블로그 글(Post)
   - 댓글 (Comment)
#### 3. URLs 설정: URL 매핑을 위해 URLs를 설정했습니다.
`makemigrations`는 모델 변경 사항을 추적하여 마이그레이션 파일을 생성하고, `migrate`는 마이그레이션 파일을 실행하여 실제 데이터베이스 스키마를 변경합니다.






#### 4. Views 작성: 웹 요청을 받고 처리한 후, 데이터베이스에서 필요한 값을 가져와 가공하여 응답 형태로 반환하는 역할을 합니다. Django에서는 Function-Based Views (FBV)와 Class-Based Views (CBV) 두 가지 방식으로 Views를 작성할 수 있습니다.

### 데이터베이스(ORM)

Django에서는 데이터베이스와의 상호작용을 편리하게 하기 위해 ORM(Object-Relational Mapping)을 제공합니다. ORM은 객체와 관계형 데이터베이스 간의 매핑을 지원하여 객체 지향 프로그래밍에서 데이터베이스를 쉽게 다룰 수 있게 해줍니다. Django의 ORM을 사용하면 SQL 쿼리를 직접 작성하지 않고도 데이터베이스(CRUD) 조작을 수행할 수 있습니다.
