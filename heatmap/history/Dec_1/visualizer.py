import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import time



def visualizeHeatmap(geoMatrix, squareFrame):

    startVisualizeHeatmap = time.clock()

    # find largest value to adjust colour in matrix
    largest = 0
    for i in range(0,squareFrame):
        for j in range(0,squareFrame):
            if geoMatrix[i][j] > largest:
                largest = geoMatrix[i][j]

    # create discrete colormap
    cmap = 'hot'
    norm = mpl.colors.Normalize(vmin=0, vmax=largest)

    fig, ax = plt.subplots()
    ax.imshow(geoMatrix, cmap= cmap, norm=norm, interpolation='bilinear')
    fig.canvas.set_window_title('Heatmap')

    # draw gridlines
    ax.grid(which='major', axis='none', linestyle='', color='k', linewidth=1)
    ax.set_xticks(np.arange(0, squareFrame, squareFrame/4));
    ax.set_yticks(np.arange(0, squareFrame, squareFrame/4));
    endVisualizeHeatmap = time.clock()
    print "visualize heatmap: ", endVisualizeHeatmap - startVisualizeHeatmap, " seconds \n"

    # print geomatrix
    print geoMatrix
    plt.show()
