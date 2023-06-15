salariu = 2
# nivel_salariu = "Salariu este ok"
# nivel_salariu = None
# if salariu > 4:
#     nivel_salariu = "Salariul este mic"
# elif salariu > 2:
#     nivel_salariu = "Salariul este 2"
# else:
#     nivel_salariu = "Salariu este ok"
# nivel_salariu = "Salariul este mic" if salariu > 4 else "Salariu este ok"
nivel_salariu = "Salariu este ok"
if (salariu_net := salariu + 2) and salariu_net > 4:
    print(salariu_net)
elif (salariu_net := salariu + 3) and salariu_net > 3:
    print(salariu_net)
print(salariu_net)
# print(nivel_salariu)
