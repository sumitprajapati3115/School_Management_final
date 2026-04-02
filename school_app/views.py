from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render
import openpyxl

from .models import Student, News, Admission, Event, Notice,LiveNews, Gallery
from .models import HeroSection
from .models import About
from .models import PrincipalManager
from .models import StudentLife
from .models import CampusEvent
from .models import GalleryImage
from .models import Contact
from .models import ContactInfo
# ------------------- HOME -------------------
def index(request):

    if request.method == "POST":
        Admission.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            mobile=request.POST.get('mobile'),
            course=request.POST.get('course'),
            photo=request.FILES.get('photo'),
            aadhar_card=request.FILES.get('aadhar_card'),
            birth_certificate=request.FILES.get('birth_certificate'),
            status="Pending"
        )
        return redirect('index')
     
    context = {
        'news': News.objects.all().order_by('-id'), 
        'events': Event.objects.all().order_by('date'),
        'notices': Notice.objects.all().order_by('-date_posted'),
        'live_news': LiveNews.objects.filter(is_active=True).order_by('-created_at'),
        'hero': HeroSection.objects.first(),
        'about': About.objects.first(),
        'pm': PrincipalManager.objects.first(),
        'students_life': StudentLife.objects.all(),
        'campus_events': CampusEvent.objects.all(),
        'gallery_images': GalleryImage.objects.all(),   
        'contact': ContactInfo.objects.first()
    }       
    
    return render(request, 'index.html', context)



# ------------------- ADMIN LOGIN -------------------
def admin_login(request):
    error = None

    if request.method == "POST":
        username = request.POST.get("admin_username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            error = "Invalid username or password"

    return render(request, 'admin_login.html', {'error': error})


def admin_logout(request):
    logout(request)
    return redirect('index')


# ------------------- DASHBOARD -------------------
@login_required(login_url='admin_login')
def admin_dashboard(request):
    students = Student.objects.all()
    admissions = Admission.objects.all()
    live_news = LiveNews.objects.filter(is_active=True).order_by('-created_at')
    gallery = Gallery.objects.all()


    context = {
        "students": students,
        "admissions": admissions,
        "total_students": students.count(),
        "total_admissions": admissions.count(),
        "approved": Admission.objects.filter(status="Approved").count(),
        "pending": Admission.objects.filter(status="Pending").count(),
        "news": News.objects.all(),
        "events": Event.objects.all(),
        "notices": Notice.objects.all(),
        'live_news': live_news,
        'gallery': gallery,
    }

    return render(request, 'admin_dashboard.html', context)


# ------------------- STUDENT -------------------
@login_required(login_url='admin_login')
def add_student(request):
    if request.method == "POST":
        admission = Admission.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            mobile=request.POST.get('mobile'),
            course=request.POST.get('course'),
            photo=request.FILES.get('photo'),
            aadhar_card=request.FILES.get('aadhar_card'),
            birth_certificate=request.FILES.get('birth_certificate'),
            status="Approved"
        )

    Student.objects.create(
    student_id="STD" + str(admission.id),
    name=admission.name,
    student_class=admission.course,
    mobile=admission.mobile,
    status="Approved"
)


    return redirect('admin_dashboard')


@login_required(login_url='admin_login')
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.student_id = request.POST['student_id']
        student.name = request.POST['name']
        student.student_class = request.POST['student_class']
        student.mobile = request.POST['mobile']
        student.save()
        return redirect('admin_dashboard')

    return render(request, 'edit_student.html', {'student': student})


@login_required(login_url='admin_login')
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('admin_dashboard')


# ------------------- ADMISSION -------------------
@login_required(login_url='admin_login')
def edit_admission(request, id):
    admission = get_object_or_404(Admission, id=id)

    if request.method == "POST":
        admission.name = request.POST.get('name')
        admission.email = request.POST.get('email')
        admission.mobile = request.POST.get('mobile')
        admission.course = request.POST.get('course')

        if request.FILES.get('photo'):
            admission.photo = request.FILES['photo']

        if request.FILES.get('aadhar_card'):
            admission.aadhar_card = request.FILES['aadhar_card']

        if request.FILES.get('birth_certificate'):
            admission.birth_certificate = request.FILES['birth_certificate']

        admission.save()
        return redirect('admin_dashboard')

    return render(request, 'edit_admission.html', {'a': admission})


@login_required(login_url='admin_login')
def delete_admission(request, id):
    admission = get_object_or_404(Admission, id=id)
    admission.delete()
    return redirect('admin_dashboard')


@login_required(login_url='admin_login')
def approve_admission(request, id):
    admission = get_object_or_404(Admission, id=id)

    if admission.status != "Approved":
        Student.objects.create(
            student_id="STD" + str(admission.id),
            name=admission.name,
            student_class=admission.course,
            mobile=admission.mobile,
            status="Approved"
        )

        admission.status = "Approved"
        admission.save()

    return redirect('admin_dashboard')


