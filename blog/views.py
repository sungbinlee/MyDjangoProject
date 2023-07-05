from typing import Any, Dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment, HashTag
from .forms import PostForm, CommentForm, HashTagForm
from django.urls import reverse_lazy, reverse

# Create your views here.
# def index(request):
#     if request.method == 'GET':
#         return HttpResponse('Index page GET')
#     elif request.method == 'POST':
#         return HttpResponse('Index page POST')
#     else:
#         return HttpResponse('Invalid method')

# 포스트


class Index(View):
    def get(self, request):
        # return HttpResponse('index page Get class')

        # 데이터베이스에 접근해서 값을 가져와야 합니다.
        # 게시판에 글들을 보여줘야하기 떄문에 데이터베이스에서 "값 조회" all()
        # MyModel.objects.all()
        post_objs = Post.objects.all()
        # context = 데이터베이스에서 가져온 값
        context = {
            "posts": post_objs,
            "title": "Blog"
        }
        return render(request, 'blog/post_list.html', context)


# def write(request):
#     if request.method == 'POST':
#         # form 확인
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save()
#             return redirect('blog:list')

#     form = PostForm()
#     return render(request, 'blog/write.html', {'form': form})


# Django 자체의 클래스 뷰 기능도 강력, 편리
# model, template_name, context_object_name,
# paginate_by, form_class, form_valid(), get_queryset()
# django.views.generitc - > ListView
# class List(ListView):
#     model = Post  # 모델
#     template_name = 'blog/post_list.html'  # 템플릿
#     context_object_name = 'posts'  # 변수 값의 이름


# class Write(CreateView):
#     model = Post  # 모델
#     form_class = PostForm  # 폼
#     success_url = reverse_lazy('blog:list')  # 성공시 보내줄 url


class Write(LoginRequiredMixin, View):

    def get(self, request):
        form = PostForm()
        context = {
            'form': form
        }
        return render(request, 'blog/post_form.html', context)

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            post.save()
            return redirect('blog:list')
        form.add_error(None, '폼이 유효하지 않습니다.')
        context = {
            'form': form,
            "title": "Blog"
        }
        return render(request, 'blog/post_form.html')


# class Detail(DetailView):
#     model = Post
#     template_name = 'blog/post_detail.html'
#     context_object_name = 'post'


# class Update(UpdateView):
#     model = Post
#     template_name = 'blog/post_edit.html'
#     fields = ['title', 'content']
#     # success_url = reverse_lazy('blog:list')
#     # initial 기능 사용 -> form에 값을 미리 넣어주기 위해서

#     def get_initial(self):
#         initial = super().get_initial()  # UpdateView(generic view)에서 제공하는 initial(딕셔너리)
#         post = self.get_object()  # pk 기반으로 객체를 가져옴
#         initial['title'] = post.title
#         initial['content'] = post.content
#         return initial

#     def get_success_url(self):
#         post = self.get_object()  # pk 기반으로 현재 객체 가져오기
#         return reverse('blog:detail', kwargs={'pk': post.pk})

class Update(View):
    def get(self, request, pk):  # post_id
        post = Post.objects.get(pk=pk)
        form = PostForm(initial={'title': post.title, 'content': post.content})
        context = {
            'form': form,
            'post': post,
            "title": "Blog"
        }
        return render(request, 'blog/post_edit.html', context)

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            return redirect('blog:detail', pk=pk)

        form.add_error('폼이 유효하지 않습니다.')
        hashrag_form = HashTagForm()
        context = {
            'form': form,
            'post': post,
            "title": "Blog"
        }
        return render(request, 'blog/post_detail_error.html', context)

# class Delete(DeleteView):
#     model = Post
#     success_url = reverse_lazy('blog:list')


class Delete(View):
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect('blog:list')


class DetailView(View):
    def get(self, request, pk):
        # 글 가져옴
        post = Post.objects.get(pk=pk)

        comments = Comment.objects.filter(post=post)
        hashtags = HashTag.objects.filter(post=post)

        # 태그 form
        hashtag_form = HashTagForm()

        # 댓글 form
        comment_form = CommentForm()

        context = {
            "title": "Blog",
            'post': post,
            'comments': comments,
            'hashtags': hashtags,
            'comment_form': comment_form,
            'hasgtag_form': hashtag_form,
            "title": "Blog"
        }

        return render(request, 'blog/post_detail.html', context)
        # 댓글


# Comment
class CommentWrite(View):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        post = Post.objects.get(pk=pk)
        if form.is_valid():
            # 사용자에게 댓글 내용을 받아옴
            content = form.cleaned_data['content']
            # 해당 아이디에 해당하는 글 불러옴
            post = Post.objects.get(pk=pk)
            # 유저 정보 가져오기
            writer = request.user
            # 댓글 객체 생성
            comment = Comment.objects.create(
                post=post, content=content, writer=writer)
            return redirect('blog:detail', pk=pk)

        # form.add_error('폼이 유효하지 않습니다.')
        hashtag_form = HashTagForm()
        context = {
            "title": "Blog",
            'post': post,
            'comments': post.comment_set.all(),
            'hashtags': post.hashtag_set.all(),
            'comment_form': form,
            'hashtag_form': hashtag_form
        }
        return render(request, 'blog/post_detail.html', context)


class CommentDelete(View):
    def post(self, reqeust, pk):
        # 커멘트 객체 가져오기
        comment = Comment.objects.get(pk=pk)

        post_id = comment.post.id
        # 댓글 삭제 로직 구현
        comment.delete()

        return redirect('blog:detail', pk=post_id)


class HashTagWrite(View):

    def post(self, request, pk):
        form = HashTagForm(request.POST)
        post = Post.objects.get(pk=pk)
        if form.is_valid():
            name = form.cleaned_data['name']
            writer = request.user
            hashtag = HashTag.objects.create(
                post=post, name=name, writer=writer)
            return redirect('blog:detail', post_id=pk)
        form.add_error(None, '폼이 유효하지 않습니다.')
        comment_form = CommentForm()
        context = {
            'title': 'Blog',
            'post': post,
            'comments': post.comment_set.all(),
            'hashtags': post.hashtag_set.all(),
            'comment_form': comment_form,
            'hashtag_form': form
        }
        return render(request, 'blog/post_detail.html', context)


class HashTagDelete(View):
    def post(self, reqeust, pk):
        # 커멘트 객체 가져오기
        hasgtag = HashTag.objects.get(pk=pk)

        post_id = hasgtag.post.id
        # 댓글 삭제 로직 구현
        hasgtag.delete()

        return redirect('blog:detail', pk=post_id)
