from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from . models import addCustomerModel, AddNewBillModel
# Create your views here.

# random number
import random
import string

def generate_random_number():
    return ''.join(random.choices(string.digits, k=10))

def Index(request):
    if request.method == 'POST':
        value = request.POST.get('crn', '')
        state = request.POST.get('paid', '')
        amrit = request.POST.get('amrit', '')
        print('hy amrit', amrit)
        print(state)
        print(value)
        data2 = AddNewBillModel.objects.all().filter(customer_id=amrit)
        print('amrit shahi klj', data2)
        AddNewBillModel.objects.filter(customer_id=amrit).update(status=state)


        data = AddNewBillModel.objects.all().filter(customer_id=value)
        
        return render(request, 'mandispafter.html', {'data': data})
    return render(request, 'index.html')

def adminView(request):
    data = AddNewBillModel.objects.count()
    data2 = addCustomerModel.objects.count()
    paid = AddNewBillModel.objects.all()
    st1 = []
    st2 = []
    for i in paid:
        if i.status == 'paid':
            st1 += i.status.split()
    paidValue = len(st1)
    
    unpaid = AddNewBillModel.objects.filter(status__isnull=True).count()
        
    return render(request, 'admin.html', {'data': data, 'data2': data2, 'paid': paidValue, 'unpaid':unpaid})

def addCustomer(request):
    rnum = generate_random_number()
    
    if request.method == 'POST':
        firstname = request.POST.get('firstname', '')
        middlename = request.POST.get('middlename', '')
        lastname = request.POST.get('lastname', '')
        contact = request.POST.get('contact', '')
        email = request.POST.get('email', '')
        gender = request.POST.get('gender', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        addCustomerModel(userid=rnum, firstname=firstname, middlename=middlename, lastname=lastname, contact=contact, email=email, gender=gender, address=address, city=city, state=state).save()
        return HttpResponse('Customer Data Created Successfully !!')

    return render(request, 'addCustomer.html')

def billCustomer(request):
    data = AddNewBillModel.objects.all()
    return render(request, 'billCustomer.html', {'data': data})

def paymentCustomer(request):
    return render(request, 'paymentStatus.html')

def viewCustomer(request):
    data = addCustomerModel.objects.all()
    
    return render(request, 'viewCustomer.html', {'data': data})

def viewUpdate(request, pk):
    data = addCustomerModel.objects.filter(id=pk)
    if request.method == 'POST':
        p = addCustomerModel.objects.get(id=pk)
        firstname = request.POST.get('firstname', '')
        middlename = request.POST.get('middlename', '')
        lastname = request.POST.get('lastname', '')
        contact = request.POST.get('contact', '')
        email = request.POST.get('email', '')
        gender = request.POST.get('gender', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        p.firstname = firstname
        p.middlename = middlename
        p.lastname = lastname
        p.contact = contact
        p.email = email
        p.gender = gender
        p.address = address
        p.city = city
        p.state = state
        p.save(update_fields=['firstname', 'middlename', 'lastname', 'contact', 'email', 'gender', 'address', 'city', 'state'])
    return render(request, 'updateCustomer.html', {'data': data})

def viewDelete(request, pk):
    data = addCustomerModel.objects.filter(id=pk)
    data.delete()
    return HttpResponseRedirect('/viewCustomer')

def viewAddBill(request):
    data = addCustomerModel.objects.values('userid')
    print(data)
    if request.method == 'POST':
        custidselect = request.POST.get('custidselect', '')
        bfm = request.POST.get('bfm', '')
        cr = request.POST.get('cr', '')
        pr = request.POST.get('pr', '')
        tu = request.POST.get('tu', '')
        cpu = request.POST.get('cpu', '')
        famount = request.POST.get('famount', '')
        dd = request.POST.get('dd', '')
        AddNewBillModel(customer_id=custidselect, bill_for_the_month=bfm, current_reading=cr, previous_reading=pr, total_unit=tu, charge_per_unit=cpu, final_amount=famount, due_date=dd).save()
        return HttpResponse('Data Saved Successfully !!')


    return render(request, 'addConnection.html', {'data': data})

def deleteAddConnection(request, pk):
    data = AddNewBillModel.objects.filter(id=pk)
    data.delete()
    return HttpResponseRedirect('/bill')


