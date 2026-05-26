import random
import sql_insert
from validacoes import validacaoTitulo, verificacaoCPF


def cadastrar_eleitor():
    """
    Realiza o cadastro de um eleitor.
    """

    continuar = "s"

    while continuar == "s":

        nome = input("Digite o nome completo: ")

        # validar nome (tem espaço = nome completo)
        if " " not in nome:
            print("Nome inválido\n")
            continue

        cpf_digitado = input("Digite o CPF: ")

        # limpar CPF (deixar só números)
        cpf = ""
        for c in cpf_digitado:
            if c.isdigit():
                cpf += c

        if not verificacaoCPF(cpf):
            print("CPF inválido\n")
            continue
        if sql_insert.verificar_cpf_banco(cpf):
            print("cpf já cadastrado\n")
            continue

        titulo = input("Digite o título: ")

        if not validacaoTitulo(titulo):
            print("Título inválido\n")
            continue

        if sql_insert.verificar_titulo_eleitor(titulo):
            print("Título já cadastrado\n")
            continue

        # mesário (True ou False)
        resposta = input("Mesário? (s/n): ").lower()
        mesario = True if resposta == "s" else False

        # gerar chave simples
        primeira_letra = nome[0].upper()
        segunda_letra = nome[1].upper()
        letra_sobrenome = nome[nome.find(" ") + 1].upper()

        numero = random.randint(1000, 9999)

        chave = primeira_letra + segunda_letra + letra_sobrenome + str(numero)

        # cadastrar no banco
        sql_insert.inserir_eleitor(nome, cpf, titulo, mesario, chave)

        print(f"\nChave gerada: {chave}")

        continuar = "n"

def editar_eleitor():
    """
    Edita os dados de um eleitor.
    """

    cpf = input("Digite o CPF do eleitor: ")
    novo_nome = input("Digite o novo nome: ")
    novo_titulo = input("Digite o novo título: ")

    # Validação do nome
    if " " not in novo_nome:
        print("❌ Nome inválido")
        return

    # Validação do título
    if not validacaoTitulo(novo_titulo):
        print("❌ Título inválido")
        return

    # Atualização no banco
    sql_insert.editar_eleitor(cpf, novo_nome, novo_titulo)

    print("✅ Eleitor atualizado com sucesso!")
    
def cadastrar_candidato():

    nome = input("Nome do candidato: ")

    numero = input("Número do candidato: ")

    partido = input("Partido: ")

    sql_insert.inserir_candidato(
        nome,
        numero,
        partido
    )
def buscar_candidato():

    numero = input(
        "Número do candidato: "
    )

    sql_insert.buscar_candidato(numero)
def remover_candidato():

    numero = input(
        "Número do candidato: "
    )

    sql_insert.remover_candidato(numero)
def editar_candidato():

    numero = input(
        "Número do candidato: "
    )

    novo_nome = input(
        "Novo nome: "
    )

    novo_partido = input(
        "Novo partido: "
    )

    sql_insert.editar_candidato(
        numero,
        novo_nome,
        novo_partido
    )