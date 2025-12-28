import matplotlib.pyplot as plt
n = int(input("enter a number"))
a = float(input("a number"))
b = float(input("b number"))
c = float(input("c number"))
x=[]
y=[]
for i in range(n+1):
    x.append(i)
    y.append(a * i**2 + b*i + c)
plt.plot(x,y)
plt.title(f" Graphe off y={a}x2+{b}x+{c} ")
plt.ylabel("y axis")
plt.xlabel("x axis")
plt.show()