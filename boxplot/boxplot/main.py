import matplotlib.pyplot as plt
import random

vetor = []

for i in range(10):
    numero_aleatorio = random.randint(0,200000)
    vetor.append(numero_aleatorio)

plt.boxplot(vetor)
plt.title("Boxplot")
print("running.....")
plt.show()
print("finish")
