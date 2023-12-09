import clips
import tkinter as tk
from tkinter import messagebox

def run_diabetes_expert_system(age, glucose_level):
    # Crear un entorno CLIPS
    env = clips.Environment()

    # Definir hechos
    env.assert_string(f'(patient (age {age}) (glucose-level {glucose_level}) (diabetes-detected FALSE))')

    # Definir reglas
    env.build('(defrule diabetes-rule '
              '(patient (age ?a) (glucose-level ?g&:(>= ?g 140)) (diabetes-detected FALSE)) '
              '=> '
              '(assert (diabetes-detected TRUE)))')

    # Ejecutar el sistema experto
    env.run()

    # Verificar si se detectó la diabetes
    return bool(env.find_fact('(diabetes-detected TRUE)'))

def on_submit():
    age = age_entry.get()
    glucose_level = glucose_entry.get()

    try:
        age = int(age)
        glucose_level = int(glucose_level)

        diabetes_detected = run_diabetes_expert_system(age, glucose_level)

        if diabetes_detected:
            messagebox.showinfo("Resultado", "Se ha detectado diabetes.")
        else:
            messagebox.showinfo("Resultado", "No se ha detectado diabetes.")

    except ValueError:
        messagebox.showerror("Error", "Ingresa valores numéricos válidos para la edad y el nivel de glucosa.")

# Crear una ventana principal de Tkinter
root = tk.Tk()
root.title("Sistema Experto para Detectar Diabetes")

# Etiqueta y entrada para la edad
age_label = tk.Label(root, text="Edad:")
age_label.pack()

age_entry = tk.Entry(root)
age_entry.pack()

# Etiqueta y entrada para el nivel de glucosa
glucose_label = tk.Label(root, text="Nivel de Glucosa:")
glucose_label.pack()

glucose_entry = tk.Entry(root)
glucose_entry.pack()

# Botón para ejecutar el sistema experto
submit_button = tk.Button(root, text="Detectar Diabetes", command=on_submit)
submit_button.pack(pady=10)

# Ejecutar el bucle principal de Tkinter
root.mainloop()
