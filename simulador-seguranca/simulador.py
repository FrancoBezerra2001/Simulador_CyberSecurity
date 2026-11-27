
from datetime import datetime
import time

# ==========================================
# SIMULADOR EDUCACIONAL DE SEGURANÇA
# ==========================================

USUARIO_TESTE = "aluno"
SENHA_TESTE = "sol123"

# Lista fictícia de senhas para o laboratório local
WORDLIST_TESTE = [
    "123456",
    "admin",
    "senha",
    "abc123",
    "sol123"
]

LIMITE_TENTATIVAS = 3


def registrar_log(mensagem):
    """Registra eventos em um arquivo de log."""
    horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open("logs.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"[{horario}] {mensagem}\n")


def simular_login_vulneravel():
    """Simula login sem limite de tentativas."""

    print("\n=== SISTEMA VULNERÁVEL ===")
    print("Limite de tentativas: inexistente\n")

    for numero, senha in enumerate(WORDLIST_TESTE, start=1):

        print(f"Tentativa {numero}: testando senha '{senha}'...")
        time.sleep(0.5)

        if senha == SENHA_TESTE:
            print("\n[SUCESSO] Senha encontrada!")
            print(f"Usuário: {USUARIO_TESTE}")
            print(f"Senha de demonstração: {senha}")

            registrar_log(
                f"SIMULACAO VULNERAVEL: "
                f"senha de teste encontrada na tentativa {numero}"
            )
            return

        print("[ERRO] Senha incorreta.")
        registrar_log(
            f"SIMULACAO VULNERAVEL: tentativa {numero} incorreta"
        )

    print("\nSenha não encontrada.")
    registrar_log("SIMULACAO VULNERAVEL: senha não encontrada")


def simular_login_protegido():
    """Simula login com limite de tentativas."""

    print("\n=== SISTEMA PROTEGIDO ===")
    print(f"Limite de tentativas: {LIMITE_TENTATIVAS}\n")

    tentativas = 0

    for senha in WORDLIST_TESTE:

        if tentativas >= LIMITE_TENTATIVAS:
            print("\n[BLOQUEIO] Limite de tentativas atingido!")
            print("Login temporariamente bloqueado.")

            registrar_log(
                "SIMULACAO PROTEGIDA: "
                "bloqueio após limite de tentativas"
            )
            return

        tentativas += 1

        print(f"Tentativa {tentativas}: testando senha...")
        time.sleep(0.5)

        if senha == SENHA_TESTE:
            print("\n[SUCESSO] Login autorizado!")

            registrar_log(
                "SIMULACAO PROTEGIDA: "
                "login autorizado"
            )
            return

        print("[ERRO] Senha incorreta.")

        registrar_log(
            f"SIMULACAO PROTEGIDA: "
            f"tentativa {tentativas} incorreta"
        )

    print("\nSimulação encerrada.")


def mostrar_menu():
    """Exibe as opções do programa."""

    while True:

        print("\n" + "=" * 40)
        print(" SIMULADOR DE SEGURANÇA DE SENHAS")
        print("=" * 40)

        print("1 - Simular sistema vulnerável")
        print("2 - Simular sistema protegido")
        print("3 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            simular_login_vulneravel()

        elif opcao == "2":
            simular_login_protegido()

        elif opcao == "3":
            print("\nEncerrando o programa.")
            break

        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    mostrar_menu()
