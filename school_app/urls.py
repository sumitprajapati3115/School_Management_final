from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),

    # AUTH
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),

    # DASHBOARD
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # CONTENT
    path('web-content/', views.web_content, name='web_content'),

    path('update-hero/', views.update_hero, name='update_hero'),
    path('update-about/', views.update_about, name='update_about'),
    path('update-principal/', views.update_principal, name='update_principal'),
    path('update-manager/', views.update_manager, name='update_manager'),
    path('update-contact/', views.update_contact, name='update_contact'),

    # STUDENT
    path('students-page/', views.students_page, name='students_page'),
    path('add-student/', views.add_student, name='add_student'),
    path('edit-student/<int:id>/', views.edit_student, name='edit_student'),
    path('export-students/', views.export_students, name='export_students'),
    path('edit-student/<int:id>/', views.edit_student, name='edit_student'),
    path('add-student-life/', views.add_student_life, name='add_student_life'),
    path('delete-student-life/<int:id>/', views.delete_student_life, name='delete_student_life'),

    # EVENTS
    path('add-campus-event/', views.add_campus_event, name='add_campus_event'),
    path('delete-campus-event/<int:id>/', views.delete_campus_event, name='delete_campus_event'),

    # GALLERY
    path('add-gallery-image/', views.add_gallery_image, name='add_gallery_image'),
    path('delete-gallery/<int:id>/', views.delete_gallery, name='delete_gallery'),

    # NEWS
    path('news-page/', views.news_page, name='news_page'),
    path('delete-student/<int:id>/', views.delete_student, name='delete_student'),

path('approve-admission/<int:id>/', views.approve_admission, name='approve_admission'),
path('edit-admission/<int:id>/', views.edit_admission, name='edit_admission'),
path('delete-admission/<int:id>/', views.delete_admission, name='delete_admission'),

path('add-news/', views.add_news, name='add_news'),
path('edit-news/<int:id>/', views.edit_news, name='edit_news'),
path('delete-news/<int:id>/', views.delete_news, name='delete_news'),

path('add-event/', views.add_event, name='add_event'),
path('edit-event/<int:id>/', views.edit_event, name='edit_event'),
path('delete-event/<int:id>/', views.delete_event, name='delete_event'),

path('add-notice/', views.add_notice, name='add_notice'),
path('edit-notice/<int:id>/', views.edit_notice, name='edit_notice'),
path('delete-notice/<int:id>/', views.delete_notice, name='delete_notice'),

path('add-live-news/', views.add_live_news, name='add_live_news'),
path('edit-live-news/<int:id>/', views.edit_live_news, name='edit_live_news'),
path('delete-live-news/<int:id>/', views.delete_live_news, name='delete_live_news'),
]