import flet as ft

def main(page: ft.Page):
    page.title = "Teste app"
    page.bgcolor = ft.colors.BLUE

    # app fica a frente de todas as janelas
    page.window_always_on_top = False

    # faz parece a barra de tarefa
    page.window_title_bar_hidden = False

    # Some o minimizar/maximinizar/fechar
    page.window_frameless = False

    # Abre o app em fullscreen
    page.window_full_screen = False

    # Altura da página(_min_height ou _max_height)
    page.window_min_height = 300
    page.window_max_height = 600

    # Largura da página(_min_width ou _max_width)
    page.window_min_width = 300
    page.window_max_width = 600

    # Bloqueia o usuário de redimencionar
    page.window_resizable = True

    # Direcionar abertura de página
    page.window_top = 100

    # Direcionar abertura de página
    page.window_left = 100

    # Usuário não consegue mover a janela
    page.window_movable = True

    # Previne o usuário de fechar a janela
    page.window_prevent_close = False

    # Mostra um progresso no icone
    page.window_progress_bar = 1
    
    print(page.platform)

    def page_resize(e):
        print('Tamanho:', page.window_width, page.window_height)
    page.on_resize = page_resize
    
    def window_event(e):
        match e.data:
            case 'moved':
                print('Moveu a página')
    page.on_window_event = window_event
    
    page.update()
ft.app(target=main)