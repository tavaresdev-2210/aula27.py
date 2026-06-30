#"""
#Interpolação básica de strings
#s - string
#d e i  - int 
#f - float
#x e X - Hexadecimal (ABCDEF0123456789)
#"""
nome = 'Lucas'
preco = 1200.92347656
variavel = '%s , o preco é R$%.2f' % (nome,preco)
print(variavel)
print('O hexadecimal de %x é %r' % (20,20))