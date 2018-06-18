from django.db.models import Sum

from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from rest_framework.views import APIView
from dateparser import parse

from apps.api.models import Animal, Herd, AnimalWeight
from apps.api.serializers import AnimalSerializer, AnimalListSerializer, AnimalWeightSerializer
from apps.api.utils import  get_interpolated_value


class AnimalViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    http_method_names = ['list', 'post', 'get']
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()

    def get_serializer_class(self):
        print(self.action)
        if self.action == 'list':
            return AnimalListSerializer
        else:
            return self.serializer_class

class AnimalweightViewSet(GenericAPIView):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = AnimalWeightSerializer
    queryset = AnimalWeight.objects.all()

    def post(self, request, *args, **kwargs):
        post_data = request.data.copy()
        post_data['animals'] = kwargs.get('unique_id')
        serializer = self.get_serializer(data=post_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)



class GetEstimatedTotalAnimalWeight(APIView):
    def get(self, request,  **kwargs):
        
        date =  parse(request.GET.get('date'))
        qs = AnimalWeight.objects.filter(weight_date=date)
        count = qs.count()
        if count > 0:
            sum_weights = qs.aggregate(total=Sum('weight'))['total']
        else:
            count = 1
            sum_weights = get_interpolated_value(date)
        ctx = dict()
        ctx['num_animals'] = count
        ctx['estimated_total_weight'] = sum_weights

        return Response(ctx, status=HTTP_200_OK)
    
        
            
            


 



