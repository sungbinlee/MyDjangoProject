from django.urls import path
# from . import views
from blog.views import Index

# 기본 구조
# urlpatterns = [
#     # path(패턴, 매핑)
# ]

urlpatterns = [
    # path("", views.index), # FBV way
    path("", Index.as_view())
    # 글 조회
    # 글 작성
    # 글 수정
    # 글 삭제
    # 코멘트 작성
    # 코멘트 삭제
]