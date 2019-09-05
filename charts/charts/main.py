import matplotlib.pyplot as plt


x1 = [1,2,3,4,5]
y1 = [2,3,7,1,0]

x2 = [2,4,5,6,7]
y2 = [4,7,8,3,10]

titulo = "grafico de barras"

eixox="eixo x"
eixox="eixo y"

plt.title(titulo)

plt.xlabel(eixox)
plt.ylabel(eixox)

plt.bar(x1,y1, label = "group 1")
plt.scatter(x2,y2, label = "group 2", color = 'g')
plt.plot(x2,y2, color = 'g')
plt.legend()
plt.show()