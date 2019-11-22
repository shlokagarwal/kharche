from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from .models import User,Expense
import json
import datetime
import pytz
import ast



def index(request):
    return HttpResponse("Hello, world. You're at the expenses index.")

def register(request):
    # getting the request body and saving it in body_data
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)

    # checking if user is already registered
    request_email = body_data["email"]
    request_password = body_data["password"]
    try:
        User.objects.get(email = request_email)
        return JsonResponse({"status": "Account already exists."})
    except:     
        q = User(first_name = body_data["first_name"],last_name = body_data["last_name"],email = request_email,join_date= timezone.localtime(),password = request_password)
        q.save()
        return JsonResponse({"id": q.id, "status": "Account created successfully", "joining_date": q.join_date})


def login(request):
    # getting the request body and saving it in body_data
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)

    
    request_email = body_data["email"]
    request_password = body_data["password"]

    try:
        # user account is present
        q = User.objects.get(email = request_email)
        if(q.password == request_password):
            # correct login pass
            return JsonResponse({"id":q.id,"status": "Successful Login."})
        else:
            return JsonResponse({"status": "Authentication details don't match."})    
        
    except:    
        # user account not present 
        return JsonResponse({"status": "User does not exit."})   

def expenses(request):
    # getting the request body and saving it in body_data
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)

    # getting id and date range
    request_id =body_data["id"]
    user_timezone = pytz.timezone(User.objects.get(pk = request_id).tz)
    request_from = datetime.datetime.strptime(body_data["from"],'%d-%m-%Y')
    request_to = datetime.datetime.strptime(body_data["to"],'%d-%m-%Y')
    request_from = request_from.replace(tzinfo=user_timezone)
    request_to = request_to.replace(tzinfo=user_timezone)

    print(type(request_from))
    try:
        q = User.objects.get(pk = request_id)
       
        expenses = q.expense_set.all()
        required_expenses = []
        for expense in expenses:
            print(type(expense.expense_date))
            if(expense.expense_date >= request_from and expense.expense_date <= request_to):
                required_expenses.append(expense.layOut())    
        return JsonResponse({"output": required_expenses})           

        
    except:     
        return JsonResponse({"status": "User does not exit."})   


def get_categories(request):
    # getting the request body and saving it in body_data
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)

    # getting id
    request_id =body_data["id"]

    try:
        q = User.objects.get(pk = request_id)
        current_categories = q.preferred_categories
        return JsonResponse({"user_categories": current_categories})        
    except:     
        return JsonResponse({"status": "User does not exit."})   


def add_expense(request):
    # getting the request body and saving it in body_data
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)

    # getting id
    request_id =body_data["id"]
    request_category = body_data["category"]
    request_amount = body_data["amount"]
    request_additional_note = body_data["additional_note"]

    try:
        q = User.objects.get(pk = request_id)
        q.expense_set.create(category = request_category, amount = request_amount,additional_note=request_additional_note,expense_date = timezone.localtime())     
    except:     
        return JsonResponse({"status": "An error has occured."})   


        