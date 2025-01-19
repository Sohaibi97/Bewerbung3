import matplotlib.pyplot as plt


def show_total(total_endangered_species):
# Plotting total endangered species over time
    plt.figure(figsize=(10, 6))
    plt.plot(total_endangered_species.index.values, total_endangered_species.values)
    plt.xlabel('Year')
    plt.ylabel('Number of Total Endangered Species')
    plt.title('Total Endangered Species Over Time')
    plt.grid(True)
    plt.show()
    return None
    



