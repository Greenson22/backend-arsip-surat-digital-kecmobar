"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import google.generativeai as genai
from PIL import Image

class MyGenAi():
     # Create the model
     def __init__(self) -> None:     
          genai.configure(api_key='AIzaSyB8KwQjNr6RAyElNxcTMTDI_rPGtPjvWUw')
          self.generation_config = {
               "temperature": 1,
               "top_p": 0.95,
               "top_k": 64,
               "max_output_tokens": 8192,
               "response_mime_type": "application/json",
          }
          self.model = self.create_model()
          self.chat_session = self.create_chat()
     
     def create_model(self):
          model = genai.GenerativeModel(
               model_name="gemini-1.5-flash",
               generation_config=self.generation_config,
               # safety_settings = Adjust safety settings
               # See https://ai.google.dev/gemini-api/docs/safety-settings
               system_instruction="Ambil semua entitie mulai dari: no agenda, nomor surat, tanggal surat, tanggal terima, asal surat, perihal, penerima. \n1. Kembalikan dalam bentuk json\n2. Untuk perihal tolong ringkas dari surat tersebut\n3. Format tanggal dd/mm/yy dengan menggunakan angka semua\n4. Untuk semua key lebih dari satu kata, dihubungkan dengan tanda underscore.\n5. Jika suatu entitie kosong, maka buatkan saya string kosong",
          )
          return model

     def create_chat(self):
          chat_session = self.model.start_chat(
               history=[
               ]
          )
          return chat_session
     
     def send_message(self, file_path):
          image = Image.open(file_path)
          response = self.chat_session.send_message(image)
          return response.text