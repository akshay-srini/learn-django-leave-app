from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import CompanyUser, Leaves
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        position = request.POST.get('position')
        if CompanyUser.objects.filter(username=username).exists():
            messages.error(request,"User already exists")
            return redirect('login')
        if password: 
            password = make_password(password)
        User = CompanyUser.objects.create(username=username, password=password, position=position)
        if position == 'manager':
            login(request, User)
            return redirect('manage')
        else:
            login(request,User)
            return redirect('home')
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username, password = password)
        if user:
            login(request, user)
            if user.position == 'manager':
                return redirect('manage')
            else:
                return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    user_position = dict(CompanyUser.position_choices).get(request.user.position)
    casual_leave_records = Leaves.objects.filter(employee=request.user, leave_type='casual', status='successful')
    sick_leave_records = Leaves.objects.filter(employee=request.user, leave_type='sick', status='successful')
    no_of_casual_leaves_applied = Leaves.objects.filter(employee=request.user, leave_type='casual', status='pending')
    no_of_sick_leaves_applied = Leaves.objects.filter(employee=request.user, leave_type='sick', status='pending')
    sum_of_casual_leave_count = sum(record.no_of_days for record in casual_leave_records)
    sum_of_sick_leave_count = sum(record.no_of_days for record in sick_leave_records)
    sum_of_casual_leave_applied = sum(record.no_of_days for record in no_of_casual_leaves_applied)
    sum_of_sick_leaves_applied = sum(record.no_of_days for record in no_of_sick_leaves_applied)
    total_casual_leave_available = 12 - sum_of_casual_leave_count
    total_sick_leave_available = 5 - sum_of_sick_leave_count
    print(f"{sum_of_casual_leave_count}")
    user_info = {
        'user_position': user_position,
        'casual_leave_records': sum_of_casual_leave_count,
        'sick_leave_records': sum_of_sick_leave_count,
        'total_casual_leaves_applied': sum_of_casual_leave_applied,
        'total_sick_leaves_applied': sum_of_sick_leaves_applied,
        'total_casual_leave_available': total_casual_leave_available,
        'total_sick_leave_available': total_sick_leave_available
    }
    if request.method == 'POST':
        no_of_days = request.POST.get('no_of_days')
        leave_type = request.POST.get('leave_type')
        reason = request.POST.get('reason')
        Leaves.objects.create(
            employee=request.user,
            no_of_days=no_of_days,
            leave_type=leave_type,
            reason=reason
        )
        return redirect('home')
    return render(request, 'home.html', user_info)

@login_required(login_url='login')
def manager_home(request):
    leave_records = Leaves.objects.filter(status='pending')
    manager_data = {
        'leave_records': leave_records
    }
    if request.method == 'POST':
        leave_id = request.POST.get('leave_id')
        action = request.POST.get('action')
        leave = Leaves.objects.get(id=leave_id)
        try: 
            if action == 'accept':
                leave.status = 'successful'
                leave.save()
            elif action == 'reject':
                leave.status = 'rejected'
                leave.save()
        except leave.DoesNotExist:
            messages.error('something went wrong, couldnt find the leave record')
        return redirect('manage')
    return render(request, 'manager-home.html', manager_data)