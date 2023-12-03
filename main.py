import flet as ft
import time

def main(page: ft.Page):
    t = ft.Text(value="Hello, world!", color="green")
    page.controls.append(t)
    t = ft.Text()
    page.add(t) # it's a shortcut for page.controls.append(t) and then page.update()

    for i in range(10):
        t.value = f"Step {i}"
        page.update()
        time.sleep(1)
    

# Якщо потрібно відкрити в браузері додамо цей параметр - view=ft.AppView.WEB_BROWSER
ft.app(target=main)