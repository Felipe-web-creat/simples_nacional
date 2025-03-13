menu = '''

SELECIONE

[1] ANEXO I
[2] ANEXO II
[3] ANEXO III
[4] ANEXO IV
[5] ANEXO V
[Q] SAIR

=>'''



while True:
    opcao = input(menu)

    if opcao == "1":
        receita_rpa = float(input("Receita RPA: "))
        devolucao = float(input("Devolução PA: "))
        rbt_12 = float(input("Receita Bruta dos Últimos 12 meses (RBT12): "))
        if rbt_12 <= 180000.00:
            apuracao_1 = float((receita_rpa - devolucao)* 0.0265)
            print("\n============= VALOR APURADO ANEXO III ===============\n")
            print (f"Valor apurado: R$ {apuracao_1:.2f}\n")
            print("=====================================================\n")

    elif opcao == "Q":
        break
    else:
        print("Opção incorreta!")