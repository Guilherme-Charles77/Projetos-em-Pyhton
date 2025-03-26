
def logistica(lista_produtos):
    produto_barato = {"id_produto": None, "nome": None, "valor": float('inf')}
    produto_maiores = []
    total_gasto = 0

    for produto in lista_produtos:

        total_gasto += produto["valor"]

        if produto["valor"] < produto_barato["valor"]:
            produto_barato = produto

        if produto["valor"] > 1000:
            produto_maiores.append(produto)

    return produto_barato, produto_maiores, total_gasto


def main():
    lista_produtos = []


    while True:

        print("="*90)
        print("                                      LOJA VAREJÃO")
        print("="*90)
        
        print(" === Cadastrar nova compra ===")

        nome = input("Digite o nome do produto: ")
        valor = float(input("Digite o valor do produto: "))
        id_compra = len(lista_produtos)+1

        lista_produtos.append({"id": id_compra, "nome":nome, "valor":valor })
        logistica(lista_produtos)
        opcao = input(" Deseja continuar? (S/N)").strip().upper()
        if opcao != "S":

            produto_barato, produto_maiores, total_gasto = logistica(lista_produtos)
           

            print("Produtos que ultrapassam 1000$: ")
            for produto in produto_maiores:
                print(f" - {produto}")
            
            print(f"Produto mais barato: {produto_barato}")
            print(f"Total Gasto: {total_gasto:.2f}")


            
            
            print("\nObrigado por dar preferência a nossa loja")
            break

if __name__ == "__main__":
    main()
