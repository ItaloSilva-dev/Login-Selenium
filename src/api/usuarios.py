import requests

def criar_usuario(nome,email,senha):
    url = "https://serverest.dev/usuarios"

    dados = {
        "nome": nome,
        "email": email,
        "password": senha,
        "administrador": "false"
    }

    resposta = requests.post(url, json=dados)
    return resposta

def excluir_usuario(usuario_id):
    url = f"https://serverest.dev/usuarios/{usuario_id}"
    resposta = requests.delete(url)
    return resposta
    