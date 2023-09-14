from django.shortcuts import render, redirect
from .models import *
from .forms import OrderCreateForm
from cart.cart import Cart
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import razorpay
from django.http import HttpResponse
import uuid  
from phonepe.sdk.pg.payments.models.request_v1.pg_pay_request import PgPayRequest  
from phonepe.sdk.pg.payments.payment_client import PhonePePaymentClient  
from phonepe.sdk.pg.env import Env

merchant_id = "PGTESTPAYUAT"  
salt_key = "099eb0cd-02cf-4e2a-8aca-3e6c6aff0399"  
salt_index = 1 # insert your salt index  
env = Env.UAT  
should_publish_events = True  
phonepe_client = PhonePePaymentClient(merchant_id, salt_key, salt_index, env, should_publish_events)

merchant_transaction_id = str(uuid.uuid4())  
ui_redirect_url = "http://127.0.0.1:8000/orders/sucess/"  
s2s_callback_url = "http://127.0.0.1:8000/orders/callback/"  

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        
        form = OrderCreateForm(request.POST,initial={'userid': request.user.id}, user=request.user)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['size'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            #cart.clear()
            amount=int(request.POST.get("ordertotal"))*100
            name=str(order.first_name+" "+order.last_name)
            orderid=str(order.id)
            
            id_assigned_to_user_by_merchant = name  
            pay_page_request = PgPayRequest.pay_page_pay_request_builder(merchant_transaction_id=merchant_transaction_id,  
                                                                        amount=amount,  
                                                                        merchant_user_id=id_assigned_to_user_by_merchant,  
                                                                        callback_url=s2s_callback_url,  
                                                                        redirect_url=ui_redirect_url)  
            pay_page_response = phonepe_client.pay(pay_page_request)  
            pay_page_url = pay_page_response.data.instrument_response.redirect_info.url
            print(pay_page_url)
            #client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
           
            order = Ordernow.objects.create(
                name=name, amount=amount, provider_order_id=orderid
            )
            order.save()
            print(order)
            o1=Order.objects.get(id=orderid)
            o1.paid=True
            o1.save()
            print(o1)
           
        #return render(request, "orders/order/payment.html")
        return redirect(pay_page_url)

        #return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm(initial={'userid': request.user.id}, user=request.user)
    return render(request, 'orders/order/create.html', {'form': form})




@csrf_exempt
def sucess(request):
    cart = Cart(request)
    cart.clear()
    response = phonepe_client.check_status(merchant_transaction_id)
    print(response)
    return render(request,"orders/order/sucess.html")

@csrf_exempt
def callback(request):
    cart = Cart(request)
    cart.clear()
    #razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))
    #    return client.utility.verify_payment_signature(response_data)
    response = phonepe_client.check_status(merchant_transaction_id)
    print(response)
    