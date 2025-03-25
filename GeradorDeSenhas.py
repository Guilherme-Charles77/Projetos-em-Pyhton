"""
=============================================================================
            O programa terá as seguintes funcionalidades:

        1. Gerar senhas aleatórias.
        2. Permitir ao usuário escolher:
            - O comprimento da senha.
            - Se deve incluir letras maiúsculas, minúsculas, números e símbolos.
        3. Salvar as senhas geradas em um arquivo para referência futura.
=============================================================================

"""
import random
import string



def exibir_menu():
    print("=============================================================================")
    print("              ===  GERADOR DE SENHAS  ===\n")
    print("                 1. Gerar Nova Senha.")
    print("                 2. Salvar Senha.")
    print("                 3. Sair.")
    print("=============================================================================")


def gerar_senha(comprimento, in_maiusculas, in_numeros, in_simbolos):
    caracteres = string.ascii_lowercase #Definido letras minusculas por padrão

    if in_maiusculas: caracteres += string.ascii_uppercase
    if in_numeros: caracteres += string.digits
    if in_simbolos: caracteres+= string.punctuation

    senha = ''.join(random.choice(caracteres) for i in range (comprimento))
    return senha


def salvar_senha(nome_servico, senha):
    with open("Salvar_Senhas.txt", "a") as arquivo:
        arquivo.write(f"{nome_servico}: {senha}\n", )
        print("Senha salva com sucesso!")

def main():
    while True:
        exibir_menu()

        opcao = input("\nDigite a Opção Desejada: ") 
        if opcao == "1":
            comprimento = int(input("\nQual o comprimento que deseja? "))
            in_maiusculas = input("Deseja incluir maiuscula? (s/n)").lower == "s"
            in_numeros = input("Deseja inlcuir numeros? (s/n)").lower == "s"
            in_simbolos = input("Deseja incluir simbolos? (s/n)").lower == "s"

            gerar_senha(comprimento, in_maiusculas, in_numeros, in_simbolos)
            senha = gerar_senha(comprimento, in_maiusculas, in_numeros, in_simbolos)
            print(f"Senha Gerada = {senha}")
        elif opcao == "2":
            if senha:
                nome_servico = input("Digite o nome do serviço: \n")
                salvar_senha(nome_servico, senha)
            else: print("Nenhuma senha para salvar.")
     
        elif opcao == "3":
           print("Saindo do Programa...")
           break
        else:
           print("Opção Inválida. \nTente Novamente!")

    

if __name__=="__main__":
    main()
