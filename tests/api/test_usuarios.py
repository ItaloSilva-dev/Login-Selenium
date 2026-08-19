from src.api.usuarios import criar_usuario
from src.api.usuarios import excluir_usuario


def test_criar_usuario():
    resposta = criar_usuario(
        "Italo Teste", 
        "italo.testee@example.com",
        "senha123"
    )

    print(resposta.status_code)
    print(resposta.json())

    usuario_id = resposta.json()["_id"]
    

    print("ID do usuário criado:", usuario_id)

    assert resposta.status_code == 201 


def test_excluir_usuario():

    resposta = excluir_usuario("D4CkbdX5ofjIPgBj")

    print(resposta.status_code)
    print(resposta.json())

    assert resposta.status_code == 200