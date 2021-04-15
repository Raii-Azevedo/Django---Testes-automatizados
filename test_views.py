from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.dados = {
            'nome': 'Raissa Azevedo',
            'email': 'rhaii.azevedo@gmail.com',
            'assunto': 'Qualquer assunto',
            'mensagem': 'Qualquer mensagem'
        }
        self.client = Client()

    def test_form_valid(self):
        request = self.client.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self): #Informar dados incompletos = Inválidos
        self.dados = {
            'nome': 'Raissa Azevedo',
            'email': 'rhaii.azevedo@gmail.com',
        }
        request = self.client.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 200)
