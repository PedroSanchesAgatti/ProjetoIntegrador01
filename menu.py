import sql_insert 
from menus import *
from votacao import *
from gerenciamento import *
from validacoes import *
import mysql.connector
import os
import datetime

inicio = ""
while inicio != "3":
    menu_principal()
    inicio= input("Escolha a opção desejada:")
    match inicio:
        case "1":
            Votação=""
            while Votação!="4":
                menu_votacao()
                Votação=input("Escolha a opção desejada:")
                match Votação:
                    case "1":
                        Auditoria=""
                        while Auditoria!="3":
                            menu_auditoria()
                            Auditoria=input("Escolha a opção desejada:")
                            match Auditoria:
                                case "1":
                                    sql_insert.exibir_protocolos()
                                case "2":
                                    sql_insert.exibir_logs()
                                case "3":
                                    print("Voltando...\n")
                                case _:
                                    print("Opção inválida\n")
                    case "2":
                        Abrir_sistema=""
                        abrir()
                        while Abrir_sistema!="4":
                                menu_sistema_votacao()
                                Abrir_sistema = input("Escolha a opção desejada:")
                                match Abrir_sistema:
                                    case "1":
                                        abrir()
                                    case "2":
                                        votar()
                                    case "3":
                                        encerrar()
                                    case "4":
                                        print("Voltando...\n")
                                    case _:
                                        print("Opção inválida\n")              
                    case "3":
                        Resultados=""
                        while Resultados!="5":
                            menu_resultados()
                            Resultados=input("Escolha a opção desejada:")
                            match Resultados:
                                case "1":
                                    sql_insert.boletim_urna()
                                case "2":
                                    sql_insert.estatistica_comparecimento()
                                case "3":
                                    sql_insert.validar_integridade()
                                case "4":
                                    sql_insert.votos_partido()
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
                menu_gerenciamento()
                Gerenciamento=input("Escolha a opção desejada:")
                match Gerenciamento:
                    case "1":
                        Eleitores=""
                        while Eleitores!="6":
                            menu_eleitores()
                            Eleitores=input("Escolha a opção desejada:")
                            match Eleitores:
                                case "1":
                                    sql_insert.excluir_eleitor(input("Digite o CPF ou o Título de eleitor: "))
                                case "2":
                                    valor = input("Digite o título ou CPF do eleitor para busca: ")
                                    sql_insert.buscar_eleitor(valor)
                                case "3":
                                    sql_insert.listar_eleitores()
                                case "4":
                                    editar_eleitor()
                                case "5":
                                    cadastrar_eleitor()
                                case "6":
                                    print("Voltando...\n")
                                case _:
                                    print("Opção inválida\n")
                    case "2":
                        Candidatos=""
                        while Candidatos!="6":
                            menu_candidatos()
                            Candidatos=input("Escolha a opção desejada:")
                            match Candidatos:
                                case "1":
                                    buscar_candidato()
                                case "2":
                                    cadastrar_candidato()
                                case "3":
                                    editar_candidato()
                                case "4":

                                    sql_insert.remover_candidato(int(input("\nDigite o número do candidato: ")))

                                case "5":
                                    sql_insert.listar_candidatos()
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

sql_insert.fechar_conexao()
