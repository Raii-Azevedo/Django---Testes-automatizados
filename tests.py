from django.test import TestCase

# Teste de números


def add_num(num):
    return num + 1


class SimplesTestCase(TestCase):

    # Roda toda vez
    def setUp(self):
        self.numero = 41

    # Testa a unidade de código
    def test_add_num(self):
        valor = add_num(self.numero)
        self.assertTrue(valor == 42 )
