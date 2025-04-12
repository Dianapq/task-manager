# main.py

from task_manager.storage import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\n--- MENÚ ---")
        print("1. Crear tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")

        option = input("Seleccione una opción: ")

        if option == "1":
            desc = input("Descripción de la tarea: ")
            manager.add_task(desc)

        elif option == "2":
            manager.list_tasks()

        elif option == "3":
            idx = int(input("Número de tarea a completar: ")) - 1
            manager.complete_task(idx)

        elif option == "4":
            idx = int(input("Número de tarea a eliminar: ")) - 1
            manager.delete_task(idx)

        elif option == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
