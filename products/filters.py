import django_filters
from job.models import AvailableJobs



class JobFilter(django_filters.FilterSet):
    title =django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model= AvailableJobs
        fields =['title','location','job_type','industry']