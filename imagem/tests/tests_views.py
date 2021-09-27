from rest_framework.test import APIClient
from django.test import TestCase
from imagem.models import Imagem, Analise


class ImagemTestCase(TestCase):

    url_base = "http://localhost:8000/"

    def setUp(self):
        Imagem.objects.create(nome_imagem='skate', tipo_imagem='png')

    def test_imagem_post(self):
        client = APIClient()
        response = client.post("http://localhost:8000/imagem/", data={
                               'id_imagem': '1', 'nome_imagem': 'skate', 'tipo_imagem': 'png'}, 
                               format='json')
        self.assertEqual(response.status_code, 201)

    def test_imagem_get(self):
        client = APIClient()
        response = client.get("http://localhost:8000/imagem/",
                              data={'id_imagem': '1'}, format='json')
        self.assertEqual(response.status_code, 200)

    def test_analise_post(self):
        client = APIClient()
        response = client.post("http://localhost:8000/analise/", data={
                               'id_analise': '1', 'analise': 'Imagem de um skate na oficina', 'id_imagem': '1', 'tipo_analise': 'visual', 'status': 'analisado'})
        self.assertEqual(response.status_code, 201)

    def test_analise_get(self):
        client = APIClient()
        response = client.get("http://localhost:8000/analise/",
                              data={'id_analise': '1'}, format='json')
        self.assertEqual(response.status_code, 200)

    def test_analise_imagem_get(self):
        client = APIClient()
        response = client.get(
            "http://localhost:8000/imagem-analise/", data={'id_imagem': '1'})
        self.assertEqual(response.status_code, 200)

    def test_analise_imagem_get_sem_id_imagem(self):
        client = APIClient()
        response = client.get("http://localhost:8000/imagem-analise/")
        self.assertEqual(response.status_code, 200)

    def test_imagem_analise_get(self):
        client = APIClient()
        response = client.get("http://localhost:8000/analise-imagem/")
        self.assertEqual(response.status_code, 200)

    def test_analise_delete(self):
        client = APIClient()
        response = client.delete(
            "http://localhost:8000/analise/", data={'id_analise': '1'}, format='json')
        self.assertEqual(response.status_code, 204)

    def test_imagem_delete(self):
        client = APIClient()
        response = client.delete(
            "http://localhost:8000/imagem/", data={'id_imagem': '1'}, format='json')
        self.assertEqual(response.status_code, 204)
