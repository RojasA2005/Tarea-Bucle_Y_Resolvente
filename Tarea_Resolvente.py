import math

a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))
c = int(input("Ingrese c: "))

try:
     result_positive = (-b + math.sqrt(pow(b, 2) - 4*a*c)) / (2*a)
     result_negative = (-b - math.sqrt(pow(b, 2) - 4*a*c)) / (2*a)
     print("Los resultados de la resolvente son {} y {}".format(result_positive, result_negative))
except:
     print("Los valores no tienen resultados reales")