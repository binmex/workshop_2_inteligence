#from clips import Environment
#import clips as clips
import tkinter as tk
from tkinter import ttk

# Crear un entorno CLIPS
env = Environment()

# Cargar reglas en el entorno
env.load("diagnostico_diabetes.clp")

# Función para ejecutar el sistema al hacer clic en el botón
def ejecutar_diagnostico():
    # Obtener datos de la interfaz
    edad = int(edad_entry.get())
    glucosa = int(glucosa_entry.get())
    presion = int(presion_entry.get())
    historial = historial_combobox.get()

    # Crear un hecho con los datos del paciente
    paciente_fact = env.assert_string(f"(Paciente (Edad {edad}) (NivelGlucosa {glucosa}) (PresionArterial {presion}) (HistorialFamiliar {historial}))")

    # Ejecutar el sistema
    env.run()

    # Obtener el diagnóstico
    diagnostico_fact = env.find_fact("(Diagnostico (ProbabilidadDiabetes ?prob))")
    probabilidad_diabetes.set(f"Probabilidad de tener diabetes: {diagnostico_fact[0].slots['ProbabilidadDiabetes']}%")

    # Retract para limpiar la memoria
    env.retract(paciente_fact)

# Crear la interfaz
root = tk.Tk()
root.title("Sistema de Diagnóstico de Diabetes")

# Widgets
edad_label = ttk.Label(root, text="Edad:")
edad_entry = ttk.Entry(root)

glucosa_label = ttk.Label(root, text="Nivel de Glucosa:")
glucosa_entry = ttk.Entry(root)

presion_label = ttk.Label(root, text="Presión Arterial:")
presion_entry = ttk.Entry(root)

historial_label = ttk.Label(root, text="Historial Familiar:")
historial_combobox = ttk.Combobox(root, values=["positivo", "negativo"])
historial_combobox.set("negativo")

ejecutar_button = ttk.Button(root, text="Ejecutar Diagnóstico", command=ejecutar_diagnostico)

probabilidad_diabetes = tk.StringVar()
resultado_label = ttk.Label(root, textvariable=probabilidad_diabetes)

# Posicionamiento de Widgets
edad_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
edad_entry.grid(row=0, column=1, padx=5, pady=5)

glucosa_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
glucosa_entry.grid(row=1, column=1, padx=5, pady=5)

presion_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
presion_entry.grid(row=2, column=1, padx=5, pady=5)

historial_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
historial_combobox.grid(row=3, column=1, padx=5, pady=5)

ejecutar_button.grid(row=4, columnspan=2, pady=10)

resultado_label.grid(row=5, columnspan=2, pady=10)

# Iniciar la interfaz
root.mainloop()
