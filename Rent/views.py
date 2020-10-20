from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect
from Rent import models, forms
from django.contrib.auth.models import Group
from django.conf import Settings
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import datetime, date

# Create your views here.


def index(request):
    return render(request,'index.html')


def adminclick(request):

    return render(request,'adminclick.html')

def executiveclick(request):
    return render(request,'executiveclick.html')





def executivesignup(request):
    userform = forms.ExecutiveUserForm()
    executiveform = forms.ExecutiveForm()
    mydict ={'userform':userform,
             'executiveform':executiveform}

    if request.method=='POST':
        userform=forms.ExecutiveUserForm(request.POST)
        executiveform=forms.ExecutiveForm(request.POST, request.FILES)
        if userform.is_valid() and executiveform.is_valid():
            user = userform.save()
            user.set_password(user.password)
            executive = executiveform.save(commit=False)
            executive.user = user
            executive = executive.save()

            my_executive_group = Group.objects.get_or_create(name='Executive Panel')
            my_executive_group[0].user_set.add(user)

            return HttpResponseRedirect('executivelogin')

    return render(request,'executivesignup.html', context=mydict)



#..............................is_ permission........................................#


def is_admin(user):
    return user.groups.filter(name='Admin Panel').exists()


def is_executive(user):
    return models.Executive.objects.all()



def afterlogin_view(request):
    if is_admin(request.user):
        return redirect('admin_dashboard')
    elif is_executive(request.user):
        accountapproval = models.Executive.objects.all().filter(status=True)
        if accountapproval:
            return redirect('executive_dashboard')
        else:
            return render(request, 'executive_wait_for_approval.html')




def executive_wait(request):
    return render(request, 'executive_wait_for_approval.html')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_dashboard_view(request):
    # for both table in admin dashboard
    agreement = models.Agreement.objects.all().order_by('-id')
    rent = models.Rent.objects.all().order_by('-id')
    # for three cards
    executivecount = models.Executive.objects.all().filter(status=True).count()
    pendingexecutivecount = models.Executive.objects.all().filter(status=False).count()

    agreementcount = models.Agreement.objects.all().filter(status=True).count()
    pendingagreementcount = models.Agreement.objects.all().filter(status=False).count()

    rentcount = models.Rent.objects.all().filter(status=True).count()
    pendingrentcount = models.Rent.objects.all().filter(status=False).count()
    mydict = {
        'agreement':agreement,
        'rent':rent,
        'executivecount':executivecount,
        'pendingexecutivecount':pendingexecutivecount,
        'agreementcount':agreementcount,
        'pendingagreementcount':pendingagreementcount,
        'rentcount':rentcount,
        'pendingrentcount':pendingrentcount
   }
    return render(request, 'admin_dashboard.html', context=mydict)


