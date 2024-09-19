import reflex as rx
from links import Links
from components.idom import lang_ui, conditional_render
from styles.styles import format_page

@rx.page(
    route="/crud",
)
def crud_page() -> rx.Component:
    mark_dic = {
        "Castellano": """<div style="margin-top: 0; padding-top: 20px;">
                Una aplicación CRUD es un tipo específico de software que realiza cuatro operaciones básicas: Crear, Leer, Actualizar y Eliminar. En otras palabras, una aplicación CRUD permite a los usuarios interactuar directamente con una base de datos sin darse cuenta.
                Típicamente, este tipo de aplicaciones consta de tres componentes: la base de datos, la interfaz de usuario y las APIs. Sin embargo, en este proyecto, trabajé con un framework de Python llamado Flet (la versión de Python de Flutter), que unifica las capas de la interfaz de usuario y API. Esta aplicación en particular consta de dos partes principales:
                <ul style="margin: 0; padding: 0; list-style-position: inside;">
                    <li><strong>Base de datos:</strong> Utilicé SQLite para construir toda la base de datos.</li>
                    <li><strong>Python:</strong> Utilicé el framework Flet para desarrollar la interfaz de usuario, permitiendo a los usuarios enviar todas las consultas a la base de datos sin problemas.</li>
                </ul>
                Este proyecto existe gracias a mi padre, un arquitecto que buscaba una aplicación para gestionar la contabilidad de sus clientes. Específicamente, necesitaba una función para rastrear tareas de mantenimiento para reparar o inspeccionar elementos en sus proyectos.
                </div>""",
        "English": """<div style="margin-top: 0; padding-top: 20px;">
                    A CRUD app is a specific type of software application that performs four basic operations: Create, Read, Update, and Delete. In other words, a CRUD app allows users to interact directly with a database without realizing it.
                    Typically, these kinds of apps consist of three components: the database, the user interface, and APIs. However, in this project, I worked with a Python framework called Flet (the Python version of Flutter), which unifies the user interface and API layers. This particular app consists of two main parts:
                    <ul style="margin: 0; padding: 0; list-style-position: inside;">
                        <li><strong>Database:</strong> I used SQLite to build the entire database.</li>
                        <li><strong>Python:</strong> I used the Flet framework to develop the UI, enabling users to send all the database queries seamlessly.</li>
                    </ul>
                    This project exists thanks to my father, an architect who was looking for an application to manage the accounting of his clients. Specifically, he needed a feature to track maintenance tasks for repairing or inspecting items in his projects.
                    </div>""",
    }

    looks_dic = {
        "Castellano": "La aplicación se ve así:",
        "English": "The application looks like:",
    }

    erd_dic = {
        "Castellano": "Diagrama Entidad-Relacion",
        "English": "Entity-Relationship Diagram (ERD).",
    }
    return rx.box(
        lang_ui(),
        rx.container(
            rx.vstack(
                rx.heading("Crud App", size="8"),
                rx.link(
                    rx.icon("github"),
                    href=Links.Crud_repo.value,
                    is_external=True,
                    padding_top="5px",
                ),
                rx.markdown(conditional_render(mark_dic)),
                rx.link(
                    rx.text(conditional_render(erd_dic), size="7"),
                    href=Links.Crud_repo.value,
                    is_external=True,
                ),
                rx.image(
                    "/crud_assets/diagram.png",
                    align="center",
                    width="70em",
                    height="auto",
                ),
                rx.markdown(f"## {conditional_render(looks_dic)}"),
                rx.image(
                    "/crud_assets/maintenence.jpg",
                    align="center",
                    width="70em",
                    height="auto",
                ),
                rx.image(
                    "/crud_assets/picture.jpg",
                    align="center",
                    width="70em",
                    height="auto",
                ),
                **format_page
            ),
        ),
    )
