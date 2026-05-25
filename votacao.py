import random
import sql_insert
from criptografia import *

def abrir():

    if sql_insert.votacao_esta_aberta():
        print("\nA votação já está aberta!\n")
        return

    titulo_mesario = input("Digite o título do mesário: ")
    cpf_mesario = input("Digite os 4 primeiros dígitos do CPF do mesário: ")
    chave_mesario = input("Digite a chave de acesso do mesário: ")

    autorizado = sql_insert.verificacao_mesario(
        titulo_mesario,
        cpf_mesario,
        chave_mesario
    )

    if autorizado:

        sql_insert.abrir_votacao()

        print("\n✅ Votação aberta com sucesso!\n")

        sql_insert.registrar_log(
            "ABERTURA: Votação aberta com sucesso."
        )

    else:

        print("\n❌ Credenciais inválidas.\n")

        sql_insert.registrar_log(
            "ABERTURA: Tentativa inválida."
        )
    
def votar():
    """
    Realiza o processo de votação do eleitor.
    """

    if not sql_insert.votacao_esta_aberta():
        print("\n❌ A votação está fechada.\n")
        return

    titulo = input("Digite o título do eleitor: ").upper().strip()
    cpf = input("Digite os 4 primeiros dígitos do CPF: ").upper().strip()
    chave = input("Digite a chave de acesso: ").upper().strip()

    
    titulo = titulo.replace(".", "").replace("-", "")
    cpf = cpf.replace(".", "").replace("-", "")

    resultado = sql_insert.verificao_votacao(titulo, cpf, chave)

    if resultado is None:
        print("\n❌ Dados inválidos.\n")
        sql_insert.registrar_log("ALERTA: Tentativa de acesso negado.")
        return

    id_eleitor, status = resultado

    if status == 1:
        print("\n❌ Eleitor já votou.\n")
        sql_insert.registrar_log("ALERTA: Tentativa de voto duplo.")
        return

    confirmado = False

    while not confirmado:

        numero = input("\nDigite o número do candidato: ")

        candidato = sql_insert.buscar_candidato(numero)

        
        # VOTO NULO
        if candidato is None:

            print("\n⚠️ Número inexistente.")
            print("O voto será NULO.")

            confirmar = input("\nConfirmar voto nulo? (s/n): ").lower()

            if confirmar == "s":
                id_candidato = None
                nome = "NULO"
                partido = "-"
                confirmado = True
            else:
                print("\nDigite novamente.\n")

        else:

            id_candidato, nome, numero_candidato, partido = candidato

            print("\n=========== CONFIRMAÇÃO ===========")
            print(f"Nome: {nome}")
            print(f"Número: {numero}")
            print(f"Partido: {partido}")

            confirmar = input("\nConfirmar voto? (s/n): ").lower()

            if confirmar == "s":
                confirmado = True
            else:
                print("\nDigite novamente.\n")

    # gerar protocolo
    protocolo = random.randint(100000, 999999)
    protocolo_str = str(protocolo)

    # registrar voto
    protocolo_criptografada = criptografia(protocolo_str)
    sql_insert.registrar_voto(id_eleitor, id_candidato, protocolo_criptografada)

    print("\n✅ Voto confirmado!")
    print(f"Candidato: {nome} ({numero} - {partido})")
    print(f"Protocolo: {protocolo}\n")

def encerrar():

    if not sql_insert.votacao_esta_aberta():

        print("\nA votação já está encerrada.\n")
        return

    confirmar = input(
        "\nDeseja realmente encerrar? (s/n): "
    ).lower()

    if confirmar != "s":

        print("\nEncerramento cancelado.\n")
        return

    titulo_mesario = input("Digite o título do mesário: ")
    cpf_mesario = input("Digite os 4 primeiros dígitos do CPF: ")
    chave_mesario = input("Digite a chave de acesso: ")

    if sql_insert.verificacao_mesario(
        titulo_mesario,
        cpf_mesario,
        chave_mesario
    ):

        chave_confirmacao = input(
            "\nDigite novamente a chave para confirmar: "
        )

        if chave_confirmacao != chave_mesario:

            print("\n❌ Chave de confirmação incorreta.\n")

            sql_insert.registrar_log(
                "ALERTA: Tentativa inválida de encerramento."
            )

            return

        sql_insert.encerrar_votacao()

        print("\n✅ Votação encerrada.\n")

    else:

        print("\n❌ Credenciais inválidas.\n")

        sql_insert.registrar_log(
            "ALERTA: Tentativa de acesso negado."
        )