from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

from django.db.models.fields.related import ForeignKey  
# Create your models here.

class Login(models.Model):
   Username  = models.CharField(max_length=30,unique=True)
   password  = models.CharField(max_length=30,unique=True)
   Email     = models.CharField(max_length=50)
   EntryDate = models.DateTimeField(auto_now=True)
   def __str__(self):
      return str(self.id)

class LoginDetail(models.Model):
	LoginID   = models.ForeignKey(Login, on_delete=models.CASCADE)
	Username  = models.CharField(max_length=30)
	Email     = models.CharField(max_length=50)
	LoginTime = models.DateTimeField(auto_now=True)

class DistributerPersonalDetail(models.Model):
	FirstName     = models.CharField(max_length=30)
	LastName      = models.CharField(max_length=30)
	FatherName    = models.CharField(max_length=30)
	CNIC          = models.CharField(max_length=13,unique=True,blank=True)
	Age           = models.IntegerField()
	Gender        = models.CharField(max_length=8)
	MaritalStatus = models.CharField(max_length=10)
	EntryDate     = models.DateTimeField(auto_now=True)

class DistributerContactDetail(models.Model):
   DistributerPID = models.ForeignKey(DistributerPersonalDetail,on_delete=models.CASCADE)
   Address        = models.CharField(max_length=100)
   City           = models.CharField(max_length=100)
   Country        = models.CharField(max_length=100)
   PhoneNo        = models.CharField(max_length=13)
   LandLineNo     = models.CharField(max_length=15,blank=True)
   Email          = models.CharField(max_length=50,blank=True)
   Others         = models.CharField(max_length=100,blank=True)
   EntryDate      = models.DateTimeField(auto_now=True)
   def __str__(self):
      return str(self.id)

class DistributerBrandDetail(models.Model):
   DistributerPID = models.ForeignKey(DistributerPersonalDetail, on_delete=models.CASCADE)
   BrandName      = models.CharField(max_length=30,unique=True)
   Address        = models.CharField(max_length=100)
   Email          = models.CharField(max_length=50,unique=True,blank=True)
   PhoneNo        = models.CharField(max_length=13,unique=True)
   EntryDate      = models.DateTimeField(auto_now=True)
   def __str__(self):
      return str(self.id)

class Ingredient(models.Model):
   IngredientName  = models.CharField(max_length=30,unique=True)
   IngredientPrice = models.DecimalField(max_digits=8, decimal_places=2)
   Size            = models.CharField(max_length=10,blank=True)
   Description     = models.CharField(max_length=100,blank=True)
   EntryDate       = models.DateTimeField(auto_now=True)
   def __str__(self):
      return str(self.id)

class ProductPurchase(models.Model):
   BrandID       = models.ForeignKey(DistributerBrandDetail, on_delete=models.CASCADE)
   IngredientID  = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
   PurchasePrice = models.DecimalField(max_digits=8, decimal_places=2)
   Quantity      = models.IntegerField() 
   Size          = models.CharField(max_length=10,blank=True)
   PurchaseDate  = models.DateTimeField(auto_now=True)
   def __str__(self):
      return str(self.id)

class DistributerPayment(models.Model):
   DistributerPID = models.ForeignKey(DistributerPersonalDetail, on_delete=models.CASCADE)
   PurchaseID     = models.ForeignKey(ProductPurchase, on_delete=models.CASCADE)
   PaidAmount     = models.DecimalField(max_digits=8, decimal_places=2)
   RemaningAmount = models.DecimalField(max_digits=8, decimal_places=2) 
   PaymentMethod  = models.CharField(max_length=50)
   PaymentType    = models.CharField(max_length=13)
   EntryDate      = models.DateTimeField(auto_now=True)
   def __str__(self):
      return str(self.id)

class CurrentStock(models.Model):
   IngredientID = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
   Quantity     = models.IntegerField()
   EntryDate    = models.DateTimeField(auto_now=True)
   def __str__(self):
      return str(self.id)

class Product(models.Model):
    name  = models.CharField(max_length=100) 
    price = models.CharField(max_length=100) 
    image = models.ImageField(upload_to='images/')

class Food(models.Model):
   FoodImage       = models.ImageField(upload_to="images/")
   FoodName        = models.CharField(max_length=30,unique=True)
   FoodType        = models.CharField(max_length=50)
   FoodDescription = models.CharField(max_length=100,blank=True)
   EntryDate       = models.DateTimeField(auto_now=True)
   def __str__(self):
      return str(self.id)

class FoodSize(models.Model):
   FoodID    = models.ForeignKey(Food, on_delete=models.CASCADE)
   FoodSize  = models.CharField(max_length=10)
   FoodPrice = models.DecimalField(max_digits=8, decimal_places=2) 
   EntryDate = models.DateTimeField(auto_now=True)
   def __str__(self):
      return str(self.id)

