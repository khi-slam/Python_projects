import matplotlib.pyplot as plt #call the matplotlib library
x = [i for i in range(-5, 6)] #dataset for x using the function range to generate integers between [-5 ,5]
y = [3*x**2 - 2*x + 1 for x in x] #dataset for y using the previous x dataset
plt.plot(x, y) #for matplotlib to make the graph
plt.axhline(y=0, color='black', linewidth=1)  # for the horizontal line
plt.axvline(x=0, color='black', linewidth=1)  # for the vertical line
plt.title("graph of f(x)=3x^2-2x+1 over [-5, 5]") #write the title
plt.xlabel("x axis") #the libel on x
plt.ylabel("y axis") #the label on y
plt.show() #for the plot to appear