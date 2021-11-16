while True:
    cpf = input('Seu cpf (sem [.] e [-]) = ')
    if not cpf.isnumeric():
        print('só número seu retardado')
        print()
        continue
    if cpf.isnumeric():
        cpf_L = list(map(int, cpf))
        if (len(cpf_L)) == 11:
            break

        if (len(cpf_L)) < 11 or (len(cpf_L)) > 11:
            print("você digitou seu cpf errado")
        print()

cpf_L = list(map(int, cpf))
digito1 = (cpf_L[0] * 10 + cpf_L[1] * 9 +
cpf_L[2] * 8 + cpf_L[3] * 7 +
cpf_L[4] * 6 + cpf_L[5] * 5 +
cpf_L[6] * 4 + cpf_L[7] * 3 +
cpf_L[8] * 2
)
digito1 = 11 - (digito1 % 11)

digito2=(cpf_L[0]*11 +cpf_L[1]*10 +
cpf_L[2]*9 +cpf_L[3]*8 +cpf_L[4]*7 +
cpf_L[5]*6 +cpf_L[6]*5 +cpf_L[7]*4 +
cpf_L[8]*3 +cpf_L[9]*2
)
digito2 = 11 - (digito2 % 11)

if digito1 > 9:
    digito1 = 0
if digito2 > 9:
    digito2 = 0

digito1 = str(digito1)
digito2 = str(digito2)
digito = digito1 + digito2

if digito == str(cpf_L[9])+str(cpf_L[10]):
    print('Seu cpf é válido')
else:
    print('seu cpf é inválido')
print(cpf_L[0],cpf_L[1],cpf_L[2],'.',cpf_L[3],cpf_L[4],cpf_L[5],'.',cpf_L[6],cpf_L[7],cpf_L[8],'-',digito)
