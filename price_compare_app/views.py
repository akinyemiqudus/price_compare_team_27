from multiprocessing import context

from django.shortcuts import get_object_or_404, render

from price_compare_app.form import ReviewForm

from .form import ReviewForm
from .models import Phone

#from pyexpat import model


# Create your views here.

def home_page(request):
    if 'q' in request.GET:
        q = request.GET['q']
        all_phone = Phone.objects.filter(name__icontains=q)
    
    else:
        all_samsung= Phone.objects.filter(brand__name__icontains='samsung')
        all_iphones= Phone.objects.filter(brand__name__icontains='iphone')
        all_huawei= Phone.objects.filter(brand__name__icontains='huawei')


    context={
        'iphones':all_iphones,
        'samsung':all_samsung,
        'huawei':all_huawei
    }

    return render(request,'price_compare_app/index.html',context)


def about_page(request):
    return render(request,'price_compare_app/about.html')

def PhoneDetailView(request, id):
    data = get_object_or_404(Phone, pk=id)
    reviews = data.reviews
    new_review = None

    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():

            # Create Comment object but don't save to database yet
            new_review = review_form.save(commit=False)
            # Assign the current post to the comment
            new_review.data = data
            # Save the comment to the database
            new_review.save()
    else:
        review_form = ReviewForm()

    context = {"data":data,
               "reviews": reviews,
               "new_review": new_review,
               "review_form": review_form}
    return render(request, 'price_compare_app/details-test.html', context)