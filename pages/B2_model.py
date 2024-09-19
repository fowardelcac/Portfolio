import reflex as rx
import joblib
import pandas as pd
from links import Links
from components.idom import conditional_render
from styles.styles import format_page


class ModelStuff:
    pipeline = joblib.load("assets/wines/sklearn/pipeline.pkl")
    model = joblib.load("assets/wines/sklearn/model.pkl")

    countries: list[str] = [
        "Italy",
        "Portugal",
        "US",
        "Spain",
        "Germany",
        "France",
        "Argentina",
        "Chile",
        "Australia",
        "South Africa",
        "Israel",
        "Hungary",
        "Austria",
        "Greece",
        "Mexico",
        "Canada",
        "New Zealand",
        "Romania",
        "Slovenia",
        "Georgia",
        "Uruguay",
        "England",
        "Bulgaria",
        "Turkey",
    ]
    provinces: list[str] = [
        "Sicily & Sardinia",
        "Douro",
        "Oregon",
        "Northern Spain",
        "Alsace",
        "California",
        "Mosel",
        "Mendoza Province",
        "Southern Italy",
        "Bordeaux",
        "Central Italy",
        "Washington",
        "Champagne",
        "South Australia",
        "Tuscany",
        "New York",
        "Piedmont",
        "Southwest France",
        "Northeastern Italy",
        "Burgundy",
        "Veneto",
        "Catalonia",
        "Loire Valley",
        "Provence",
    ]
    variety: list[str] = [
        "White Blend",
        "Portuguese Red",
        "Riesling",
        "Pinot Noir",
        "Pinot Gris",
        "Cabernet Sauvignon",
        "Malbec",
        "Red Blend",
        "Merlot",
        "Chardonnay",
        "Sangiovese",
        "Cabernet Franc",
        "Champagne Blend",
        "Sauvignon Blanc",
        "Bordeaux-style Red Blend",
        "Rosé",
        "Zinfandel",
        "Syrah",
        "Nebbiolo",
        "Rhône-style Red Blend",
        "Portuguese White",
        "Grüner Veltliner",
        "Sparkling Blend",
        "Tempranillo",
    ]
    winery: list[str] = [
        "Jean-Baptiste Adam",
        "Tasca d'Almerita",
        "Yalumba",
        "Heron Hill",
        "Lamoreaux Landing",
        "Kuentz-Bas",
        "Domaine Zind-Humbrecht",
        "Testarossa",
        "Dutton-Goldfield",
        "La Chablisienne",
        "Viña Bisquertt",
        "Emiliana",
        "J. Lohr",
        "Wagner",
        "D'Arenberg",
        "Willamette Valley Vineyards",
        "Viña Cobos",
        "Salomon-Undhof",
        "Talley",
        "Clos La Chance",
        "Robert Weil",
        "Louis Latour",
        "Lapostolle",
        "Tommasi",
        "San Pedro",
        "Undurraga",
        "Milbrandt",
        "Winzer Krems",
        "Robert Mondavi",
        "Chehalem",
        "Henri de Villamont",
        "Domaine Serene",
        "Dr. Loosen",
        "Sparkman",
        "Babcock",
        "Fenestra",
        "Maximin Grünhäuser",
        "Iron Horse",
        "Terre Rouge",
        "Loring Wine Company",
        "Midnight",
        "Rodney Strong",
        "Foxen",
        "Quinta da Lagoalva de Cima",
        "Reichsgraf von Kesselstatt",
        "Seven Hills",
        "Chateau Ste. Michelle",
        "Casca Wines",
        "Wines & Winemakers",
        "De Loach",
        "Adelsheim",
        "Laetitia",
        "Brian Carter Cellars",
        "Efeste",
        "Georges Duboeuf",
        "Maryhill",
        "J Vineyards & Winery",
        "Aveleda",
        "Santa Ema",
        "Morandé",
        "Kendall-Jackson",
        "Fournier Père et Fils",
        "Trisaetum",
        "Poças",
        "Williams Selyem",
        "Cayuse",
        "Santa Alicia",
        "Concha y Toro",
        "Santa Rita",
        "Trapiche",
        "Pali",
        "Bacalhôa Wines of Portugal",
        "Fess Parker",
        "J. Portugal Ramos",
        "Balletto",
        "Cameron Hughes",
        "Domäne Wachau",
        "Martin Ray",
        "Louis Jadot",
        "Georges Vigouroux",
        "Domaines Barons de Rothschild (Lafite)",
        "Bründlmayer",
        "Santa Carolina",
        "Herdade do Esporão",
        "DFJ Vinhos",
        "Valentin Bianchi",
        "Recanati",
        "Quinta do Casal Branco",
        "François Lurton",
        "Gérard Bertrand",
        "Caliterra",
        "Errazuriz",
        "Rock Wall",
        "L. Tramier & Fils",
        "Kokomo",
        "Columbia Crest",
        "Montes",
        "Canoe Ridge",
        "Domaines Devillard",
        "Novelty Hill",
        "Casa Santos Lima",
        "Marimar Estate",
        "Hirsch",
        "Januik",
        "Gloria Ferrer",
        "Echeverria",
        "Barton & Guestier",
        "V. Sattui",
        "Jean-Luc and Paul Aegerter",
        "MacPhail",
        "Bodegas Valdemar",
        "Lynmar",
        "Companhia das Quintas",
        "Naggiar",
        "Joseph Swan Vineyards",
        "Viu Manent",
        "Morgan",
        "Feudi di San Gregorio",
        "Zaca Mesa",
        "Kunde",
        "Sojourn",
        "Gary Farrell",
        "Concannon",
        "Zuccardi",
        "Henri Bourgeois",
        "Mumm Napa",
        "Chanson Père et Fils",
        "Mark Ryan",
        "Bernardus",
        "Calera",
        "King Estate",
        "K Vintners",
        "Sineann",
        "José Maria da Fonseca",
        "Raymond",
        "Torii Mor",
        "Dão Sul",
        "Siduri",
        "Albert Bichot",
        "Olivier Leflaive",
        "Gorman",
        "Adelaida",
        "Schramsberg",
        "Bouchard Père & Fils",
        "Dr. Pauly Bergweiler",
    ]


