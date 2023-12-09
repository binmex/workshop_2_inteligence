
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

        self.pregunta_label = tk.Label(master, text="¿su glucosa es mayor a 127?")
        self.pregunta_label.pack()

        self.si_button = tk.Button(master, text="Sí", command=self.respuesta_si)
        self.si_button.pack(side=tk.LEFT)

        self.no_button = tk.Button(master, text="No", command=self.respuesta_no)
        self.no_button.pack(side=tk.RIGHT)

    def respuesta_si(self):
        # Definir hechos en Clips según la respuesta
        self.env.assert_string("(respuesta si)")
        self.realizar_inferencia()

    def respuesta_no(self):
        # Definir hechos en Clips según la respuesta
        self.env.assert_string("(respuesta no)")
        self.realizar_inferencia()

    def realizar_inferencia(self):
        # Ejecutar el motor Clips y obtener la respuesta
        self.env.run()
        facts = self.env.facts()
        for fact in facts:
            if fact.template.name == 'recomendacion':
                respuesta = fact[0]  # Acceder al primer elemento de la tupla
                break
        messagebox.showinfo("Recomendación", f"%diabetes  {respuesta}")

root = tk.Tk()
app = SistemaExpertoClipsGUI(root)
root.mainloop()