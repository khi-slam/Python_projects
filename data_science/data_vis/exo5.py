import matplotlib.pyplot as plt #call the matplotlib library
hours = [1, 2, 3, 4, 5, 6] #dataset for how many study hours
scores = [40, 50, 55, 65, 70, 85] #dataset for exam scores
plt.scatter(hours, scores) #tells matplotlib to make scatter chart
plt.title("Study Hours vs Score") #write the title
plt.xlabel("Hours") #write hours on x axis
plt.ylabel("Score") #write score on y axis
plt.show() #make the chart appear