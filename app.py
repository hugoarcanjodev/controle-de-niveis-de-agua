from colorama import Fore, Style

mensagens_do_reservatorio = ["Muito baixo (crítico)", "Baixo","Médio","Alto","Muito alto (alerta)"]

def exibir_status(nivel_indice):
    if nivel_indice == 0:
        cor = Fore.RED
    elif nivel_indice == 1:
        cor = Fore.YELLOW
    elif nivel_indice == 2:
        cor = Fore.GREEN
    elif nivel_indice == 3:
        cor = Fore.CYAN
    elif nivel_indice == 4:
        cor = Fore.BLUE
    else:
        print("Valor de nível de índice inválido")
        return

    mensagem = mensagens_do_reservatorio[nivel_indice]
    print(f"Status do nível de água do Reservatório: {cor}{mensagem}{Style.RESET_ALL}")

print("----------------- CONTROLE DE NÍVEIS DE ÁGUA -----------------")

for i in range(len(mensagens_do_reservatorio)):
    exibir_status(i)

print(Style.RESET_ALL + "------------------ MONITORAMENTO FINALIZADO ------------------")