import reflex as rx


class LanguageState(rx.State):
    language: str = rx.Cookie("English", path="/")

    def change_idiom(self, lang: str):
        self.language = lang


def lang_ui() -> rx.Component:
    return (
        rx.hstack(
            rx.select(
                [
                    "English",
                    "Castellano",
                ],
                on_change=LanguageState.change_idiom,
                placeholder="Language/Lenguaje",
                value=LanguageState.language
            ),
            padding="20px",
            width="100%",
            justify="end",
        ),
    )


def conditional_render(dicc: dict, idiom: str = LanguageState.language) -> rx.Component:
    return rx.match(
        idiom,
        ("English", dicc.get("English")),
        ("Castellano", dicc.get("Castellano")),
        dicc.get("English"),
    )
