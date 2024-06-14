from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
import requests
import json

class TelaLogin(BoxLayout):
    def __init__(self, **kwargs):
        super(TelaLogin, self).__init__(**kwargs)
        self.orientation= "vertical"
        self.padding= [50, 20]
        self.spacing= 10
        Window.size = (400, 696)
        Window.clearcolor= (1, 1, 1, 1)
        self.add_widget(Image(source='/Users/aluno.sesipaulista/Desktop/Login/img/imagem.png'))

        self.add_widget(Label(text='LOGIN', font_size=24, color=(0.15,0.15,0.15,1)))

        self.email_input= TextInput(hint_text='Email',background_color=(0.15, 0.15, 0.15, 1), multiline=False)
        self.password_input= TextInput(hint_text='Senha', background_color=(0.15, 0.15, 0.15, 1), password=True,multiline=False)
        self.add_widget(self.email_input)
        self.add_widget(self.password_input)

        self.buttons_layout= BoxLayout(padding=[0, 10], spacing=10)
        self.login_button= Button(text='Entrar', color=(1, 1, 1, 1), size_hint=(1, None), size=(450, 50), background_color=(0.15, 0.15, 0.15, 1))
        self.login_button.bind(on_press=self.login)
        self.signup_button= Button(text='Cadastrar', color=(1, 1, 1, 1), size_hint=(1 ,None), size=(450, 50), background_color=(0.15, 0.15, 0.15, 1))
        self.signup_button.bind(on_press=self.signup)  
        self.buttons_layout.add_widget(self.login_button)
        self.buttons_layout.add_widget(self.signup_button)
        self.add_widget(self.buttons_layout)

    def login(self,instance):
        email = self.email_input.text
        senha = self.password_input.text
        print('Email:', email)
        print('Senha:', senha)

        data = {'Email': email, 'Senha': senha}

        link = 'https://login-1811a-default-rtdb.firebaseio.com/Login'
        try:
            requisicao = requests.post('{}/.json'.format(link), data=json.dumps(data))
            resposta = requisicao.json()

            if requisicao.status_code == 200 and resposta:
                if email == 'usuario@gmail.com' and senha == 'senha123':
                    print('Login bem sucedido')
                else:
                    print('Informações erradas')
            else:
                print('Erro ao realizar login')
        except requests.RequestException as e:
            print('Erro ao conectar ao servidor: {}'.format(e))

    def signup(self, instance):
        app = App.get_running_app()
        app.root.current = 'cadastro'

class TelaCadastro(BoxLayout):
    def __init__(self, **kwargs):
        super(TelaCadastro, self).__init__(**kwargs)
        self.orientation= "vertical"
        self.padding= [50, 20]
        self.spacing= 10
        Window.clearcolor= (1, 1, 1, 1)
        self.add_widget(Image(source="/Users/aluno.sesipaulista/Desktop/Login/img/imagem.png"))

        self.add_widget(Label(text='CADASTRO', font_size=24, color=(0.15,0.15,0.15,1)))

        self.email_input= TextInput(hint_text='Email',background_color=(0.15, 0.15, 0.15, 1), multiline=False)
        self.senha_input= TextInput(hint_text='Senha',background_color=(0.15, 0.15, 0.15, 1),password=True,multiline=False)
        self.add_widget(self.email_input)
        self.add_widget(self.senha_input)

        self.buttons_layout= BoxLayout(padding=[0, 10], spacing=10)
        self.cadastrar_button= Button(text='Cadastre-se', color=(1, 1, 1, 1), size_hint=(1, None), size=(450, 50), background_color=(0.15, 0.15, 0.15, 1))
        self.cadastrar_button.bind(on_press=self.cadastrar)
        self.voltar_button= Button(text='Voltar ao Login', color=(1, 1, 1, 1), size_hint=(1,None), size=(450, 50), background_color=(0.15, 0.15, 0.15, 1))
        self.voltar_button.bind(on_press=self.voltar)  
        self.buttons_layout.add_widget(self.cadastrar_button)
        self.buttons_layout.add_widget(self.voltar_button)
        self.add_widget(self.buttons_layout)

    def cadastrar(self, instance):
        email = self.email_input.text
        senha = self.senha_input.text
        print('Email:', email)
        print('Senha:', senha)
        
        dados = {'email': email, 'senha': senha}  # Corrigido para usar um dicionário
        link = 'https://login-1811a-default-rtdb.firebaseio.com/'
        requisicao = requests.post(f'{link}/Cadastro/.json', data=json.dumps(dados))

        if requisicao.status_code == 200:
            self.add_widget(Label(text='Cadastro bem sucedido', color=(0, 1, 0, 1)))
        else: 
            self.add_widget(Label(text='Por favor, preencha todos os campos', color=(1, 0, 0, 1)))

    def voltar(self, instance):
        app = App.get_running_app()
        app.root.current = 'login'


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        
        tela_login = Screen(name='login')
        tela_login.add_widget(TelaLogin())
        
        tela_cadastro = Screen(name='cadastro')
        tela_cadastro.add_widget(TelaCadastro())
        
        sm.add_widget(tela_login)
        sm.add_widget(tela_cadastro)
        
        return sm
    
if __name__ =='__main__':
    MyApp().run()
