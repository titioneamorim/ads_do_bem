from django.test import TestCase
from edital.models import EditalModel
from edital.service import EditalService
from projeto.service import ProjetoService
from model_mommy import mommy


class EditalServiceTestCase(TestCase):
    
    def setUp(self):
        self.edital = mommy.make('EditalModel')
        service_edital = EditalService()
    
    def test_find_by_id(self):
    
        edital = EditalService.find_by_id(EditalModel, self.edital.id)
        self.assertIsInstance(edital, EditalModel)


class ProjetoServiceTestCase(TestCase):
    
    def setUp(self):
        self.perfil = mommy.make('Perfil')
        self.projeto = mommy.make('Projeto', perfil=self.perfil)
        self.service = ProjetoService()
        
    def test_find_by_id_sem_projeto(self):
        retorno = self.service.find_by_id(20)
        self.assertIsNone(retorno)
    
    def test_find_by_nome_resumo_sem_resultados(self):
        retorno = self.service.find_by_nome_resumo('qualquer', self.perfil.usuario)
        self.assertIsNone(retorno)