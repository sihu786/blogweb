
# to send date for all page 

from .models import Category

def get_all_category(requsest):
    categorys=Category.objects.all()
    context={
        "categorys":categorys
    }

    return context