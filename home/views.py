from django.shortcuts import render
from .models import Blog
from .forms import(
    CreateBlog,
    UpdateBlog

)

def index(reguest):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(reguest, "home/index.html", context)


def create_blog(reguest):
    if reguest.method == 'POST':
        title = reguest.POST['title']
        body = reguest.POST['body']
        Blog.objects.create(
            title = title,
            body = body
        )
        return redirect('http://127.0.0.1:8000/')
    form =  CreateBlog()

    context = {
            'form': form
    }
    return render(reguest, "home/create_form.html", context )

def updateblog(reguest, id):

    if reguest.method == 'POST':
        blog =  UpdateBlog(instance=reguest.POST)
        if blog.is_valid():
            blog.save()
            return redirect('http://127.0.0.1:8000/')
            blog = Blog.objects.get(pk=id)
            update_blog_form = UpdateBlog( reguest.POST,    instance=blog)
            context = {
            'update_blog_form': update_blog_form
             }
            return render(reguest,  'home/update_blog.html', context)
        return HttpResponse('error')

    blog = Blog.objects.get(pk=id)
    update_blog_form = UpdateBlog(instance=blog)
    context = {
        'update_blog_form': update_blog_form
    }

    return render(reguest, 'home/update_blog.html', context )



