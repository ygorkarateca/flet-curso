import os
import flet as ft

def main(page: ft.Page):
    btn1 = ft.ElevatedButton(text='Desligar')


    page.add(btn1)
    page.update()
ft.app(target=main)