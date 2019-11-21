from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length= 30)
    last_name = models.CharField(max_length= 30)
    email = models.EmailField()
    monthly_max_limit =  models.IntegerField()
    daily_max_limit =  models.IntegerField()
    join_date = models.DateTimeField('Joining Date')
    preferred_cateogies = models.CharField(max_length= 2000,default= "['Food & Beeverages', 'Clothes', 'Fuel', 'Shopping', 'Entertainment', 'Health', 'Holiday']")
    


class Expense(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length= 30)
    expense_date = models.DateTimeField('expense date')
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    additional_note = models.CharField(max_length = 500)

