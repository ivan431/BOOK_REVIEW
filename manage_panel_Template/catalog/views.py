from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, ProductComment, BookReview

MENU = {"главная стр.":"/", "каталог":"/catalog", "о приложении":"/about", "добавить отзыв":"/catalog/add_review"}


def catalog_page(request):
   products = Product.objects.all
   title = "Каталог"
   data = {"menu": MENU, "title": title, 'products':products}
   return render(request, "./catalog.html", context=data)

def add_comment_page(request):
   products = Product.objects.values('id','name')
   title = "Добавить комментарий"
   data = {"menu": MENU, "title": title, 'products':products}
   return render(request, "./add_comment.html", context=data)

def thanks_page(request):
   user_name=request.POST['user_name']
   comment=request.POST['comment']
   product=Product.objects.get(pk=request.POST['product'])
   ProductComment.objects.create(user_name=user_name, comment=comment, product=product)
   title = "Благодарности"
   data = {"menu": MENU, "title": title, 'user_name': user_name}
   return render(request, "./thanks.html", context=data)

def add_comment_fitbacks_page(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '')
        email = request.POST.get('email', '')
        review_text = request.POST.get('review_text', '')
        checked = request.POST.get('checked', False) == 'on'

        BookReview.objects.create(full_name=full_name, email=email, review_text=review_text, checked=checked)

        title = "Отзыв успешно отправлен"
        data = {"menu": MENU, "title": title}
        return render(request, "./feedback_success.html", context=data)

    reviews = BookReview.objects.filter(checked=True)
    print(reviews)

    title = "Форма отзывов"
    data = {"menu": MENU, "title": title, "reviews": reviews}
    print(reviews)
    return render(request, "./fitbacks.html", context=data)

def feedbacks_page(request):
 if request.method == 'POST':
     full_name = request.POST.get('full_name', '')
     email = request.POST.get('email', '')
     review_text = request.POST.get('review_text', '')
     checked = request.POST.get('checked', False) == 'on'

     BookReview.objects.create(full_name=full_name, email=email, review_text=review_text, checked=checked)

     title = "Отзыв успешно отправлен"
     data = {"menu": MENU, "title": title}
     return render(request, "./feedback_success.html", context=data)

 reviews = BookReview.objects.filter(checked=True)
 print(reviews)

 title = "Форма отзывов"
 data = {"menu": MENU, "title": title, "reviews": reviews}
 print(reviews)
 return render(request, "./fitbacks.html", context=data)