class PageState(rx.State):
    result: float = 0

    selected_country: str = ""
    selected_province: str = ""
    selected_variety: str = ""
    selected_winery: str = ""
    value_age: int = 10
    value_points: float = 80.6

    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        self.form_data = {**form_data}

    def set_country(self, country: str):
        self.selected_country = country

    def set_province(self, province: str):
        self.selected_province = province

    def set_variety(self, variety: str):
        self.selected_variety = variety

    def set_winery(self, winery: str):
        self.selected_winery = winery

    def set_age(self, age: int):
        self.value_age = age

    def set_points(self, points: float):
        self.value_points = points

    def model_function(self):
        dic: dict = {
            "Pais": self.form_data["country"],
            "Provincia": self.form_data["province"],
            "Variedad": self.form_data["variety"],
            "Bodega": self.form_data["winery"],
            "Antiguedad": self.form_data["age"],
            "Puntos": self.form_data["points"],
        }
        feature_names: list = [
            "Pais",
            "Provincia",
            "Variedad",
            "Bodega",
            "Antiguedad",
            "Puntos",
        ]
        df = pd.DataFrame(dic, index=[0], columns=feature_names)
        new_data_transformed = ModelStuff.pipeline.transform(df)
        rdo_df = pd.DataFrame(new_data_transformed, columns=feature_names)
        rdo = ModelStuff.model.predict(rdo_df)
        self.result = rdo[0]


def slider_age() -> rx.Component:
    txt_dic = {
        "Castellano": "Selecciona la edad del vino",
        "English": "Select the wine's age",
    }
    return rx.vstack(
        rx.heading(f"{conditional_render(txt_dic)}: {PageState.value_age}"),
        rx.slider(
            default_value=10,
            min=1,
            max=150,
            on_value_commit=PageState.set_age,
            width="100%",
            name="age",
        ),
    )


def slider_points() -> rx.Component:
    txt_dic = {
        "Castellano": "Selecciona los puntos",
        "English": "Select the wine's points",
    }
    return rx.vstack(
        rx.heading(f"{conditional_render(txt_dic)}: {PageState.value_points}"),
        rx.slider(
            default_value=80.6,
            min=1,
            max=100,
            on_value_commit=PageState.set_points,
            width="100%",
            name="points",
        ),
    )


