from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.clipboard import Clipboard
import datetime

class MainApp(App):
    def build(self):
        self.title = 'Gerador de Senha'
        
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.texto1 = Label(text='', color=(0.27, 0.03, 0.65, 1))
        self.layout.add_widget(self.texto1)

        self.botao1 = Button(text='Gerar', on_press=self.gerar_senha)
        self.layout.add_widget(self.botao1)

        self.botao2 = Button(text='Apagar', on_press=self.apagar)
        self.layout.add_widget(self.botao2)

        self.botao3 = Button(text='Copiar', on_press=self.copiar)
        self.layout.add_widget(self.botao3)

        return self.layout

    def gerar_senha(self, instance):
        data = datetime.date.today()
        data = str(data)
        data2 = data.split('-')
        ano = int(data2[0])
        mes = int(data2[1])
        senha_geral = ano * mes * ano
        senha_geral = f'{senha_geral:.1f}'
        senha_geral = senha_geral.replace('.', '')
        senha_geral = f'PEDRO{mes}' + senha_geral
        senha_geral = senha_geral.replace('1', '9')
        senha_geral = senha_geral.replace('2', '8')
        self.texto1.text = f'{senha_geral}'
        return senha_geral

    def copiar(self, instance):
        texto = self.texto1.text
        Clipboard.copy(texto)

    def apagar(self, instance):
        self.texto1.text = ''


if __name__ == '__main__':
    MainApp().run()
