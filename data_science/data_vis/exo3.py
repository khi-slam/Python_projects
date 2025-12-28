import matplotlib.pyplot as plt #call for matplotlib
products = ["Ax", "Bx", "Cx", "Dx"] #dataset for products
sales= [50, 80, 30, 90] #dataset fo sales
plt.bar(products, sales) #for making bar chart
plt.title("Sales per Product") #for the title
plt.xlabel("Product") #for the label on the x axis
plt.ylabel("Sales") #for the label on the y axis
plt.show() #for the bar chart to appear