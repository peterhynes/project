from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

class Retailer(TenantMixin):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    businessName = models.CharField(max_length=100)
    businessAddress = models.CharField(max_length=100)
    rbn = models.CharField(max_length=50)
    businessType = models.CharField(max_length=100)
    businessDescription = models.TextField(max_length=100)
    created_on = models.DateField(auto_now_add=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True

class Domain(DomainMixin):
    pass
