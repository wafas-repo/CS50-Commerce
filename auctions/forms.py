from django import forms


from .models import Auction_listings, Comment, Category

def append_categories():
    if(Category is not None):
        CATEGORIES= Category.objects.all().values_list('name','name')# pylint: disable=maybe-no-member
    category_list = []
    for choice in CATEGORIES:
        category_list.append(choice)
    return category_list

class CreateListingForm(forms.ModelForm):
    class Meta:
        model = Auction_listings
        fields = ('title', 'description', 'price', 'image', 'category')
        labels = {"image": " Image URL (optional)", "price": "Starting Bid"}

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'padding': '10px','border-radius': '10px'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'box-shadow':'4px 4px 10px'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.TextInput(attrs={'class': 'form-control', 'padding': '10px','border-radius': '10px'}),
            'category': forms.Select(choices=append_categories(), attrs={'class': 'form-control', 'padding': '10px','border-radius': '10px'}),
            'time_posted': forms.DateTimeField()
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        labels = {"comment": ""}

        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows':'3'})
        }
