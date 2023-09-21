
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from location.models import Location
from api.views import child_detail, guardian_detail

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)
STATUS_CHOICES = (
    ('A', 'Active'),
    ('I', 'Inactive'),
)

class Child(models.Model):
    first_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    guardian = models.ForeignKey('Guardian', on_delete=models.CASCADE, related_name='children')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A') 
   

    def  deactivate_child(self):
        child = Child.objects.get(pk=child_detail)
        child.status = 'I'
        child.save()
    def __str__(self):
        return f"{self.first_name} {self.last_name} (Child of {self.guardian})"



from django.db import models
from child.models import Child  



class Guardian(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(unique=True, region='IR')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A') 


    def  deactivate_guardian(self):
        Guardian = Child.objects.get(pk=guardian_detail)
        Guardian.status = 'I'
        Guardian.save()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def register_child(self):
        child = Child.objects.create(
            first_name=self.first_name,
            last_name=self.last_name,
            guardian=self,
        )
        return child

    def get_children(self):
        return self.children.all()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"