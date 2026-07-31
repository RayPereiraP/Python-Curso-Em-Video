#faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
n1 = input('digite um número') # usamos 3 váriaves n1 s a
s = n1 + 1
a = n1 - 1
print('Analisando o valor escolhido: {}, o antecessor é {} e o sucessor é {}'.format(n1, a, s))

#outra forma de fazer, sem utilizar tantas váriaveis,logo economiza a memória do nosso computador 
n = input('digite um número')
print('Analisando o valor escolhido: {}, o antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))