@login_required(login_url='admin_login')
def add_admission(request):
    if request.method == "POST":
        Admission.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            mobile=request.POST.get('mobile'),
            course=request.POST.get('course'),
            photo=request.FILES.get('photo'),
            aadhar_card=request.FILES.get('aadhar_card'),
            birth_certificate=request.FILES.get('birth_certificate'),
            status="Pending"
        )
    return redirect('admin_dashboard')


# ------------------- NEWS -------------------
@login_required(login_url='admin_login')
def add_news(request):
    if request.method == "POST":
        News.objects.create(
            title=request.POST.get('title'),
            is_new=request.POST.get('is_new') == 'on'
        )
    return redirect('admin_dashboard')


@login_required(login_url='admin_login')
def edit_news(request, id):
    news = get_object_or_404(News, id=id)

    if request.method == "POST":
        news.title = request.POST.get('title')
        news.save()
        return redirect('admin_dashboard')

    return render(request, 'edit_news.html', {'n': news})


@login_required(login_url='admin_login')
def delete_news(request, id):
    news = get_object_or_404(News, id=id)
    news.delete()
    return redirect('admin_dashboard')


# ------------------- EVENTS -------------------
@login_required(login_url='admin_login')
def add_event(request):
    if request.method == "POST":
        Event.objects.create(
            title=request.POST.get('title'),
            date=request.POST.get('date'),
            description=request.POST.get('description', '')
        )
    return redirect('admin_dashboard')


@login_required(login_url='admin_login')
def edit_event(request, id):
    event = get_object_or_404(Event, id=id)

    if request.method == "POST":
        event.title = request.POST.get('title')
        event.date = request.POST.get('date')
        event.description = request.POST.get('description', '')
        event.save()
        return redirect('admin_dashboard')

    return render(request, 'edit_event.html', {'e': event})


@login_required(login_url='admin_login')
def delete_event(request, id):
    event = get_object_or_404(Event, id=id)
    event.delete()
    return redirect('admin_dashboard')


# ------------------- NOTICES -------------------
@login_required(login_url='admin_login')
def add_notice(request):
    if request.method == "POST":
        Notice.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description', '')
        )
    return redirect('admin_dashboard')


@login_required(login_url='admin_login')
def edit_notice(request, id):
    notice = get_object_or_404(Notice, id=  id)

    if request.method == "POST":
        notice.title = request.POST.get('title')
        notice.description = request.POST.get('description', '')
        notice.save()
        return redirect('admin_dashboard')

    return render(request, 'edit_notice.html', {'no': notice})


@login_required(login_url='admin_login')
def delete_notice(request, id):
    notice = get_object_or_404(Notice, id=id)
    notice.delete()
    return redirect('admin_dashboard')


# ------------------- EXPORT EXCEL -------------------
@login_required(login_url='admin_login')
def export_students(request):
    wb = openpyxl.Workbook()
    ws = wb.active

    ws.append(['Student ID', 'Name', 'Class', 'Mobile'])

    for s in Student.objects.all():
        ws.append([s.student_id, s.name, s.student_class, s.mobile])

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=students.xlsx'

    wb.save(response)
    return response

def add_live_news(request):
    if request.method == "POST":
        text = request.POST['text']
        LiveNews.objects.create(text=text)
        return redirect('admin_dashboard')


def delete_live_news(request, id):
    LiveNews.objects.get(id=id).delete()
    return redirect('admin_dashboard')

from django.shortcuts import get_object_or_404

def edit_live_news(request, id):
    news = get_object_or_404(LiveNews, id=id)

    if request.method == "POST":
        news.text = request.POST['text']
        news.save()
        return redirect('admin_dashboard')

    return render(request, 'edit_live_news.html', {'news': news})

def students_page(request):
    students = Student.objects.all()
    return render(request, 'students_page.html', {'students': students})

def news_page(request):
    news = News.objects.all()
    return render(request, 'news_page.html', {'news': news})

def web_content(request):
    return render(request, 'web_content.html', {
        'hero': HeroSection.objects.first(),
        'contact': ContactInfo.objects.first(),
        'student_life': StudentLife.objects.all(),
        'events': CampusEvent.objects.all(),
        'gallery': GalleryImage.objects.all(),
    })
    
def update_hero(request):
    hero = HeroSection.objects.first()

    if not hero:
        hero = HeroSection.objects.create()

    if request.method == "POST":
        hero.title = request.POST.get('title')
        hero.subtitle = request.POST.get('subtitle')

        if request.FILES.get('slide1'):
            hero.slide1 = request.FILES['slide1']

        if request.FILES.get('slide2'):
            hero.slide2 = request.FILES['slide2']

        if request.FILES.get('slide3'):
            hero.slide3 = request.FILES['slide3']

        hero.save()

        return redirect('web_content')
        messages.success(request, "Hero section updated successfully!")
    return redirect('web_content')


    return render(request, 'web_content.html', {
        'hero': hero,
    })

