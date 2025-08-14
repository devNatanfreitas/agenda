from django.core.files.storage import Storage
from django.core.files.base import ContentFile
from django.conf import settings
from supabase import create_client, Client
import os
from uuid import uuid4

class SupabaseStorage(Storage):
    def __init__(self):
        self.supabase_url = os.environ.get('SUPABASE_URL')
        self.supabase_key = os.environ.get('SUPABASE_SERVICE_KEY')
        self.bucket_name = os.environ.get('SUPABASE_BUCKET', 'media')
        self.supabase: Client = create_client(self.supabase_url, self.supabase_key)

    def _save(self, name, content):
        # Gera um nome único para o arquivo
        file_name = f"{uuid4()}_{name}"
        
        # Lê o conteúdo do arquivo
        content.seek(0)
        file_data = content.read()
        
        # Faz upload para o Supabase Storage
        try:
            # A chamada .upload() já levanta uma exceção em caso de erro.
            # Se a linha abaixo executar sem erro, o upload foi bem-sucedido.
            self.supabase.storage.from_(self.bucket_name).upload(
                path=file_name,
                file=file_data,
            )
            
            # Se chegamos até aqui, o upload funcionou.
            # Simplesmente retorne o nome do arquivo.
            return file_name
                
        except Exception as e:
            # Captura qualquer exceção do upload e a relança
            # com uma mensagem mais amigável.
            raise Exception(f"Falha no upload para Supabase: {str(e)}")
        
    def _open(self, name, mode='rb'):
        try:
            # Baixa o arquivo do Supabase
            result = self.supabase.storage.from_(self.bucket_name).download(name)
            return ContentFile(result)
        except Exception as e:
            raise FileNotFoundError(f"Arquivo '{name}' não encontrado: {str(e)}")

    def url(self, name):
        # Retorna a URL pública do Supabase
        try:
            result = self.supabase.storage.from_(self.bucket_name).get_public_url(name)
            return result
        except:
            return f"{self.supabase_url}/storage/v1/object/public/{self.bucket_name}/{name}"

    def exists(self, name):
        try:
            self.supabase.storage.from_(self.bucket_name).download(name)
            return True
        except:
            return False

    def delete(self, name):
        try:
            result = self.supabase.storage.from_(self.bucket_name).remove([name])
            return result.status_code == 200
        except:
            return False

    def size(self, name):
        try:
            result = self.supabase.storage.from_(self.bucket_name).download(name)
            return len(result)
        except:
            return 0