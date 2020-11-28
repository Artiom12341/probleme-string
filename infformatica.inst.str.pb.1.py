import colorama
n=str(input("Dati cuvuntul="))
d=str(input("Dati litera="))
colorama . init()
for c in range(0,len(n)):
    s=n[:c]
    f=n[c+1:]
    print('{a}{g}{b}'.format(a=s,'\033[31m',"g",'\033'=d,b=f))