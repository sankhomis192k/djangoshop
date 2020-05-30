from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
	user = models.OneToOneField(User,null=True,blank=True,on_delete = models.CASCADE);
	name = models.CharField(max_length=50, null=True)
	email = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=50, null=True)
	price = models.DecimalField(max_digits=7,decimal_places=2)
	digital = models.BooleanField(default=False)
	image = models.CharField(max_length=50,null=True,blank=True)

	def __str__(self):
		return self.name

	@property
	def imageUrl(self):
		try:
			url = self.image #self.image.url when image is ImageField
		except:
			url = ''
		return url
	

class Order(models.Model):
	customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)	
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=50,null=True)

	def __str__(self):
		return str(self.id)

	@property
	def shipping(self):
		shipping = False
		orderItems = self.orderitem_set.all()
		for item in orderItems:
			if item.product.digital == False:
				shipping = True

		return shipping
	

class OrderItem(models.Model):
	product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
	order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
	quantity = models.IntegerField(default=0,null=True,blank=True)
	data_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.id)


class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
	order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
	address = models.CharField(max_length=50,null=False)
	city = models.CharField(max_length=50,null=False)
	state = models.CharField(max_length=50,null=False)
	zipcode = models.CharField(max_length=50,null=False)
	data_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address





