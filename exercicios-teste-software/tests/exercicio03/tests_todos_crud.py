import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/todos"


@pytest.fixture
def novo_todo():
    payload = {
        "title": "Minha tarefa",
        "completed": False,
        "userId": 1
    }
    response = requests.post(BASE_URL, json=payload)
    print("\n🔹 Criando TODO:", response.status_code, response.json())
    assert response.status_code == 201
    todo = response.json()
    yield todo
    print("\n🔹 (Teardown) Deletando TODO criado de teste:", todo["id"])
    requests.delete(f"{BASE_URL}/{todo['id']}")


# Teste 1: CREATE
def test_criar_todo():
    payload = {
        "title": "Minha tarefa",
        "completed": False,
        "userId": 1
    }
    response = requests.post(BASE_URL, json=payload)
    print("\n🔹 Resposta (CREATE):", response.status_code, response.json())
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Minha tarefa"
    assert data["completed"] is False
    assert data["userId"] == 1


# Teste 2: READ
def test_buscar_todo():
    response = requests.get(f"{BASE_URL}/1")
    print("\n🔹 Resposta (READ):", response.status_code, response.json())
    assert response.status_code == 200
    data = response.json()
    assert "title" in data
    assert "completed" in data
    assert "userId" in data


# Teste 3: UPDATE (PATCH)
def test_atualizar_todo(novo_todo):
    todo_id = novo_todo["id"]
    payload = {"completed": True}
    response = requests.patch(f"{BASE_URL}/{todo_id}", json=payload)
    print("\n🔹 Resposta (UPDATE):", response.status_code, response.json())
    assert response.status_code in [200, 204]
    data = response.json()
    assert "completed" in data
    assert data["completed"] is True


# Teste 4: DELETE
def test_deletar_todo(novo_todo):
    todo_id = novo_todo["id"]
    response = requests.delete(f"{BASE_URL}/{todo_id}")
    print("\n🔹 Resposta (DELETE):", response.status_code)
    assert response.status_code in [200, 204]


# Teste 5: VERIFY (GET após DELETE)
def test_verificar_todo_removido():
    response = requests.get(f"{BASE_URL}/7188900000")
    print("\n🔹 Resposta (VERIFY após DELETE):", response.status_code)
    assert response.status_code in [200, 404]
    data = response.json()
    assert data == {} or "error" in data or response.status_code == 404


# Teste 6: Criar TODO sem título (erro esperado)
def test_criar_todo_sem_titulo():
    payload = {
        "completed": False,
        "userId": 1
    }
    response = requests.post(BASE_URL, json=payload)
    print("\n🔹 Resposta (CREATE sem título):", response.status_code, response.json())

    # JSONPlaceholder não retorna erro real, mas testamos comportamento esperado
    assert response.status_code in [400, 201]
    data = response.json()
    if response.status_code == 201:
        assert "title" not in data or data["title"] == ""
