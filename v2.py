import os 

produtos = {
    1 : ["Graco Premier Modes Lux Stroller, Midtown™ Collection", "Graco", 2200, 10],
    2 : ["Extend™ LX R129", "Graco", 566, 3],
    3 : ["FastAction™ Fold Sport Click Connect™ Travel System","Graco", 1700, 5],
    4 : ["Butterfly Ultra-Compact Stroller","Bugaboo",2320, 7],
    5 : ["Bugaboo Donkey5 Mono Complete Stroller", "Bugaboo", 7196, 12],
    6 : ["Bugaboo Fox 5 Complete Full-Size Stroller", "Bugaboo" , 5667, 9],
    7 : ["Fisher-Price Soothing Motions Bassinet","Fisher-Price", 464, 6],
    8 : ["Fisher-Price Rainforest Jumperoo","Fisher-price", 438, 10],
    9 : ["Fisher-Price Little People Big Animal Zoo","Fisher-price" ,190, 3],
    10 : ["Baby Einstein Take Along Tunes Musical Toy", "BabyEinstein", 46, 12],
    11 : ["Baby Einstein Sea Dreams Soother","BabyEinstein", 206, 11],
    12 : ["Baby Einstein Glow & Discover Light Bar","BabyEinstein", 92, 13],
    13 : ["VTech Kidizoom Smartwatch DX3","VTech", 309, 6],
    14 : ["VTech Sit-to-Stand Learning Walker","VTech", 180, 13],
    15 : ["VTech Go! Go! Smart Ultimate RC Speedway","VTech" , 257, 9],
    16 : ["Body de mangá curta","Carter's", 40, 12],
    17: ["Macacão de malha","Carter's", 80, 11],
    18: ["Conjunto de bebê","Carter's" , 90, 14],
    19 : ["Vestidos estampados","Lilica Ripilica" ,140, 9],
    20 :["Conjunto de camiseta e calça","Lilica Ripilica" ,200, 17],
    21 : ["Três_meias","Puket", 20, 25],
    22 : ["Body","Puket", 50, 16],
    23 : ["Conjunto de pijama","Puket", 70, 14]
}

clientes = {}
vendedores = {
    "premium": {"nome": "ANDRÉ BABY IMPORTS", "cargo": "Vendedor Premium", "vendas": "5000+ vendas"},
    "ceo": {"nome": "André Leandro de Medeiros Araújo", "idade": 33, "descricao": "Com mestrado em administração e gestão de negócios, atua no mercado de produtos infantis há 10 anos."}
}

carrinho = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def modulo_cliente():
    limpar_tela()
    print("_______________________________________")
    print("_______           Módulo Cliente          _______")
    print("_______________________________________")
    print("____  1 - Cadastrar Cliente              _____")
    print("_____ 2 - Exibir Dados do Cliente       _____")
    print("_____ 3 - Alterar Dados do Cliente       _____")
    print("_____ 4 - Excluir Cliente               _____")
    resp2 = input("##### Escolha sua opção: ")
    
    if resp2 == "1":
        nome = input("Qual seria o seu nome completo? ")
        endereco = input("Qual o seu endereço completo? ")
        telefone = input("Qual o seu número de telefone? ")
        produtos_interesse = input("Qual seria os tipos de produto que seria de seu interesse? (Temos as opções de roupas, fraldas e brinquedos) ")
        metodo_pagamento = input("Qual seria o método de pagamento desejado? ")
        clientes[nome] = {
            "endereco": endereco,
            "telefone": telefone,
            "produtos_interesse": produtos_interesse,
            "metodo_pagamento": metodo_pagamento
        }
    elif resp2 == "2":
        nome = input("Digite o nome do cliente: ")
        if nome in clientes:
            cliente = clientes[nome]
            print("Nome:", nome)
            print("Endereço:", cliente["endereco"])
            print("Telefone:", cliente["telefone"])
            print("Produtos de Interesse:", cliente["produtos_interesse"])
            print("Método de Pagamento:", cliente["metodo_pagamento"])
        else:
            print("Cliente não encontrado.")
        input("Pressione ENTER para continuar...")
    elif resp2 == "3":
        nome = input("Digite o nome do cliente: ")
        if nome in clientes:
            cliente = clientes[nome]
            cliente["endereco"] = input("Edite seu endereço: ")
            cliente["telefone"] = input("Edite seu telefone: ")
            cliente["produtos_interesse"] = input("Edite sua preferência de produtos: ")
            cliente["metodo_pagamento"] = input("Edite seu método de pagamento: ")
        else:
            print("Cliente não encontrado.")
        input("Pressione ENTER para continuar...")
    elif resp2 == "4":
        nome = input("Digite o nome do cliente: ")
        if nome in clientes:
            del clientes[nome]
            print("Cliente excluído com sucesso.")
        else:
            print("Cliente não encontrado.")
        input("Pressione ENTER para continuar...")

