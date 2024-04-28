from django.db import models
from django.core.exceptions import ValidationError

from api import utils as AppUtils
from .customer_models import Customer


class Quote(models.Model):
    customer = models.ForeignKey(Customer, blank=False, related_name="policies", on_delete=models.CASCADE)
    policy_type = models.CharField(max_length=25, blank=False, choices=AppUtils.QuoteType.choices)
    premium = models.IntegerField(blank=True, default=0)
    coverage = models.IntegerField(blank=True, default=0)
    state = models.CharField(max_length=25, choices=AppUtils.QuoteState.choices, default=AppUtils.QuoteState.QUOTED)

    # DJango Admin calls this one
    def clean(self):
        # Process for PATCH
        if self.id is not None:
            obj = Quote.objects.get(pk=self.id)
            self.customer_id = obj.customer_id
            self.policy_type = obj.policy_type
            self.premium = obj.premium
            self.coverage = obj.coverage
            return super().clean()
        
        # Process for POST
        try:
            self.customer
        except Exception as ex:
            raise ValidationError(message=f"Customer having ID '{self.customer_id}' does not exist.")
        
        # self.policy_type = self.policy_type.lower()
        policy_type_dict = AppUtils.get_all_policies()
        # if self.policy_type not in policy_type_dict.keys():
        #     raise ValidationError(message=f"Invalid 'policy_type' provided. Valid values are [{' | '.join(policy_type_dict.keys())}]")

        policy_type_obj = policy_type_dict[self.policy_type]
        if not policy_type_obj.validate_policy_against_dob(self.customer.dob):
            raise ValidationError(message=f"policy_type '{self.policy_type}' is not applicable for your age-group. Allowed policies are [{' | '.join(AppUtils.PolicyTypeDetail.get_policies_against_dob(policy_type_dict, self.customer.dob))}]")
        
        if Quote.objects.filter(customer_id=self.customer_id, policy_type=self.policy_type).exists():
            raise ValidationError(message=f"Customer {self.customer} has already availed '{self.policy_type}' policy")

        self.state = str(AppUtils.QuoteState.QUOTED)
        self.premium = policy_type_obj.premium
        self.coverage = policy_type_obj.coverage
        
        return super().clean()

class QuoteHistory(models.Model):
    quote = models.ForeignKey(Quote, blank=False, related_name='history', on_delete=models.CASCADE)
    state = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now_add=True)
