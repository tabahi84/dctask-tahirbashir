from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler

from django.db import IntegrityError


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, IntegrityError):
        return Response({'detail': str(exc.detail['non_field_errors'][0])}, status=status.HTTP_400_BAD_REQUEST)

    return response
