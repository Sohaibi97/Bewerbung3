#!/usr/bin/env python3

''' Reaserach Question 6: Is there a correlation between CO2 emissions and
permanent crops for the top ten countries?'''

import matplotlib.pyplot as plt
from logger import log

def plot_data(data):
    '''Plots the data on carbondioxide emissions
      to analyze research question six'''
    final_df = data

    # Scatter plot
    plt.figure(figsize=(8,7))
    for country in final_df['Country'].unique():
        plt.scatter(final_df[final_df['Country']==country]['Value_Crops'],
                    final_df[final_df['Country']==country]['Value_Emission'],
                    label=country)

    # labels
    plt.xlabel('Permanent Crops (thousand hectares)', fontfamily ='Arial', fontsize = 12)
    plt.ylabel('CO2 Emissions (thousand metric tons)', fontfamily ='Arial', fontsize = 12)
    plt.title('Impact of Permanent Crops on CO2 Emissions for Top Countries',
              fontfamily ='Georgia',fontsize = 14, fontweight = 'bold')

    #legend
    plt.legend(loc='best')
    plt.gcf().set_facecolor('lightgrey')
    plt.grid(True)
    plt.grid(color='lightgrey', linewidth = 0.5)

    plt.show()

    log.info("Called plot.show() in 'view.rq_6_land_co2'")
