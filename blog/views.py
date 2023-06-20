from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
# def index(request):
#     if request.method == 'GET':
#         return HttpResponse('Index page GET')
#     elif request.method == 'POST':
#         return HttpResponse('Index page POST')
#     else:
#         return HttpResponse('Invalid method')
    
class Index(View):
    def get(self, request):
        # return HttpResponse('index page Get class') 

        # 데이터베이스에 접근해서 값을 가져와야 합니다.
        # context = 데이터베이스에서 가져온 값
        return render(request, 'blog/board.html')
