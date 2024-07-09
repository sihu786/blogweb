from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog,Tag,Category,Contact
from django.core.paginator import PageNotAnInteger,EmptyPage,Paginator
from django.db.models import Q
# Create your views here.

def home(request):
    blogs=Blog.objects.order_by('create_date')
    tags=Tag.objects.order_by('created_date')

    context={
        "blogs":blogs,
        "tags":tags
    }
    return render(request,'home.html',context)



def blog(request):
    queryset=Blog.objects.order_by('create_date')
    tags=Tag.objects.order_by('created_date')
    page=request.GET.get('page',1)
    paginator=Paginator(queryset,4)
    try:
        blogs=paginator.page(page)
    except EmptyPage:
        blogs.paginator.page(1)
    except PageNotAnInteger:
        blogs=paginator.page(1)
        return redirect('blog')        
        



    context={
        "blogs":blogs,
        "tags":tags,
        "paginator":paginator
    }

    return render(request,'blog.html',context)

def category_blogs(request,slug):
    category=get_object_or_404(Category,slug=slug)
    blogs=category.category_blogs.all()
     
    tags=Tag.objects.order_by('created_date')[:3]
    page=request.GET.get('page',1)
    paginator=Paginator(blogs,2)
    
    try:
        blogs=paginator.page(page)
    except EmptyPage:
        blogs.paginator.page(1)
    except PageNotAnInteger:
        blogs=paginator.page(1)
        return redirect('blog')
  
    
    
    context={

        
        "tags":tags,
        "blogs":blogs,
        "paginator":paginator,
        

    }

    return render(request,'category_blog.html',context)



def tag_blogs(request,slug):
    tag=get_object_or_404(Tag,slug=slug)
    queryset=tag.blog_tag.all()
     
    tags=Tag.objects.order_by('created_date')[:5]
  
    
    page=request.GET.get('page',1)
    paginator=Paginator(queryset,2)
    
    try:
        blogs=paginator.page(page)
    except EmptyPage:
        blogs.paginator.page(1)
    except PageNotAnInteger:
        blogs=paginator.page(1)
        return redirect('blog')
    context={
        
        
        "tags":tags,
        "blogs":blogs,
        "paginator":paginator,
        

    }

    return render(request,'tag_blog.html',context)


def blog_details(request,slug):
    blog=get_object_or_404(Blog,slug=slug)
    category=Category.objects.get(id=blog.category.id)
    related_blogs=category.category_blogs.all()[:3]
    tags=Tag.objects.order_by('created_date')[:5]
    context={
        "blog":blog,
        "related_blogs":related_blogs,
        "tags":tags
    }
    
    return render(request,'blog_details.html',context)
   


def search_blog(requset):
    search_key=requset.GET.get("search") 
    if search_key:
        blogs=Blog.objects.filter(
            Q(title__icontains=search_key) |
            Q(category__category__icontains=search_key) |
            Q(user__username__icontains=search_key) |
            Q(tags__tags__icontains=search_key)

        ).distinct()
        resent_blogs=Blog.objects.order_by('create_date')
        tags=Tag.objects.order_by('created_date')
                
        page=requset.GET.get('page',1)
        paginator=Paginator(blogs,4)
            
        try:
            blogs=paginator.page(page)
        except EmptyPage:
            blogs.paginator.page(1)
        except PageNotAnInteger:
            blogs=paginator.page(1)
            return redirect('blog')
        context={ 
            
            "blogs":blogs,
            "paginator":paginator,
            "tags":tags,
            "resent_blogs":resent_blogs
            
            }
        return render(requset,'search.html',context)
    else:
        return redirect('home')




def contact(request):
    contacts=Contact.objects.all()
    context={
        "contacts":contacts
    }

    return render(request,'contact.html',context)      
        
                

            

        

       
        

   

