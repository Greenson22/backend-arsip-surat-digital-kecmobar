from rest_framework.views import APIView
from rest_framework.response import Response
import json
import tempfile
import os

from .mygenai import MyGenAi
from .mygenai import system_intructions, load_vectorizer_nb, load_letter_model_nb

model_incomingmail = MyGenAi(system_intructions['incomingmail'])
model_outgoingmail = MyGenAi(system_intructions['outgoingmail'])
model_summary = MyGenAi(system_intructions['summary'])
model_ocr = MyGenAi(system_intructions['ocr'])

# naive bayes
model_naivebayes = load_letter_model_nb()
vectorizer = load_vectorizer_nb()

class ExtractLetterEntitiesView(APIView):
     def post(self, request):
          model = model_incomingmail
          # mengecek jika request terdapat model dan type outgoingmail
          if 'model_type' in request.data and request.data['model_type'] == 'outgoingmail':
               model = model_outgoingmail

          file = request.FILES['file']
          data = json.loads(model.generate_content_file(file))
          response = {
               'name' : file.name,
               'entities' : data
               }
          return Response(response)

class LetterOCRView(APIView):
     def post(self, request):
          model =  model_ocr

          file = request.FILES['file']
          data = model.generate_content_file(file)
          response = {
               'name' : file.name,
               'content' : data
               }
          return Response(response)

class LetterClassificationView(APIView):
     def post(self, request):
          modelnb = model_naivebayes
          tfidf_vectorizer = vectorizer
          letter = request.data['letter']
          letter_matrix = tfidf_vectorizer.transform([letter])
          predict = modelnb.predict(letter_matrix)
          return Response({'category': predict})
          # {'Surat Perintah': 1,
          # 'Surat Undangan': 4,
          # 'Surat Edaran': 0,
          # 'Surat Permohonan': 2,
          # 'Surat Tugas': 3}


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