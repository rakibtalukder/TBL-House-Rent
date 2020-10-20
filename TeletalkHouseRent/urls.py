
from django.contrib import admin
from django.urls import path
from Rent import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout', LogoutView.as_view(template_name='index.html'), name='logout'),
    path('', views.index ),
    path('adminclick/', views.adminclick, name='adminclick' ),
    path('addingadmin', views.adminsignup, name='addingadmin'),

    path('adminlogin/', LoginView.as_view(template_name='adminlogin.html'), name='adminlogin'),
    path('afterlogin', views.afterlogin_view, name='afterlogin'),
    path('admin-dashboard/', views.admin_dashboard_view, name= 'admin_dashboard'),
    path('executiveclick', views.executiveclick, name='executiveclick'),
    path('executivesignup', views.executivesignup, name='executivesignup'),



    path('admin-executive/', views.admin_executive, name='admin_executive'),
    path('admin-bts/', views.admin_bts, name='admin_bts'),

    path('admin-view-executive', views.admin_view_executive, name='admin-view-executive'),
    path('admin_update_executive/<int:pk>', views.update_executive, name='admin_update_executive'),
    path('delete-executive/<int:pk>', views.delete_executive,
         name='delete-executive'),
    path('admin-add-executive', views.admin_add_executive, name='admin_add_executive.html'),

    path('delete-admin/<int:pk>', views.delete_admin,
         name='delete-admin'),
    path('admin-list', views.admin_list_view, name='admin-list'),

    path('admin-approve-executive/', views.admin_approve_executive, name='admin-approve-executive'),
    path('approve_executive/<int:pk>', views.approve_executive, name='approve_executive'),
    path('reject_executive/<int:pk>', views.reject_executive, name='reject_executive'),
    path('admin-bts/', views.admin_bts, name='admin-bts'),
    path('bts-record',views.bts_record, name='bts-record'),
    path('admin_update_agreement/<int:pk>', views.admin_update_bts, name='admin_update_agreement'),
    path('delete-agreement/<int:pk>', views.delete_bts, name='delete-agreement'),
    path('admin_add_agreement', views.admin_add_agreement, name='admin_add_agreement'),
    path('admin-approve-agreement', views.admin_approve_agreement, name='admin-approve-agreement'),
    path('approve_agreement/<int:pk>', views.approve_agreement, name='approve_agreement'),
    path('reject_agreement/<int:pk>', views.reject_agreement, name='reject_agreement'),
    path('active_increment/<int:pk>', views.active_increment, name='active_increment'),

    path('admin-rent', views.admin_rent, name='admin-rent'),
    path('admin_add_rent', views.admin_add_rent, name='admin_add_rent'),
    path('admin_delete_rent/<int:pk>', views.admin_delete_rent, name='admin_delete_rent'),
    path('rent-record', views.rent_record, name='rent-record'),
    path('admin-approve-rent', views.admin_approve_rent, name='admin-approve-rent'),
    path('approve_rent/<int:pk>', views.approve_rent, name='approve_rent'),
    path('reject_rent/<int:pk>', views.reject_rent, name='reject_rent'),
    path('view_rent/<int:pk>', views.view_rent_individually, name='view_rent'),
    path('generate_check/<int:pk>', views.admin_generate_check, name='generate_check'),

    path('executivelogin/', LoginView.as_view(template_name='executivelogin.html'), name='executivelogin'),
    path('executive_wait', views.executive_wait, name='executive_wait'),
    path('executive_dashboard', views.executive_dashboard_view, name='executive_dashboard'),
    path('executive-bts', views.executive_bts, name='executive-bts'),
    path('executive_add_agreement', views.executive_add_agreement, name='executive_add_agreement'),
    path('executive-bts-record', views.executive_bts_record, name='executive-bts-record'),
    path('requested-bts-record', views.requested_bts_record, name='requested-bts-record'),
    path('delete-agreement/<int:pk>', views.executive_delete_bts, name='delete-agreement'),

    path('executive-rent', views.executive_rent, name='executive-rent'),
    path('executive_add_rent', views.executive_add_rent, name='executive_add_rent'),
    path('executive_delete_rent/<int:pk>', views.executive_delete_rent, name='executive_delete_rent'),
    path('executive_rent_record', views.executive_rent_record, name='executive_rent_record'),
    path('executive_requested_rent_record', views.executive_requested_rent_record, name='executive_requested_rent_record'),


]
