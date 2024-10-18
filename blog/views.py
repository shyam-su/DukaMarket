from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.core.cache import cache
from .models import *
from django.core.paginator import Paginator


def blog_view(request):
    try:
        cach_data=cache.get('blog_page_data')
        
        if cach_data:
            context=cach_data
        else:
            banner = Blog_Banner.objects.order_by('-id')
            post = Blog.objects.order_by('-id')

            # Implement pagination
            paginator = Paginator(post, 5)  # 5 posts per page
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            popular = Blog.objects.order_by('-id')[:5]
            cate=Category.objects.all()[:5]



            context = {
                'banner': banner,
                'post': page_obj,  # Use the paginated posts
                'popular': popular,
                'cate': cate,
            }
            cache.set('blog_page_data',context,60)
        return render(request, "blog/blog.html", context) 
    except Exception as e:
        print(f"An error occurred: {e}")     
        messages.error(request,"An error occurred while loading the About page. Please try again later.")     
        return render(request, 'errors/404.html')
    
    
# Create your views here.
# def blog_view(request):
#     banner = Blog_Banner.objects.order_by('-id')
#     post = Blog.objects.order_by('-id')

#     # Implement pagination
#     paginator = Paginator(post, 5)  # 5 posts per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     popular = Blog.objects.order_by('-id')[:5]
#     cate=Category.objects.all()[:5]



#     context = {
#         'banner': banner,
#         'post': page_obj,  # Use the paginated posts
#         'popular': popular,
#         'cate': cate,
#     }
#     return render(request, "blog/blog.html", context)



def blog_detail(request,slug):
    try:
        cach_data = cache.get('blog_detail_page_data')
        if cach_data:
            context =cach_data
        else:
            banner=Blog_Details_Banner.objects.all()
            post=get_object_or_404(Blog,slug=slug)
            popular=Blog.objects.order_by('-id')[:5]
            tag=Tag.objects.all()[:3]
            cate=Category.objects.all()
            comment=Comment.objects.filter(post=post).order_by('-date')[:3]

            context={
                'banner':banner,
                'post':post,
                'tag':tag,
                'popular':popular,
                'cate':cate,
                'slug':slug,
                'comment':comment,
            }
            cache.set('blog_detail_page_data',context,60)
        return render(request, "blog/blog_details.html",context)
    except Exception as e:
        print(f"Unknow error: {e}")
        messages.error('An error occurred while loading the Blog Deils page. Please try again later.')
        return render(request, 'errors/404.html')
    


# def blog_detail(request,slug):
#     banner=Blog_Details_Banner.objects.all()
#     post=get_object_or_404(Blog,slug=slug)
#     popular=Blog.objects.order_by('-id')[:5]
#     tag=Tag.objects.all()[:3]
#     cate=Category.objects.all()
#     comment=Comment.objects.filter(post=post).order_by('-date')[:3]

#     context={
#         'banner':banner,
#         'post':post,
#         'tag':tag,
#         'popular':popular,
#         'cate':cate,
#         'slug':slug,
#         'comment':comment,
#         # 'object_or_title': blog.title,

        
#     }
#     return render(request, "blog/blog_details.html",context)


def add_comment(request, slug):
    try:
        # Only handle POST requests
        if request.method == "POST":
            # Get the blog post associated with the slug
            post = get_object_or_404(Blog, slug=slug)

            # Retrieve data from the form submission
            name = request.POST.get("name")
            email = request.POST.get("email")
            comment = request.POST.get("comment")
            website = request.POST.get("website")

            # Create a new comment
            Comment.objects.create(
                name=name,
                email=email,
                comment=comment,
                website=website,
                post=post,
            )

            # Invalidate cache for the blog detail page since new comment is added
            cache.delete(f'blog_detail_{slug}')

        # Redirect to the blog detail page after comment submission
        return redirect('blog:blog_detail', slug=slug)
    except Exception as e:
        print(f"Unknown error: {e}")
        # Send an error message to the user
        messages.error(request, 'An error occurred while processing your comment. Please try again later.')
        # Redirect to a 404 error page in case of failure
        return render(request, 'errors/404.html')
    

    
# def add_comment(request, slug):
#     if request.method == "POST":
#         post=get_object_or_404(Blog, slug=slug)
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         comment = request.POST.get("comment")
#         website = request.POST.get("website")

#         Comment.objects.create(
#             name=name,
#             email=email,
#             comment=comment,
#             website=website,
#             post=post,
#         )
#         return redirect('blog:blog_detail', slug=slug)
#     return redirect('blog:blog_details.html')

