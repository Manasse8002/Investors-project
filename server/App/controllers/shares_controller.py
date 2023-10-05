from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Share
from .serializers import ShareSerializer

@api_view(['GET'])
def shares_index(request):
    shares = Share.objects.all()
    serializer = ShareSerializer(shares, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def shares_detail(request, share_id):
    share = get_object_or_404(Share, pk=share_id)
    serializer = ShareSerializer(share)
    return Response(serializer.data)

@api_view(['POST'])
def shares_create(request):
    serializer = ShareSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def shares_update(request, share_id):
    share = get_object_or_404(Share, pk=share_id)
    serializer = ShareSerializer(share, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def shares_delete(request, share_id):
    share = get_object_or_404(Share, pk=share_id)
    share.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
