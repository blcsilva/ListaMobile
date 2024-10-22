import flet as ft
import requests

API_URL = "http://127.0.0.1:8000/api/tasks/"  # URL da API DRF

def main(page: ft.Page):
    page.title = "Todo App with DRF and Flet"
    page.vertical_alignment = ft.MainAxisAlignment.START

    tasks = ft.Column()

    def fetch_tasks():
        response = requests.get(API_URL)
        if response.status_code == 200:
            for task_data in response.json():
                add_task_to_ui(task_data['id'], task_data['title'], task_data['completed'])
        else:
            print("Erro ao buscar tarefas.")

    def add_task_to_ui(task_id, title, completed):
        task_checkbox = ft.Checkbox(
            label=title,
            value=completed,
            on_change=lambda e: update_task_status(task_id, e.control.value)
        )
        delete_button = ft.IconButton(
            icon=ft.icons.DELETE,
            on_click=lambda e: delete_task(task_id)
        )
        task_row = ft.Row([task_checkbox, delete_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        tasks.controls.append(task_row)
        page.update()

    def add_task(e):
        task_title = new_task.value
        if task_title:
            response = requests.post(API_URL, json={"title": task_title, "completed": False})
            if response.status_code == 201:
                task_data = response.json()
                add_task_to_ui(task_data['id'], task_data['title'], task_data['completed'])
            new_task.value = ""
            page.update()

    def update_task_status(task_id, completed):
        response = requests.patch(f"{API_URL}{task_id}/", json={"completed": completed})
        if response.status_code != 200:
            print("Erro ao atualizar tarefa.")

    def delete_task(task_id):
        response = requests.delete(f"{API_URL}{task_id}/")
        if response.status_code == 204:
            tasks.controls.clear()
            fetch_tasks()
            page.update()

    # Campo para nova tarefa
    new_task = ft.TextField(hint_text="Nova tarefa", width=300)
    add_button = ft.ElevatedButton("Adicionar", on_click=add_task)

    # Layout principal
    page.add(
        ft.Row([new_task, add_button], alignment=ft.MainAxisAlignment.START),
        tasks
    )

    # Buscar tarefas ao carregar
    fetch_tasks()

ft.app(target=main)
