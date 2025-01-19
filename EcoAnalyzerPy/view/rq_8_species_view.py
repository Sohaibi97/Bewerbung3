import matplotlib.pyplot as plt


# Plotting total endangered species by type

def show_total_by_type(total_endangered_type):
    plt.figure(figsize=(10, 6))
    for species_type, data in total_endangered_type.groupby('Type'):
        plt.plot(data.index.get_level_values('Year').values, data.values, label=species_type)
    plt.xlabel('Year')
    plt.ylabel('Total Endangered Species')
    plt.title('Total Endangered Species by Type')
    plt.legend()
    plt.grid(True)
    plt.show()
    return None



