# EcoAnalyzerPy

## Exploring Threatened Species, Land Usage and CO2 Emissions

> _"The greatest danger to our future is apathy."_ — Dr. Jane Goodall

Research Software Engineering Group Project at University of Potsdam

## About The Project

In this project i am analyzing data from [UN Data](https://data.un.org/default.aspx) on Threatened Species, Land Usage and Carbon Dioxide Emmision Estimates.

I want to examine the number of threatened species (with a focus on vertebrates) over the years (2004 to 2022) and compare land usage (Important sites for terrestrial biodiversity protected) and CO2 Emissions in relation to numbe rof threatened species in the areas that the datasets provide for the year 2021.

The first csv contains data on threatened species with the variables area, year, series (vertebrates, invertebrates, plants).
The csv on land usage provides data for 2005, 2010, 2019, 2021 about "Sites protected for terre-strial biodiversity", as well as data about total land, permanent crop culture and forest covered land. The third csv has data on regions, year and values of emissions in thousand metric tons of carbon dioxide.

I am interested in comparing the values of the datasets and in visualizing the values of threatened species.

## Installation instructions

1. Clone the repository:

```bash
git clone https://github.com/<your_github_username>/<your_repository_name>.git
```

2. Navigate to the root project directory:

```bash
cd <your_repository_name>

```

3. Navigate to the project directory:

```bash
pip install -r requirements.txt
```

4. Run main.py for command line tools

```bash
python ./EcoAnalyserPy/main.py
```

## Project Structure Overview

The package directory EcoAnalyzerPy contains the main.py file which starts the commmand line interface and parses arguments. The parsed arguments will call controller methods which will call methods in model files. The model file methods return filtered dataframes to the controller. The controller then passes the dataframes to the view, where the data is plotted.

Alternatively to the package the user can use this project through the jupyter notebook file EcoNotebook.ipynb in the directory /jupyter.

The file utilities.py contains helpful functions, for example open_csv which opens the cleaned data files.
The directory /data contains the original datasets in /raw and cleaned datasets in /clean. The original is not needed and serves only as reference.

## Usage Guide

Navigate to the package directory:

```bash
cd EcoAnalzerPy

```

From there you can start the command line tools:

- **with Python**

```bash
python main.py

```

- **with Jupyter Notebook**

```bash
jupyter notebook

```

### Command Line Interface

| Research Question                                                                           | CLI Argument | Chart Type        |
| ------------------------------------------------------------------------------------------- | ------------ | ----------------- |
| How has the forest cover developed from 2005 to 2019 in different countries?                | `-rq1`       | geopandas map     |
| How have CO2 emissions changed over time for different countries or regions?                | `-rq3`       | Line Graph        |
| What is the trend in the number of threatened vertebrate species in different countries?    | `-rq4`       | Line Graph        |
| How do CO2 emissions relate to land usage?                                                  | `-rq5`       | Stacked Bar Chart |
| Is there a correlation between CO2 emissions and permanent crops for the top ten countries? | `-rq6`       | Scatter Plot      |

| Option    | Description                                |
| --------- | ------------------------------------------ |
| `-config` | Absolute path to a .yml configuration file |

## Documentation

I developed the python package EcoAnalzerPy to examine data on threatened species, land usage and carbondioxide emissions.
A computational narrative has been implemented and the full sphinx documentation for the project is available for further information.

## License

This project is licensed under the GNU General Public License version 3 (GPL-3.0). Please see the [LICENSE](https://www.gnu.org/licenses/gpl-3.0.en.html) file for more details.

## Citation

Please consult the [rse_project_2/CITATION.cff](/CITATION.cff) file for citation details.

## Code of Conduct

To understand our code of conduct when participating in this project, please review the [CONDUCT](/CONDUCT.md) file.

## Contribution

If you want to contribute to this project, please refer to [Contribution](/CONTRIBUTING.md).

## Contact

Get in touch!
Suggestions, feedback and contributions are very welcome.

Name: Sohaib Khamlichi
**Email:** mohamed.sohaib.khamlichi@uni-potsdam.de

## Acknowledgements

- Visit [Undata.org](https://data.un.org/default.aspx) and go to "Popular statistical tables, country (area) and regional profiles" and scroll to "Environment". You will find the csv files **"Land"**, **"CO2 emissions estimates"**, **"Threatened species"**. All three csv files have been updated on 18-Oct-2022.
- [Merely-useful.tech](https://merely-useful.tech/py-rse/scripting.html)
- [Pandas Library](https://pandas.pydata.org/)
