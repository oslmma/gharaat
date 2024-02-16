from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


from .models import Student, Score, Jozve, Score_monthly

# it's main page first page that people in there
def home(request):
    if not request.user.is_authenticated:
        return redirect("login/") 
    if request.user.pk - 1 == 0:
        userpk = request.user.pk
    else:
        userpk = request.user.pk - 1
    # print(userpk)
    user = User.objects.get(pk=userpk)
    student = Student.objects.get(user=user)
    return render(request, 'home.html', {'student': student})

# for show top people 
def top_people(request):
    # getting all score of guys
    stu = Student.objects.all()
    context = {
        'students': stu,
    } 
    return render(request, 'top.html', context=context)
    

# show profile actually 
def profile(request, id):
    dmonth = {
        "farvardin": 1,
        "ordibehesht": 2,
        "khordad": 3,
        "tir": 4,
        "mordad": 5,
        "shahrivar": 6,
        "mehr": 7,
        "aban": 8,
        "azar": 9,
        "dey": 10,
        "bahman": 11,
        "esfand": 12,
    }
    data1 = [0,0,0,0,0,0,0,0,0,0,0,0]
    data2 = [0,0,0,0]
    user = User.objects.get(pk=id)
    std = Student.objects.get(pk=user.pk)
    mscore = Score_monthly.objects.filter(user=std.user)
    for ms in mscore:
        data1[dmonth[ms.month]-1] = ms.score
    if not Score.objects.filter(user=std.user): 
        pass
    else: 
        dscore = Score.objects.filter(user=std.user)[::-1][0]
        data2[0] = dscore.say_pray 
        data2[1] = dscore.gharaat
        data2[2] = dscore.payegah
        data2[3] = dscore.setad_namaz
    
    data2 = [i for i in range(1,5)]

    print(data1, data2)

    context = {
        'muser': user,
        'student': std,
        # 'mscore': jsonmscore,
        # 'dscore': jsondscore,
        'mdata': data1,
        'ddata': data2,
    }
    return render(request, 'profile2.html', context)

def jozve(request):
    files = Jozve.objects.all()
    return render(request, 'jozve2.html', {'files': files})


def mylogin(request):
    if request.GET.get('username', None):
        username = request.GET.get("username")
        password = request.GET.get("password")
        print(username, password)
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("home")
    else:
        if request.method== "POST":
            form = AuthenticationForm(request.POST)
            username = request.POST['username']
            password = request.POST['password']
            print(username, password)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, 'نام کاربری یا رمز صحیح نمی باشد.')
                return redirect('login')
        else:    
            form = AuthenticationForm()
            return render(request, "login.html", {'form': form, 'messages': messages})

# def login_with_qrcode(request, code):
#     if request.GET.get('q', None): 
#         r = request.GET.get('q')
#         u = User.objects.get(username=r)
#         user = authenticate(username=u.username, password=u.password)
#         if user is not None:
#             return redirect("home")
#         else:
#             messages.error(request, 'شما هنوز ثبت نشده اید به مسئولین مراجعه کنید.')
#             return redirect("no-register")
#     else:
#         return redirect("no-register")

def no_register(request):
    return render(request, "no-register.html")

def my_logout(request):
    logout(request)
    return redirect("login")

def top_cs(request):
    return render(request, "top-coming-soon4.html")