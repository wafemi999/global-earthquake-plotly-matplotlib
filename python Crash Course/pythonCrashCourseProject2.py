import matplotlib.pyplot as plt
input_values  = [1,2,3,4,5]
squares = [1,4,9,16,25]
#to use seaborn or other styles
plt.style.use('seaborn-v0_8')
fig,ax = plt.subplots()

#plotting series of points or a point scatterdly
ax.scatter(2,4, s = 200)
x_values = range(1,1001)
y_values = [x**2 for x in x_values]

# defining Custom Colors
#ax.scatter(x_values, y_values, color=(0, 0.8, 0), s=10)

#Using a Colormap
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)


# Set the range for each axis.
ax.axis([0, 1100, 0, 1_100_000])

# Customizing Tick Labels
ax.ticklabel_format(style='plain')

#thickness
#ax.plot(input_values, squares, linewidth = 3)

#show title and axes
ax.set_title("square numbers", fontsize = 24)
ax.set_xlabel("value", fontsize = 14)
ax.set_ylabel("square of value", fontsize = 14)

#set size of tick labels.
ax.tick_params(labelsize = 14)





#this shows the plot in another window
#plt.show()
# 

# Saving Your Plots Automatically 
plt.savefig('squares_plot.png', bbox_inches='tight')