# Admin Sidebar Hit click Start

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_executive(request):
    return render(request, 'admin-executive.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_list_view(request):
    admin = models.User.objects.all().filter(is_superuser=True)
    return render(request, 'admin-list.html', {'admin':admin})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_executive(request):
    executive = models.Executive.objects.all().filter(status=True)
    return render(request, 'admin-view-executive.html', {'executive':executive})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_admin(request, pk):
    admin = models.User.objects.get(id=pk)
    #user = models.User.objects.get(id=executive.user_id)
    admin.delete()
    return redirect('admin-list-view')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_executive(request, pk):
    executive = models.Executive.objects.get(id=pk)
    user = models.User.objects.get(id=executive.user_id)
    user.delete()
    executive.delete()
    return redirect('admin-view-executive')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def update_executive(request, pk):
    executive = models.Executive.objects.get(id=pk)
    user = models.User.objects.get(id=executive.user_id)

    userform = forms.ExecutiveUserForm(instance=user)
    executiveform = forms.ExecutiveForm(request.FILES, instance=executive)
    mydict = {'userform': userform, 'executiveform': executiveform}
    if request.method == 'POST':
        userform = forms.ExecutiveUserForm(instance=user)
        executiveform = forms.ExecutiveForm(request.FILES, instance=executive)
        if userform.is_valid() and executiveform.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()
            executive = executiveform.save(commit=False)
            executive.status = True
            executive.save()
        return redirect('admin-view-executive')
    return render(request, 'admin_update_executive.html', context=mydict)



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_executive(request):

    userform = forms.ExecutiveUserForm()
    executiveform = forms.ExecutiveForm()
    mydict ={'userform':userform,
             'executiveform':executiveform}

    if request.method=='POST':
        userform=forms.ExecutiveUserForm(request.POST)
        executiveform=forms.ExecutiveForm(request.POST, request.FILES)
        if userform.is_valid() and executiveform.is_valid():
            user = userform.save()
            user.set_password(user.password)
            executive = executiveform.save(commit=False)
            executive.user = user
            executive.status = True
            executive = executive.save()

            my_executive_group = Group.objects.get_or_create(name='Executive Panel')
            my_executive_group[0].user_set.add(user)

            return HttpResponseRedirect('admin-view-executive')

    return render(request,'admin_add_executive.html', context=mydict)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def adminsignup(request):
    form = forms.AdminSignupForm()
    if request.method == 'POST':
        form = forms.AdminSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_superuser = True
            my_admin_group = Group.objects.get_or_create(name='Admin Panel')
            my_admin_group[0].user_set.add(user)


        return redirect('admin-list')

    return render(request,'addingadmin.html',{'form':form})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_approve_executive(request):
    executive = models.Executive.objects.all().filter(status=False)
    return render(request, 'admin-approve-executive.html', {'executive': executive})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def approve_executive(request, pk):
    executive = models.Executive.objects.get(id=pk)
    executive.status = True
    executive.save()
    return redirect(reverse('admin-approve-executive'))


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def reject_executive(request, pk):
    executive = models.Executive.objects.get(id=pk)
    user = models.User.objects.get(id=executive.user_id)
    user.delete()
    executive.delete()
    return redirect('admin-approve-executive')



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_bts(request):
    return render(request, 'admin-bts.html')



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_rent(request):
    return render(request, 'admin-rent.html')






@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_bts(request):
    return render(request,'admin-bts.html')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_agreement(request):
    form = forms.AgreementForm()
    if request.method == 'POST':
        form = forms.AgreementForm(request.POST, request.FILES)
        if form.is_valid():
            agreement = form.save()
            agreement.status = True
            agreement = agreement.save()
            return HttpResponseRedirect('bts-record')

    return render(request, 'admin_add_agreement.html', {'form':form})



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)

