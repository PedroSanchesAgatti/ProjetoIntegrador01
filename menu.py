import mysql.connector
from mysql.connector import Error

# 1. Configuração Única da Conexão (Centralizada)
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '@@PHSAg3474', # Usando a senha que você forneceu no dump
    'database': 'pis'
}

try:
    conexao = mysql.connector.connect(**db_config)
    cursor = conexao.cursor()
except Error as e:
    print(f"ERRO DE CONEXÃO: {e}")
    exit()

def verificacaoCPF(cpf):
    # 1. Verificações Matemáticas (Formato)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    for i in range(9, 11):
        valor = sum(int(cpf[num]) * ((i + 1) - num) for num in range(i))
        digito = ((valor * 10) % 11) % 10
        if digito != int(cpf[i]):
            return False
            
    # 2. Verificação de Disponibilidade (Banco de Dados)
    # Usamos a conexão global já estabelecida
    try:
        query = "SELECT id FROM eleitores WHERE cpf = %s"
        cursor.execute(query, (cpf,))
        resultado = cursor.fetchone()
        
        # Se encontrou resultado, o CPF JÁ ESTÁ cadastrado
        if resultado is not None:
            return "CADASTRADO" 
                
    except Error as e:
        print(f"Erro ao consultar banco: {e}")
        return False 

    # Se chegou aqui, o CPF é válido e NÃO existe no banco
    return True 

inicio = ""
while inicio != "3":
    print(f"\nInício")
    print(f"\n----------------------------Sistema de Votação----------------------------------")
    print("\n1-Votação\n2-gerenciamento\n3-sair\n")
    inicio= input("Escolha a opção desejada:")
    match inicio:
        case "1":
            Votação=""
            while Votação!="4":
                print(f"\n----------------------------Votação---------------------------------------------")
                print("\n1-Auditoria\n2-Abrir sistema de votação\n3-Resultados\n4-Voltar\n")
                Votação=input("Escolha a opção desejada:")
                match Votação:
                    case "1":
                        Auditoria=""
                        while Auditoria!="3":
                            print(f"\n----------------------------Auditoria-------------------------------------------")
                            print("\n1-Protocolos de votação\n2-Logs de ocorrência\n3-Voltar\n")
                            Auditoria=input("Escolha a opção desejada:")
                            match Auditoria:
                                case "1":
                                    pass
                                case "2":
                                    pass
                                case "3":
                                    print("Voltando...\n")
                                case _:
                                    print("Opção inválida\n")
                    case "2":
                        Abrir_sistema=""
                        while Abrir_sistema!="3":
                            print(f"\n------------------------------Sistema de Votação--------------------------------")
                            print("\n1-Votar\n2-Encerrar sistema de votação\n3-Voltar\n")
                            Abrir_sistema=input("Escolha a opção desejada:")      
                            match Abrir_sistema:
                                case "1":
                                    Votar=""
                                    while Votar!="1":
                                        print(f"\n----------------------------Votação---------------------------------------------")
                                        print("\n1-Cancelar voto\n2-Confirmar voto\n")
                                        Votar=input("Escolha a opção desejada:")
                                        match Votar:
                                            case "1":
                                                print("Voto cancelado\n")
                                            case "2":
                                                print("Voto confirmado\n")
                                                Votar="1"
                                                Abrir_sistema="3"
                                            case _:
                                                print("Opção inválida\n")
                                case "2":
                                    Encerrar="1"
                                    while Encerrar=="1":
                                        print(f"\n----------------------------Encerrar Votação------------------------------------")
                                        print("\n1-Não encerrar\n2-Encerrar\n3-Voltar\n")
                                        Encerrar=input("Escolha a opção desejada:")
                                        match Encerrar:
                                            case "1" :
                                                print("Sistema de votação não encerrado\n")
                                            case "2":
                                                print("Encerrando sistema de votação...\n")
                                                Abrir_sistema=3  
                                            case "3":
                                                print("Voltando...\n")      
                                            case _:
                                                print("Opção inválida\n")                  
                                case "3":
                                    print("Voltando...\n")
                                case _:
                                    print("Opção inválida\n")                    
                    case "3":
                        Resultados=""
                        while Resultados!="5":
                            print(f"\n----------------------------Resultados------------------------------------------")
                            print("\n1-Boletim de urna\n2-Estatística de comparecimento\n3-Validação de integridade\n4-Votos por partido\n5-Voltar\n")
                            Resultados=input("Escolha a opção desejada:")
                            match Resultados:
                                case "1":
                                    pass
                                case "2":
                                    pass
                                case "3":
                                    pass
                                case "4":
                                    pass
                                case "5":
                                    print("Voltando...\n")
                                case _:
                                    print("Opção inválida\n")
                    case "4":
                       print("Voltando...")
                    case _:
                        print("Opção inválida\n")
        case "2":
            Gerenciamento=""
            while Gerenciamento!="3":
                print(f"\n----------------------------Gerenciamento---------------------------------------")
                print("\n1-Eleitores\n2-Candidatos\n3-Voltar\n")
                Gerenciamento=input("Escolha a opção desejada:")
                match Gerenciamento:
                    case "1":
                        Eleitores=""
                        while Eleitores!="6":
                            print(f"\n----------------------------Eleitores-------------------------------------------")
                            print("\n1-Remoção de eleitores\n2-Buscar eleitores\n3-Listagen de eleitores\n4-Editar dados de eleitores\n5-Cadastrar eleitores\n6-Voltar\n")
                            Eleitores=input("Escolha a opção desejada:")
                            match Eleitores:
                                case "1":
                                    pass
                                case "2":
                                    pass
                                case "3":
                                    pass
                                case "4":
                                    pass
                                case "5":
                                    cpf_digitado = input("Digite o CPF apenas números: ")
                                    cpf_limpo = ""
                                    for char in cpf_digitado:
                                        if char.isdigit():
                                            cpf_limpo = cpf_limpo + char
                        
                                    status_cpf = verificacaoCPF(cpf_limpo)
                                    
                                    if status_cpf == True:
                                        print(f"O CPF {cpf_digitado} é VÁLIDO e disponível para cadastro.")
                                    elif status_cpf == "CADASTRADO":
                                        print(f"ERRO: O CPF {cpf_digitado} já está cadastrado no sistema.")
                                    else:
                                        print(f"ERRO: O CPF {cpf_digitado} é INVÁLIDO.")

                                case "6":
                                    print("Voltando...\n")
                                case _:
                                    print("Opção inválida\n")
                    case "2":
                        Candidatos=""
                        while Candidatos!="6":
                            print(f"\n----------------------------Candidatos------------------------------------------")
                            print("\n1-Buscar candidato\n2-Cadastro de candidatos\n3-Editar dados de candidatos\n4-Remover candidato\n5-Listar candidatos\n6-Voltar\n")
                            Candidatos=input("Escolha a opção desejada:")
                            match Candidatos:
                                case "1":
                                    pass
                                case "2":
                                    pass
                                case "3":
                                    pass
                                case "4":
                                    pass
                                case "5":
                                    pass
                                case "6":
                                    print("Voltando...")
                                case _:
                                    print("Opção inválida\n")
                    case "3":
                        print("Voltando...\n")
                    case _:
                        print("Opção inválida\n")
        case "3":
            print("Saindo...")
        case _:
            print("Opção inválida\n")

# Fechar conexão ao sair
if 'conexao' in locals() and conexao.is_connected():
    cursor.close()
    conexao.close()