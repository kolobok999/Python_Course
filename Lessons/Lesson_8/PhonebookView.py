class PhonebookView:
    def __init__(self, model, controller) -> None:
        self.model = model
        self.controller = controller
        self.controller.setView(self)

    def print_start_message(self) -> None:
        print("A-добавить. P-печать. E-экспорт. I-импорт. F-поиск. D-удалить."
              + "U-изменить. Q-выход")

    def print_message(self, message: str) -> None:
        print(message)
