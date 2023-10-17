from rest_framework import serializers
from .models import *
class task_serializers(serializers.ModelSerializer):
    class Meta:
        model=task_manage
        fields=('id','Title','Description','Date','Completed')