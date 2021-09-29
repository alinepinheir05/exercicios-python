variavel = ['Aline', 'Tiago', 'Leo', 'Maria']

comeca_com_j = False
for valor in variavel:
    if valor.startswith('J'):
        comeca_com_j = True
if comeca_com_j:
    print('Existe uma palavra que começa com J.')
else:
    print('Não existe uma palavra que começa com J.')
    