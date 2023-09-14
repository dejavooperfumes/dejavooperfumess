from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class category(models.Model):
    type=models.CharField(max_length=20)
    photo=models.ImageField(upload_to='category/')
    class Meta:
        db_table="category"
    def __str__(self):
        return self.type

class brand(models.Model):
    name=models.CharField(max_length=50)
    photo=models.ImageField(upload_to='brand/')
    class Meta:
        db_table="brand"
    def __str__(self):
        return self.name

    
class products(models.Model):
    sizechoice=(
        ('50ML','50ML'),
        ('6ML 12ML','6ML 12ML'),
        ('6ML','6ML'),
        ('12ML','12ML'),
    )
    typechoice=(
        ('Perfume','Perfume'),
        ('Oriental','Oriental')
    )
    tags=(
        ('Luxury','Luxury'),
        ('Top','Top'),
        ('All','All')
    )
    name=models.CharField(max_length=50)
    photo1=models.ImageField(upload_to='product/')
    photo2=models.ImageField(upload_to='product/')
    photo3=models.ImageField(upload_to='product/',default='All')
    mrp=models.CharField(max_length=10)
    sellingprice=models.CharField(max_length=10)
    description=models.TextField()
    brandid=models.ForeignKey(brand,on_delete=models.CASCADE)
    categoryid=models.ForeignKey(category,on_delete=models.CASCADE)
    size=models.CharField(max_length=20,choices=sizechoice)
    type=models.CharField(max_length=20,choices=typechoice)
    tag=models.CharField(max_length=20,choices=tags,default='All')
    mrp12=models.CharField(max_length=10,default="")
    sellingprice12=models.CharField(max_length=10,default="")


    def __str__(self):
        return self.name


class feedback(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    message=models.TextField()
    class Meta:
        db_table="feedback"
    def __str__(self):
        return self.name
    

class review(models.Model):
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    productsid=models.ForeignKey(products,on_delete=models.CASCADE)
    username=models.CharField(max_length=50)  
    rating=models.CharField(max_length=10)
    message=models.TextField()
    photo=models.ImageField(upload_to='review/',default="")
    class Meta:
        db_table="review"
    def __str__(self):
        return self.username
    
class productsize(models.Model):
    sizechoice=(
        ('50ML','50ML'),
        ('6ML 12ML','6ML 12ML'),
        ('6ML','6ML'),
        ('12ML','12ML'),
        ('100ML','100ML'),
    )
    productid=models.ForeignKey(products,on_delete=models.CASCADE, related_name="sizes")
    size=models.CharField(max_length=20,choices=sizechoice)
    mrp=models.CharField(max_length=10)
    sellingprice=models.CharField(max_length=10)   
    def __str__(self):
        return self.size