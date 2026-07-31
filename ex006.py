n = int(input('digite um número: '))
dob = n * 2
tri = n * 3
raiz = n ** (1/2) #por conta da ordem de precedencia em matemática
print('O dobro de {} vale {}, \n o triplo de {} vale {}, \n a raiz quadrada de {} é igual a {:.2f}'.format(n, dob, n, tri, n, raiz))

#outra forma de fazer
n = int(input('digite um número: '))
print('O dobro de {} vale {}, \n o triplo de {} vale {}, \n a raiz quadrada de {} é igual a {:.2f}'.format(n, (n*2), n, (n*3), n, (n**(1/2)))) #poderiamos usamo o n**(1/2) como pow(n, (1/2))