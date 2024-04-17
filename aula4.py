# AND = para ser true tudo tem que ser true
# or = para ser true apenas um tem que ser true

#print (True and True)
#print (True and False)
#print (False and False)
#print (True or True)
#print (True or False)
#print (False or False)

saldo = 1000
saque = 250 
limite = 200
cont_especial = True

exp_1 = (saldo >= saque and saque <= limite) or (cont_especial and saldo >= saque)

print (exp_1)