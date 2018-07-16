from django.shortcuts import render,HttpResponse,redirect
from app01.models import Book

# Create your views here.
def index(request):
    if request.method=='POST':
        return redirect('/add/')
    else:
        book_list = Book.objects.all()
        # for book in book_list:
        #     print(book.price)
        # return HttpResponse('tianjia')
        return render(request,'index.html',{'book_list':book_list})

def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        publish = request.POST.get('publish')
        Book.objects.create(title=title,price=price,pub_date=pub_date,publish=publish)
        return redirect('/index/')
    return render(request,'add.html')


def update(request,id):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        publish = request.POST.get('publish')
        Book.objects.filter(id=id).update(title=title,price=price,pub_date=pub_date,publish=publish)
        return redirect('/index/')

    book_list = Book.objects.filter(id=id)
    return render(request,'update.html',{'book_list':book_list})

def bookdel(request,id):
    Book.objects.filter(id=id).delete()
    return redirect('/index/')