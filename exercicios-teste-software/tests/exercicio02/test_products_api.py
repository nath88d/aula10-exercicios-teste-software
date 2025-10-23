import pytest
import requests

BASE_URL = "https://fakestoreapi.com/products"


# Teste 1: Listar todos os produtos
def test_listar_produtos():
    response = requests.get(BASE_URL)
    print("\n🔹 Resposta (listar produtos):", response.status_code)
    assert response.status_code == 200

    data = response.json()
    print(f"Total de produtos retornados: {len(data)}")
    assert len(data) > 0
    assert "title" in data[0]
    assert "price" in data[0]
    assert "category" in data[0]


# Teste 2: Buscar produto por ID
@pytest.mark.parametrize("product_id", [1, 5, 10])
def test_buscar_produto_por_id(product_id):
    response = requests.get(f"{BASE_URL}/{product_id}")
    print(f"\n🔹 Resposta (produto ID {product_id}):", response.status_code)
    assert response.status_code == 200

    product = response.json()
    print(product)
    assert product["id"] == product_id
    assert "title" in product
    assert "price" in product
    assert "category" in product


# Teste 3: Filtrar produtos por categoria
@pytest.mark.parametrize("categoria", ["electronics", "jewelery", "men's clothing", "women's clothing"])
def test_filtrar_produtos_por_categoria(categoria):
    response = requests.get(f"{BASE_URL}/category/{categoria}")
    print(f"\n🔹 Resposta (categoria: {categoria}):", response.status_code)
    assert response.status_code == 200

    produtos = response.json()
    print(f"Quantidade retornada: {len(produtos)}")
    assert len(produtos) > 0
    for p in produtos:
        assert p["category"] == categoria


# Teste 4: Validar schema da resposta
def test_validar_schema_produto():
    response = requests.get(f"{BASE_URL}/1")
    assert response.status_code == 200
    produto = response.json()
    print("\n🔹 Schema do produto ID 1:", produto)

    chaves_esperadas = {"id", "title", "price", "description", "category", "image"}
    assert set(produto.keys()) >= chaves_esperadas


# Teste 5: Testar limite de produtos retornados
def test_limite_de_produtos():
    limite = 5
    response = requests.get(f"{BASE_URL}?limit={limite}")
    print("\n🔹 Resposta (limite de produtos):", response.status_code)
    assert response.status_code == 200

    data = response.json()
    print(f"Quantidade retornada: {len(data)}")
    assert len(data) == limite
