import numpy as np
from ss_plotting.make_plots import plot
import matplotlib.pyplot as plt

data_rotation_rgb = [0.428, 0.203, 0.484, 0.457, 0.423, 0.441, 0.531, 0.107, 0.197, 0.508, 0.312, 0.201, 0.121]
data_rotation_rgb.reverse()
data_rotation_rgbd = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
x_rot = np.arange(0,65,5)
series2 = [(x_rot, data_rotation_rgb), (x_rot, data_rotation_rgbd)]
series_labels2 = ['RGB', 'RGBD']
series_colors2 = ['red', 'blue']
ylabel = 'Error Percentage'
xlabel = 'Rotation Angle (degrees)'
title = 'Viewing Angle Errors'

fig2, ax2 = plot(series2, 
     series_labels=series_labels2,
     series_colors=series_colors2,
	 plot_ylabel = ylabel,
	 plot_xlabel = xlabel,
	 plot_title = title,
     linewidth=5,
     fontsize=15,
     legend_fontsize=15)

plt.show()