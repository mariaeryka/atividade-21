# Crie um programa que faça uma contagem regressiva de 10 até 0 e exiba "FIM!" ao final.

import time

for i in range(10, -1, -1):
    print(i)
    time.sleep(1)

print ("FIM!")

