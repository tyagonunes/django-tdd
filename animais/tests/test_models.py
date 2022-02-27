from django.test import TestCase, RequestFactory
from animais.models import Animal

class AnimalModelTestCase(TestCase):
  def setUp(self):
    self.animal = Animal.objects.create(
      nome_animal = 'Leão',
      predador= 'Sim',
      venenoso='Não',
      domestico='Não'
    )

  def test_animal_cadastrado_com_catacteristicas(self):
    """Test verifica se o animal esta cadastrado com as suas caracteristicas"""
    self.assertEqual(self.animal.nome_animal, 'Leão')