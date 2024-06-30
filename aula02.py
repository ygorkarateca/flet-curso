import flet as ft

def main(page: ft.Page):
    page.bgcolor = 'amber100'
    page.bgcolor = '#B12B12'
    page.bgcolor = ft.colors.RED

    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.vertical_alignment = ft.MainAxisAlignment.START

    page.padding = ft.padding.symmetric(vertical=100, horizontal=30)
    page.padding = ft.padding.all(10)
    page.padding = ft.padding.only(top=10, left=10, right=10, bottom=30)
    page.padding = 20

    page.spacing = 100

    page.title = 'Flet app'
    
   
    page.add(
        ft.Text(value='Olá, Mundo!'),
        ft.Container(ft.Text(value='Olá, Mundo'), bgcolor='black'),
    )

    page.update()
ft.app(target=main)