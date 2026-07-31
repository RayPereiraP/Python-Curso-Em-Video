#faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele
a = input("Digite algo: ")
print('O tipo primitivo desse valor é:', type(a))
print('Só tem espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('Está em maiúsculas?', a.isupper())
print('Está em minúsculas?', a.islower())  # Corrigido de "slower" para "islower"
print('Está capitalizada?', a.istitle()) # esse a é um objeto que tem métodos(caracteristicas)
print('É ASCII?', a.isascii())
print('É decimal?', a.isdecimal())
print('É um dígito?', a.isdigit())
print('É um identificador válido?', a.isidentifier())
print('É imprimível?', a.isprintable())
# esse a é um objeto que tem métodos(caracteristicas)




'''
isalnum() Retorna True se todos os caracteres na string forem alfanuméricos
isalpha() Retorna True se todos os caracteres na string forem do alfabeto
isascii() Retorna True se todos os caracteres na string forem caracteres ascii
isdecimal() Retorna True se todos os caracteres na string forem decimais
isdigit() Retorna True se todos os caracteres na string forem dígitos
isidentifier() Retorna True se a string for um identificador
islower() Retorna True se todos os caracteres na string forem minúsculos
isnumeric() Retorna True se todos os caracteres na string forem numéricos
isprintable() Retorna True se todos os caracteres na string forem imprimíveis
isspace() Retorna True se todos os caracteres na string forem espaços em branco
istitle() Retorna True se a string seguir as regras de um título
isupper() Retorna True se todos os caracteres na string forem maiúsculos
'''