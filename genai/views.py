from rest_framework.views import APIView
from rest_framework.response import Response
import json
import tempfile
import os

from .mygenai import MyGenAi
from .mygenai import system_intructions

model_incomingmail = MyGenAi(system_intructions['incomingmail'])
model_outgoingmail = MyGenAi(system_intructions['outgoingmail'])
model_summary = MyGenAi(system_intructions['summary'])

class ExtractLetterEntitiesView(APIView):
     def post(self, request):
          model = model_incomingmail
          # mengecek jika request terdapat model type outgoingmail
          if 'model_type' in request.data and request.data['model_type'] == 'outgoingmail':
               model = model_outgoingmail

          file = request.FILES['file']
          data = json.loads(model.generate_content_file(file))
          response = {
               'name' : file.name,
               'entities' : data
               }
          return Response(response)
     
class SummarizeLetterView(APIView):
     def post(self, request):
          global model2
          response = process_file_with_model(request.FILES['file'], model_summary)
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