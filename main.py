from notes_manager.manager import NotesManager


if __name__ == "__main__":
    notes_manager = NotesManager()

    while True:
        print("\nМеню:")
        print("1. Создать заметку")
        print("2. Изменить заметку")
        print("3. Удалить заметку")
        print("4. Показать заметку по ID")
        print("5. Показать заметки по дате")
        print("6. Показать все заметки")
        print("7. Выход")

        choice = input("\nВыберите опцию (1-7): ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            message = input("Введите текст заметки: ")
            notes_manager.add_note(title, message)

        elif choice == "2":
            note_id = int(input("Введите номер заметки для изменения: "))
            title = input("Введите новый заголовок: ")
            message = input("Введите новый текст заметки: ")
            notes_manager.edit_note(note_id, title, message)

        elif choice == "3":
            note_id = int(input("Введите номер заметки для удаления: "))
            notes_manager.delete_note(note_id)

        elif choice == "4":
            note_id = int(input("Введите номер заметки для просмотра: "))
            note = notes_manager.get_note_by_id(note_id)
            if note:
                print(
                    f"{note['id']}. {note['title']} - {note['message']} ({note['timestamp']})"
                )
            else:
                print(f"Заметка с ID {note_id} не найдена.")

        elif choice == "5":
            date_filter = input("Введите дату для фильтрации (гггг-мм-дд): ")
            notes_manager.list_notes(date_filter)

        elif choice == "6":
            notes_manager.list_notes()

        elif choice == "7":
            break

        else:
            print("Неверный выбор. Пожалуйста, повторите ввод.")
