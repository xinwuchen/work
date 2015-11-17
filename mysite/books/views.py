#c4
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from django.shortcuts import *
from books.models import Author,Book
from django.db import models
def Books_information(request,book_ISBN):
    try:
        book_ISBN = int(book_ISBN)
    except ValueError:
        raise Http404()
    books = Book.objects.filter(ISBN = book_ISBN)
    return render_to_response('Books_information.html',locals())

def search(request):
    error = False
    global Name
    if 'query' in request.GET:
        query  = request.GET['query']
        if not query:
            error = True
        else:
            books = Book.objects.filter(Author__Name = query)
            return render_to_response('search_result.html',locals())
    return render_to_response('search_form.html',locals())

def Delete(request):
    ISBN  = request.GET['ISBN']
    book = Book.objects.filter(ISBN = ISBN)
    name = book[0].Author.Name
    query = name
    books = Book.objects.filter(Author__Name__icontains = name)
    Book.objects.filter(ISBN = ISBN).delete()
    return render_to_response('search_result.html',locals())

def Edit(request):
    post=request.POST
    ISBN = request.GET['ISBN']
    errors = []
    if request.method == 'POST':
        if not request.POST.get('AuthorID',''):
            errors.append('请填写作者ID。')
        if not request.POST.get('Name',''):
            errors.append('请填写作者姓名。')
        if not request.POST.get('Age',''):
            errors.append('请填写作者年龄。')
        if not request.POST.get('Country',''):
            errors.append('请填写作者国籍。')
        if not request.POST.get('ISBN',''):
            errors.append('请填写书籍ISBN。')
        if not request.POST.get('Title',''):
            errors.append('请填写书籍标题。')
        if not request.POST.get('Publisher',''):
            errors.append('请填写书籍出版社。')
        if not request.POST.get('PublishDate',''):
            errors.append('请填写书籍出版日期。')
        if not request.POST.get('Price',''):
            errors.append('请填写书籍价格。')
        if not errors:
            books = Book.objects.filter(ISBN=ISBN)
            books.update(ISBN=post['ISBN'],
                        Title=post['Title'],
                        Publisher=post['Publisher'],
                        PublishDate=post['PublishDate'],
                        Price=post['Price'],)
            name = books[0].Author.Name
            author = Author.objects.filter(Name=name)
            author.update(AuthorID=post['AuthorID'],
                          Name=post['Name'],
                          Age=post['Age'],
                          Country=post['Country'],)
            temp = Author.objects.get(Name=name)
            books.update(Author=temp,)
            return render_to_response('edit_success.html',locals())
    books = Book.objects.filter(ISBN = ISBN)
    return render_to_response('edit.html',locals())

def About(request):
    return render_to_response('about.html',locals())

def Home(request):
    return render_to_response('home.html',locals())

def addA(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('AuthorID',''):
            errors.append('请填写作者ID。')
        if not request.POST.get('Name',''):
            errors.append('请填写作者姓名。')
        if not request.POST.get('Age',''):
            errors.append('请填写作者年龄。')
        if not request.POST.get('Country',''):
            errors.append('请填写作者国籍。')
        if not errors:
            post = request.POST
            author = Author(AuthorID=post['AuthorID'],
                  Name=post['Name'],
                  Age=post['Age'],
                  Country=post['Country'],)
            author.save()
            return render_to_response('edit_success.html',locals())
    return render_to_response('addA.html',locals())

def addB(request):
    errors = []
    authors = Author.objects.all()
    if request.method == 'POST':
        if not request.POST.get('ISBN',''):
            errors.append('请填写书籍ISBN。')
        if not request.POST.get('Title',''):
            errors.append('请填写书籍标题。')
        if not request.POST.get('Author',''):
            errors.append('请填写书籍作者。')
        if not request.POST.get('Publisher',''):
            errors.append('请填写书籍出版社。')
        if not request.POST.get('PublishDate',''):
            errors.append('请填写书籍出版日期。')
        if not request.POST.get('Price',''):
            errors.append('请填写书籍价格。')
        if not errors:
            post = request.POST
            name = post['Author']
            temp = Author.objects.get(Name=name)
            book = Book(ISBN=post['ISBN'],
                        Title=post['Title'],
                        Publisher=post['Publisher'],
                        PublishDate=post['PublishDate'],
                        Price=post['Price'],
                        Author=temp,)
            book.save()
            return render_to_response('edit_success.html',locals())
    return render_to_response('addB.html',locals())