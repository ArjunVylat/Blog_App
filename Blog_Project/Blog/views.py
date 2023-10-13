from django.shortcuts import render

posts = [
    {
        'author' : 'Arjun Krishna',
        'title' : 'Blog Post 1',
        'content' : 'First Post Content',
        'date_posted' : 'August 27, 2023'
    },
    {
        'author' : 'Jane Doe',
        'title' : 'Blog Post 2',
        'content' : 'Second Post Content',
        'date_posted' : 'August 28, 2023'
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'Blog/home.html', context)

def about(request):
    return render(request, 'Blog/about.html', {'title' : 'About'})