def bts_record(request):
    agreement = models.Agreement.objects.all().filter(status=True)

    return render(request,'bts-record.html', {'agreement':agreement})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_update_bts(request,pk):
    agreement = models.Agreement.objects.get(id=pk)
    form = forms.AgreementForm(request.FILES, instance=agreement)
    if request.method == 'POST':
        form = forms.AgreementForm(request.POST, request.FILES, instance=agreement)
        if form.is_valid():
            agreement = form.save()
            agreement = agreement.save()
            return HttpResponseRedirect('bts-record')

    return render(request, 'admin_update_agreement.html', {'form': form})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_bts(request,pk):
    agreement = models.Agreement.objects.get(id=pk)
    agreement.delete()
    return redirect('bts-record')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_approve_agreement(request):
    agreement = models.Agreement.objects.all().filter(status=False)
    return render(request, 'admin-approve-agreement.html', {'agreement':agreement})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def approve_agreement(request,pk):
    agreement = models.Agreement.objects.get(id=pk)
    agreement.status = True
    agreement.save()
    return redirect('admin-approve-agreement')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def reject_agreement(request,pk):
    agreement= models.Agreement.objects.get(id=pk)
    agreement.delete()
    return redirect('admin-approve-agreement')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def active_increment(request, pk):
    agreement = models.Agreement.objects.get(id=pk)
    agreement.incrementstatus = True
    agreement.save()
    return redirect('bts-record')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_rent(request):
    return render(request,'admin-rent.html')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_rent(request):
    rentform = forms.RentForm()
    mydict = {'rentform':rentform}
    if request.method == 'POST':
        rentform = forms.RentForm(request.POST, request.FILES)
        if rentform.is_valid():
            rent = rentform.save(commit=False)
            rent.btsid = request.POST.get('btsid')
            rent.btsname = models.Agreement.objects.get(id=request.POST.get('btsid')).name
            rent.agreementid = models.Agreement.objects.get(id=request.POST.get('btsid')).agreementid
            rent.monthrent = models.Agreement.objects.get(id=request.POST.get('btsid')).monthrent
            rent.address = models.Agreement.objects.get(id=request.POST.get('btsid')).address
            rent.hownername = models.Agreement.objects.get(id=request.POST.get('btsid')).hownername
            rent.contractperiod = models.Agreement.objects.get(id=request.POST.get('btsid')).contractperiod
            rent.monthincrement = models.Agreement.objects.get(id=request.POST.get('btsid')).incrementamount

            rent.rentexcludingincrement =(models.Agreement.objects.get(id=request.POST.get('btsid')).monthrent)*rent.totalmonth
            rent.checkstatus = models.Agreement.objects.get(id=request.POST.get('btsid')).incrementstatus
            if rent.checkstatus:
                rent.incrementamount = (models.Agreement.objects.get(
                    id=request.POST.get('btsid')).incrementamount) * rent.totalmonth
                rent.totalrent = (models.Agreement.objects.get(id=request.POST.get('btsid')).monthrent) * (
                    rent.totalmonth) + ((models.Agreement.objects.get(id=request.POST.get('btsid')).incrementamount )*(rent.totalmonth))
            else:
                rent.totalrent = (models.Agreement.objects.get(id=request.POST.get('btsid')).monthrent) * (
                    rent.totalmonth)


            rent.status = True
            rent.save()
        else:
            print(rentform.errors)


        return HttpResponseRedirect('rent-record')

    return render(request, 'admin_add_rent.html', context=mydict)

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_delete_rent(request,pk):
    rent = models.Rent.objects.get(id=pk)
    rent.delete()
    return redirect('rent-record')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def rent_record(request):
    rent = models.Rent.objects.all().filter(status=True)
    return render(request, 'rent-record.html', {'rent':rent})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_approve_rent(request):
    rent = models.Rent.objects.all().filter(status=False)
    return render(request, 'admin_approve_rent.html', {'rent':rent})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def approve_rent(request,pk):
    rent = models.Rent.objects.get(id=pk)
    rent.status = True
    rent.save()
    return redirect('admin-approve-rent')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def reject_rent(request,pk):
    rent= models.Rent.objects.get(id=pk)
    rent.delete()
    return redirect('admin-approve-rent')  #url ae jei namta disi oita dite hobe, template name jai hokna keno


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def view_rent_individually(request,pk):
    rent = models.Rent.objects.get(id=pk)
    return render(request,'view_rent_individually.html',{'rent':rent})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_generate_check(request,pk):
    rent = models.Rent.objects.get(id=pk)
    bill ={
        'agreementid':rent.agreementid,
        'btsname':rent.btsname,
        'todate':rent.todate,
        'monthrent':rent.monthrent,
        'totalmonth':rent.totalmonth,
        'totalrent':rent.totalrent,
        'address':rent.address,
        'hownername':rent.hownername,
        'contractperiod':rent.contractperiod,
        'monthincrement':rent.monthincrement,
        'incrementamount':rent.incrementamount,
        'rent':rent.rentexcludingincrement,
        'eligibility': rent.checkstatus
    }
    return render(request,'admin_generate_check.html',context=bill)


