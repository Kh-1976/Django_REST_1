from .models import Car
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from .serializers import CarSerializer


class CarApiView(APIView):
    def get(self, request, *args, **kwargs):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        car = Car.objects.create(**serializer.validated_data)
        context = CarSerializer(car)
        return Response(context.data, status=HTTP_201_CREATED)

