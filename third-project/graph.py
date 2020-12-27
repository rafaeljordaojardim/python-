import matplotlib.pyplot as pyp 
import matplotlib.animation as animation

# creating a new figure 
figure = pyp.figure()

# creating a subplot with 1 row, 1 column and index 1 - this means a single subplot in our
subplot = figure.add_subplot(1, 1, 1)

def animation_function(i):
    # opening the file and reading each row of cpu utilization data in the file
    cpu_data = open('/home/rjardim/courses/python/third-project/output.txt').readlines()

    # creating an empty list whitch to append each value in the file converted from string
    x = []

    # iterating over the list of cpu values and appending each value 
    for each_value in cpu_data:
        if len(each_value) > 1:
            x.append(float(each_value))

    # clearing/refreshing the figure to avoid unnecessary overwriting for each new poll
    subplot.clear()

    # ploting the values in the list
    subplot.plot(x)
# using the figure, the function and pollling interval of 10000 ms (10 seconds to build
graph_animation = animation.FuncAnimation(figure, animation_function, interval = 10000)

#displaying the graph to the screen
pyp.show()