import tkinter as tk
from tkinter import messagebox
import clips

class SistemaExpertoClipsGUI:
    def __init__(self, master):
        self.master = master
        master.title("Sistema Experto con Clips")

        # Crear el entorno Clips
        self.env = clips.Environment()

        # Cargar reglas en el motor Clips
        self.env.load("reglas.clp")

        # Crear etiquetas y campos de entrada para edad, nivel de insulina e IMC
        self.edad_label = tk.Label(master, text="Edad:")
        self.edad_label.pack()
        self.edad_entry = tk.Entry(master)
        self.edad_entry.pack()

        self.glucosa_label = tk.Label(master, text="Nivel de Glucosa:")
        self.glucosa_label.pack()
        self.glucosa_entry = tk.Entry(master)
        self.glucosa_entry.pack()

        self.imc_label = tk.Label(master, text="Índice de Masa Corporal:")
        self.imc_label.pack()
        self.imc_entry = tk.Entry(master)
        self.imc_entry.pack()

        # Botón para enviar la respuesta y datos adicionales
        self.submit_button = tk.Button(master, text="Enviar", command=self.enviar_respuesta)
        self.submit_button.pack()

    def validar_datos_numericos(self, valor):
        try:
            valor_numerico = float(valor)
            return valor_numerico >= 0
        except ValueError:
            return False

    def enviar_respuesta(self):
        # Obtener las respuestas de los campos de texto
        edad = self.edad_entry.get()
        glucosa = self.glucosa_entry.get()
        imc = self.imc_entry.get()

        # Validar los datos
        if not (self.validar_datos_numericos(edad) and
                self.validar_datos_numericos(glucosa) and
                self.validar_datos_numericos(imc)):
            messagebox.showwarning("Datos inválidos", "Por favor, ingresa valores numéricos mayores o iguales a 0.")
            return

        # Enviar los datos al motor Clips
        self.env.assert_string(f"(edad {edad}) (nivel-insulina {glucosa}) (imc {imc})")

        # Realizar inferencia
        self.realizar_inferencia()

    # ...

    def realizar_inferencia(self):
        # Ejecutar el motor Clips y obtener la respuesta
        self.env.run()
        facts = self.env.facts()
        respuesta = None  # Inicializar respuesta antes del bucle
        probabilidad = None  # Inicializar probabilidad

        for fact in facts:
            if fact.template.name == 'recomendacion':
                respuesta = fact[0]  # Acceder al segundo elemento de la tupla (valor del atributo)
            elif fact.template.name == 'probabilidad-total':
                probabilidad = fact[0]  # Acceder al primer y único elemento de la tupla (valor del atributo)



# Crear la ventana principal
root = tk.Tk()
app = SistemaExpertoClipsGUI(root)
root.mainloop()