# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
# Выберите наиболее удобную структуру данных для хранения справочника.
# 2) CRUD: Create, Read, Update, Delete
# Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
# Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. Берем первое совпадение по фамилии.
# Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
# Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
# 4) импорт данных из текстового файла формата csv

from os.path import join, abspath, relpath, dirname, exists
MAIN_DIR = abspath(dirname(__file__))


class PhonebookModel:
    def __init__(self) -> None:
        self.phonebook = {0: ["firstname1", "secondname1", "phone1", "description1"],
                          1: ["firstname2", "secondname2", "phone2", "description2"]}
        # self.phonebook = dict()

    def create(self, phone_list: list) -> dict:
        self.phone_list = phone_list
        size = len(self.phonebook)
        self.phonebook[size] = self.phone_list
        return self.phonebook

    def export_phonebook(self, file_name: str):
        full_name = join(MAIN_DIR, "data", file_name + '.csv')
        with open(full_name, mode="w", encoding="UTF-8") as file:
            for value in self.phonebook.values():
                file.write(f'{value[0]}#{value[1]}#{value[2]}#{value[3]}\n')

    def import_phonebook(self, file_name: str) -> dict:
        full_name = join(MAIN_DIR, "data", file_name + '.csv')
        with open(full_name, mode='r', encoding='UTF-8') as file:
            for line in file:
                user = line.strip().split('#')
                self.phonebook.update(self.create(user))
        return self.phonebook

    def find(self, search_word: str) -> int:
        for idx, user in self.phonebook.items():
            last_name = user[0]
            if last_name.upper().startswith(search_word.upper()):
                return idx

    def update(self, upd: str, phone_list: list):
        idx = self.find(upd)
        self.phonebook[idx] = phone_list

    def delete(self, deleting: str):
        if deleting.isdigit():
            deleting = int(deleting)
        if isinstance(deleting, int):
            user = self.phonebook.pop(deleting, 'Такого id нет')
            self.update_idx()
            return user
        if isinstance(deleting, str):
            user = self.phonebook.pop(
                self.find(deleting), 'Такого человека нет')
            self.update_idx()
            return user

    def update_idx(self):
        idx = 0
        phones = self.phonebook.copy()
        self.phonebook.clear()
        for value in phones.values():
            self.phonebook[idx] = value
            idx += 1

