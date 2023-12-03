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
    page.add(ft.Row(controls=[ft.Text("A"),ft.Text("B"),ft.Text("C")]))
    
    #Поле вводу та кнопка
    page.add(
    ft.Row(controls=[
        ft.TextField(label="Your name"),
        ft.ElevatedButton(text="Say my name!")
    ]))
    
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
    
#Ключевий блок виводу
# Якщо потрібно відкрити в браузері додамо цей параметр - view=ft.AppView.WEB_BROWSER
ft.app(target=main)