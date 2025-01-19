
import matplotlib.pyplot as plt



# Plotting percentage increase of endangered species by type
def show_precentage_increase(percentage):
    plt.figure(figsize=(10, 6))
    for species_type, percentage_increase in percentage.items():
        plt.bar(species_type, percentage_increase)
    plt.ylabel('Percentage Increase in 18 Years')
    plt.title('Percentage Increase of Endangered Species by Type')
    plt.grid(True)
    plt.show()
    return None

