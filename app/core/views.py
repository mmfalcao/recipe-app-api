"""
Core Views for the app
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def health_check(request):
    """Returns successful response"""
    return Response({'healthy': True})
