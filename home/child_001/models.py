from django.db import models

# Create your models here.

class addCustomerModel(models.Model):
    userid = models.CharField(max_length=50, blank=True, null=True)
    firstname = models.CharField(max_length=50, blank=True, null=True)
    middlename = models.CharField(max_length=50, blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.firstname + self.lastname}"
    

class AddNewBillModel(models.Model):
    customer_id = models.CharField(max_length=50, blank=True, null=True)
    bill_for_the_month = models.CharField(max_length=100, blank=True, null=True)
    current_reading = models.CharField(max_length=100, blank=True, null=True)
    previous_reading = models.CharField(max_length=100, blank=True, null=True)
    total_unit = models.CharField(max_length=100, blank=True, null=True)
    charge_per_unit = models.CharField(max_length=100, blank=True, null=True)
    final_amount = models.CharField(max_length=100, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.customer_id