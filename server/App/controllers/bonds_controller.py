from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Bond
from .serializers import BondSerializer

@api_view(['GET'])
def bonds_index(request):
    bonds = Bond.objects.all()
    serializer = BondSerializer(bonds, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def bonds_detail(request, bond_id):
    bond = get_object_or_404(Bond, pk=bond_id)
    serializer = BondSerializer(bond)
    return Response(serializer.data)

@api_view(['POST'])
def bonds_create(request):
    serializer = BondSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def bonds_update(request, bond_id):
    bond = get_object_or_404(Bond, pk=bond_id)
    serializer = BondSerializer(bond, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def bonds_delete(request, bond_id):
    bond = get_object_or_404(Bond, pk=bond_id)
    bond.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
