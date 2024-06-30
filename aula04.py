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
        selectable= False,
        size= 30,
        text_align= ft.TextAlign.CENTER,
        weight = ft.FontWeight.NORMAL,
    )

    link_style = ft.TextStyle(color= ft.colors.BLUE, decoration=ft.TextDecoration.UNDERLINE)
    title_style = ft.TextStyle(
        bgcolor= ft.colors.AMBER,
        color= ft.colors.RED,
        decoration= ft.TextDecoration.OVERLINE,
        decoration_color= ft.colors.GREEN,

    )

    t2 = ft.Text(
        spans= [
            ft.TextSpan(text='Texto com link', style=link_style, url='www.x.com'),
            ft.TextSpan(text='\ncontinuacao do texto...'),
            ft.TextSpan(text='Texto em destaque!!! ', style=title_style),
        ],
        size= 40,
    )

    page.add(t1, t2)


    page.update()
ft.app(target=main, assets_dir='Fonts')