import json
from .models import Product,Order,OrderItem,Customer

def cookieCart(request):
	
	items = []
	order = { 'get_order_total': 0, 'get_order_items': 0,'shipping': False}
	cartItems = order['get_order_items'];

	try:
		cart = json.loads(request.COOKIES['cookieCart']);
	except:
		cart = {}

	for i in cart:
		try:
			cartItems += cart[i]['quantity']
			product = Product.objects.get(id=i)
			total = float(product.price*cart[i]['quantity'])

			order['get_order_total'] += total
			order['get_order_items'] += cart[i]['quantity']
			item = {
				'product': {
					'id': product.id,
					'name': product.name,
					'price': product.price,
					'imageUrl': product.imageUrl
				},
				'quantity':cart[i]['quantity'],
				'get_total': total
			}
			items.append(item)

			if(product.digital == False):
				order['shipping']=True
		except:
			pass
	return { 'cartItems':cartItems,'items':items,'order':order}

def cartData(request):	
	cookieData = cookieCart(request)
	cartItems = cookieData['cartItems']
	order = cookieData['order']
	items = cookieData['items']

	
	return { 'cartItems': cartItems, 'order': order, 'items': items }

def guestOrder(request,data):
	name = data['form']['name']
	email = data['form']['email']

	cookieData = cookieCart(request)
	items = cookieData['items']
	customer,created = Customer.objects.get_or_create(email=email)

	if request.user.is_authenticated:
		customer.user = request.user

	customer.name = name
	customer.save()
	#print(customer)
	order = Order.objects.create(
			customer=customer,
			complete=False
		)

	for item in items:
		product = Product.objects.get(id=item['product']['id'])
		orderItem = OrderItem.objects.create(
				product=product,
				order=order,
				quantity=item['quantity']
			)
	request.COOKIES['cookieCart']={}
	
	return customer,order


def getCartDetail(request,id):
	try:
		cart = json.loads(request.COOKIES['cookieCart']);
	except:
		cart = {}

	itemId = str(id)
	quantity = 0;

	if itemId in cart.keys():
		quantity = cart[itemId]['quantity'];
		

	return quantity