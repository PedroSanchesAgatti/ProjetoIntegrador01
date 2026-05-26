import mysql.connector
import datetime
import os
from criptografia import *

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='senha',
    database='database'
)

cursor = conexao.cursor()

# =========================
# CANDIDATOS
# =========================

def inserir_candidato():
    continuar = "s"

    while continuar== "s":
        print("\n=== CADASTRO DE CANDIDATO ===")

        nome=input("Nome: ")
        numero=input("Número: ")
        partido=input("Partido: ")

        sql="INSERT INTO candidatos (nome, numero, partido) VALUES (%s, %s, %s)"
        valores=(nome, numero, partido)
        cursor.execute(sql, valores)
        conexao.commit()

        print("\nCandidato cadastrado com sucesso!")
        continuar=input("\nCadastrar outro candidato? (s/n): ").lower()



def buscar_candidato(numero):

    sql = """
    SELECT id, nome, numero, partido
    FROM candidatos
    WHERE numero = %s
    """

    cursor.execute(sql, (numero,))

    resultado = cursor.fetchone()

    if resultado:

        id, nome, numero, partido = resultado

        print(
            f"ID: {id} | "
            f"Nome: {nome} | "
            f"Número: {numero} | "
            f"Partido: {partido}"
        )
        return resultado

    else:

        print("Candidato não encontrado.")
        return resultado

def remover_candidato(numero):

    sql = """
    DELETE FROM candidatos
    WHERE numero = %s
    """

    cursor.execute(sql, (numero,))

    conexao.commit()

    if cursor.rowcount > 0:

        print("Candidato removido.")

    else:

        print("Candidato não encontrado.")   

def editar_candidato(
    numero,
    novo_nome,
    novo_partido
):

    sql = """
    UPDATE candidatos
    SET nome = %s,
        partido = %s
    WHERE numero = %s
    """

    valores = (
        novo_nome,
        novo_partido,
        numero
    )

    cursor.execute(sql, valores)

    conexao.commit()

    if cursor.rowcount > 0:

        print("Candidato atualizado.")

    else:

        print("Candidato não encontrado.") 

def listar_candidatos():
    cursor.execute("SELECT id, nome, numero, partido FROM candidatos")
    
    for (id, nome, numero, partido) in cursor.fetchall():
        print(f"ID: {id} | Nome: {nome} | Numero: {numero} | Partido: {partido}")



# =========================
# ELEITORES
# =========================


def inserir_eleitor(nome, cpf, titulo, mesario, chave_acesso):
    chave_criptografada = criptografia(chave_acesso)
    cpf_criptografada = criptografia(cpf)
    titulo_criptografada = criptografia(titulo)
    sql = """
    INSERT INTO eleitores 
    (nome, cpf, titulo, mesario, chave_acesso) 
    VALUES (%s, %s, %s, %s, %s)
    """
    
    valores = (nome, cpf_criptografada, titulo_criptografada, mesario, chave_criptografada)
    cursor.execute(sql, valores)
    conexao.commit()
    
    print("Eleitor cadastrado com sucesso!")

def buscar_eleitor(valor):
    valor_criptografada = criptografia(valor)
    sql = """
    SELECT id, nome, cpf, titulo, status_voto , mesario
    FROM eleitores
    WHERE titulo = %s OR cpf = %s
    """
    
    cursor.execute(sql, (valor_criptografada, valor_criptografada))
    resultado = cursor.fetchall()
    
    if resultado:
        for id, nome, cpf, titulo, status, mesario in resultado:
            cpf_criptografada = descriptografia(cpf)
            titulo_criptografada = descriptografia(titulo)
            print(f"ID: {id} | Nome: {nome} | CPF: {cpf_criptografada} | Titulo: {titulo_criptografada} | Votou: {"Sim" if status == 1 else "Não"} | Mesário: {"Sim" if mesario == 1 else "Não"}")
    else:
        print("Nenhum eleitor encontrado.")

def listar_eleitores():
    cursor.execute("SELECT id, nome, cpf, titulo, status_voto, mesario FROM eleitores")
    
    for (id, nome, cpf, titulo, status, mesario) in cursor.fetchall():
        cpf_criptografada = descriptografia(cpf)
        titulo_criptografada = descriptografia(titulo)
        print(f"ID: {id} | Nome: {nome} | CPF: {cpf_criptografada} | Titulo: {titulo_criptografada} | Votou: {"Sim" if status == 1 else "Não"} | Mesário: {"Sim" if mesario == 1 else "Não"}")
        
def excluir_eleitor(valor):
    sql = """
    DELETE FROM eleitores
    WHERE cpf = %s OR titulo = %s
    """
    valor_criptografada = criptografia(valor)
    cursor.execute(sql, (valor_criptografada, valor_criptografada))

    if cursor.rowcount > 0:
        conexao.commit()
        print("\nEleitor deletado com sucesso!")
    else:
        print("\nNenhum eleitor encontrado.")

