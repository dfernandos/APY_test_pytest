import requests

ENDPOINT = "https://reqres.in"

def test_consegue_chamar_o_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
    pass

def test_pode_criar_um_usuário():

    # payload para criar um usuário
    payload = {
    "name": "nadja",
    "job": "zion resident"
    }
    # faz o post para criar um usuário
    responseCreateUser = requests.post("https://reqres.in/api/users/", payload)
    # valida se retornou o status code correto
    assert responseCreateUser.status_code == 201
    #pega o dado do response
    data = responseCreateUser.json()
    # pega o id do usuário criado
    nome = data["name"]
    #mostra usuário no console
    print(nome)
    print(data)
    #valida se nome do usuário está correto
    assert nome == "nadja"

def test_pode_deletar_um_usuário():
    id = "2"
    responseDeleteUser = requests.delete("https://reqres.in/api/users/" + id)

    statuscode = responseDeleteUser.status_code
    assert statuscode == 204

def test_pode_pegar_um_usuário():
    id = "2"
    responseGetUser = requests.get("https://reqres.in/api/users/" + id)

    statuscode = responseGetUser.status_code
    assert statuscode == 200

    data = responseGetUser.json()
    nome = data["data"]["first_name"]
    #mostra usuário no console
    print(nome)
    print(data)
    #valida se nome do usuário está correto
    assert nome == "Janet"

def test_pode_atualizar_um_usuário():

    # payload para criar um usuário
    payload = {
    "name": "nadja",
    "job": "zion resident"
    }
    # faz o put para atualizar um usuário de id 2
    responseCreateUser = requests.put("https://reqres.in/api/users/2", payload)
    # valida se retornou o status code correto
    assert responseCreateUser.status_code == 200
    #pega o dado do response
    data = responseCreateUser.json()
    # pega o id do usuário criado
    nome = data["name"]
    #mostra usuário no console
    print(nome)
    print(data)
    #valida se nome do usuário está correto
    assert nome == "nadja"



