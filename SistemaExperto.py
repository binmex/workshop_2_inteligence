import tkinter as tk
from tkinter import messagebox
from clipspy import ClipsEngine

class SistemaExpertoClipsGUI:
    def __init__(self, master):
        self.master = master
        master.title("Sistema Experto con Clips")

        self.engine = ClipsEngine()

        # Cargar reglas en el motor Clips
        self.engine.load("reglas.clp")

        self.pregunta_label = tk.Label(master, text="¿Te gusta estar activo al aire libre?")
        self.pregunta_label.pack()

        self.si_button = tk.Button(master, text="Sí", command=self.respuesta_si)
        self.si_button.pack(side=tk.LEFT)

        self.no_button = tk.Button(master, text="No", command=self.respuesta_no)
        self.no_button.pack(side=tk.RIGHT)

    def respuesta_si(self):
        # Definir hechos en Clips según la respuesta
        self.engine.assert_string("(respuesta si)")
        self.realizar_inferencia()

    def respuesta_no(self):
        # Definir hechos en Clips según la respuesta
        self.engine.assert_string("(respuesta no)")
        self.realizar_inferencia()

    def realizar_inferencia(self):
        # Ejecutar el motor Clips y obtener la respuesta
        self.engine.run()
        respuesta = self.engine.get_fact("(recomendacion ?actividad)")
        messagebox.showinfo("Recomendación", f"Te recomendamos hacer {respuesta}")

root = tk.Tk()
app = SistemaExpertoClipsGUI(root)
root.mainloop()