def verificar_titulo_eleitor(titulo):
    sql = """
    SELECT COUNT(*) FROM eleitores
    WHERE titulo = %s
    """
    titulo_criptografada = criptografia(titulo)
    cursor.execute(sql, (titulo_criptografada,))
    resultado = cursor.fetchone()[0]
    return resultado > 0

def editar_eleitor(
    cpf,
    novo_nome,
    novo_titulo
):
    cpf_criptografada = criptografia(cpf)
    titulo_criptografada = criptografia(novo_titulo)
    sql = """
    UPDATE eleitores
    SET nome = %s,
        titulo = %s
    WHERE cpf = %s
    """

    valores = (
        novo_nome,
        titulo_criptografada,
        cpf_criptografada
    )

    cursor.execute(sql, valores)

    conexao.commit()

    if cursor.rowcount > 0:

        print("Eleitor atualizado.")

    else:

        print("Eleitor não encontrado.")


# =========================
# RELATÓRIOS
# =========================


def validar_integridade():

    """
    Valida integridade da eleição.

    Compara total de votos
    com total de eleitores
    marcados como já votaram.

    Args:
        None

    Returns:
        None
    """

    cursor.execute("""
        SELECT COUNT(*)
        FROM votos
    """)

    total_votos = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM eleitores
        WHERE status_voto = TRUE
    """)

    total_eleitores = cursor.fetchone()[0]

    print("\n=========== VALIDAÇÃO ===========\n")

    print(f"Votos registrados: {total_votos}")

    print(f"Eleitores que votaram: {total_eleitores}")

    if total_votos == total_eleitores:

        print("\n✅ Integridade válida.")

    else:

        print("\n❌ Inconsistência encontrada.")

def registrar_log(mensagem):
    data_hora = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

    with open("logs_ocorrencias.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{data_hora} {mensagem}\n")

def exibir_logs():
    if not os.path.exists("logs_ocorrencias.txt"):
        print("Nenhum log encontrado.")
        return

    print("\n================ LOGS DE OCORRÊNCIAS ================\n")

    with open("logs_ocorrencias.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())

def exibir_protocolos():
    cursor.execute("""
        SELECT protocolo
        FROM votos
        ORDER BY protocolo ASC
    """)

    resultados = cursor.fetchall()

    print("\n================ PROTOCOLOS DE VOTAÇÃO ================\n")

    if resultados:
        for protocolo in resultados:
            print(protocolo[0])
    else:
        print("Nenhum protocolo encontrado.")

def zerezima():

    """
    Realiza a zerézima da votação.

    Remove votos antigos,
    reseta status dos eleitores
    e exibe candidatos com zero votos.

    Args:
        None

    Returns:
        None
    """

    cursor.execute("""
        DELETE FROM votos
    """)

    cursor.execute("""
        UPDATE eleitores
        SET status_voto = FALSE
    """)

    conexao.commit()

    print("\n=========== ZERÉZIMA ===========\n")

    cursor.execute("""
        SELECT nome, numero, partido
        FROM candidatos
        ORDER BY nome ASC
    """)

    candidatos = cursor.fetchall()

    if candidatos:

        for nome, numero, partido in candidatos:

            print(
                f"Nome: {nome} | "
                f"Número: {numero} | "
                f"Partido: {partido} | "
                f"Votos: 0"
            )

    else:

        print("Nenhum candidato cadastrado.")

    registrar_log(
        "ABERTURA: Zerézima realizada com sucesso."
    )
def boletim_urna():

    """
    Exibe o boletim de urna.

    Lista candidatos em ordem alfabética
    com total de votos e mostra o vencedor.

    Args:
        None

    Returns:
        None
    """

    print("\n=========== BOLETIM DE URNA ===========\n")

    cursor.execute("""
        SELECT 
            c.nome,
            c.numero,
            c.partido,
            COUNT(v.id) AS total_votos
        FROM candidatos c
        LEFT JOIN votos v
            ON c.id = v.id_candidato
        GROUP BY c.id
        ORDER BY c.nome ASC
    """)

    resultados = cursor.fetchall()

    maior = -1
    vencedor = None

    for nome, numero, partido, votos in resultados:

        print(
            f"Nome: {nome} | "
            f"Número: {numero} | "
            f"Partido: {partido} | "
            f"Votos: {votos}"
        )

        if votos > maior:

            maior = votos

            vencedor = (
                nome,
                numero,
                partido,
                votos
            )

    if vencedor:

        print("\n=========== VENCEDOR ===========\n")

        print(
            f"Nome: {vencedor[0]} | "
            f"Número: {vencedor[1]} | "
            f"Partido: {vencedor[2]} | "
            f"Votos: {vencedor[3]}"
        )
def estatistica_comparecimento():

    """
    Exibe estatísticas de comparecimento.

    Mostra quantidade de eleitores
    que votaram e percentual.

    Args:
        None

    Returns:
        None
    """

    cursor.execute("""
        SELECT COUNT(*)
        FROM eleitores
    """)

    total_eleitores = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM eleitores
        WHERE status_voto = TRUE
    """)

    total_votaram = cursor.fetchone()[0]

    if total_eleitores > 0:

        percentual = (
            total_votaram / total_eleitores
        ) * 100

    else:

        percentual = 0

    print("\n=========== COMPARECIMENTO ===========\n")

    print(f"Total de eleitores: {total_eleitores}")

    print(f"Total que votaram: {total_votaram}")

    print(f"Percentual: {percentual:.2f}%")


