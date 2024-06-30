import flet as ft

def main(page: ft.Page):
    mensagem = ft.Text(value="Olá, mundo!")
    page.add(mensagem)

ft.app(target=main)