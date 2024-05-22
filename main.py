from cola import Cola 


class Main:
    def __init__(self):
        self.cola = Cola()
        
    def mostrar_menu(self):
        while True:
            print("\n--- Menú de Gestión de Turnos ---")
            print("1. Asignar Turno")
            print("2. Llamar Turno")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                self.cola.asignarTurno()
            elif opcion == '2':
                turno = self.cola.llamarTurno()
                if turno == "No hay turnos asignados":
                    print(turno)
                else:
                    print(f"Turno llamado: {turno}")
            elif opcion == '3':
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida, por favor seleccione nuevamente.")

# Ejecución del menú
if __name__ == "__main__":
    main = Main()
    main.mostrar_menu()