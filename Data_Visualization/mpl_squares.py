import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.style.use('seaborn-darkgrid')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth = 3)

#set chart title and label axes
ax.set_title("Square numbers", fontsize = 26)
ax.set_xlabel("Input", fontsize = 15)
ax.set_ylabel("Output", fontsize = 15)

#set size of tick labels
ax.tick_params(axis = 'both', labelsize = 15)
plt.show()