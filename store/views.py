from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,Order,OrderItem,Customer,ShippingAddress
from django.http import JsonResponse
from .cart import Cart
from .utils import cookieCart,cartData,guestOrder,getCartDetail
import json
import datetime


def store(request):
	#cart = Cart(request);
	#cart.clear();
	print(request.session);
	data = cartData(request)	
	cartItems = data['cartItems']
	products = Product.objects.all()
	
	context = { "products": products,'cartItems': cartItems}
	return render(request,'store/store.html',context)

def cart(request):
	data = cartData(request)
	items = data['items']
	order = data['order']
	cartItems = data['cartItems']	
	context = { 'items': items, 'order': order, 'cartItems': cartItems}
	return render(request,'store/cart.html',context)

def checkout(request):
	data = cartData(request)
	items = data['items']
	order = data['order']
	cartItems = data['cartItems']
	context = { 'items': items, 'order': order, 'cartItems': cartItems}
	return render(request,'store/checkout.html',context)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body.decode("utf-8"))
	
	customer,order = guestOrder(request,data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id
	#if(total == order.get_order_total):
	order.complete = True
	#Saving order
	order.save()
	#Saving shipping address
	if order.shipping == True:
		ShippingAddress.objects.create(
				customer = customer,
				order = order,
				address = data['shippingInfo']['address'],
				city = data['shippingInfo']['city'],
				state = data['shippingInfo']['state'],
				zipcode = data['shippingInfo']['zipcode']
			);

	return JsonResponse("Payment processed successfully",safe=False)

def displayProduct(request,id):	
	data = cartData(request)
	product = get_object_or_404(Product,id=id)
	cartItems = data['cartItems']
	quantity = getCartDetail(request,id)

	context = { "product": product, "cartItems": cartItems,"quantity": quantity}
	return render(request,"store/detail.html",context)

