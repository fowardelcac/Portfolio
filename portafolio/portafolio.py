import reflex as rx
from links import Links
from pages.A_crud import crud_page
from pages.B_wines import wines_page
from components.idom import lang_ui, conditional_render
from styles.styles import format_page


def profile_icons() -> rx.Component:
    return (
        rx.hstack(
            rx.link(rx.icon("linkedin"), href=Links.Linkedin.value, is_external=True),
            rx.link(rx.icon("github"), href=Links.Github.value, is_external=True),
            rx.link(
                rx.icon("file-text"),
                href=Links.Cv.value,
                is_external=True,
            ),
            rx.link(
                rx.icon(
                    "mail",
                    on_click=[
                        rx.set_clipboard("juansaldano01@gmail.com"),
                        rx.toast("Gmail copied!"),
                    ],
                ),
            ),
        ),
    )


def about_me() -> rx.Component:
    about_dic = {"Castellano": "Sobre mi", "English": "About me"}
    text_dic = {
        "Castellano": """ 
                Soy Juan Cruz de Argentina, un Científico de Datos Junior con una pasión por Python. Estoy en mi último año de estudio de Ciencias de Datos en la Universidad Siglo 21 en Córdoba. Me gusta programar, ya sea análisis de datos, web scraping, automatización de tareas, creación de modelos de aprendizaje automático o incluso desarrollar aplicaciones de escritorio y web como esta.

                Tengo experiencia en todas las etapas del proceso de datos. Puedo recopilar datos utilizando herramientas de web scraping como Scrapy, BeautifulSoup y Selenium, para luego procesarlos y analizarlos con bibliotecas de Python como Pandas. También disfruto creando visualizaciones de datos fáciles de entender y construyendo modelos de aprendizaje automático con Scikit-learn y TensorFlow.

                Mi primer trabajo fue en Latam Connect, donde trabajé en la extracción y procesamiento de datos, y además descubrí cómo automatizar tareas integrando Python con Google Sheets. Esto me ayudó a desarrollar habilidades sólidas en la gestión de datos y en la creación de soluciones eficientes.

                Actualmente, estoy buscando nuevas oportunidades laborales donde pueda seguir creciendo y aplicar mis habilidades en proyectos interesantes.
                """,
        "English": """
                    I'm Juan Cruz from Argentina, a Junior Data Scientist with a passion for Python. I'm in my last year of studying Data Science at Siglo 21 University in Córdoba. I like coding, whether it's data analysis, web scraping, automating tasks, building machine learning models, or even creating desktop and web apps like this one.
                    I have experience in all stages of the data process. I can gather data using web scraping tools like Scrapy, BeautifulSoup, and Selenium, then process and analyze it with Python libraries like Pandas. I also enjoy creating easy-to-understand data visualizations and building machine learning models with Scikit-learn and TensorFlow.

                    My first job was at Latam Connect, where I worked on data extraction, processing, and I also figured out how to automate tasks by the itegration of Python along Google Sheets. This helped me develop solid skills in data management and building efficient solutions.

                    Right now, I'm looking for new job opportunities where I can continue growing and apply my skills to interesting projects.


                    """,
    }
    return rx.section(
        rx.center(rx.heading(conditional_render(about_dic))),
        rx.text(
            conditional_render(text_dic),
            padding_top="15px",
        ),
    )


def experience() -> rx.Component:
    exp_dic = {"Castellano": "Experiencia", "English": "Experience"}
    text_dic = {
        "Castellano": """
            Trabajé como pasante en una exitosa empresa española llamada Latam Connect. Mi rol fue de Analista de Datos, y era responsable de extraer datos de la web y entregarlos en formato Excel. En ese momento, utilizábamos mucho Google Sheets, y parte de mi trabajo consistía en agregar manualmente información para enriquecer los datos. Esta tarea podía llevar horas, especialmente con grandes volúmenes de datos.
            Para solucionar esto, encontré una manera de integrar Python con Google Sheets. Creé un script que realizaba búsquedas en Google basadas en consultas hechas desde otras columnas de la hoja. Esta automatización nos ahorró mucho tiempo y hizo que el proceso fuera mucho más eficiente.""",
        "English": """  I worked as an intern at a successful Spanish company called Latam Connect. My role was as a Data Analyst, and I was responsible for extracting data from the web and delivering it in Excel format. At that time, we used Google Sheets a lot, and part of my job was to manually add information to enrich the data. This task could take hours, especially with large amounts of data.
                        To solve this, I found a way to integrate Python with Google Sheets. I created a script that performed Google searches based on queries made from other columns in the sheet. This automation saved us a lot of time and made the process much more efficient.""",
    }
    return (
        rx.section(
            rx.center(rx.heading(conditional_render(exp_dic))),
            rx.markdown(
                f"""- <a href="{Links.Latam.value}" target="_blank" rel="noopener noreferrer"><strong>Latam Connect</strong></a> | Data analyst.     January 2024 - April 2024""",
                padding_top="15px",
            ),
            rx.text(
                conditional_render(text_dic),
            ),
        ),
    )