#@login_required(login_url='executivelogin')
@user_passes_test(is_executive)
def executive_dashboard_view(request):

    rent= models.Rent.objects.all().filter().order_by('-id')
    agreement = models.Agreement.objects.all().filter().order_by('-id')
    agreementcount = models.Agreement.objects.all().filter(status=True).count()
    rentcount = models.Rent.objects.all().filter(status=True).count()
    pendingagreementcount = models.Agreement.objects.all().filter(status=False).count()
    pendingrentcount = models.Rent.objects.all().filter(status=False).count()
    mydict ={
        'rent': rent, 'agreement': agreement,
        'agreementcount':agreementcount,
        'rentcount':rentcount,
        'pendingagreementcount':pendingagreementcount,
        'pendingrentcount':pendingrentcount
    }

    return render(request, 'executive_dashboard.html', context=mydict)



def executive_bts(request):
    return render(request,'executive-bts.html')


def executive_add_agreement(request):
    form = forms.AgreementForm()
    if request.method == 'POST':
        form = forms.AgreementForm(request.POST, request.FILES)
        if form.is_valid():
            agreement = form.save()
            agreement = agreement.save()
            return HttpResponseRedirect('requested-bts-record')

    return render(request, 'executive_add_agreement.html', {'form':form})


def requested_bts_record(request):
    agreement = models.Agreement.objects.all().filter(status=False)
    return render(request, 'requested-bts-record.html', {'agreement':agreement})


def executive_delete_bts(request,pk):
    agreement = models.Agreement.objects.get(id=pk)
    agreement.delete()
    return redirect('executive-bts-record')


def executive_bts_record(request):
    agreement = models.Agreement.objects.all().filter(status=True)

    return render(request,'executive-bts-record.html', {'agreement':agreement})


def executive_rent(request):
    return render(request,'executive-rent.html')




def executive_add_rent(request):
    rentform = forms.RentForm()
    mydict = {'rentform':rentform}
    if request.method == 'POST':
        rentform = forms.RentForm(request.POST, request.FILES)
        if rentform.is_valid():
            rent = rentform.save(commit=False)
            rent.btsid = request.POST.get('btsid')
            rent.btsname = models.Agreement.objects.get(id=request.POST.get('btsid')).name
            rent.monthrent = models.Agreement.objects.get(id=request.POST.get('btsid')).monthrent
            rent.agreementid = models.Agreement.objects.get(id=request.POST.get('btsid')).agreementid
            rent.address = models.Agreement.objects.get(id=request.POST.get('btsid')).address
            rent.hownername = models.Agreement.objects.get(id=request.POST.get('btsid')).hownername
            rent.contractperiod = models.Agreement.objects.get(id=request.POST.get('btsid')).contractperiod

            rent.monthincrement = models.Agreement.objects.get(id=request.POST.get('btsid')).incrementamount

            rent.rentexcludingincrement =(models.Agreement.objects.get(id=request.POST.get('btsid')).monthrent)*rent.totalmonth
            rent.checkstatus = models.Agreement.objects.get(id=request.POST.get('btsid')).incrementstatus
            if rent.checkstatus:
                rent.incrementamount = (models.Agreement.objects.get(
                    id=request.POST.get('btsid')).incrementamount) * rent.totalmonth
                rent.totalrent = (models.Agreement.objects.get(id=request.POST.get('btsid')).monthrent) * (
                    rent.totalmonth) + ((models.Agreement.objects.get(id=request.POST.get('btsid')).incrementamount )*(rent.totalmonth))
            else:
                rent.totalrent = (models.Agreement.objects.get(id=request.POST.get('btsid')).monthrent) * (
                    rent.totalmonth)

            rent.save()
        else:
            print(rentform.errors)


            return HttpResponseRedirect('executive_rent_record')

    return render(request, 'executive_add_rent.html', context=mydict)



def executive_delete_rent(request,pk):
    rent = models.Rent.objects.get(id=pk)
    rent.delete()
    return redirect('executive_requested_rent_record')



def executive_rent_record(request):
    rent = models.Rent.objects.all().filter(status=True)
    return render(request, 'executive_rent_record.html', {'rent':rent})


def executive_requested_rent_record(request):
    rent = models.Rent.objects.all().filter(status=False)
    return render(request, 'executive_requested_rent_record.html',{'rent':rent})