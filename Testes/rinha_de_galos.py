import flet as ft

def main(page: ft.Page):
    page.title= 'Venda de galos'
    page.bgcolor= ft.colors.WHITE
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.scroll= True,
    page.selectable = True,


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
        spans= [
            ft.TextSpan(text='Belo Galinaceo de grande belesa e desempenho', style=estilo_font,)
        ],
    )

    img1 = ft.Image(
        src='https://brunoestevamrj.github.io/galos/galos/galo1.jpeg',
        border_radius= ft.border_radius.all(20),
    )
    img2 = ft.Image(src='https://brunoestevamrj.github.io/galos/galos/galo2.jpeg')

    page.add(t1, t2, img1, img2)
    page.update()
ft.app(target=main, view=ft.AppView.WEB_BROWSER, assets_dir='assets')