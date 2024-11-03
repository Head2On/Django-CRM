from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from  .forms import SignUpForm,AddRecordForm
from .models import Customer

# Create your views here.
def home(request):
    customers = Customer.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.success(request, 'invalid username or password please check and refill !')
            return redirect('home')
    else:
        return render(request, 'home.html', {'customers':customers})

def logout_user (request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #  Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request,"You have successfully register..")
            return redirect('home')
    else:
        form = SignUpForm()       
        return render(request,'register.html', {'form':form})
    return render(request,'register.html', {'form':form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Customer.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You must be logged in to view this page..")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Customer.objects.get(id =pk)
        delete_it.delete()
        messages.success(request, "Delete successfull ✅")
        return redirect('home')
    else:
        messages.success(request, "Sorry you are not loged in..")
        return redirect('home')
    
def add_customer(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                new_customer = form.save()
                messages.success(request, f"Record for {new_customer.first_name} added successfully.")
                return redirect('home')
        return render(request, 'add_customer.html', {'form': form})
    else:
        messages.error(request, "You must be logged in to add a record.")
        return redirect('home')


def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Customer.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			new_customer = form.save()
			messages.success(request, f"Record for {new_customer.first_name} update successfully.")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')