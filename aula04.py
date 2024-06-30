import flet as ft

def main(page: ft.Page):
    page.fonts = {
        'Kanit': 'Fonts/Dragon Slayer.ttf',
    }

    t1 = ft.Text(
        value='Seja Bem-vindo a Academia Perfil\nSinta-se em casa!',
        style= ft.TextThemeStyle.DISPLAY_LARGE,
        bgcolor= ft.colors.RED,
        color= ft.colors.BLACK,
        # font_family= 'Kanit',
        italic= True,
        # max_lines= 1,
        # overflow= ft.TextOverflow.ELLIPSIS
        # no_wrap= True,
        selectable= True,
    )
    page.add(t1)


    page.update()
ft.app(target=main, assets_dir='Fonts')