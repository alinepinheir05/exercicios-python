"""
For in em Python
Interando strings com for
Função range(starte=0, stop, step=1)

texto = "python"

c = 0
while c < len(texto);
    print(texto[c])
    c += 1
"""

texto = 'python'
for letra in texto:
    print(letra)

for n, letra in enumerate (texto):
    print(n, letra)