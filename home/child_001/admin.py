from django.contrib import admin
from . models import addCustomerModel, AddNewBillModel

# Register your models here.
admin.site.register(addCustomerModel)
admin.site.register(AddNewBillModel)