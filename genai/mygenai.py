"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import google.generativeai as genai
import pathlib

system_intructions = {
     "incomingmail" : "**Instruksi:**\n\n1. **Ekstraksi Entitas:** Dari file yang diberikan, ekstrak semua entitas berikut:\n    * no agenda\n    * nomor surat\n    * tanggal surat\n    * tanggal terima\n    * asal surat\n    * perihal\n    * penerima\n\n2. **Format JSON:** Kembalikan entitas yang diekstrak dalam format JSON dengan struktur berikut:\n    * `agenda_number`: (nilai dari 'no agenda')\n    * `letter_number`: (nilai dari 'nomor surat')\n    * `letter_date`: (nilai dari 'tanggal surat', diformat sebagai yyyy-mm-dd)\n    * `received_date`: (nilai dari 'tanggal terima', diformat sebagai yyyy-mm-dd)\n    * `source`: (nilai dari 'asal surat')\n    * `subject`: (ringkasan dari 'perihal' dalam surat)\n    * `recipient`: (nilai dari 'penerima')\n\n3. **Penanganan Nilai Kosong:** Jika suatu entitas tidak ditemukan dalam teks, berikan null (`\"\"`) untuk kunci yang sesuai dalam JSON.\n\n4. **Output Eksklusif:** Pastikan output hanya berisi JSON yang dijelaskan di atas, tanpa informasi tambahan lainnya.",
     "summary" : "Tolong proses file ini:\n1. **Ringkasan:** Buat ringkasan yang baik dari file ini dalam bahasa Indonesia.\n2. **Output:** \n   * Buat objek JSON dengan key \"summary\" dan value berupa ringkasan yang telah dibuat.",
}

class MyGenAi():
     # Create the model
     def __init__(self, instruction) -> None:     
          genai.configure(api_key='AIzaSyB8KwQjNr6RAyElNxcTMTDI_rPGtPjvWUw')
          self.generation_config = {
               "temperature": 1,
               "top_p": 0.95,
               "top_k": 64,
               "max_output_tokens": 8192,
               "response_mime_type": "application/json",
          }
          self.create_model(instruction)
          self.create_chat()
     
     def create_model(self, system_instruction):
          model = genai.GenerativeModel(
               model_name="gemini-1.5-flash",
               generation_config=self.generation_config,
               # safety_settings = Adjust safety settings
               # See https://ai.google.dev/gemini-api/docs/safety-settings
               system_instruction=system_instruction,
          )
          self.model = model
          self.create_chat()

     def create_chat(self):
          chat_session = self.model.start_chat(
               history=[
               ]
          )
          self.chat_session = chat_session
     
     def send_message_file(self, file):
          response = self.chat_session.send_message(genai.upload_file(file))
          return response.text

     def generate_content(self, file):
          response = self.model.generate_content(genai.upload_file(file))
          return response.text
     
     def generate_content_file(self, file):
          prompt = ''
          response = self.model.generate_content([
               prompt,
                   {
                         "mime_type": "application/pdf",
                         "data": file.read()
                    }
          ])
          return response.text