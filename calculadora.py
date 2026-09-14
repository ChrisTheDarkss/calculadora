"""
Ejercicio 1 - Sesión 11
Calculadora (GridLayout 4x5)
TINF1119 - Diseño y Construcción de Interfaces Gráficas con Layouts
"""

import re

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

# Operadores válidos que acepta el evaluador de expresiones
_ALLOWED_CHARS = re.compile(r"^[0-9+\-*/.%\s]*$")


def evaluar_expresion(expresion: str) -> str:
    """Evalúa una expresión aritmética simple de forma segura.

    Sólo permite dígitos, punto decimal y los operadores +,-,*,/,%.
    Devuelve el resultado como texto o 'Error' si la expresión no es válida.
    """
    if not expresion or not _ALLOWED_CHARS.match(expresion):
        return "Error"
    try:
        resultado = eval(expresion, {"__builtins__": {}}, {})
        if isinstance(resultado, float) and resultado.is_integer():
            resultado = int(resultado)
        return str(resultado)
    except ZeroDivisionError:
        return "Error: /0"
    except Exception:
        return "Error"


class Calculadora(BoxLayout):
    """Calculadora con GridLayout de 4 columnas x 5 filas."""

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=10, spacing=10, **kwargs)

        self.expresion = ""

        # --- Label: visualizador en tiempo real ---
        self.display = Label(
            text="0",
            font_size="32sp",
            size_hint=(1, 0.22),
            halign="right",
            valign="middle",
        )
        self.display.bind(size=self._actualizar_text_size)
        self.add_widget(self.display)

        # --- GridLayout 4 columnas x 5 filas ---
        grid = GridLayout(cols=4, rows=5, spacing=6, size_hint=(1, 0.78))

        botones = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", "00", ".", "+",
            "C", "⌫", "%", "=",
        ]

        for etiqueta in botones:
            boton = Button(text=etiqueta, font_size="22sp")
            boton.bind(on_release=self._on_boton)
            grid.add_widget(boton)

        self.add_widget(grid)

    def _actualizar_text_size(self, instance, value):
        instance.text_size = value

    def _on_boton(self, instance):
        texto = instance.text

        if texto == "C":
            self.expresion = ""
            self.display.text = "0"
            return

        if texto == "⌫":
            self.expresion = self.expresion[:-1]
            self.display.text = self.expresion if self.expresion else "0"
            return

        if texto == "=":
            self.expresion = evaluar_expresion(self.expresion)
            self.display.text = self.expresion if self.expresion else "0"
            return

        self.expresion += texto
        self.display.text = self.expresion


class CalculadoraApp(App):
    title = "Calculadora - GridLayout 4x5"

    def build(self):
        return Calculadora()


if __name__ == "__main__":
    CalculadoraApp().run()
