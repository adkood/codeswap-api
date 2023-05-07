from django.shortcuts import render
import json
import random
from django.http import JsonResponse
from api.models import Room
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404


@csrf_exempt
def create_room(request):

    if request.method == 'POST':
        # Generate a random id for the new room
        room_id = random.randint(1000, 9999)

        # Create a new room instance with the random id
        room = Room.objects.create(id=room_id, value='')

        # Return the room id as a JSON response
        response_data = {'room_id': room_id}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def get_room(request, room_id):
    if request.method == 'GET':
        # Generate a random id for the new room
        room = get_object_or_404(Room, id=room_id)
        # Return the room id as a JSON response
        response_data = {'room_id': room.id,
                         'value': room.value, 'language': room.language, 'readonly': 'true'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def patch_room(request, room_id):
    if request.method == 'PATCH':
        # Generate a random id for the new room
        room = Room.objects.get(id=room_id)
        request_data = json.loads(request.body)
        room.value = request_data.get('value', room.value)
        room.language = request_data.get('language', room.language)
        room.save()
        # Return the room id as a JSON response
        response_data = {'room_id': room.id}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid request method'})
