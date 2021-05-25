from .models import Book, Review
from django import forms
from django.forms import ModelForm

class AddBook(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'cover']
        labels = {'cover': 'Cover Photo:'}

class AddReview(ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'review', 'author']
        

