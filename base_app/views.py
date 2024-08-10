from django.shortcuts import render, redirect
from .models import MenuItem, Reservation, Review
from .forms import ReservationForm, ReviewForm

def index(request):
    return render(request, 'restaurant/index.html')

def menu(request):
    items = MenuItem.objects.all()
    return render(request, 'restaurant/menu.html', {'items': items})

def contact(request):
    return render(request, 'restaurant/contact.html')

def reservations(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('reservations')
    else:
        form = ReservationForm()
    return render(request, 'restaurant/reservations.html', {'form': form})

def reviews(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews')
    else:
        form = ReviewForm()
    reviews = Review.objects.all()
    return render(request, 'restaurant/reviews.html', {'form': form, 'reviews': reviews})

def about(request):
    return render(request, 'restaurant/about.html')