def model_tab() -> rx.Component:
    title_dic = {"Castellano": "Modelo Random Forest", "English": "Random Forest Model"}
    desc_dic = {
        "Castellano": "Este modelo de aprendizaje automático está destinado únicamente a fines de demostración y no tiene aplicaciones prácticas. Por ejemplo, si el usuario selecciona Italia como país, no debería poder elegir Mendoza como provincia, ya que está en otro país, y así sucesivamente. El Random Forest Regressor en este proyecto predice los precios de los vinos en función de varios parámetros, incluyendo el país y la provincia de origen, la bodega, la variedad, la edad del vino y su puntuación en puntos. Una vez que el usuario presiona enviar, la aplicación procesa las entradas a través de un pipeline y devuelve un precio predicho.",
        "English": "This machine learning model is intended solely for demonstration purposes and does not have practical applications. For example, if the user selects Italy as the country, they should not be able to choose Mendoza as the province since it's in a different country, and so on. The Random Forest Regressor in this project predicts wine prices based on several parameters, including the country and province of origin, the winery, variety, wine's age, and its rating in points. Once the user presses submit, the application processes the inputs through a pipeline and returns a predicted price.",
    }
    count_dic = {"Castellano": "Selecciona el pais.", "English": "Select one country."}
    prov_dic = {
        "Castellano": "Selecciona una provincia",
        "English": "Select one province.",
    }
    var_dic = {"Castellano": "Selecciona la variedad", "English": "Select the variety."}
    win_dic = {"Castellano": "Selecciona la bodega.", "English": "Select the winery."}
    sub_dic = {"Castellano": "Enviar", "English": "Submit"}
    predic_dic = {"Castellano": "Predecir", "English": "Predict"}
    rdo_dic = {"Castellano": "Precio predecido", "English": "Predicted price"}
    txt_dic = {
        "Castellano": """Además de los proyectos anteriores, he desarrollado una aplicación de escritorio para Windows y una API utilizando FastAPI.

- **Aplicación de Escritorio para Windows**: Los modelos de aprendizaje automático son poderosos, pero sin una interfaz de usuario, pueden ser difíciles de utilizar. Para solucionar esto, creé una aplicación de escritorio para Windows utilizando Flet. Si eres usuario de Windows, puedes descargarla [aquí](Links.Windows_app.value). Después de descargar el archivo ZIP, extráelo y ejecuta la aplicación `randomforest`. Puede tardar unos segundos en abrirse. No dudes en contactarme si encuentras algún problema. Aquí está el [repositorio](Links.Windows_repo.value).

- **Aplicación FastAPI**: Esta es una API estándar construida con FastAPI. Puedes explorarlo más a fondo [aquí](Links.FastApi.value).

        """,
        "English": """In addition to the previous projects, I've developed a Windows desktop app and an API using FastAPI.
                        
- **Windows Desktop App**: Machine learning models are powerful, but without a user interface, they can be difficult to interact with. To solve this, I created a Windows desktop app using Flet. If you're a Windows user, you can download it from <a href="{Links.Windows_app.value}" target="_blank" rel="noopener noreferrer"><strong>here</strong></a>. After downloading the ZIP file, extract it, and run the `randomforest` application. It may take a few seconds to open. Feel free to reach out if you encounter any issues. Here is the <a href="{Links.Windows_repo.value}" target="_blank" rel="noopener noreferrer"><strong>repository</strong></a>. 
                       
 - **FastAPI Application**: This is a standard API built with FastAPI. You can explore it further <a href="{Links.FastApi.value}" target="_blank" rel="noopener noreferrer"><strong>here</strong></a>""",
    }
    return (
        rx.container(
            rx.vstack(
                rx.heading(conditional_render(title_dic), size="8"),
                rx.text(conditional_render(desc_dic)),
                rx.form(
                    rx.vstack(
                        rx.vstack(
                            rx.hstack(
                                rx.select(
                                    ModelStuff.countries,
                                    placeholder=conditional_render(count_dic),
                                    on_change=PageState.set_country,
                                    name="country",
                                ),
                                rx.select(
                                    ModelStuff.provinces,
                                    placeholder=conditional_render(prov_dic),
                                    on_change=PageState.set_province,
                                    name="province",
                                ),
                                rx.select(
                                    ModelStuff.variety,
                                    placeholder=conditional_render(var_dic),
                                    on_change=PageState.set_variety,
                                    name="variety",
                                ),
                                rx.select(
                                    ModelStuff.winery,
                                    placeholder=conditional_render(win_dic),
                                    on_change=PageState.set_winery,
                                    name="winery",
                                ),
                            ),
                            rx.hstack(slider_age(), slider_points()),
                        ),
                        rx.button(
                            conditional_render(sub_dic), type="submit", width="50%"
                        ),
                        spacing="4",
                        align="center",
                        justify="center",
                    ),
                    on_submit=[PageState.handle_submit, rx.toast("Submitted.")],
                    padding_top="15px",
                ),
                rx.spacer(),
                rx.hstack(
                    rx.button(
                        conditional_render(predic_dic),
                        on_click=PageState.model_function,
                    ),
                    rx.cond(
                        PageState.result != 0,
                        rx.text(f"{conditional_render(rdo_dic)}: ${PageState.result}"),
                    ),
                ),
                rx.divider(),
                rx.markdown(
                    f"{conditional_render(txt_dic)}",
                    padding_top="15px",
                ),
                **format_page,
            ),
        ),
    )
