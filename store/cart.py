from decimal import Decimal
from django.conf import settings
from .models import Product

#1IE3H5DRO5JPQ3U4G4RA SESSION_CART_ID
class Cart(object):

	def __init__(self,request):
		'''
		Sets session
		'''
		self.session = request.session
		cart = self.session.get(settings.SESSION_CART_ID)

		if not cart:
			cart = self.session[settings.SESSION_CART_ID]={}

		self.cart = cart

	def add(self,product,quantity=1): #,update_quantity=False
		'''
		Adds item in cart
		'''
		print(product)
		product_id = str(product.id)
		if product_id not in self.cart:
			self.cart[product_id] = {'quantity': quantity, 'price': product.price }
			#print(self.cart[product_id])
		else:
			self.cart[product_id]['quantity'] += quantity
		
		self.save()

	def remove(self,product):
		'''
		Removes item from cart
		'''		
		product_id = str(product.id)
		if product_id in self.cart:		
			del self.cart[product_id]			
			self.save()			

	def increment(self,product):
		product_id = str(product.id)
		self.cart[product_id]['quantity'] += 1
		self.save()

	def decrement(self,product):
		product_id = str(product.id)

		if self .cart[product_id]['quantity'] > 0:
			self.cart[product_id]['quantity'] -= 1
			self.save()
			if self .cart[product_id]['quantity'] == 0:
				self.remove(product)
			

	def save(self):
		'''
		Updates session
		'''
		self.session[settings.SESSION_CART_ID] = self.cart
		self.session.modified = True

	def __iter__(self):
		'''
		Iterate cart
		'''
		product_ids = self.cart.keys()
		print(product_ids)

		products = Product.objects.filter(id__in=product_ids)

		for product in products:
			self.cart[str(product.id)]['product'] = product 

		for item in self.cart.values():
			item['price'] = Decimal(item['price'])
			item['total_price'] = item['price'] * item['quantity']
			yield item

	def __len__(self):
		'''
		Counts all item in cart
		'''
		return sum(item['quantity'] for item in self.cart.values())

	def clear(self):
		'''
		Removes all item from cart session
		'''
		self.session[settings.SESSION_CART_ID] = {}
		self.session.modified = True

	def get_total_price(self):
		'''
		Returns Total Price
		'''
		return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

	def getCartItems(self):
		#self.cart.values() quantity,price cart={"pid":{"quantity": ,"price": }}
		print(self.cart.keys())
		return len(self.cart.keys())