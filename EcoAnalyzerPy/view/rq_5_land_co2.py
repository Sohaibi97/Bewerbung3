#!/usr/bin/env python3

''' Reaserach Question 5: How do CO2 emissions relate to land usage?'''

import matplotlib.pyplot as plt
from logger import log

def plot_data(data):
    '''Plots the data on carbondioxide emissions
      to analyze research question five'''

    top_countries = data
    fig, ax1 = plt.subplots(figsize=(10, 6))

    color = 'tab:blue'
    ax1.set_ylabel('Permanent Crops', color=color, fontfamily ='Arial',
                   fontsize = 12, fontweight = 'bold' )
    ax1.bar(top_countries["Country"], top_countries["Value_Crops"], color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    plt.xticks(rotation=90)

    ax2 = ax1.twinx()

    color = 'tab:red'
    ax2.set_ylabel('CO2 Emissions', color=color, fontfamily ='Arial',
                   fontsize = 12, fontweight = 'bold' )
    ax2.bar(top_countries["Country"], top_countries["Value_Emission"], alpha=0.5, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.title('Top 10 Countries by Permanent Crops and their highest CO2 Emissions',
              fontfamily ='Georgia',fontsize = 14, fontweight = 'bold')
    plt.gcf().set_facecolor('lightgrey')
    #plt.grid(True, color='0.3', linewidth = 0.5)

    plt.show()

    log.info("Called plot.show() in 'view.rq_5_land_co2'")
