"""
Desempacotamento de listas e python
"""
lista = ['Luiz', 'João', 'Maria',1,2,3,4,5,6]
n1, n2, n3, *outra_lista, ultimo_da_lista = lista
print(n1, n2, outra_lista)
print(ultimo_da_lista)