def modulo_vendedor():
    limpar_tela()
    print("_______________________________________")
    print("_______           Módulo Vendedor          _______")
    print("_______________________________________")
    print("____   1 - Informações do Vendedor             _____")
    print("_____  2 - Informações do CEO      _____")
    print("_____  3 - Gestão de Estoque      _____")
    resp2 = input("##### Escolha sua opção: ")
    
    if resp2 == "1":
        vendedor = vendedores["premium"]
        print(vendedor["nome"])
        print(vendedor["cargo"])
        print(vendedor["vendas"])
    elif resp2 == "2":
        ceo = vendedores["ceo"]
        print(ceo["nome"])
        print(ceo["idade"])
        print(ceo["descricao"])
    input("Pressione ENTER para continuar...")

def modulo_produto_vendas():
    limpar_tela()
    print("_______________________________________")
    print("_______           Módulo Produtos          _______")
    print("_______________________________________")
    print("____  1 - Ver Produtos           _____")
    input("Temos produtos dos mais variados para sua criança: CARRINHOS, BRINQUEDOS, ROUPAS (Aperte ENTER)")
    print("Do 1 ao 6, marcas de carrinho, do 7 ao 15, marcas de brinquedo e do 16 ao 23, marcas de roupa")
    id_produto = int(input("Qual é o ID de verificação do produto desejado? "))
    if id_produto in produtos:
        produto = produtos[id_produto]
        print("Informações do Produto:")
        print("Nome:", produto[0])
        print("Marca:", produto[1])
        print("Preço unitário:", produto[2])
        adicionar_ao_carrinho = input("Deseja adicionar ao carrinho? (S/N) ").upper()
        if adicionar_ao_carrinho == "S":
            carrinho.append(produto)
            print(f"{produto[0]} adicionado ao carrinho.")
    else:
        print("Produto não encontrado.")
    input("Pressione ENTER para continuar...")

def modulo_caixa():
    limpar_tela()
    print("_______________________________________")
    print("_______           Módulo Caixa         _______")
    print("_______________________________________")
    print("____  1 - Controle de Estoque             _____")
    print("____  2 - Comprar produtos            _____")


    resp2 = input("##### Escolha sua opção: ")
    
    if resp2 == "1":
        print("Para verificação de estoque, você irá chamar um conjunto de números que até uma sequência específica ele irá demonstrar uma modalidade de produto")
        print("Do 1 ao 6, marcas de carrinho, do 7 ao 15, marcas de brinquedo e do 16 ao 23, marcas de roupa")
        id_produto = int(input("Qual é o ID de verificação de estoque desejado? "))
        if id_produto in produtos:
            produto = produtos[id_produto]
            print("Informações do Produto:")
            print("Nome:", produto[0])
            print("Marca:", produto[1])
            print("Preço unitário:", produto[2])
            print("Quantidade disponível em estoque:", produto[3])
        else:
            print("Produto não encontrado.")
    input("Pressione ENTER para continuar...")

    if resp2 == "2":
        print("Para escolha do produto específico do estoque, você irá chamar um conjunto de números que até uma sequência específica ele irá demonstrar uma modalidade de produto")
        print("Do 1 ao 6, marcas de carrinho, do 7 ao 15, marcas de brinquedo e do 16 ao 23, marcas de roupa")
        id_produto = int(input("Qual é o ID de verificação de estoque desejado? "))

        if id_produto in produtos:
            produto = produtos[id_produto]
            quantidade = int(input(f"Você deseja adicionar quantas unidades do produto {produto[0]}? "))
            quantidade += produto[3]  # Supondo que o índice 3 é a quantidade em estoque
            aviso = input(f"Foram adicionadas {quantidade} unidades do produto {produto[0]} ao seu estoque.")
        else:
            print("ID de produto não encontrado no estoque.")



        

def modulo_carrinho():
    limpar_tela()
    total = sum(produto[2] for produto in carrinho)
    print(f"O total no seu carrinho é: {total}")
    finalizar_compra = input("Deseja finalizar a compra?")
    if finalizar_compra.upper() == "S":
        print("Compra finalizada com sucesso!")
        carrinho.clear()
    else:
        print("Compra não finalizada.")
    input("Pressione ENTER para continuar...")

def menu_principal():
    while True:
        limpar_tela()
        print("_______________________________________")
        print("_______     Sistema de Gestão de Loja        _______")
        print("_______________________________________")
        print("____   1 - Módulo Cliente             _____")
        print("_____  2 - Módulo Vendedor            _____")
        print("_____  3 - Módulo Produto/Vendas      _____")
        print("_____  4 - Módulo Caixa               _____")
        print("_____  5 - Módulo Carrinho                   _____")
        print("_____  5 - Módulo Administração                  _____")
        print("_____  0 - Sair                       _____")
        resp = input("##### Escolha sua opção: ")
        
        if resp == "1":
            modulo_cliente()
        elif resp == "2":
            modulo_vendedor()
        elif resp == "3":
            modulo_produto_vendas()
        elif resp == "4":
            modulo_caixa()
        elif resp == "5":
            modulo_carrinho()
        elif resp == "0":
            break

if __name__ == "__main__":
    menu_principal()
