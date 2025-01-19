'''Research question: How has the forest cover developed from 2005 to 
    2019 in different countries?
    This file is responsible for plotting the world map needed for
    answering the research question.'''

import geopandas as gpd
import matplotlib.pyplot as plt
from logger import log

def plot_data(data, show):
    '''Plots the data needed for answering research
    question one.'''

    log.info("Called function 'view.research_question_one.plot_data' with parameter show=%s", show)
    
    # Plot the world map
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    merged_df = world.merge(data, left_on='name', right_on='Land')

    # Create a plot
    fig, ax = plt.subplots(figsize=(15, 10))
    merged_df.plot(column='Difference', cmap='coolwarm', 
                   linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
    # Add title and axis labels
    plt.title('Change of forest covered area from 2005 to 2019 (In %)')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')

    if show:
        plt.show()
