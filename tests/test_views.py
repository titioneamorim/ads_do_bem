from django.test import Client
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from perfil.views import replace_mascara
from perfil.models import Perfil
from perfil.service import PerfilService
from projeto.models import Projeto
from model_mommy import mommy

class AccountViewTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user1.save()
        
    def test_registrar(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        dados = {
            'username': 'RegistroTeste',
            'password': 'senhaTeste',
            'password2': 'senhaTeste',
        }
        request = self.client.post(reverse('register'), data=dados)
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, 'register_done.html')
    
    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        
    def test_login_usuario(self):
        dados = {
            'username': 'testuser1',
            'password': '1X<ISRUkw+tuK',
        }
        request = self.client.post(reverse('login'), data=dados)
        self.assertEquals(request.status_code, 302)
        
    def test_home(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_termo(self):
        response = self.client.get(reverse('termo'))
        self.assertEqual(response.status_code, 200)
        
    
class PerfilViewTestCase(TestCase):
    
    def setUp(self):
        self.service = PerfilService()
        self.client = Client()
        self.test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        self.test_user1.save()
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        self.dados = {
            'nome_instituicao': 'aaaaaaaaaaaaaa',
            'dirigente': 'aaaaaaaaaaaaaa',
            'logradouro': 'aaaaaaaaaaaaaa',
            'numero': '321321',
            'bairro': 'aaaaaaaaaaaaaa',
            'cidade': 'aaaaaaaaaaaaaa',
            'UF': 'SC',
            'telefone': '99999999999',
            'fax': '9999999999',
            'site' : 'www.algumacoisa.com.br',
            'email_instituicao': 'email_instituicao@gmail.com',
            'usuario': self.test_user1.id
        }
        
    def test_perfil(self):
        response = self.client.post(reverse('perfil'), data=self.dados)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'perfil.html')
        
        # perfil = self.service.find_by_user(self.test_user1.pk)
        # print(f"AAAAAAAAAAA {perfil}")
        # self.assertIsNotNone(perfil)
        
        response = self.client.get(reverse('perfil'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'perfil.html')
        
    def test_replace_mascara(self):
        telefone = "(99)99999-9999"
        retorno = replace_mascara(telefone)
        self.assertEquals(retorno, "99999999999")
        
class ProjetoViewTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user1.save()
        self.projetos = mommy.make('projeto', 5)
        
    def test_projetos(self):
        pass
    
    # def test_delete_projeto(self):
    #     id_projeto = 1
        
    #     self.assertRaises(Projeto.DoesNotExist, Projeto.objects.get, pk=id_projeto)
    
    def test_edit_projeto(self):
        pass
    
    def test_download_projeto(self):
        pass
    
    def test_create_projeto(self):
        pass
    
    def test_save_projeto(self):
        pass
    
    def test_pesquisa_projetos(self):
        pass
    
    def test_insere_mascara_telefone_fax(self):
        pass