def update_about(request):
    about = About.objects.first()

    if not about:
        about = About.objects.create(description="Default About Text")

    if request.method == "POST":
        about.description = request.POST['description']

        if request.FILES.get('image'):
            about.image = request.FILES['image']

        about.save()
        return redirect('web_content')
        messages.success(request, "About section updated successfully!")
        
    return redirect('web_content')

def update_principal_manager(request):
    pm = PrincipalManager.objects.first()

    if not pm:
        pm = PrincipalManager.objects.create(
            principal_p1="",
            principal_p2="",
            principal_p3="",
            principal_name="",
            manager_p1="",
            manager_p2="",
            manager_p3="",
            manager_name=""
        )

    if request.method == "POST":

        # Principal
        pm.principal_p1 = request.POST['principal_p1']
        pm.principal_p2 = request.POST['principal_p2']
        pm.principal_p3 = request.POST['principal_p3']
        pm.principal_name = request.POST['principal_name']

        if request.FILES.get('principal_image'):
            pm.principal_image = request.FILES['principal_image']

        # Manager
        pm.manager_p1 = request.POST['manager_p1']
        pm.manager_p2 = request.POST['manager_p2']
        pm.manager_p3 = request.POST['manager_p3']
        pm.manager_name = request.POST['manager_name']

        if request.FILES.get('manager_image'):
            pm.manager_image = request.FILES['manager_image']

        pm.save()
        return redirect('web_content')
        messages.success(request, "Principal updated successfully!")
        
        messages.success(request, "Manager updated successfully!")
        
    return redirect('web_content')




def update_contact(request):
    contact = ContactInfo.objects.first()

    if not contact:
        contact = ContactInfo.objects.create(
            map_link="",
            email="",
            phone="",
            address=""
        )

    if request.method == "POST":
        contact.map_link = request.POST['map_link']
        contact.email = request.POST['email']
        contact.phone = request.POST['phone']
        contact.address = request.POST['address']
        contact.save()

    return redirect('web_content')

from .models import PrincipalManager

def update_principal(request):
    pm = PrincipalManager.objects.first()

    if not pm:
        pm = PrincipalManager.objects.create()

    if request.method == "POST":
        if request.FILES.get('principal_image'):
            pm.principal_image = request.FILES['principal_image']

        pm.principal_p1 = request.POST.get('principal_p1')
        pm.principal_p2 = request.POST.get('principal_p2')
        pm.principal_p3 = request.POST.get('principal_p3')
        pm.principal_name = request.POST.get('principal_name')

        pm.save()

    return redirect('web_content')

def update_manager(request):
    pm = PrincipalManager.objects.first()

    if not pm:
        pm = PrincipalManager.objects.create()

    if request.method == "POST":
        if request.FILES.get('manager_image'):
            pm.manager_image = request.FILES['manager_image']

        pm.manager_p1 = request.POST.get('manager_p1')
        pm.manager_p2 = request.POST.get('manager_p2')
        pm.manager_p3 = request.POST.get('manager_p3')
        pm.manager_name = request.POST.get('manager_name')

        pm.save()

    return redirect('web_content')

def add_student_life(request):
    if request.method == "POST":
        StudentLife.objects.create(
            image=request.FILES['image'],
            title=request.POST['title']
        )
        messages.success(request, "Student added successfully!")
       

    return redirect('web_content')


def delete_student_life(request, id):
    StudentLife.objects.get(id=id).delete()
    messages.success(request, "Student deleted successfully!")
    
    return redirect('web_content')
    
def add_campus_event(request):
    if request.method == "POST":
        CampusEvent.objects.create(
            image=request.FILES['image'],
            date=request.POST['date'],
            description=request.POST['description']
        )
        messages.success(request, "Event added successfully!")
        
    return redirect('web_content')


def delete_campus_event(request, id):
    CampusEvent.objects.get(id=id).delete()
    messages.success(request, "Event deleted successfully!")
    
    return redirect('web_content')

def add_gallery_image(request):
    if request.method == "POST":
        GalleryImage.objects.create(
            image=request.FILES['image']
        )
        messages.success(request, "Image added successfully!")
       
    return redirect('web_content')


def delete_gallery_image(request, id):
    GalleryImage.objects.get(id=id).delete()
    messages.success(request, "Image deleted successfully!")
    
    return redirect('web_content')

from django.shortcuts import redirect, get_object_or_404
from .models import GalleryImage

def delete_gallery(request, id):
    img = get_object_or_404(GalleryImage, id=id)
    img.delete()
    return redirect('web_content')

from school_app.models import HeroSection

HeroSection.objects.create(
    title="Test Title",
    subtitle="Test Subtitle"
)
