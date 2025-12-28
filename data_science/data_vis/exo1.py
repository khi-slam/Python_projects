import matplotlib.pyplot as plt #call the matplotlib library
y = 0#int(input("Enter the y axis: ")) # for y value in 2x - y
x_values = [i for i in range(-10,11)] #dataset for x using the function range to generate integers between [-10 ,10]
y_values = [2*x-y for x in x_values] #dataset for y using the previous x dataset
plt.axhline(y=0, color='black', linewidth=1) # for the horizontal line
plt.axvline(x=0, color='black', linewidth=1) # for the vertical line
plt.plot(x_values, y_values) #for matplotlib to make the graph
plt.title(f"Graphe off y=2x-{y}") #for the graph title
plt.ylabel("y axis") #the label on y
plt.xlabel("x axis") #the libel on x
plt.show() #for the plot to appear