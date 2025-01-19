#!/usr/bin/env python3

'''Research Question 3: How have CO2 emissions
changed over time for different countries or regions?'''

import matplotlib.pyplot as plt
from logger import log


def plot_data(data):
    '''Plots the data on carbon dioxide emissions
    to analyze research question three'''

    emissions_df = data

    # Plot top ten regions
    region_totals = emissions_df.groupby('Region')['Value'].sum()
    top_ten = region_totals.nlargest(10)
    top_ten_emissions = emissions_df[emissions_df['Region'].isin(top_ten.index)]
    emissions_by_year_country = top_ten_emissions.pivot(index='Region', 
                                                        columns='Year', values='Value')
    emissions_by_year_country.T.plot(marker='o', figsize=(10, 6))

    # Labels
    plt.xlabel('Year', fontfamily='Arial', fontsize=12)
    plt.ylabel('CO2 Emissions (kt CO2)', fontfamily='Arial', fontsize=12)
    plt.title(
        'Trend of Carbon Dioxide Emissions for the top ten Countries with highest Emission rates',
        fontfamily='Georgia', fontsize=14, fontweight='bold')

    # Legend
    plt.legend(title='Country', loc='best')

    # Grid and background
    plt.grid(True, color="lightgray", linewidth=0.5)
    plt.gcf().set_facecolor('lightgray')

    plt.show()

    log.info("Called plot.show() in 'view.rq_3_co2'")
