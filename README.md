# ADS_do_Bem

<p align="center">
  <img src="https://r.mobirisesite.com/196538/assets/images/nuvem-1256x1256.png?v=1NziBv" width="256" height="256" alt="Logo"/>
</p>

<p align="center">
<a href="#Sobre">Sobre </a>   ◘   
<a href="#Instalação"> Instalação </a>   ◘   
<a href="#Licença"> Licença </a>   ◘   
<a href="#Ajustando_o_projeto_para_rodar_localmente"> Ajustando o projeto para rodar localmente </a>   ◘   
<a href="#Ajustando_o_projeto_para_rodar_na_nuvem"> Ajustando o projeto para rodar na nuvem</a>


## Sobre

Esse site é um Trabalho de Conclusão de Sistema - TCS dos alunos [Felipe](https://github.com/arandel25), [Lucas](https://github.com/lcgandolfi), [Marcelo](https://github.com/pac57282) e [Titione](https://github.com/titioneamorim), da 5ª fase do curso de [Análise e Desenvolvimento de Sistemas](https://vestibular.sc.senac.br/cursos/analise-e-desenvolvimento-de-sistemas/) da [Faculdade Senac Palhoça](https://portal.sc.senac.br/).

Diante do desafio lançado, **"Criar um sistema inovador, que auxilie a resolver o problema de um cliente ou interessado"**. Devido aos membros de nossa equipe conhecerem algumas Instituições do Terceiro Setor de nosso município, sabendo da importância de seus trabalhos nos bairros carentes e de suas dificuldades financeiras, surgiu a ideia de desenvolver um sistema, que auxilie as instituições a captarem recursos através de editais.

Utilizamos o [edital 003/2021](https://www.sds.sc.gov.br/images/Conselhos/cedca/Edital%20CEDCA%20Para%20publicar.pdf) da [Secretaria de Estado de Desenvolvimento Social de SC](https://www.sds.sc.gov.br/) para criar o template padrão para o sistema, a fim de atender uma maior variedade de projetos, segundo entidades entrevistadas, esse template é bem utilizado em editais municipais, estaduais e federais.

O sistema pode ser acessado através do [link de acesso ADS do Bem](https://ads-do-bem.herokuapp.com/).

<a href="#ads_do_bem">Voltar</a>


## Licença

Este sistema está disponível gratuitamente sobre a licença [Attribution Non-commercial Share Alike (BY-NC-SA)](https://creativecommons.org/licenses/by-nc-sa/3.0/br/), essa licença permite a cópia e redistribuição do código, desde que seja utilizado para fins não comerciais, seja dado os créditos apropriados a equipe de desenvolvimento e seja distribuído sob a mesma licença.

<a href="#ads_do_bem">Voltar</a>


## Instalação

O sistema foi desenvolvido com o framework Django na versão 4.0.4, você precisa acessar o local em que vai armazenar o projeto, depois pode clonar através do comando: ``gh repo clone titioneamorim/ads_do_bem``

Acessar a pasta do projeto: ``cd ads_do_bem``

Sugerimos criar uma venv, maiores informações sobre o que é uma venv, consultar a [documentação do python](https://docs.python.org/pt-br/3/library/venv.html#:~:text=O%20m%C3%B3dulo%20venv,diret%C3%B3rios%20do%20site.).

``python3 -m venv venv``

Uma vez criado seu ambiente virtual, você deve ativá-lo.

No **Windows**, execute:

``venv\Scripts\activate.bat``

No **Unix** ou no **MacOS**, executa:

``source venv/bin/activate``

Instalar as bibliotecas necessárias para execução do sistema: ``pip install -r requirements-dev.txt``

Criar o banco de dados sqlite3 local: ``python3 manage.py migrate``

Criar o super usuário do sistema: ``python3 manage.py createsuperuser`` e preencher os dados solicitados pelo Django para a criação do super usuário.

Executando o projeto: ``python3 manage.py runserver``

Com o projeto rodando, acessar o link [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

Realize o login e após, é necessário criar um edital no [link](http://127.0.0.1:8000/admin/edital/editalmodel/add/), o preenchimento do campo Edital: não pode conter espaços.

Após criar o edital, é necessário alterar o nome do arquivo **ads_do_bem/projeto/templates/003_2021_SDSSC.html** para o nome que você deu para o arquivo, na etapa anterior.

<a href="#ads_do_bem">Voltar</a>


## Ajustando_o_projeto_para_rodar_localmente


É necessário efetuar alguns ajustes em alguns arquivos do projeto.

1) Acesse o arquivo **ads_do_bem/config/settings.py**

2) Preencher os campos solicitados abaixo da linha **Configuração de envio de e-mail pelo Django** para configurar a conta de e-mail que será utilizada na restauração da senha do usuário.

3) Gere uma senha para o Secret Key via terminal: ``python -c "import secrets; print(secrets.token_urlsafe())" `` 

4) Copie a senha gerada e cole no campo SECRET_KEY do arquivo **ads_do_bem/.env**.

5) Caso precise debugar o projeto, altere o **DEBUG** para **True**, quando for rodar em produção precisa voltar o valor para **False**.

**Pronto, o sistema está apto para rodar localmente.**

<a href="#ads_do_bem">Voltar</a>


## Ajustando_o_projeto_para_rodar_na_nuvem


1) Realizar as etapas anteriores do tópico **Ajustando o projeto para rodar localmente**

2) Abrir o arquivo **ads_do_bem/config/settings.py** e preencher o domínio que será utilizado no campo **ALLOWED_HOSTS**.

3) Caso for executar o projeto no [Heroku](https://www.heroku.com/), precisar alterar a versão do **Python** para a que está instalada na sua **venv**, no arquivo **ads_do_bem/runtime.txt**.

4) O projeto está ajustado para utilizar no **Heroku**, maiores informações de como utilizar o **Heroku** pode ser obtido nesse [link](https://devcenter.heroku.com/categories/deployment).

**Pronto, o sistema está apto para rodar na nuvem.**

<a href="#ads_do_bem">Voltar</a>
