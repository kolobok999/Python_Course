class PhonebookController:
    def __init__(self, model):
        self.model = model
        

    def setView(self, view):
        self.view = view

    def input_user(self):
        user = list()
        user.append(input('Введите Фамилию: '))
        user.append(input('Введите Имя: '))
        user.append(input('Введите номер телефона: '))
        user.append(input('Введите описание: '))
        return user

    def get_action(self):
        return input('Выберите действие: ').upper()

    def run_phone_book(self):
        self.view.print_start_message()
        
        while True:
            action = self.get_action()
            if action == 'Q':
                break
            elif action == 'A':
                self.model.phonebook = self.model.create(self.input_user())
                self.view.print_message(f'Мы добавили пользователя '
                                        + f'{self.model.phonebook[len(self.model.phonebook) - 1][0]} '
                                        + 'в телефонный справочник')
            elif action == 'E':
                self.model.export_phonebook(input('Введите имя файла для экспорта: '))
            elif action == 'I':
                self.model.phonebook = self.model.import_phonebook(input("Введите имя файла для импорта: "))
            elif action == 'F':
                idx = self.model.find(input('Введите фамилию искомого человека: '))
                if idx == None:
                    self.view.print_message('Такого человека нет в справочнике.')
                else:
                    self.view.print_message(f'{self.model.phonebook[idx][0]} '
                                            + f'{self.model.phonebook[idx][1]} '
                                            + f'{self.model.phonebook[idx][2]} '
                                            + f'{self.model.phonebook[idx][3]}')
            elif action == 'D':
                print(f'Удаляем: {self.model.delete(input("Введите id или фамилию удаляемой записи: "))}')
            elif action == 'U':
                self.model.update(input('Введите фамилию, кого обновить: '), self.input_user())
            else:
                self.view.print_message("Ни одна из комманд не подходит. Давайте попробуем ещё раз.")
