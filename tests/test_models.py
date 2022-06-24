from django.test import TestCase
from model_mommy import mommy


class PerfilTestCase(TestCase):
    
    def setUp(self) -> None:
        self.perfil = mommy.make('Perfil')
        
    def test_str(self):
        self.assertEquals(str(self.perfil), self.perfil.nome_instituicao)
        

class EditalModelTestCase(TestCase):
    
    def setUp(self) -> None:
        self.edital = mommy.make('EditalModel')
        
    def test_str(self):
        self.assertEquals(str(self.edital), self.edital.edital)
        
        
class ProjetoTestCase(TestCase):
    
    def setUp(self) -> None:
        self.projeto = mommy.make('Projeto')
        
    def test_str(self):
        self.assertEquals(str(self.projeto), self.projeto.nome_projeto)