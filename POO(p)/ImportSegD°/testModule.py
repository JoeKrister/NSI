
import secondDegre as sD

p = input("Donnez les coefficients du polynome séparés par des virgules :")
p = tuple(map(float, p.split(",")))

p = sD.polynome(p)
print(sD.tangente(p,3))



#(37).bit_length()
#bin()