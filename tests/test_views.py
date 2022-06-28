from urllib import response
from urllib.parse import urlencode
from django import views
from django.http import HttpRequest
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from requests import request
from edital.models import EditalModel
from perfil.views import replace_mascara
from perfil.models import Perfil
from perfil.service import PerfilService
from projeto.models import Projeto
from projeto.service import ProjetoService
from account.forms import FormularioLogin, RegistroUsuario
from model_mommy import mommy

from projeto.views import insere_mascara_telefone_fax, projetos, save_projeto

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
        self.usuario = {
            'username': 'Felipe',
            'password': 'teste321',
            'password2': 'teste321'
        }
        self.user_form = RegistroUsuario(self.usuario)
        self.usuario_test = self.user_form.save(commit=False)
        self.usuario_test.set_password(self.user_form.cleaned_data['password'])
        self.usuario_test.save()
            
        login = self.client.login(username='Felipe', password='teste321')
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
            'usuario': ''
        }
        
    def test_perfil_get_post_error(self):
        response = self.client.post('/perfil/', data=self.dados)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'perfil.html')
        
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
        self.service_projeto = ProjetoService()
        self.test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        self.test_user1.save()
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        self.perfil = mommy.make('perfil', usuario=self.test_user1)
        self.edital = mommy.make('EditalModel', edital="003_2021_SDSSC")
        self.projetos = mommy.make('projeto', _quantity=5, perfil=self.perfil, template=self.edital)
        
    def test_projetos(self):
        response = self.client.get(reverse('projetos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projetos.html')
        self.assertTrue(len(response.context['projetos']) == 5)
    
    def test_delete_projeto(self):
        response = self.client.post('/projeto/del/1')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(len(Projeto.objects.all()) == 4)
    
    def test_edit_projeto(self):
        response = self.client.get('/projeto/edit/2')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projeto.html')
        self.assertQuerysetEqual(response.context['editais'], EditalModel.objects.filter(id=self.edital.id))
        self.assertEquals(response.context['projeto'], Projeto.objects.filter(id=2)[0])
    
    def test_download_projeto(self):
        projeto = self.projetos[0]
        response = self.client.post(f'/projeto/download/{projeto.id}')
        self.assertEquals(response.context['projeto'], projeto)
        self.assertEquals(response.context['perfil'], projeto.perfil)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, f'{projeto.template.edital}.html')
    
    def test_create_projeto(self):
        response = self.client.get(reverse('create_projeto'))
        self.assertQuerysetEqual(response.context['editais'], EditalModel.objects.filter(id=self.edital.id))
        self.assertEquals(response.context['perfil'], Perfil.objects.filter(id=self.perfil.id)[0])
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projeto.html')
    
    def test_save_projeto_novo_error(self):
        projeto = self.projetos[0]
        projeto.id = ''
        projeto.inicio_execucao = ''
        projeto.fim_execucao = ''
        projeto = projeto.__dict__
        response = self.client.post('/projeto/save/', data=projeto)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projeto.html')
        
    # def test_save_projeto_novo_success(self):
        
        
    def test_save_projeto_editado_error(self):
        self.projetos[3].inicio_execucao = ''
        self.projetos[3].fim_execucao = ''
        self.projetos[3].nome_projeto = 'ProjetoTeste'
        projeto = self.projetos[3].__dict__
        response = self.client.post('/projeto/save/', data=projeto)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('projeto.html')
        self.assertNotEquals(response.context['projeto'], Projeto.objects.filter(id=self.projetos[3].id))
        
    # def test_save_projeto_editado_success(self):
        
    
    def test_pesquisa_projetos_success(self):
        for n in range(3):
            self.projetos.append(mommy.make('projeto', nome_projeto="Projeto_teste", perfil=self.perfil, template=self.edital))
        response = self.client.get('/projeto/pesquisa/', data={'termo': 'Projeto_teste'})
        self.assertEqual(response.status_code, 200)
        self.assertEquals(len(response.context['projetos']), 3)
        
    def test_pesquisa_projetos_warning(self):
        response = self.client.get('/projeto/pesquisa/', data={'termo': 'Para não achar'})
        self.assertEqual(response.status_code, 302)
        self.assertFalse('projetos' in response)
        
    
    def test_insere_mascara_telefone_fax(self):
        numero1 = '99999999999'
        numero2 = '8888888888'
        tel = insere_mascara_telefone_fax(numero1)
        self.assertEqual('(99) 99999-9999', tel)
        fax = insere_mascara_telefone_fax(numero2)
        self.assertEqual('(88) 8888-8888', fax)
        