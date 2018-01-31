from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page


def about(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request,'rango/about.html', context=context_dict)

def index(request):

    category_list = Category.objects.order_by('-likes')[:5]
    #print (category_list)
    context_dict = {'categories': category_list}

    mostViewed_list = Page.objects.order_by('-views')[:5]
    #print (mostViewed_list)
    mostViewed_dict = {'mostViewed':  mostViewed_list}


    return render(request, 'rango/index.html',context_dict, mostViewed_dict)

def show_category(request, category_name_slug):

    context_dict = {}

    try:

        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category=category)


        context_dict['pages'] = pages
       

        context_dict['category'] = category

    except Category.DoesNotExist:

    
        context_dict['category'] = None
        context_dict['pages'] = None


    return render(request, 'rango/category.html', context_dict)

def show_mostViewed(request, pages_name_slug):


    mostViewed_dict = {}

    try:

        
        pages = Page.objects.filter(category=category)
        mostViewed_dict['pages'] = pages
        mostViewed_dict['views'] = views
      
        mostViewed_list = Page.objects.order_by('-views')[:5] 
        mostViewed_dict = {'mostViewed':  mostViewed_list}

    except Category.DoesNotExist:
        
        mostViewed_dict['pages'] = None
        mostViewed_dict['views'] = None


    return render(request, 'rango/index.html',mostViewed_dict)
    

