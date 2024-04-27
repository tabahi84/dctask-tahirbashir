from datetime import date, datetime, timedelta
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError



# ======================================
#  VALIDATION - SECTION
# ======================================
regex_name_validator = RegexValidator(
    regex=r'^[A-Za-z]+(?:[-\s]?[A-Za-z]+)*$',
    message="Incorrect name string. Names can only contain alphabets, '-' and (space)"
)

def validate_date(dt:date, lower_bound_years:int=100) -> date|None:
    today = datetime.now().date()
    lower_bound = today - timedelta(days=lower_bound_years*365)

    if dt >= today: raise ValidationError(message="Date of Birth cannot be today or in future.")
    if dt <= lower_bound: raise ValidationError(message=f"Date of Birth cannot be more than {lower_bound_years} years ago.")


