import reflex as rx
from .B1_visual import visualizations
from .B2_model import model_tab
from components.idom import lang_ui, conditional_render
from styles.styles import format_page


@rx.page(route="/wines")
def wines_page():
    chart_dic = {
        "Castellano": "Graficos",
        "English": "Charts",
    }
    model_dic = {
        "Castellano": "Modelo",
        "English": "Model",
    }
    return rx.box(
        lang_ui(),
        rx.container(
            rx.tabs.root(
                rx.tabs.list(
                    rx.tabs.trigger(conditional_render(chart_dic), value="tab1"),
                    rx.tabs.trigger(conditional_render(model_dic), value="tab2"),
                ),
                rx.tabs.content(
                    visualizations(),
                    value="tab1",
                ),
                rx.tabs.content(
                    model_tab(),
                    value="tab2",
                ),
                default_value="tab1",
            ),
            **format_page
        ),
    )
