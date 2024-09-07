from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import StreamingHttpResponse
import json
import tempfile
import os

from .mygenai import MyGenAi
from .mygenai import system_intructions

model = MyGenAi(system_intructions['incomingmail'])
model2 = MyGenAi(system_intructions['summary'])
import time

class ExtractLetterEntitiesView(APIView):
     def post(self, request):
          global model
          file = request.FILES['file']
          print('perminataan')
          data = json.loads(model.generate_content_file(file))
          response = {
               'name' : file.name,
               'entities' : data
               }
          return Response(response)
     
class SummarizeLetterView(APIView):
     def post(self, request):
          global model2
          response = process_file_with_model(request.FILES['file'], model2)
          return Response(json.loads(response))
     
class MultipleExtractLetterEntitiesView(APIView):
     def post(self, request):
          files = request.FILES.getlist('file')
          with tempfile.TemporaryDirectory() as temp_dir:
               for file in files:
                    temp_file_path = os.path.join(temp_dir, file.name)
                    with open(temp_file_path, 'wb') as temp_file:
                        for chunk in file.chunks():
                            temp_file.write(chunk)
          return Response({})
     
def process_file_with_model(file, model):
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file_path = os.path.join(temp_dir, file.name)
        with open(temp_file_path, 'wb') as temp_file:
            for chunk in file.chunks():
                temp_file.write(chunk)
        response = model.generate_content(temp_file_path)
    return response