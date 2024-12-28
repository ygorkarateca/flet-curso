import flet as ft

def main(page: ft.Page):
    page.title= 'Venda de galos'
    page.bgcolor= ft.colors.WHITE
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.scroll= True,
    page.selectable = False,



    t1 = ft.Text(
        value='Foto dos Galos',
        color= ft.colors.BLACK,
        text_align= ft.TextAlign.CENTER,
        style= ft.TextThemeStyle.DISPLAY_LARGE,
    )

    estilo_font = ft.TextStyle(
        color= ft.colors.BLACK
    )

    t2 = ft.Text(
        value='Belo Galinaceo de grande beleza e desempenho',
        text_align= ft.TextAlign.CENTER,
        color= ft.colors.BLACK,

    )

    img1 = ft.Image(
        src='https://brunoestevamrj.github.io/galos/galos/galo1.jpeg',
        border_radius= ft.border_radius.all(20),
        tooltip= 'Belo - O Galão de bringa',

    )


    img2 = ft.Image(
        src='https://brunoestevamrj.github.io/galos/galos/galo2.jpeg',
        border_radius= ft.border_radius.all(20),
        tooltip='Negrão, O espanca frango',

        )

    page.scroll = "auto"
    page.add(t1, t2, img1, img2)
    page.update()
    
ft.app(target=main, assets_dir='assets') #, view=ft.AppView.WEB_BROWSER)