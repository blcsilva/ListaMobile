Aqui está o README atualizado com instruções específicas para usar o Flet em dispositivos móveis:

```markdown
# Todo App

Um aplicativo de lista de tarefas (Todo App) construído usando Django REST Framework para a API e Flet para a interface do usuário. Este projeto permite que os usuários criem, leiam, atualizem e excluam tarefas de maneira simples e intuitiva.

## Tecnologias Utilizadas

- **Django**: Framework web para Python.
- **Django REST Framework**: Para criar APIs RESTful.
- **Flet**: Para a criação da interface do usuário.
- **SQLite**: Banco de dados padrão para desenvolvimento.

## Funcionalidades

- Criar novas tarefas.
- Listar todas as tarefas.
- Atualizar tarefas existentes.
- Excluir tarefas.

## Pré-requisitos

- Python 3.9 ou superior
- Pip

## Configuração do Ambiente

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/blcsilva/ListaMobile
   cd ListaMobile
   ```

2. **Crie um ambiente virtual:**

   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual:**

   - No Windows:

     ```bash
     venv\Scripts\activate
     ```

   - No macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

   **`requirements.txt` deve conter:**

   ```plaintext
   Django>=4.0,<5.0
   djangorestframework>=3.14,<4.0
   flet>=0.24,<0.25
   ```

5. **Configure o banco de dados:**

   ```bash
   python manage.py migrate
   ```

6. **Crie um superusuário (opcional):**

   ```bash
   python manage.py createsuperuser
   ```

## Executando o Servidor

1. **Inicie o servidor Django:**

   ```bash
   python manage.py runserver
   ```

   O servidor estará disponível em [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

2. **Abra o aplicativo Flet:**

   Em um novo terminal (com o ambiente virtual ativado), execute:

   ```bash
   python frontend.py
   ```

   O aplicativo Flet será iniciado e abrirá uma interface no seu navegador.

## Executando no Dispositivo Móvel

O Flet permite que você crie aplicativos que podem ser executados em dispositivos móveis. Siga as instruções abaixo para executar o aplicativo em um dispositivo Android ou iOS:

### Pré-requisitos para Dispositivos Móveis

- **Para Android**: Você precisará do Android SDK instalado e configurado.
- **Para iOS**: Você precisará de um Mac com Xcode instalado.

### Passos para Android

1. **Instale o `flet` no seu dispositivo Android**:

   Use o seguinte comando para instalar o Flet no seu dispositivo:

   ```bash
   pip install flet
   ```

2. **Conecte seu dispositivo Android ao computador**:

   Ative o modo de desenvolvedor no seu dispositivo e conecte-o via USB.

3. **Execute o aplicativo Flet**:

   No terminal, execute o comando para iniciar o aplicativo. O Flet irá se conectar ao dispositivo e exibir o aplicativo nele.

   ```bash
   python frontend.py
   ```

### Passos para iOS

1. **Instale o `flet` no seu ambiente de desenvolvimento**:

   ```bash
   pip install flet
   ```

2. **Use o Xcode para criar um novo projeto**:

   No Xcode, crie um novo projeto e selecione o template adequado para aplicativos iOS.

3. **Execute o aplicativo no simulador ou em um dispositivo físico**:

   Você pode executar o aplicativo diretamente no simulador do Xcode ou em um dispositivo físico.

## Estrutura do Projeto

```plaintext
todo_project/
├── manage.py
├── requirements.txt
├── todo_app/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── todo_project/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## Contribuição

Contribuições são bem-vindas! Se você deseja contribuir, por favor, abra uma issue ou envie um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Contato

Se você tiver alguma dúvida ou sugestão, entre em contato pelo e-mail: bruno.tasc@gmail.com.
```

