# Definição da lista de produtos
produtos = [
    {'id': 1, 'nome': 'Coca-cola', 'preco': 10.0},
    {'id': 2, 'nome': 'Feijão', 'preco': 8.0},
    {'id': 3, 'nome': 'Arroz', 'preco': 20.0},
    {'id': 4, 'nome': 'Azeite', 'preco': 15.0},
    {'id': 5, 'nome': 'Sal', 'preco': 2.0}
]

# Carrinho de compras
carrinho = {}

# Função para listar produtos
def listar_produtos():
    print("\nProdutos disponíveis:")
    for produto in produtos:
        print(f"ID: {produto['id']} - Nome: {produto['nome']} - Preço: R${produto['preco']:.2f}")

# Função para adicionar produto ao carrinho
def adicionar_ao_carrinho(id_produto, quantidade):
    produto = next((p for p in produtos if p['id'] == id_produto), None)
    if produto:
        if id_produto not in carrinho:
            carrinho[id_produto] = quantidade
        else:
            carrinho[id_produto] += quantidade
        print(f"\nProduto '{produto['nome']}' adicionado ao carrinho. Quantidade: {quantidade}")
    else:
        print("\nProduto não encontrado.")

# Função para visualizar o carrinho
def visualizar_carrinho():
    if not carrinho:
        print("\nCarrinho está vazio.")
        return
    print("\nCarrinho de Compras:")
    total = 0
    for id_produto, quantidade in carrinho.items():
        produto = next((p for p in produtos if p['id'] == id_produto), None)
        if produto:
            subtotal = produto['preco'] * quantidade
            total += subtotal
            print(f"Produto: {produto['nome']} - Quantidade: {quantidade} - Subtotal: R${subtotal:.2f}")
    print(f"Valor total: R${total:.2f}")

# Função para finalizar a compra
def finalizar_compra():
    if not carrinho:
        print("\nCarrinho está vazio. Não há compra a finalizar.")
        return
    print("\nFinalizando a compra...")
    visualizar_carrinho()
    carrinho.clear()
    print("Compra finalizada com sucesso. Obrigado!")

# Interface interativa
def interface_interativa():
    while True:
        print("\nEscolha uma opção:")
        print("1. Listar produtos")
        print("2. Adicionar produto ao carrinho")
        print("3. Visualizar carrinho")
        print("4. Finalizar compra")
        print("5. Sair")
        opcao = input("Opção: ")

        if opcao == '1':
            listar_produtos()
        elif opcao == '2':
            try:
                id_produto = int(input("Digite o ID do produto: "))
                quantidade = int(input("Digite a quantidade: "))
                adicionar_ao_carrinho(id_produto, quantidade)
            except ValueError:
                print("\nEntrada inválida. Tente novamente.")
        elif opcao == '3':
            visualizar_carrinho()
        elif opcao == '4':
            finalizar_compra()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

# Iniciar a interface interativa
interface_interativa()
