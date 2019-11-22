from django.db import models
import pytz

class User(models.Model):
    first_name = models.CharField(max_length= 30)
    last_name = models.CharField(max_length= 30)
    password = models.CharField(max_length= 100,default ="password")
    email = models.EmailField()
    tz = models.CharField(max_length= 40,default='Asia/Kolkata')
    monthly_max_limit =  models.IntegerField(default=5000)
    daily_max_limit =  models.IntegerField(default=500)
    join_date = models.DateTimeField('Joining Date')
    preferred_categories = models.CharField(max_length= 2000,default= "['Food & Beeverages', 'Clothes', 'Fuel', 'Shopping', 'Entertainment', 'Health', 'Holiday']")

    def __str__(self):
        return self.email

class Expense(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length= 30)
    expense_date = models.DateTimeField('expense date')
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    additional_note = models.CharField(max_length = 500)

    def layOut(self):

        
        user_timezone = pytz.timezone(self.user.tz)

        return {
            "category": self.category,
            "amount": self.amount,
            "additional_note": self.additional_note,
            "expense_date": (self.expense_date).astimezone(user_timezone),
            "user": self.user.email
        }

