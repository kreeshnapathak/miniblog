from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render,HttpResponseRedirect, redirect
from .forms import LoginForm, SignUpForm, PostForm, CommentForm
from django.contrib import messages
from .models import Post,BlogComment
from django.contrib.auth.models import Group
from django.core.cache import cache
from django.db.models import Q
from django.core.paginator import Paginator

def home(request):
    posts=Post.objects.all().order_by('-id')
    paginator=Paginator(posts,3,orphans=1)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    return render(request,'blog/home.html',{'page_obj':page_obj})


def about(request):
    return render(request,'blog/about.html')

def contact(request):
    return render(request,'blog/contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        posts=Post.objects.all()
        user=request.user
        full_name=user.get_full_name()
        gps=user.groups.all()
        ip=request.session.get('ip',0)
        ct=cache.get("count",version=user.pk)
        return render(request,'blog/dashboard.html',{'posts':posts,'full_name':full_name,'groups':gps,
        'ip':ip,'ct':ct})
    else:
        return HttpResponseRedirect("login")

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def user_signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulation!! You have become an Author...')
            user=form.save()
            group=Group.object.get(name='Author')
            user.groups.add(group)
            form.save()
    else:
        form=SignUpForm()
    return render(request,'blog/signup.html',{'form':form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,"Logged in Sucessfully!!!")
                    return HttpResponseRedirect("/dashboard/")

        else:
            form=LoginForm()
        return render(request,'blog/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')


def add_post(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=PostForm(request.POST)
            if form.is_valid():
                title=form.cleaned_data['title']
                desc=form.cleaned_data['desc']
                pst=Post(title=title,desc=desc)
                pst.save()
                form=PostForm()
        else:
            form=PostForm()
        return render(request,'blog/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect("/login/")

def update_post(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post.objects.get(pk=id)
            form=PostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
                messages.success(request, 'Congratulation!! You have updated the content...')
                return HttpResponseRedirect("/dashboard/")
                
        else:
            pi=Post.objects.get(pk=id)
            form=PostForm(instance=pi)        
        return render(request,'blog/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect("/login/")

def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect("/dashboard/")
    else:
        return HttpResponseRedirect("/login/")


def details(request,id):
    mypost=Post.objects.filter(pk=id).first()
    if request.method=='POST':
        form=CommentForm(request.POST)
        
        if form.is_valid():
            obj=form.save(commit=False)
            obj.posts=mypost
            obj.save()
            return redirect(f'/details/{mypost.id}')
    else:
        form=CommentForm()
    return render(request,'blog/details.html',{'form':mypost,'comments':form})


def search(request):
    query=request.GET['query']
    if len(query)>78:
        reasult=[]
    else:
        reasult=Post.objects.filter(Q(title__icontains=query) | Q(desc__icontains=query)  )
    return render(request,'blog/search.html',{'reasult':reasult,'query':query})


    
