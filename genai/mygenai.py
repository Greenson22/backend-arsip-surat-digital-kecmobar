"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import google.generativeai as genai
import pickle

system_intructions = {
     "incomingmail" : "**Instruksi:**\n\n1. **Ekstraksi Entitas:** Dari file yang diberikan, ekstrak semua entitas berikut:\n    * no agenda\n    * nomor surat\n    * tanggal surat\n    * tanggal terima\n    * asal surat\n    * perihal\n    * penerima\n\n2. **Format JSON:** Kembalikan entitas yang diekstrak dalam format JSON dengan struktur berikut:\n    * `agenda_number`: (nilai dari 'no agenda')\n    * `letter_number`: (nilai dari 'nomor surat')\n    * `letter_date`: (nilai dari 'tanggal surat', diformat sebagai yyyy-mm-dd)\n    * `received_date`: (nilai dari 'tanggal terima', diformat sebagai yyyy-mm-dd)\n    * `source`: (nilai dari 'asal surat')\n    * `subject`: (ringkasan dari 'perihal' dalam surat)\n    * `recipient`: (nilai dari 'penerima')\n\n3. **Penanganan Nilai Kosong:** Jika suatu entitas tidak ditemukan dalam teks, berikan null (`\"\"`) untuk kunci yang sesuai dalam JSON.\n\n4. **Output Eksklusif:** Pastikan output hanya berisi JSON yang dijelaskan di atas, tanpa informasi tambahan lainnya.",
     "outgoingmail" : "**Instruksi:**\n1. **Ekstraksi Entitas:** Dari file yang diberikan, ekstrak semua entitas berikut:\n    * tanggal surat\n    * tujuan surat\n    * nomor surat\n    * perihal\n\n2. **Format JSON:** Kembalikan entitas yang diekstrak dalam format JSON dengan struktur berikut:\n    * `letter_date`: (nilai dari 'tanggal surat', diformat sebagai yyyy-mm-dd)\n    * `destination`: (nilai dari 'tujuan surat')\n    * `letter_number`: (nilai dari 'nomor surat')\n    * `subject`: (ringkasan dari 'perihal' dalam surat)\n\n3. **Penanganan Nilai Kosong:** Jika suatu entitas tidak ditemukan dalam teks, masukan null untuk kunci yang sesuai dalam JSON.\n\n4. **Output Eksklusif:** Pastikan output hanya berisi JSON yang dijelaskan di atas, tanpa informasi tambahan lainnya.",
     "summary" : "Tolong proses file ini:\n1. **Ringkasan:** Buat ringkasan yang baik dari file ini dalam bahasa Indonesia.\n2. **Output:** \n   * Buat objek JSON dengan key \"summary\" dan value berupa ringkasan yang telah dibuat.",
     "ocr": "Kamu adalah seorang asisten AI yang ahli dalam mengekstrak teks dari file PDF. \n\nBerikut adalah beberapa hal yang perlu kamu perhatikan:\n\n* **Prioritaskan akurasi**: Pastikan teks yang diekstrak akurat dan sesuai dengan isi PDF.\n* **Pertahankan format**: Pertahankan format asli dari teks, termasuk paragraf, spasi, dan struktur dokumen.\n* **Identifikasi elemen**: Identifikasi elemen-elemen penting dalam PDF, seperti judul, subjudul, tabel, dan gambar.\n* **Abaikan noise**: Abaikan elemen-elemen yang tidak relevan, seperti header, footer, dan nomor halaman.\n* **Abaikan noise**: noise yang diabaikan tidak usah di sebut lagi.\n* **Berikan output yang terstruktur**: Berikan output dalam format yang terstruktur dan mudah dibaca, seperti teks biasa. Dan tidak ada awalan lain selain dari isi surat tersebut.",
}

# memuat model naive bayes yang telah dilatih
def load_letter_model_nb():
     return pickle.load(open('genai/my_model/model_naive_bayes.sav', 'rb'))
# memuat vectorizer tfidf
def load_vectorizer_nb():
     return pickle.load(open('genai/my_model/vectorizer_tfidf.sav', 'rb'))

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