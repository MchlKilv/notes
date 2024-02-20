from datetime import datetime
import json
import os


class NotesManager:
    def __init__(self, filename="data/notes.json"):
        # Загрузка заметок из файла JSON
        self.filename = filename
        self.notes = []
        self.load_notes()

    def load_notes(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                try:
                    self.notes = json.load(file)
                except json.JSONDecodeError:
                    # Обработка ошибки в случае некорректного JSON
                    print(
                        "Ошибка при загрузке данных из файла. Создан новый файл notes.json."
                    )
                    self.notes = []
        else:
            self.notes = []

    def save_notes(self):
        # Сохранение заметок в файл JSON
        with open(self.filename, "w") as file:
            json.dump(self.notes, file, indent=2)

    def add_note(self, title, message):
        # Добавление новой заметки
        note = {
            "id": len(self.notes) + 1,
            "title": title,
            "message": message,
            "timestamp": str(datetime.now()),
        }
        self.notes.append(note)
        self.save_notes()
        print("Заметка успешно сохранена.")

    def list_notes(self, date_filter=None):
        # Вывод списка заметок с фильтром по дате
        if date_filter:
            filtered_notes = [
                note for note in self.notes if note["timestamp"].startswith(date_filter)
            ]
            for note in filtered_notes:
                print(
                    f"{note['id']}. {note['title']} - {note['message']} ({note['timestamp']})"
                )
        else:
            for note in self.notes:
                print(
                    f"{note['id']}. {note['title']} - {note['message']} ({note['timestamp']})"
                )

    def edit_note(self, note_id, title, message):
        # Изменение заметки по ID
        if 1 <= note_id <= len(self.notes):
            self.notes[note_id - 1]["title"] = title
            self.notes[note_id - 1]["message"] = message
            self.notes[note_id - 1]["timestamp"] = str(datetime.now())
            self.save_notes()
            print(f"Заметка {note_id} успешно изменена.")
        else:
            print("Неверный номер заметки.")

    def delete_note(self, note_id):
        # Удаление заметки по ID
        if 1 <= note_id <= len(self.notes):
            deleted_note = self.notes.pop(note_id - 1)
            self.save_notes()
            print(f"Заметка {note_id} успешно удалена: {deleted_note}")
        else:
            print("Неверный номер заметки.")

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note["id"] == note_id:
                return note
        return None
