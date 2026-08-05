import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

# A plot is simply a graph or chart that visually displays data.
# fig represents the entire figure which is the collection of plots that are generated
# ax represents a single plot in the figure, this is the cariable we'll use most of the time when defining and customizing a SINGLE plot
# this function can generate one or more plots in the same figure.
fig, ax = plt.subplots()
ax.plot(squares)


# tries to plot the data it's given in a meaningful way. It opens matplotlib's viewer and displays the plot
plt.show()
