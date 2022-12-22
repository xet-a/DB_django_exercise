# MySQL & Django tutorial
- 복습용으로 작성한 문서
- tutorial 코드와 실제 과제 구현 코드는 상이함
- 빠진 부분 : settings.py 에서 secrets.json으로 DB pwd와 django secret key 분리함

### 1. MySQL

- 데이터베이스 생성
    
    ![Untitled](https://user-images.githubusercontent.com/78337522/209196248-0ccaa79a-439a-445f-b1ae-06eeaaa31191.png)
    
    - 쿼리 작성 후 번개 모양 누르면 아래 액션 수행 확인 가능
    - Schemas 누르면 생성된 데이터베이스 확인 후 더블클릭함
- 테이블 생성
    
    ![Untitled 1](https://user-images.githubusercontent.com/78337522/209195503-c733b89a-a871-405e-800e-ee0716ee02e3.png)
    
    - 같은 방식으로 요구된 테이블 세 개 더 만듦
- record 추가하기
    
    ![Untitled 2](https://user-images.githubusercontent.com/78337522/209195686-1318871e-4db5-4479-9053-ef0eebe03459.png)
    
    
    - 같은 방식으로 나머지 테이블에도 record 추가함
    - 테이블 우측 클릭해서 select rows 누르면 넣은 record 확인할 수 있음
    mySQL에서 boolean type은 tinyint(1) 형식으로 정의됨 (true 1, false 0)
    
    ![Untitled 3](https://user-images.githubusercontent.com/78337522/209195767-e2583d6f-eccc-4320-8420-a953d6329261.png) 

### 2. Django

- 먼저 파이썬으로 가상환경 진입하고, 장고 설치해야 함
- 루트 디렉터리 내 장고 프로젝트를 생성
django-admin startproject (프로젝트 이름)
    
    ![Untitled 4](https://user-images.githubusercontent.com/78337522/209195805-6acf949e-9368-40a1-92cb-03de0e91c242.png)
        
    - 앱 생성 : django-admin startapp (앱 이름-여기서는 myApp)
    앱 생성 시 settings.py에 앱 추가하기
        
        ![Untitled 5](https://user-images.githubusercontent.com/78337522/209195815-af432152-dd32-4665-bd8d-a4d32e881d56.png)
                
    - python manage.py migrate 로 앱들이 필요로 하는 테이블들을 생성
    (테이블 : 데이터베이스에서 데이터를 저장하기 위한 데이터 집합의 모음)
    - 모델 생성하거나 변경한 경우 테이블 작업 파일부터 만들어야 함makemigrations 실행해서 장고가 테이블 작업 수행하기 위한 파일 생성
        - 명령 실행 후 myApp/migrations/0001_initial.py 파일이 자동 생성됨
        - 변경 사항 없을 시 No changes detected
        - 이제 migrate 실행해서 장고가 등록된 앱에 있는 모델을 참조해 실제 테이블을 생성
    - DB Browser for SQLite 에서 실제 테이블명을 확인할 수 있지만 개발에서는 필요 없음
    - migrate 실행 시 어떤 쿼리문이 실행되는지는 sqlmigrate 명령으로 알 수 있음 (python manage.py sqlmigrate myApp 0001)
- 개발 서버 구동 : python manage.py runserver
    - 서버 종료 : ctrl+c
    - 로컬 서버로 실행됨 : 127.0.0.1:8000 (localhost:8000 이랑 같음)
    - 서버 접속 시 띄울 페이지 매핑은 config/urs.py에서 설정
        - config/urls.py 에서 from myApp import views와 path('myApp/', views.index), 추가
        - 이때, urlpatterns에 들어가는 url에서 호스트명과 포트 번호는 둘 다 장고 실행 환경에 따라 변하는 값이므로 생략됨.
        - 슬래시를 붙이면 사용자가 슬래시 없이 주소를 입력해도 장고가 자동으로 슬래시를 붙여줌(url 정규화 기능)
        - 장고 프로젝트 디렉터리를 settings.py에서 BASE_DIR 변수에 저장
        - config/urls.py는 실제로 (장고프로젝트 경로)/config/urls.py에 해당

- html 문서를 담을 templates 폴더 생성
마찬가지로 settings.py의 TEMPLATES에 경로를 추가함
    
    ![Untitled 6](https://user-images.githubusercontent.com/78337522/209195819-ddfd9a14-42a9-4bb1-874a-38339eb45c3d.png)
        
- 데이터베이스 연결, 데이터베이스 비밀번호 입력해야 함
    
    ![Untitled 7](https://user-images.githubusercontent.com/78337522/209196256-1f54c481-8c7a-4d1a-87ca-404a7bf16674.png)
        
- [views.py](https://github.com/xet-a/DB_django_exercise/blob/main/hardware/myApp/views.py) 작성
    - 데이터베이스 접속하기 위한 모듈로 django.db의 connection 사용
    settings.py에 입력한 데이터베이스 정보로 접속하게 됨
    - cursor() : SQL 문을 수행하고 결과를 얻는 데 사용하는 cursor 객체 생성
    - 이런 식으로 기본 틀 잡고 각각 sql 쿼리 작성하기
        
        ![Untitled 8](https://user-images.githubusercontent.com/78337522/209196262-f97821cb-81b0-4fe2-ab52-d72f2ef191b2.png)
                
    - Find the average hard disk size of PCs
        - SUM(hd) / COUNT(*) 로 구하거나 AVG(hd)로 구할 수 있음
            
            ![Untitled 9](https://user-images.githubusercontent.com/78337522/209196264-6337e794-5fa5-4cb9-be5a-5a7a3275c783.png)
            
            ![Untitled 10](https://user-images.githubusercontent.com/78337522/209196265-1e412f67-82d3-4954-a5ad-5b5c272baa1b.png)
            
    - Find the average speed of laptop for each maker
    - Find the price of laptop, which is the only laptop model of the maker
    - Find the model and price of the printer of the highest price of each maker
      - [views.py](https://github.com/xet-a/DB_django_exercise/blob/main/hardware/myApp/views.py) 참고

![Untitled 11](https://user-images.githubusercontent.com/78337522/209196267-5098dee7-6695-4e88-a569-fd5c2abd8c20.png)

view들에 대한 접근을 갖도록 [urls.py](https://github.com/xet-a/DB_django_exercise/blob/main/hardware/hardware/urls.py) 에서 매핑
전체 구조는 좌측과 같음
