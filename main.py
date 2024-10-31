#Задача: Создай класс `Task`, который позволяет управлять задачами (делами). У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task:
    def __init__(self):
        self.tasks = []

    def add_task(self, deadline,description):
        self.tasks.append({'description': description, 'deadline': deadline, 'status': 'не выполнено'})

    def complete_task(self, description):
        for task in self.tasks:
            if task['description'] == description:
                if task['status'] == 'не выполнено':
                    task['status'] = "выполнено"
                    print(f"Задача '{description}' выполнена")
                return
        print(f"Задача '{description}' не найдена")

    def show_tasks(self):
        print('Текущие задачи:')
        for task in self.tasks:
            if task['status'] == 'не выполнено':
                print(f"{task ['deadline']} - {task ['description']}")


# Пример использования
t = Task()

t.add_task("07.40","Подъем")
t.add_task("07.50","Выпить стакан воды")
t.add_task("08.10", "Сделать зарядку")
t.add_task("08.20","Умыться")

t.show_tasks()

t.complete_task("Подъем")
t.complete_task("Выпить стакан воды")

t.show_tasks()