class FoodIngredient(models.Model):
   FoodID       = models.ForeignKey(Food, on_delete=models.CASCADE)
   FoodSizeID   = models.ForeignKey(FoodSize, on_delete=models.CASCADE)
   IngredientID = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
   Quantity     = models.IntegerField()
   Size         = models.CharField(max_length=10)
   EntryDate    = models.DateTimeField(auto_now=True)
   def __str__(self):
      return str(self.id)

class Offers(models.Model):
   OfferName    = models.CharField(max_length=30,unique=True)
   OfferPrice   = models.DecimalField(max_digits=8, decimal_places=2) 
   Availability = models.CharField(max_length=10,blank=True)
   CreateTime   = models.DateTimeField(auto_now=True)
   def __str__(self):
      return str(self.id)

class OffersFood(models.Model):
   OfferID    = models.ForeignKey(Offers, on_delete=models.CASCADE)
   FoodID     = models.ForeignKey(Food, on_delete=models.CASCADE)
   FoodSizeID = models.ForeignKey(FoodSize, on_delete=models.CASCADE)
   Quantity   = models.IntegerField() 
   EntryDate  = models.DateTimeField(auto_now=True)
   def __str__(self):
      return str(self.id)

class EmployeePesonalDetail(models.Model):
   FirstName     = models.CharField(max_length=30)
   LastName      = models.CharField(max_length=30,blank=True)
   CNIC          = models.CharField(max_length=13,unique=True,blank=True)
   FatherName    = models.CharField(max_length=30)
   Age           = models.IntegerField()
   Gender        = models.CharField(max_length=8)
   MaritalStatus = models.CharField(max_length=10)
   EntryDate     = models.DateTimeField(auto_now=True)
   def __str__(self):
      return str(self.id)

class Employee(models.Model):
   EmployeePID       = models.ForeignKey(EmployeePesonalDetail, on_delete=models.CASCADE)
   JobName           = models.CharField(max_length=30)
   EmployeementYears = models.IntegerField()
   Salary            = models.DecimalField(max_digits=8, decimal_places=2) 
   Bonus             = models.DecimalField(max_digits=8, decimal_places=2) 
   DutyStartTime     = models.TimeField(blank=True)
   DutyEndTime       = models.TimeField(blank=True)
   JobDescription    = models.CharField(max_length=100)
   EntryDate         = models.DateTimeField(auto_now=True)
   def __str__(self):
      return str(self.id)

class Customer(models.Model):
   FirstName = models.CharField(max_length=30)
   LastName  = models.CharField(max_length=30,blank=True)
   CNIC      = models.CharField(max_length=13,blank=True)
   PhoneNo1  = models.CharField(max_length=13,blank=True)
   Email     = models.CharField(max_length=50,blank=True)
   Address   = models.CharField(max_length=100,blank=True)
   EntryDate = models.DateTimeField(default=datetime.now(), blank=True)
   def __str__(self):
      return str(self.id)

class CustomerOrderBooking(models.Model):
   CustomerID  = models.ForeignKey(Customer, on_delete=models.CASCADE)
   EmployeePID = models.ForeignKey(EmployeePesonalDetail, on_delete=models.CASCADE) 
   TotalBill   = models.DecimalField(max_digits=8, decimal_places=2) 
   EntryDate   = models.DateTimeField(auto_now=True)
   def __str__(self):
      return str(self.id)

class CustomerOrderDetail(models.Model): 
   CustomerOrderID = models.ForeignKey(CustomerOrderBooking, on_delete=models.CASCADE) 
   ProductName     = models.CharField(max_length=30)
   ProductSize     = models.CharField(max_length=10)
   ProductQuantity = models.IntegerField()
   SalePrice       = models.DecimalField(max_digits=8, decimal_places=2) 
   EntryDate       = models.DateTimeField(auto_now=True)
   def __str__(self):
      return str(self.id)

class EmployeeContactDetail(models.Model):
   EmployeePID = models.ForeignKey(EmployeePesonalDetail, on_delete=models.CASCADE)
   Address1    = models.CharField(max_length=100)
   City        = models.CharField(max_length=100) 
   Country     = models.CharField(max_length=100)
   PhoneNo1    = models.CharField(max_length=13,unique=True)
   LandLineNo  = models.CharField(max_length=15,blank=True)
   Email       = models.CharField(max_length=50,blank=True)
   EntryDate   = models.DateTimeField(auto_now=True)
   def __str__(self):
      return str(self.id)

