
setor = input("Digite o setor do funcionário: (financeiro, rh, tecnologia, gerente:  ").lower()
turno = input("Digite o turno de trabalho (manhã/tarde/noite): ").lower()

setores_permitidos = ["financeiro", "rh", "tecnologia"]

if setor == "gerente":
    if turno in ("tarde", "noite"):
        print("Acesso permitido ao sistema")
    else:
        print("Acesso negado ao sistema")
elif setor in setores_permitidos:
    if turno == "noite":
        print("Acesso negado ao sistema. ")
    else:
        print("Acesso permitido ao sistema. ")
else:
    print("Acesso negado ao sistema. ")