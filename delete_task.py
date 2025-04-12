def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    print("🗑️ Tarea eliminada (si existía).")

# Interfaz de consola
def main():
    while True:
        print("\n📋 Gestor de Tareas")
        print("1. Crear tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")
        
        option = input("Selecciona una opción: ")

        if option == '1':
            description = input("Descripción de la tarea: ")
            create_task(description)
        elif option == '2':
            list_tasks()
        elif option == '3':
            task_id = input("ID de la tarea a completar: ")
            complete_task(task_id)
        elif option == '4':
            task_id = input("ID de la tarea a eliminar: ")
            delete_task(task_id)
        elif option == '5':
            print("👋 Saliendo del gestor.")
            break
        else:
            print("❗ Opción no válida.")

if __name__ == "__main__":
    main()