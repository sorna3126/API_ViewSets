from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from app.models import *
from app.serializers import *
from rest_framework.response import Response

# Create your views here.


class ProductCrud(ViewSet):
    def list(self,request):
        PO=Product.objects.all()
        JDO=ProductModelSerializer(PO,many=True)
        return Response(JDO.data)

    def retrieve(self,request,pk):
        PO=Product.objects.get(pk=pk)
        JDO=ProductModelSerializer(PO)
        return Response(JDO.data)

    def create(Self,request):
        JD=request.data
        PMS=ProductModelSerializer(data=JD)
        if PMS.is_valid():
            PMS.save()
            return Response({'POST':'DAta is created/Inserted'})
        else:
            return Response({'Data is not Created/Inserted'})

    def update(self,request,pk):
        PO=Product.objects.get(pk=pk)
        PDO=ProductModelSerializer(PO,data=request.data)
        if PDO.is_valid():
            PDO.save()
            return Response({'update': 'Data is updated successfully'})
        else:
            return Response({'Data is not update'})
    
    def partial_update(self,request,pk):
        PO=Product.objects.get(pk=pk)
        PDO=ProductModelSerializer(PO,data=request.data,partial=True)
        if PDO.is_valid():
            PDO.save()
            return Response({'Partial update': 'Data is updated successfully'})
        else:
            return Response({'Data is not update'})

    def destroy(self,request,pk):
        PDO=Product.objects.get(pk=pk).delete()
        return Response({'Data is deleted Successfully'})
        



