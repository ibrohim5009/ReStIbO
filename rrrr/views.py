from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer,ProductSerializer
from .models import Category,Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
import rest_framework.status as status

# Create your views here.

@api_view(["GET"])
def get_categories(request):
    queryset=Category.objects.all()
    serializer=CategorySerializer(queryset,many=True)
    data=serializer.data
    return Response(data)

def data_prepare(request):
    data=request.data
    if type(data)==dict:
        data=dict(data)
    else:
        data={key: None if value == 'null' else value for key, value in data.items()}
    return data


@api_view(["POST"])
def create_category(request):
    data=data_prepare(request)
    print(data)
    serializer=CategorySerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    item=serializer.save()
    print(item)
    return Response(serializer.data)

def get_object(**kwargs):
    queryset=Category.objects.all()
    obj=queryset.get(**kwargs)
    return obj

@api_view(["DELETE"])
def delete_category(request,pk):
    instance=get_object(pk=pk)
    instance.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryViewSet(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class ProductViewSet(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
