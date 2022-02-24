# Gestao_Produtos
1. App simples de gestão de produtos,para registrar,atualizar,mostrar e deletar produtos em um sistema de gestão
2. Para rodar o projeto clone o repositorio
3. No terminal na pasta onde vc quer colocar o projeto abra o seu terminal,( prompt de comando ou powershel no caso do windows) e digite git clone copie a url do projeto e aperte enter
4. Agora vc tem um clone do repositorio do projeto em sua maquina
5. É necessario também que o python esteja instalado no seu pc
6. Abra o terminal, vá para página raiz do projeto(parte onde está o arquivo manage.py)
## Criando uma virtualenv
8. Crie uma virtualenv.Para isso digite no terminal python3 -m venv gestao-env
9. ative a venv.Para isso digite no terminal:
10. no caso de seu sistema for windows: gestao-env\Scripts\activate.bat ou gestao-env/bin/activate. Se aparecer uma msg não permitindo executar o script,abra o power shell como adm e digite o seguinte comando Set-ExecutionPolicy Unrestricted e depois s para salvar, volte a pasta do projeto pelo powershell novamente e tente ativar a venv
11. 11. Se for um mac: source gestao-env/bin/activate
12. linux:  source gestao-env/bin/activate
13. Se der tudo certo gestao-env vai aparecer agora no seu terminal para mostrar que seu ambiente virtual está ativado (gestao-env)
## Instalando as Bibliotecas necessárias
11. No terminal na pasta raiz do projeto(aquela com o arquivo manage.py) digite pip install -r requirements.txt certifique-se de que todas as bibliotecas foram instaladas(algumas não irão instalar e utras não irãos instalar de primeira)
12. Digite o comando pip freeze para ver quais bibliotecas foram instaladas
## Criando as Migrations
14. Agora para fazer as migrações do banco de dados
15. digite python manage.py makemigrations(no caso de mac ou linux use python3)
16. depois python manage.py migrate(no caso de mac ou linux use python3)
## Criando Superuser
17. Digite python manage.py createsuperuser
18. Digite nome e senha, não precisa de email(isso serve para acessar a parte de adm do site)
## Acessando o app localmente
19. para acessar o app localmente digite no terminal na pasta raiz do projeto(aquela como manage.py) o seguinte comando python ou python3 manage.py runserver
20. Isso abrirá o aplicativo na página inicial