# =========================
# VOTAÇÃO
# =========================

def abrir_votacao():
    cursor.execute("UPDATE configuracao_votacao SET votacao_aberta = TRUE WHERE id = 1")
    conexao.commit()

    zerezima() 

    registrar_log("ABERTURA: Votação iniciada.")

    print("Votação aberta!")

def encerrar_votacao():
    cursor.execute("UPDATE configuracao_votacao SET votacao_aberta = FALSE WHERE id = 1")
    conexao.commit()

    registrar_log("ENCERRAMENTO: Votação finalizada com sucesso.")

    print("Votação encerrada!")

def votacao_esta_aberta():
    cursor.execute("SELECT votacao_aberta FROM configuracao_votacao WHERE id = 1")
    return cursor.fetchone()[0]

def verificao_votacao(titulo, cpf, chave):
    sql = """
    SELECT id, titulo, cpf, chave_acesso, status_voto
    FROM eleitores
    WHERE chave_acesso = %s
    """
    chave_criptografada = criptografia(chave)

    cursor.execute(sql, (chave_criptografada,))
    resultado = cursor.fetchone()

    if resultado is None:
        return None

    id_eleitor, titulo_db, cpf_db, chave_db, status = resultado
    titulo_db_criptografada = criptografia(titulo)
    cpf_db_criptografada = criptografia(cpf)
    chave_db_criptografada = criptografia(chave)
    if titulo_db == titulo_db_criptografada and cpf_db[:4] == cpf_db_criptografada[:4] and chave_db == chave_db_criptografada:
        return id_eleitor, status
    else:
        return None

def verificacao_mesario(titulo, cpf, chave):
    sql = """
    SELECT titulo ,cpf, chave_acesso, mesario
    FROM eleitores
    WHERE chave_acesso = %s
    """

    cursor.execute(sql, (chave,))
    resultado = cursor.fetchone()

    if resultado is None:
        return False

    titulo_db, cpf_db, chave_db, mesario = resultado
    titulo_db = descriptografia(titulo_db)
    cpf_db = descriptografia(cpf_db)

    return titulo_db == titulo and cpf_db[:4] == cpf and chave_db == chave and mesario == 1

def registrar_voto(id_eleitor, id_candidato, protocolo):
    sql = """
    INSERT INTO votos (id_eleitor, id_candidato, protocolo)
    VALUES (%s, %s, %s)
    """

    valores = (id_eleitor, id_candidato, protocolo)
    cursor.execute(sql, valores)

    cursor.execute("""
        UPDATE eleitores
        SET status_voto = TRUE
        WHERE id = %s
    """, (id_eleitor,))

    conexao.commit()

    registrar_log("SUCESSO: Voto realizado com sucesso.")

    print("Voto registrado!")


def votos_partido():

    """
    Exibe votos agrupados por partido.

    Args:
        None

    Returns:
        None
    """

    print("\n=========== VOTOS POR PARTIDO ===========\n")

    cursor.execute("""
        SELECT
            c.partido,
            COUNT(v.id) AS votos
        FROM candidatos c
        LEFT JOIN votos v
            ON c.id = v.id_candidato
        GROUP BY c.partido
        ORDER BY votos DESC
    """)

    resultados = cursor.fetchall()

    for partido, votos in resultados:

        print(
            f"Partido: {partido} | "
            f"Votos: {votos}"
        )


def listar_votos():
    cursor.execute("""
    SELECT e.nome, c.nome, v.data_hora
    FROM votos v
    LEFT JOIN eleitores e ON v.id_eleitor = e.id
    LEFT JOIN candidatos c ON v.id_candidato = c.id
    """)
    
    for eleitor, candidato, data in cursor.fetchall():
        print(f"Eleitor: {eleitor} | Candidato: {candidato} | Data: {data}")

# =========================
# FINALIZAÇÃO
# =========================

def fechar_conexao():
    cursor.close()
    conexao.close()
