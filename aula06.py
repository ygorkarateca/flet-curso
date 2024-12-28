import flet as ft

def main(page: ft.Page):
    icon1 = ft.Icon(
        name= ft.icons.ADD_LINK,
        color= ft.colors.PINK,
        size=100,

    )

    page.add(icon1)

ft.app(target=main)