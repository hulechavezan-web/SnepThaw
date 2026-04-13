## Aquí va la página principal que subirá el yabete de aquí.
## ESTA ES UNA PÁGINA VACÍA QUE SERÁ REEMPLAZADA POR LA PRINCIPAL.

import flet as ft
import title_screen as ts
import main_screen as ms

def main(page: ft.Page):
    # Configuraciones básicas
    page.title = "Enfriamiento de una bebida caliente"
    page.bgcolor = ft.Colors.WHITE
    page.window.maximized = True
    #ts.title_screen(page)
    ms.main_screen(page)
    page.update()

ft.app(target=main)