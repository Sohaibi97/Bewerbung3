import geopandas as gpd
import country_converter as coco
import matplotlib.pyplot as plt


# we wanna get a map that shows where are the most endangered species live in this world
def show_map_2022(world_nums):
    #we create a world map
    shapefile_path = gpd.datasets.get_path('naturalearth_lowres')
    gdf = gpd.read_file(shapefile_path)

    #   we convert the name of countries in our databank so we can match them all with geopandas
    replacements = {
        'Bolivia (Plurin. State of)': 'Bolivia',
        'Dem. Rep. of the Congo': 'Dem. Rep. Congo',
        'United Rep. of Tanzania': 'Tanzania',
        'Syrian Arab Republic' : 'Syria',
        'Russian Federation' : 'Russia',
        'South Sudan' : 'S. Sudan',
        'Central African Republic' : 'Central African Rep.',
        "Dem. People's Rep. Korea" : 'South korea',
        'Republic of Korea' : 'North Korea',
        'Iran (Islamic Republic of)' : 'Iran',
        'Türkiye' : 'Turkey',
        'Venezuela (Boliv. Rep. of)' : 'Venezuela',
        "Côte d’Ivoire":"Côte d'Ivoire"
    }

    # now we replace with the right names
    world_nums['Country'] = world_nums['Country'].replace(replacements)

    # Merge the world_nums dataframe with the GeoDataFrame based on country names
    merged = gdf.merge(world_nums, left_on='name', right_on='Country', how='left')

    # Plot the choropleth map
    fig, ax = plt.subplots(figsize=(15, 10))
    merged.plot(column='Value', cmap='Reds', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

    # Set the axis labels and title
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_title('Number of Endangered Species by Country in 2022')

    # Show the plot
    plt.show()
    return None





