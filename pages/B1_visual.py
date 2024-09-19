import reflex as rx
from components.idom import conditional_render
from styles.styles import format_page

def visualizations() -> rx.Component:
    title_dic = {
        "Castellano": "Visualizacion de datos",
        "English": "Data visualization",
    }
    images_dic = {
        "Castellano": "Visualizaciones",
        "English": "Visualizations",
    }

    path = conditional_render(images_dic)
    return rx.vstack(
        rx.center(
            rx.heading(conditional_render(title_dic), size="8"), padding_top="15px"
        ),
        rx.image(f"/wines/{path}/a.png", width="60em", height="auto"),
        rx.image(f"/wines/{path}/b.png", width="60em", height="auto"),
        rx.image(f"/wines/{path}/c.png", width="60em", height="auto"),
        rx.image(f"/wines/{path}/d.png", width="60em", height="auto"),
        rx.image(f"/wines/{path}/e.png", width="60em", height="auto"),
        rx.image(f"/wines/{path}/f.png", width="60em", height="auto"),
        **format_page
    )
