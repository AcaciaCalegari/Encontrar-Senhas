arquivo="/home/labnet/Desktop/mininex/seguranca.txt"
#senhareal=input("digite sua senha: ") 
senhareal="2739081av9"
lines=open(arquivo).readlines()
for line in lines:
    print("Testando a possibilidade de senha %s"%line[0:-1])
    if line[0:-1] == senhareal:
        print("encontrei sua senha. sua senha eh: %s" %line[0:-1])
print lines
