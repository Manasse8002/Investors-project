from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Bill
from .serializers import BillSerializer

@api_view(['GET'])
def bills_index(request):
    bills = Bill.objects.all()
    serializer = BillSerializer(bills, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def bills_detail(request, bill_id):
    bill = get_object_or_404(Bill, pk=bill_id)
    serializer = BillSerializer(bill)
    return Response(serializer.data)

@api_view(['POST'])
def bills_create(request):
    serializer = BillSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def bills_update(request, bill_id):
    bill = get_object_or_404(Bill, pk=bill_id)
    serializer = BillSerializer(bill, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def bills_delete(request, bill_id):
    bill = get_object_or_404(Bill, pk=bill_id)
    bill.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
