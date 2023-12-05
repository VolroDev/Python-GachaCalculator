#https://flet.dev/docs/guides/python/getting-started/

#Підключеня модулів
import flet as ft
import time

def main(page: ft.Page):
    #Запис в змінну текстового формата данних з вказанням кольору
    t = ft.Text(value="Hello, world!", color="green")
    
    #Додавання в перелік виводу
    page.controls.append(t) 
    
    #Запис в змінну тестового формату без даних
    t = ft.Text()
    
    #Додавання в перелік для виводу
    page.add(t) # it's a shortcut for page.controls.append(t) and then page.update()

    #Циклом вказуємо значення параметру, оновлюємо сторінку та ставимо затримку на 1 секунду
    for i in range(10):
        t.value = f"Step {i}"
        page.update()
        time.sleep(0.1)
    
    #Виведення єлементів один за одним. Приклад контейнера єлеентів 
    #Використовувати можна Row та Column   
    page.add(ft.Row(controls=[ft.Text("A"),ft.Text("B"),ft.Text("C")]))
    
    #Поле вводу та кнопка
    page.add(
    ft.Row(controls=[
        ft.TextField(label="Your name"),
        ft.ElevatedButton(text="Say my name!")
    ]))
    
    '''
    elements_to_remove = []
    for i in range(10):
        page.controls.append(ft.Text(f"Line {i}"))
        if i > 4:
            elements_to_remove.append(len(page.controls)-1)
    page.update()
    time.sleep(0.3)

    for index in elements_to_remove:
        page.controls.pop(index)
    page.update()
    '''
    
    #Виклик функції що додає на сторінку єлемент текстового типу
    def button_clicked(e):
        page.add(ft.Text("Clicked!"))

    #Додавання кнопки при натиснені якої відбувається киклик іншої функції
    page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))

    #Функція що додає на сторінку нову чекбокс з тою назвою що вказав користувач
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    #Спочатку ініціалізуємо поле, потім у вигляді контейнеру виводимо це поле та кнопку
    new_task = ft.TextField(hint_text="Whats needs to be done?", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))

    #Приклад двох параметрів. visible (видимість) , disabled (вимкнено/не активный)
    first = ft.TextField()
    last = ft.TextField()
    #visible - постандарту true, якщо false - елементне видно
    first.visible = False
    #disabled - по стандарту false, якщо true - елемент не активний не формі але його видно
    last.disabled = True
    page.add(first, last)

    #Control Refs , ми вказуємо для чіткого розуміння якого типу є змінна. Це робиться для більш корректного використання в функціях    
    first_name = ft.Ref[ft.TextField]()
    last_name = ft.Ref[ft.TextField]()
    greetings = ft.Ref[ft.Column]()

    def btn_click(e):
        greetings.current.controls.append(
            ft.Text(f"Hello, {first_name.current.value} {last_name.current.value}!")
        )
        first_name.current.value = ""
        last_name.current.value = ""
        page.update()
        first_name.current.focus()

    page.add(
        ft.TextField(ref=first_name, label="First name", autofocus=True),
        ft.TextField(ref=last_name, label="Last name"),
        ft.ElevatedButton("Say hello!", on_click=btn_click),
        ft.Column(ref=greetings),
    )
    
    
#Ключевий блок виводу
# Якщо потрібно відкрити в браузері додамо цей параметр - view=ft.AppView.WEB_BROWSER
ft.app(target=main)