class Qualification(models.Model):
   EmployeePID   = models.ForeignKey(EmployeePesonalDetail, on_delete=models.CASCADE)
   DegreeName    = models.CharField(max_length=50)
   InstituteName = models.CharField(max_length=50)
   PassingYear   = models.CharField(max_length=10,blank=True)
   ObtainedMarks = models.IntegerField()
   TotalMarks    = models.IntegerField()
   Grade         = models.CharField(max_length=2,blank=True)
   Other         = models.CharField(max_length=100,blank=True)
   EntryDate     = models.DateTimeField(auto_now=True)
   def __str__(self):
      return str(self.id)

class EmployeeSkill(models.Model):
   EmployeePID         = models.ForeignKey(EmployeePesonalDetail, on_delete=models.CASCADE)
   SkillName           = models.CharField(max_length=50)
   OrganizationName    = models.CharField(max_length=50)
   CertificationNumber = models.CharField(max_length=50,blank=True)
   LearnStartDate      = models.DateField()
   LearnEndDate        = models.DateField()
   Others              = models.CharField(max_length=100,blank=True)
   EntryDate           = models.DateTimeField(auto_now=True)
   def __str__(self):
      return str(self.id)

class EmployeePrevoiusExperiance(models.Model):
   EmployeePID      = models.ForeignKey(EmployeePesonalDetail, on_delete=models.CASCADE)
   OrganizationName = models.CharField(max_length=50)
   JobName          = models.CharField(max_length=50)
   JobDescription    = models.CharField(max_length=100,blank=True)
   StartDate        = models.DateField()
   EndDate          = models.DateField()
   Others           = models.CharField(max_length=100,blank=True)
   EntryDate        = models.DateTimeField(auto_now=True)
   def __str__(self):
      return str(self.id)

class CustomerOrderPayment(models.Model):
   CustomerOrderID  = models.ForeignKey(CustomerOrderBooking, on_delete=models.CASCADE) 
   PaymentMedium    = models.CharField(max_length=50)
   PaymentAmount    = models.DecimalField(max_digits=8,decimal_places=2)
   EntryDate        = models.DateTimeField(auto_now=True)
   def __str__(self):
      return str(self.id)

class Delivery(models.Model):
   EmployeePID     = models.ForeignKey(EmployeePesonalDetail, on_delete=models.CASCADE)
   CustomerOrderID = models.ForeignKey(CustomerOrderBooking, on_delete=models.CASCADE) 
   DeliveryAddress = models.CharField(max_length=100)
   ExpectedTime    = models.CharField(max_length=10)
   EntryDate       = models.DateTimeField(auto_now=True)
   def __str__(self):
      return str(self.id)

class Extras(models.Model):
   EmployeePID    = models.ForeignKey(EmployeePesonalDetail, on_delete=models.CASCADE)
   ExtrasName     = models.CharField(max_length=30)
   ExtrasType     = models.CharField(max_length=10)
   ExtrasQuantity = models.IntegerField(blank=True)
   Amount         = models.DecimalField(max_digits=8,decimal_places=2)
   Description    = models.CharField(max_length=250)
   EntryDate      = models.DateTimeField(auto_now=True)
   def __str__(self):
      return str(self.id)

class contactus(models.Model):
   Name      = models.CharField(max_length=30)
   Email     = models.CharField(max_length=50)
   Message   = models.CharField(max_length=250)
   EntryDate = models.DateTimeField(auto_now=True)
   def __str__(self):
      return str(self.id)
class WebResources(models.Model):
   Location  = models.CharField(max_length=250,blank=True)
   Phone = models.CharField(max_length=13,unique=True,blank=True)
   Day   = models.CharField(max_length=10,blank=True)
   OpeningTime = models.TimeField(blank=True)
   ClosingTime = models.TimeField(blank=True)
   LinkedInLink = models.CharField(max_length=100,blank=True)
   GitLink = models.CharField(max_length=100,blank=True)
   TwitterLink = models.CharField(max_length=100,blank=True)
   FbLink = models.CharField(max_length=100,blank=True)
   EntryDate = models.DateTimeField(auto_now=True)
   def __str__(self):
      return str(self.id)
class CEO(models.Model):
   Image     = models.ImageField(upload_to="images/")
   Name      = models.CharField(max_length=30)
   Rank      = models.CharField(max_length=50)
   EntryDate = models.DateTimeField(auto_now=True)
   def __str__(self):
      return str(self.id)

#------cart-------------------
class Req_info(models.Model):
    status=models.CharField(max_length=255, default='Pending')
    Name_Costomer=models.CharField(max_length=255, null=True)
    GrandTotal=models.FloatField(  null=True,default='0.00' )
    def __str__(self):
      return str(self.id)

class OrdereProduct(models.Model):
    order = models.ForeignKey(Req_info, on_delete=models.CASCADE)
    CustomerID = models.IntegerField(null=True)
    Name_Costomer=models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity= models.FloatField()

    def __str__(self):
        return str(self.order)
#--------endcart---------------