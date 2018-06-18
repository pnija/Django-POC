from datetime import datetime
from apps.api.models import AnimalWeight

def get_interpolated_value(input_date):

    first_obj = AnimalWeight.objects.filter(weight_date__lt=input_date).order_by('weight_date').last()
    second_obj = AnimalWeight.objects.filter(weight_date__gt=input_date).order_by('weight_date').first()
    diffrence_in_values = second_obj.weight - first_obj.weight
    number_of_dates_in_between = (second_obj.weight_date - first_obj.weight_date).days
    interval_values = round(diffrence_in_values/number_of_dates_in_between)
    number_of_dates_in_between_input_dates = (input_date - first_obj.weight_date).days
    
    calculated_weight = first_obj.weight + (interval_values * number_of_dates_in_between_input_dates)
    return calculated_weight

