from django.db import models
from django.db.models.functions import Lower

from api import utils as AppUtils



class Customer(models.Model):
    first_name = models.CharField(blank=False, max_length=100, validators=[AppUtils.regex_name_validator])
    last_name = models.CharField(blank=False, max_length=100, validators=[AppUtils.regex_name_validator])
    dob = models.DateField(blank=False, validators=[AppUtils.validate_date])

    def __str__(self):
            return f"{self.first_name} {self.last_name}"
    
    # DJango Admin calls this one
    def clean(self):
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()
        return super().clean()
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields= ['first_name', 'last_name'],
                                    name='customer_unique_fullname',
                                    violation_error_message="Customer with same first and last names already exists")
        ]
