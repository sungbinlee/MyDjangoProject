# 장고 연습용 레포지토리 (Django Practice Repository)

이 레포지토리는 장고(Django) 연습을 위해 만들어진 레포지토리입니다. 이 레포지토리를 통해 장고의 기본 개념과 개발 방법을 익히고, 각 작업일마다 어떤 이론을 학습하고 어떤 실습을 진행했는지에 대한 내용을 상세하게 담고 있습니다.

## 7월 4일
### 작업내용:
1. 포스트 작성자와 현재 사용자가 일치하는 경우, 수정과 삭제 버튼을 표시하는 조건문을 작성했습니다.
2. `Comment`, `HashTag`모델 재정의: 작성자 외래키 추가
3. `Form_error.html` 템플릿을 작성했습니다. 해당 템플릿은 폼 오류 메시지를 출력하는 역할을 합니다. 폼 유효성 검사에서 실패할 경우, 폼 오류 메시지를 추가하고 폼을 포함한 컨텍스트를 form_error.html 템플릿에 전달하여 오류 메시지를 출력합니다.
4. `post_detail.html` 템플릿에서 포스트의 작성자와 현재 사용자를 비교하여 작성자일 경우에만 수정 버튼과 삭제 버튼이 표시되도록 구현했습니다.
5. `post_edit.html` 에 수정 폼이 추가되었습니다. 작업 내용은 폼 에러 메시지를 포함하도록 수정되었고, 수정 폼이 표시되는 기능이 구현되었습니다.
6. `Update` 클래스 기반 뷰를 작성했습니다. 해당 뷰는 GET 요청일 경우 포스트의 수정 폼을 보여주고, POST 요청일 경우 폼 데이터를 받아 포스트를 수정한 후 상세 페이지로 리디렉션합니다.

### 학습내용정리:
1. 포스트 작성자와 현재 사용자가 일치하는 경우, 수정과 삭제 버튼을 표시하는 조건문을 작성했습니다. 이를 통해 웹 애플리케이션에서 권한 기반 접근 제어를 구현할 수 있습니다. 사용자가 자신의 포스트만 수정하고 삭제할 수 있도록 보안을 강화했습니다.
2. `Comment`와 `HashTag` 모델을 재정의하여 작성자 외래키를 추가했습니다. 이를 통해 댓글과 해시태그에 작성자 정보를 연결할 수 있습니다.
3. `Form_error.html` 템플릿을 작성했습니다. 이 템플릿은 폼 유효성 검사에서 실패한 경우에 오류 메시지를 출력하기 위해 사용됩니다. 폼 에러 메시지를 포함한 컨텍스트를 해당 템플릿에 전달하여 사용자에게 유효성 검사 오류를 시각적으로 표시할 수 있습니다.
4. `post_detail.html` 템플릿에서는 포스트의 작성자와 현재 사용자를 비교하여 작성자일 경우에만 수정 버튼과 삭제 버튼을 표시하도록 구현했습니다. 이를 통해 포스트 작성자에게만 수정 및 삭제 권한을 부여하고, 다른 사용자는 이러한 조작을 할 수 없도록 보안성을 강화했습니다.
5. `post_edit.html` 템플릿에는 수정 폼이 추가되었습니다. 폼 에러 메시지를 포함하도록 수정되었고, 수정 폼이 표시되는 기능이 구현되었습니다. 이를 통해 사용자는 포스트를 편집할 수 있고, 유효성 검사 오류 메시지를 통해 잘못된 입력을 수정할 수 있습니다.
6. `Update` 클래스 기반 뷰를 작성했습니다. 이 뷰는 GET 요청일 경우 포스트의 수정 폼을 보여주고, POST 요청일 경우 폼 데이터를 받아 포스트를 수정한 후 상세 페이지로 리디렉션합니다. 이를 통해 사용자는 포스트를 쉽게 수정할 수 있고, 수정 후에는 수정된 내용을 확인할 수 있습니다.

## 7월 3일

