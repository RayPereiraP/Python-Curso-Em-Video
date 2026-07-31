n1 = int(input('Primeira nota: '))
n2 = int(input('Segunda nota: '))
média = (n1 + n2) / 2
print('a média entre {:.1f} e {:.1f} é igual {:.1F}'.format(n1, n2, média)) #depois do ponto flutuante coloque uma casa decimal {:.1f}

#outra forma de fazer 
n1 = int(input('Primeira nota: '))
n2 = int(input('Segunda nota: '))
print('a média entre {:.1f} e {:.1f} é igual {:.1F}'.format(n1, n2, ((n1 + n2) / 2))) #depois do ponto flutuante coloque uma casa decimal {:.1f}