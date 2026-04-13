import flet as ft
import main_screen

def title_screen(page: ft.Page):
    page.controls.clear()

    background = ft.Container(
        expand=True,
        bgcolor="#FFFCDE"
    )

    menu = ft.Container(
        expand = True,
        content = ft.Column(
            ft.Row([
                ft.Image(
                    src = "assets/prueba.png",
                    fit = "contain"
                ),
                ft.Text(
                    "HeatCalico",
                    color = "#B71C1C",
                    weight = "bold",
                    font_family = "Arial Black"
                )
            ]),

            ft.Row([
                  ft.Text(
                        "Inicio",
                        color = "BLACK"
                  )
            ])
        )
    )

    image_layer = ft.Container(
        content=ft.Image(
            src="assets/prueba.png",
            width=450,
            height=450,
            fit="contain"
        ),
        alignment=ft.Alignment(1, 0), 
        padding=ft.padding.only(right=80)
    )

    text_content = ft.Container(
        expand=True,
        padding=ft.padding.only(left=80), 
        content=ft.Column(
            [
                ft.Text(
                    "HEAT-CALICO",
                    color="#B71C1C",
                    size=55,
                    weight="bold",
                    font_family="Arial Black"
                ),
                ft.Container(height=10),
                ft.ElevatedButton(
                    content = ft.Text(
                        "Inicio",
                        color = "WHITE",
                        size = 22
                    ),
                    bgcolor = "#424242",
                    width = 240,
                    height = 65,
                    elevation = 8
                    #on_click = lambda e: segunda_pantalla(page)
                )
            ],
            alignment="center",
            horizontal_alignment="start" 
        )
    )

    page.add(ft.Stack(
        [background, image_layer, text_content],
        expand=True
    ))
    page.update()
