from django.db import connection
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Tenant
from rest_framework import serializers
from rest_framework.generics import ListAPIView


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = "__all__"


class TenantMapView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

    def list(self, request, *args, **kwargs):
        connection.cursor().execute(f"SET search_path to public")

        queryset = self.filter_queryset(Tenant.objects.all())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = TenantSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
