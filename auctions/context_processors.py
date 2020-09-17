from .models import Category

def get_context_data(request):
    cat_menu = Category.objects.all()# pylint: disable=maybe-no-member
    return {
        "cat_menu": cat_menu
    }