### 작업내용:
1. `User` 모델 커스터마이즈: `AbstractUser` 모델을 상속받아 `User` 모델을 정의하였습니다. 이 모델은 추가적인 필드로 이메일(`email`), 이름(`name`), 비밀번호(`password`) 등을 포함하고 있습니다.
2. `UserManager` 클래스: `BaseUserManager`를 상속받은 `UserManager` 클래스를 정의하였습니다. 이 클래스는 사용자 생성과 관련된 메서드를 제공하며, `_create_user()` 메서드를 통해 사용자를 생성합니다. `create_user()` 메서드와 `create_superuser()` 메서드를 구현하여 일반 사용자와 슈퍼유저를 생성할 수 있도록 하였습니다.
3. `RegisterForm`과 LoginForm: UserCreationForm을 상속받은 RegisterForm과 AuthenticationForm을 상속받은 LoginForm 폼을 정의하였습니다. 
4. `Index` 뷰: `Index` 클래스 기반 뷰를 작성하여 인덱스 페이지를 재구현하였습니다. 해당 뷰는 로그인된 사용자의 경우에만 접근 가능하도록 `LoginRequiredMixin`을 사용하였습니다.
5. `Write` 뷰: `Write` 클래스 기반 뷰를 작성하여 글 작성 기능을 재구현하였습니다. 이 뷰도 로그인된 사용자만 접근 가능하도록 `LoginRequiredMixin`을 사용하였습니다. 글 작성 폼을 템플릿에 렌더링하고, 유효한 데이터인 경우에만 저장하도록 처리하였습니다.
6. `Post` 모델: `Post` 모델을 재정의하였습니다. 작성자와 `User` 모델을 외래키로 연결하였습니다.

### 학습내용정리:
1. 커스텀 사용자 모델(Custom User Model) 구현: Django의 기본 User 모델을 커스터마이즈하여 추가 필드를 포함한 사용자 모델을 생성하였습니다. UserManager 클래스를 통해 사용자 생성, 수정, 삭제와 관련된 도우미 메서드를 구현하였습니다.
2. 회원가입(RegisterForm)과 로그인(LoginForm) 폼 정의: Django의 폼(forms)을 사용하여 사용자 등록과 로그인을 위한 폼을 정의했습니다. RegisterForm은 UserCreationForm을 확장하고, LoginForm은 AuthenticationForm을 확장하여 사용자로부터 필요한 정보를 입력받을 수 있도록 했습니다.

## 6월 26일

### 작업내용:

1. `User` 모델과 `RegisterForm`, `LoginForm` 폼을 정의했습니다.
2. `admin.site.register(User)`를 통해 User 모델을 관리자 페이지에 등록했습니다.
3. `IndexMain` 뷰를 작성하여 인덱스 페이지에 로그인 및 회원가입 화면을 구현했습니다.
4. 회원가입과 로그인을 위한 URL 패턴을 `user/urls.py` 에 추가했습니다.
5. `Registration`, `Login`, `Logout` 클래스 기반 뷰를 작성하여 회원가입, 로그인, 로그아웃 기능을 구현했습니다.
6. 회원가입과 로그인에 대한 HTML 템플릿을 작성하고, 해당 템플릿에서 폼을 사용하여 입력을 받을 수 있도록 구현했습니다.

### 학습내용 정리:

1. User 모델: Django의 기본 User 모델은 사용자 정보를 저장하는 모델입니다. 이 모델을 커스터마이즈하여 추가 필드를 포함시킬 수 있습니다. 커스텀 User 모델을 정의하고 이를 활용하여 사용자 정보를 관리할 수 있습니다.

2. 인증 및 권한: Django의 인증 시스템은 사용자 인증과 권한 부여를 처리합니다. 사용자가 로그인하면 인증된 세션을 생성하고, 로그아웃하면 세션을 파기합니다. 인증된 사용자에게는 특정 권한을 부여하여 접근 제한을 설정할 수 있습니다.

3. 인증 뷰와 폼: Django에서는 인증과 관련된 기능을 간편하게 구현할 수 있는 인증 뷰와 폼을 제공합니다. 로그인, 로그아웃, 비밀번호 변경, 비밀번호 초기화 등을 처리하는 기능을 클래스 기반 뷰와 폼을 사용하여 구현할 수 있습니다.

4. 관리자 페이지: Django의 관리자 페이지는 인증과 관련된 기능을 포함한 사용자 관리 기능을 제공합니다. 사용자 생성, 권한 설정, 그룹 관리 등을 관리자 페이지에서 간편하게 처리할 수 있습니다.

## 6월 23일

### 작업내용:

1. `CommentDelete` 클래스: 댓글 삭제 기능을 처리하는 뷰 클래스를 작성하였습니다. 댓글을 삭제하고, 삭제 후에는 `blog:detail` 뷰로 리디렉션합니다.

2. `HashTagWrite` 클래스: 해시태그 작성 기능을 처리하는 뷰 클래스를 작성하였습니다. 입력받은 해시태그 이름을 사용하여 `HashTag` 객체를 생성하고, 생성 후에는 `blog:detail` 뷰로 리디렉션합니다.

