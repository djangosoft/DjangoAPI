from rest_framework import viewsets
from .serielizer import ActiveSerielizer, EmpSerielizer, MemberSerielizer
from .models import Emp, Active, Member


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all().order_by('ok')
    serializer_class = MemberSerielizer
