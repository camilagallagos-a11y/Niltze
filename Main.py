from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

palabras = {
    "agua": "Atl",
    "casa": "Calli",
    "perro": "Chichi",
    "niño": "Konetl",
    "ojo": "Ixtli",
    "boca": "Kamachtli",
    "mano": "Mahtli",
    "corazón": "Yollotl",
    "déjalo / ya basta": "Xikaua",
    "entiéndeme": "Nechkaki",
    "ahora todo está bien": "Axkan nochi cualli",
    "gracias por todo": "Tlazohcamati nochi",
    "te veo mañana": "Nimitzittaz mostla",
    "¿cómo estás?": "¿Kenin timoztia?",
    "estoy bien, ¿y tú?": "Cualli ni, ¿tehuatl?",
    "todo bien": "Nochi cualli",
    "ahora, ¿qué quieres?": "Axcan tlen ticnequi?",
    "quiero comida": "Tlacualli nicnequi",
    "chile": "Chilli",
    "aguacate": "Ahuacatl",
    "ehocolate": "Xocoātl",
    "esquite": "Izquitl",
    "elote": "Elotl",
    "ajolote": "Āxōlōtl",
    "coyote": "Coyotl",
    "chapulín": "Chapulin",
    "mapache": "Mapachin",
    "comal": "Comalli",
    "hola": "Niltze",
    "gracias": "Tlazohcamati",
    "buenas tardes": "Ximopanolti",
    "buenas noches": "Ximoyecti",
    "te quiero": "Nimitztasojtla",
    "bien": "Cualli",
    "¿cómo te llamas?": "¿Kenin timotoka?",
    "yo me llamo": "Nehuatl notoka",
    "estoy bien": "Cualli ni",
    "¿qué quieres?": "¿Tlen ticnequi?",
    "ayúdame": "Xinechpalehui",
    "buen": "Cualli"
}


class DiccionarioApp(App):
    def build(self):
        pantalla = BoxLayout(
            orientation="vertical",
            padding=25,
            spacing=15
        )

        pantalla.add_widget(Label(
            text="NIL TZE\nDiccionario de náhuatl",
            font_size=25
        ))

        self.entrada = TextInput(
            hint_text="Escribe una palabra o frase",
            multiline=False,
            size_hint_y=None,
            height=55
        )
        pantalla.add_widget(self.entrada)

        boton = Button(
            text="BUSCAR",
            size_hint_y=None,
            height=55
        )
        boton.bind(on_press=self.buscar)
        pantalla.add_widget(boton)

        self.resultado = Label(
            text="¡Descubre palabras en náhuatl!",
            font_size=18
        )
        pantalla.add_widget(self.resultado)

        return pantalla

    def buscar(self, instancia):
        palabra = self.entrada.text.strip().lower()

        if palabra in palabras:
            self.resultado.text = (
                "En náhuatl es:\n" + palabras[palabra]
            )
        else:
            self.resultado.text = (
                "Todavía no tenemos esa palabra. "
                "Estamos trabajando en ello."
            )


DiccionarioApp().run()
