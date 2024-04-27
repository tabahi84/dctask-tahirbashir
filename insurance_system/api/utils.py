from functools import lru_cache
from datetime import date, datetime, timedelta

from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError



class QuoteState(models.TextChoices):
    QUOTED = "quoted"
    ACCEPTED = "accepted"
    ACTIVE = "active"
class QuoteType(models.TextChoices):
    PERSONAL_CAR = 'personal-car'
    PERSONAL_PROPERTY = 'personal-property'
    LIFE_COVERAGE = 'life-coverage'
    ACCIDENT_COVERAGE = 'accident-coverage'


# ======================================
#  VALIDATION - SECTION
# ======================================
regex_name_validator = RegexValidator(
    regex=r'^[A-Za-z]{2}(?:[-\s]?[A-Za-z]+)*$',
    message="Incorrect name. Names can only contain alphabets, '-' and (space)"
)

regex_title_validator = RegexValidator(
    regex=r'^[A-Za-z]{3}(?:[-()&.:]?[A-Za-z0-9/\s]+)*(?:[.)]){0,2}$',
    message="Incorrect title. Titles can only contain alphabets, numbers, '/', '-', '.', ':', '&', '(', ')' and (space)"
)

def validate_date(dt:date, lower_bound_years:int=100) -> date|None:
    today = datetime.now().date()
    lower_bound = today - timedelta(days=lower_bound_years*365)

    if dt >= today: raise ValidationError(message="Date of Birth cannot be today or in future.")
    if dt <= lower_bound: raise ValidationError(message=f"Date of Birth cannot be more than {lower_bound_years} years ago.")



# ======================================
#  POLICY_TYPE - SECTION
# ======================================
from typing import Dict, List
from dataclasses import dataclass
@dataclass
class PolicyTypeDetail():
    policy_type:str
    min_age:int
    max_age:int
    premium:int
    coverage:int
    
    def validate_policy_against_dob(self, dt:date):
        today:date = date.today()
        age = today.year - dt.year
        return self.min_age <= age <= self.max_age
    
    @staticmethod
    def get_policies_against_dob(all_policies:Dict, dt:date):
        today:date = date.today()
        age = today.year - dt.year
        applicable_policies:List[str] = []
        for k, v in all_policies.items():
            if v.min_age <= age <= v.max_age:
                applicable_policies.append(k)       
        return applicable_policies


@lru_cache
def get_all_policies() -> Dict[str, PolicyTypeDetail]:
    return {
        str(QuoteType.PERSONAL_CAR):      PolicyTypeDetail(policy_type=str(QuoteType.PERSONAL_CAR),      min_age=20, max_age=60, premium=2500, coverage=  50000),
        str(QuoteType.PERSONAL_PROPERTY): PolicyTypeDetail(policy_type=str(QuoteType.PERSONAL_PROPERTY), min_age=35, max_age=50, premium=9000, coverage=1000000),
        str(QuoteType.LIFE_COVERAGE):     PolicyTypeDetail(policy_type=str(QuoteType.LIFE_COVERAGE),     min_age=18, max_age=40, premium=3000, coverage= 750000),
        str(QuoteType.ACCIDENT_COVERAGE): PolicyTypeDetail(policy_type=str(QuoteType.ACCIDENT_COVERAGE), min_age=25, max_age=55, premium=3000, coverage=  35000),
    }