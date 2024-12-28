import flet as ft
import os


def main(page: ft.Page):
    page.spacing = 40,

    btn1 = ft.ElevatedButton(text='Botão Ativo')
    btn2 = ft.ElevatedButton(text='Botão Inativo', disabled=True, tooltip='Botão Desativado')
    btn3 = ft.ElevatedButton(text='Botão com ícone', icon=ft.icons.ADD_LINK, color=ft.colors.WHITE)
    btn4 = ft.ElevatedButton(
        text= 'Demais propriedades',
        bgcolor= ft.colors.RED,
        color= ft.colors.WHITE,
        icon= ft.icons.FAVORITE_BORDER_OUTLINED,
        icon_color= ft.colors.WHITE,
        tooltip='Olá, eu sou um botão',
        url= 'https://www.x.com',
    )

    style = ft.ButtonStyle(
        color={
            ft.MaterialState.HOVERED: ft.colors.WHITE,
            ft.MaterialState.DEFAULT: ft.colors.RED,
        },

        bgcolor={
            ft.MaterialState.HOVERED: ft.colors.PINK,
            ft.MaterialState.DEFAULT: ft.colors.YELLOW,

        },
        padding={
            ft.MaterialState.HOVERED: 20,
            ft.MaterialState.DEFAULT: 21,
        },

        animation_duration=1000,

        side={
            ft.MaterialState.HOVERED: ft.BorderSide(width=1, color=ft.colors.BLUE),
            ft.MaterialState.DEFAULT: ft.BorderSide(width=5, color=ft.colors.ORANGE_600),
        },

        shape={
            ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=10),
            ft.MaterialState.DEFAULT: ft.ContinuousRectangleBorder(radius=10),

            # Define uma borda padrão
            # ft.MaterialState.DEFAULT: ft.StadiumBorder(),
            
            # Define uma borda circular
            # ft.MaterialState.DEFAULT: ft.CircleBorder(),

            # Defie uma borda retangular
            # ft.MaterialState.DEFAULT: ft.BeveledRectangleBorder(),

        },
    )

    btn5 = ft.ElevatedButton(text='Botão com estilo pesonalizado', style= style)

    btn = ft.ElevatedButton(text='AGORA VAI!')
    txt = ft.Text()

    page.add(btn1, btn2, btn3, btn4, btn5, btn, txt)
    page.update()
ft.app(target=main, view=ft.AppView.WEB_BROWSER)