3. `HashTagDelete` 클래스: 해시태그 삭제 기능을 처리하는 뷰 클래스를 작성하였습니다. 입력받은 해시태그를 삭제하고, 삭제 후에는 해당 글의 blog:detail 뷰로 리디렉션합니다.

4. `post_detail.html` 템플릿: 댓글 작성 및 삭제 기능, 해시태그 작성 및 삭제 기능이 있는 상세 페이지 템플릿을 작성하였습니다. `CommentForm` 폼을 사용하여 댓글 작성을 구현하고, `HashTagForm` 폼을 사용하여 해시태그 작성을 구현하였습니다. 댓글 및 해시태그 목록도 표시되며, 삭제 버튼을 통해 해당 댓글이나 해시태그를 삭제할 수 있습니다.

### 학습내용정리:

1. 모델 관계 설정: `HashTag` 모델에서 `Post`와의 관계를 `ForeignKey`로 설정하였습니다. 이를 통해 각 해시태그는 특정 게시물에 속하게 되고, 게시물과 연관된 해시태그를 관리할 수 있습니다.

2. 뷰 클래스 상속: `UpdateView`, `DeleteView` 등의 제네릭 뷰를 상속하여 업데이트와 삭제 기능을 구현하였습니다. 이를 통해 기존의 제네릭 뷰를 재사용하고, 필요한 기능만 추가하여 효율적으로 코드를 작성할 수 있습니다.

3. 폼 활용: `HashTagForm`과 `CommentForm`을 사용하여 해시태그와 댓글을 입력받는 폼을 생성하였습니다. 폼을 사용하면 사용자로부터 데이터를 안전하게 입력받을 수 있고, 유효성 검사를 통해 입력된 데이터의 유효성을 확인할 수 있습니다.

4. URL 패턴 설정: `urls.py` 파일에서 URL 패턴을 설정하여 각 기능에 대한 경로를 지정하였습니다. 이를 통해 각 기능에 대한 요청을 적절한 뷰로 매핑시킬 수 있습니다.

5. 템플릿 작성: `post_detail.html` 템플릿에서 댓글 작성과 삭제, 해시태그 작성과 삭제 기능을 구현하였습니다. 템플릿을 사용하여 서버에서 전달된 데이터를 동적으로 표시하고, 사용자와의 상호작용을 구현할 수 있습니다.

## 6월 22일

### 작업내용:

1. 템플릿을 작성하였습니다.

   - 폼을 통해 `title`과 `content` 필드를 입력받아 수정하는 HTML 폼을 작성하였습니다.

2. `UpdateView`를 상속받은 Update 클래스를 작성하였습니다.

   - Post 모델을 대상으로 하는 업데이트 기능을 처리합니다.
   - 'blog/post_edit.html' 템플릿을 사용합니다.
   - `title`과 `content` 필드를 포함하는 폼을 생성합니다.
   - 초기값을 설정하기 위해 `get_initial()` 메서드를 오버라이드하였습니다.
   - `get_success_url()` 메서드를 사용하여 성공 시 이동할 URL을 지정하였습니다.

3. DeleteView를 상속받은 Delete 클래스를 작성하였습니다.

   - `Post` 모델을 대상으로 하는 삭제 기능을 처리합니다.
   - 삭제 후 이동할 URL을 `reverse_lazy()`를 사용하여 설정하였습니다.

4. `DetailView` 클래스를 작성하였습니다.

   - `post_id`에 해당하는 `Post` 객체와 관련된 작업을 처리합니다.

5. `CommentWrite` 클래스를 작성하였습니다.

   - 댓글 작성 기능을 처리합니다.
   - `CommentForm`을 사용하여 댓글을 작성하고, 작성한 댓글을 저장합니다.

6. URL 패턴을 설정하였습니다.
   - `edit` 패턴은 `Update` 뷰와 연결되어 글 편집 기능을 제공합니다.
   - `delete` 패턴은 `Delete` 뷰와 연결되어 글 삭제 기능을 제공합니다.

### 학습내용정리:

- Django의 클래스 기반 뷰 사용: UpdateView, DeleteView를 상속하여 업데이트 및 삭제 기능을 구현하였습니다. 이를 통해 Django의 제네릭 뷰를 활용하여 CRUD(Create, Read, Update, Delete) 기능을 간편하게 처리할 수 있습니다.
- 상속과 오버라이딩: 클래스를 상속하고 필요한 메서드를 오버라이딩하여 원하는 동작을 구현할 수 있습니다. `get_initial()`과 `get_success_url()` 메서드를 오버라이딩하여 초기값 설정과 성공 시 이동할 URL을 지정하는 방법을 익힐 수 있습니다.
- 데이터베이스 조작: `Post`와 `Comment` 모델을 조작하는 과정을 통해 데이터베이스 연동 및 객체 생성, 저장, 삭제 등을 학습할 수 있습니다.

