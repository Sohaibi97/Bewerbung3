#!/usr/bin/env python3

''' Reaserach Question 4: What is the trend in number of threatened
vertebrate species in different countires?'''

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from logger import log

def plot_data(data):
    '''Plots the data on carbondioxide emissions
      to analyze research question four'''
    filtered_species_regions = data
    grouped_df = filtered_species_regions.groupby('Region')

    # animated line graph plot:
    regions = grouped_df.groups.keys()
    fig, ax = plt.subplots(figsize=(12, 6.4)) #size
    lines = [ax.plot([], [], label=region)[0] for region in regions]

    # limits
    ax.set_xlim(filtered_species_regions['Year'].min(), filtered_species_regions['Year'].max())
    ax.set_ylim(filtered_species_regions['Value'].min(), filtered_species_regions['Value'].max())

    # labels
    ax.set_xlabel('Year', fontsize = 12, fontfamily = "Arial")
    ax.set_ylabel('Threatened Vertebrate Species in Number', 
                  fontsize = 14, fontfamily = "Arial")
    ax.set_title('Trend of Threatened Vertebrate Species over Time', fontsize = 14, 
                 fontweight = "bold", fontfamily = "Georgia")

    # legend
    ax.legend(loc= 'upper left')
    fig.patch.set_facecolor('lightgray')
    ax.grid(True, linewidth = 0.5, color="0.6")

    # Update function to animate the plotted lines
    def update(frame):
        for region, line in zip(regions, lines):
            data = grouped_df.get_group(region)
            line.set_data(data['Year'][:frame], data['Value'][:frame])
        return lines

    # run the animation
    animation = FuncAnimation(fig, update, frames=filtered_species_regions['Year'].nunique(), interval=400, blit=True)
    plt.show()

    log.info("Called plot.show() in 'view.rq_4_species'")
