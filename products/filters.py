import django_filters
from job.models import JobsCreated



class JobFilter(django_filters.FilterSet):
    title =django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model= JobsCreated
        fields =['title','state','job_type','industry']