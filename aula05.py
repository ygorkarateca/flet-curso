import flet as ft

def main(page: ft.Page):
    img = ft.Image(
        src='https://miro.medium.com/v2/resize:fit:720/format:webp/1*3IcLSFuT8PQg4cUBaRXH1A.png',
        border_radius= ft.border_radius.all(20),
        height=100,
        width=400,
        fit=ft.ImageFit.CONTAIN,
    )
   
    im2 = ft.Image(
        src= 'images/flet-img.png',
        tooltip='Flet counter example',
    )
    page.add(img, im2)
ft.app(target=main, assets_dir='assets', port=8000, view=ft.AppView.WEB_BROWSER)