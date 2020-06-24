from rest_framework import serializers
from .models import Emp, Active, Member


class ActiveSerielizer(serializers.ModelSerializer):
    class Meta:
        model = Active
        fields = ('start_time', 'end_time')


class EmpSerielizer(serializers.ModelSerializer):
    activity_status = ActiveSerielizer(many=True)

    class Meta:
        model = Emp
        fields = ('id', 'real_name', 'tz', 'activity_status')


class MemberSerielizer(serializers.ModelSerializer):
    members = EmpSerielizer(many=True)

    class Meta:
        model = Member
        fields = ('ok', 'members')