## 6월 21일

### 작업내용:

1. blog/forms.py 파일에 `PostForm` 클래스를 정의하였습니다.
2. 데이터베이스 값을 생성했습니다.
3. 블로그 글 URL 구성했습니다.
   - 블로그 글의 URL은 일반적으로 특정 패턴을 따릅니다. 예를 들어, http://www.domain.co.kr/blog는 블로그 글 목록을 보여주는 페이지를 나타내며, http://www.domain.co.kr/blog/detail/1은 ID가 1인 특정 블로그 글의 상세 페이지를 나타냅니다. URL 패턴을 설정하고 해당 패턴에 따라 뷰와 매핑하여 원하는 동작을 구현할 수 있습니다.

### 학습내용정리:

- 모델 폼(ModelForm)을 사용하여 데이터 모델에 대한 폼을 생성하는 방법을 학습했습니다.
- URL 패턴을 정의하고 뷰를 연결하여 웹 애플리케이션의 다양한 기능을 구현하는 방법을 알아보았습니다.
- 클래스 기반 뷰(`ListView`, `CreateView`, `DetailView`)를 사용하여 재사용 가능한 뷰를 작성하는 방법을 익혔습니다.
- 템플릿 파일을 작성하고, 템플릿 확장과 블록 설정을 사용하여 템플릿 파일을 구조화하는 방법을 배웠습니다.
- 폼 유효성 검사: Django는 폼 유효성 검사 기능을 제공하여 서버 측에서 클라이언트에서 전달된 값들에 대한 유효성을 검증할 수 있습니다.
- 폼 처리: `CommentForm`을 사용하여 댓글 작성 폼을 구현하였습니다. 이를 통해 사용자의 입력을 받고 유효성 검사를 수행할 수 있습니다. 폼을 생성하고 처리하는 방법을 익힐 수 있습니다.

## 6월 20일

오늘은 Django 개발 세팅을 완료하고, 프로젝트를 생성하고 앱을 생성했습니다. 또한, 기능 정리, 데이터베이스 모델 작성, URLs 설정, Views 작성까지 진행했습니다.

### 오늘은 Django 개발 세팅을 진행했습니다.

1. Python과 Django를 설치하고 가상환경을 구축했습니다.
2. Django 프로젝트를 생성했습니다.
3. Django 앱을 생성했습니다.

### 또한, Django 개발 순서에 따라 작업을 진행했습니다.

#### 1. 기능 정리: 블로그 기능들을 정리 했습니다.

| blog            | request         | method      |
| --------------- | --------------- | ----------- |
| 1. 글쓰기       | /blog/write     | post        |
| 2. 게시판(목록) | /blog/board     | get         |
| 3. 글 상세 조회 | /blog/detail/1  | get         |
| 4. 글 수정      | /blog/edit      | put/post    |
| 5. 글 삭제      | /blog/delete    | delete/post |
| 6. 댓글 조회    | /comments       | get         |
| 7. 댓글 쓰기    | /comment/write  | post        |
| 8. 댓글 삭제    | /comment/delete | delete/post |
| 9. 태그(달기)   | /tag            | post        |

#### 2. Models(데이터베이스) 작성: 관계형 데이터베이스를 구성하기 위해 데이터 모델을 작성했습니다.

- 블로그 글(Post)
- 댓글 (Comment)

#### 3. URLs 설정: URL 매핑을 위해 URLs를 설정했습니다.

`makemigrations`는 모델 변경 사항을 추적하여 마이그레이션 파일을 생성하고, `migrate`는 마이그레이션 파일을 실행하여 실제 데이터베이스 스키마를 변경합니다.

#### 4. Views 작성: 웹 요청을 받고 처리한 후, 데이터베이스에서 필요한 값을 가져와 가공하여 응답 형태로 반환하는 역할을 합니다. Django에서는 Function-Based Views (FBV)와 Class-Based Views (CBV) 두 가지 방식으로 Views를 작성할 수 있습니다.

### 데이터베이스(ORM)

Django에서는 데이터베이스와의 상호작용을 편리하게 하기 위해 ORM(Object-Relational Mapping)을 제공합니다. ORM은 객체와 관계형 데이터베이스 간의 매핑을 지원하여 객체 지향 프로그래밍에서 데이터베이스를 쉽게 다룰 수 있게 해줍니다. Django의 ORM을 사용하면 SQL 쿼리를 직접 작성하지 않고도 데이터베이스(CRUD) 조작을 수행할 수 있습니다.