def techs() -> rx.Component:
    tech_dic = {"Castellano": "Tecnologias", "English": "Technologies"}
    return (
        rx.section(
            rx.center(
                rx.heading(conditional_render(tech_dic)),
            ),
            rx.hstack(
                rx.image("/tech_icons/python_icon.png", width="3em", height="auto"),
                rx.image("/tech_icons/sql_icon.png", width="3em", height="auto"),
                padding_top="15px",
                spacing="9",
            ),
        ),
    )


def projects() -> rx.Component:
    proj_dic = {"Castellano": "Proyectos", "English": "Projects"}
    wine_dic = {
        "Castellano": "En este proyecto, procesé un conjunto de datos de vinos y creé diversas visualizaciones de datos. Además, desarrollé un modelo de aprendizaje automático y exploré tres métodos diferentes para su aplicación: integración en una página web, una aplicación de escritorio para Windows y una API utilizando FastAPI.",
        "English": "In this project, I processed a dataset of wines and created various data visualizations. Additionally, I developed a machine learning model and explored three different methods for its application: integration into a web page, a Windows desktop application, and an API using FastAPI.",
    }

    crud_dic = {
        "Castellano": "Desarrollé una aplicación CRUD utilizando Python y el framework Flet (la versión de Python de Flutter). La aplicación cuenta con una base de datos SQLite y una interfaz de usuario intuitiva para gestionar la contabilidad de clientes y tareas de mantenimiento, inspirada en las necesidades arquitectónicas de mi padre.",
        "English": "Developed a CRUD application using Python and the Flet framework (Python's version of Flutter). The app features a SQLite database and a user-friendly UI to manage client accounting and maintenance tasks, inspired by my father's architectural needs",
    }

    titles_wine_dic = {
        "Castellano": "Análisis de Datos de Vinos",
        "English": "Wines Data Analysis",
    }
    return (
        rx.section(
            rx.center(rx.heading(conditional_render(proj_dic))),
            rx.hstack(
                rx.box(
                    rx.link(
                        rx.heading(conditional_render(titles_wine_dic)),
                        href="/wines/",
                        is_external=True,
                    ),
                    rx.text(
                        conditional_render(wine_dic),
                        margin_top="0.5em",
                    ),
                    rx.text(
                        "#Python #Data Analisys #MachineLearning #FastApi ",
                        color_scheme="teal",
                        padding_top="5px",
                    ),
                    padding="2em",
                    border_width="1px",
                ),
                rx.box(
                    rx.link(rx.heading("Crud App"), href="/crud", is_external=True),
                    rx.text(
                        conditional_render(crud_dic),
                        margin_top="0.5em",
                    ),
                    rx.text(
                        "#Python #SqlLite #Desktop app #Flet ",
                        color_scheme="teal",
                        padding_top="5px",
                    ),
                    padding="2em",
                    border_width="1px",
                ),
                padding_top="2em",
            ),
            padding_top="15px",
        ),
    )


def index() -> rx.Component:
    heading_dic = {
        "Castellano": "Científico de datos junior y desarrollador en Python",
        "English": "Jr Data scientist and Python dev.",
    }

    subheading_dic = {
        "Castellano": "¡Bienvenido a mi portafolio! Soy Juan Cruz de Argentina. Soy científico de datos junior y desarrollador Python.",
        "English": "Welcome to my portfolio! I'm Juan Cruz from Argentina. I'm Jr Data scientist and Python dev.",
    }
    return rx.box(
        lang_ui(),
        rx.container(
            rx.vstack(
                rx.heading(
                    conditional_render(heading_dic),
                    size="8",
                ),
                rx.text(conditional_render(subheading_dic)),
                profile_icons(),
                about_me(),
                experience(),
                projects(),
                techs(),
                **format_page
            ),
        ),
    )


app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        radius="large",
        accent_color="teal",
    )
)
app.add_page(index)
app.add_page(crud_page)
app.add_page(wines_page)
