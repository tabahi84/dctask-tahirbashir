from django.db import models
from django.db.models.functions import Lower

from api import utils as AppUtils



class Customer(models.Model):
    first_name = models.CharField(blank=False, max_length=100, validators=[AppUtils.regex_name_validator])
    last_name = models.CharField(blank=False, max_length=100, validators=[AppUtils.regex_name_validator])
    dob = models.DateField(blank=False, validators=[AppUtils.validate_date])

    def __str__(self):
            return f"{self.first_name} {self.last_name}"
    
    class Meta:
        constraints = [
            models.UniqueConstraint(Lower('first_name') + " " + Lower('last_name'),
                                    name='unique_fullname',            
                                    # fields=[Lower('first_name'), Lower('last_name')],
                                    violation_error_message="Customer with same first and last names already exists")
            # models.UniqueConstraint(
            #     expressions=[
            #         Lower('first_name'), 
            #         Lower('last_name')
            #     ],
            # )
        ]
