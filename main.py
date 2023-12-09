import clips
import tkinter as tk

def run_clips_system():
    # Crear un entorno CLIPS
    env = clips.Environment()

    # Definir hechos
    fact1 = env.assert_string('(ordered-fact 1 2 3)')
    fact2 = env.assert_string('(ordered-fact 3 2 1)')

    # Definir regla
    env.build('(defrule ordered-fact-rule '
              '(ordered-fact ?a ?b ?c) '
              '(test (> ?a ?b)) '
              '=> '
              '(printout t "Los elementos no están en orden ascendente." crlf))')

    # Ejecutar el sistema experto
    env.run()

    # Acceder a los datos de los hechos
    print(f'Fact1: {list(fact1)}')
    print(f'Fact2: {list(fact2)}')

def main():
    # Crear una ventana principal de Tkinter
    root = tk.Tk()
    root.title("Sistema Experto con Tkinter")

    # Botón para ejecutar el sistema experto
    run_button = tk.Button(root, text="Ejecutar Sistema Experto", command=run_clips_system)
    run_button.pack(pady=10)

    # Etiqueta para mostrar resultados (puedes adaptarlo según tus necesidades)
    result_label = tk.Label(root, text="")
    result_label.pack(pady=10)

    # Función para actualizar la etiqueta de resultados
    def update_result_label():
        result_label.config(text="¡Sistema experto ejecutado!")

    # Botón para actualizar la etiqueta de resultados
    update_button = tk.Button(root, text="Actualizar Resultados", command=update_result_label)
    update_button.pack(pady=10)

    # Ejecutar el bucle principal de Tkinter
    root.mainloop()

if __name__ == "__main__":
    main()
