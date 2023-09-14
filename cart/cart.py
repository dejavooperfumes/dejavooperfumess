from decimal import Decimal
from django.conf import settings
from perfumes.models import products, productsize


class Cart(object):
    def __init__(self, request):
        
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        
        

    '''def add(self, product,psize, quantity=1, update_quantity=False):
        product_id = str(product.id)
        
        if product_id not in self.cart:
            if product.type=='Oriental' and psize=='6ML':
                self.cart[product_id] = {'quantity': 0, 'price': str(product.sellingprice),'psize':psize}
            elif product.type=='Oriental' and psize=='12ML':
                self.cart[product_id] = {'quantity': 0, 'price': str(product.sellingprice12),'psize':psize}
            else:
                self.cart[product_id] = {'quantity': 0, 'price': str(product.sellingprice),'psize':psize}
        if product_id in self.cart and self.cart[product_id]['psize']!=psize:   
            if product.type=='Oriental' and psize=='6ML':
                self.cart[product_id] = {'quantity': 0, 'price': str(product.sellingprice),'psize':psize}
            elif product.type=='Oriental' and psize=='12ML':
                self.cart[product_id] = {'quantity': 0, 'price': str(product.sellingprice12),'psize':psize}
            else:
                self.cart[product_id] = {'quantity': 0, 'price': str(product.sellingprice),'psize':psize} 
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
           
        else:
            self.cart[product_id]['quantity'] += quantity
            
        a=dict(self.cart[product_id])
        print(a['quantity'])
        print(self.cart[product_id]['psize'])
        self.save()'''
    def add(self,product,size_,quantity=1,update_quantity=False):
        size_id = str(size_.id)
        if size_id not in self.cart:
            if size_.sellingprice:
                self.cart[size_id] = {'quantity': 0, 'price': size_.sellingprice}
        if update_quantity:
            self.cart[size_id]['quantity']=quantity
        else:
            self.cart[size_id]['quantity'] += quantity
        self.save()
  
    
    def save(self):
        self.session[settings.CART_SESSION_ID]=self.cart
        self.session.modified = True   

    def remove(self,size_):
        product_id = str(size_.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        sizes_ids = self.cart.keys()
        productss = productsize.objects.filter(id__in=sizes_ids)
        for size in productss:
            self.cart[str(size.id)]['size'] = size

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
