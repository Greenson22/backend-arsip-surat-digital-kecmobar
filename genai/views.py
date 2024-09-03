from rest_framework.views import APIView
from rest_framework.response import Response
from django.apps import apps
import json
import tempfile
import os
from .mygenai import MyGenAi
from .mygenai import system_intructions

model = MyGenAi(system_intructions['incomingmail'])
model2 = MyGenAi(system_intructions['summary'])

class LetterDetailView(APIView):
     def post(self, request):
          global model
          response = process_file_with_model( request.FILES['file'], model)
          return Response(json.loads(response))
     
class LetterSummaryView(APIView):
     def post(self, request):
          global model2
          response = process_file_with_model(request.FILES['file'], model2)
          return Response(json.loads(response))
     
def process_file_with_model(file, model):
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file_path = os.path.join(temp_dir, file.name)
        with open(temp_file_path, 'wb') as temp_file:
            for chunk in file.chunks():
                temp_file.write(chunk)
        response = model.send_message_file(temp_file_path)
    return response