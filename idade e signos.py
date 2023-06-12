print('Idade e Signos - Python')
def qualseu_signo(dia, mes):
    if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "aquário"
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        return "peixes"
    elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "áries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "touro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "gêmeos"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "câncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "leão"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "virgem"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "escorpião"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "sagitário"
    else:
        return "capricórnio"

dia = int(input("Digite o dia do seu nascimento: "))
mes = int(input("Digite o mês do seu nascimento: "))
ano = int(input("Digite o ano do seu nascimento: "))

signo = qualseu_signo(dia, mes)
idade = (2023 -ano)

print('Você tem',idade,'anos e seu signo é', signo)
input("Pressione Enter para sair da tela ...")
