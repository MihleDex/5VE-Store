from django.shortcuts import redirect
from django_unicorn.components import UnicornView, QuerySetType
from django.contrib.auth.models import User
from django.db.models import F
from main.models import UserItem 

class CartView(UnicornView):
    user_items: QuerySetType[UserItem] = None
    user_pk: int
    total: float = 0
    shipping: float = 150.0
    item_total:float =0

    def __init__(self,*args, **kwargs):
        super().__init__(**kwargs)
        self.user_pk = kwargs.get('user')
        self.user_items = UserItem.objects.filter(user=self.user_pk)
        self.get_total()
    

    def add_item(self,item_pk):
        item, created = UserItem.objects.get_or_create(
        user_id =self.user_pk,product_id=item_pk
        )

        if not created:
            item.quantity = F('quantity') + 1
            item.save()
        self.user_items = UserItem.objects.filter(user=self.user_pk)
        self.get_total()
        return redirect('/')


    def get_total(self):
        self.total = sum(
            product.total_price for product in self.user_items
        )
        self.total = self.total + self.shipping
        self.item_total = self.total - self.shipping

    def delete_item(self, item_pk):
        item = UserItem.objects.filter(pk=item_pk)
        item.delete()
        self.user_items = self.user_items.exclude(pk=item_pk)
        self.get_total()
        return redirect('/')


        
