from tenant.models import Tenant
from rest_framework import serializers




class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = ['id', 'schema_name', 'tenant_uuid', 'paid_until', 'on_trial', 'created_on', 'domain_url', 'is_active']