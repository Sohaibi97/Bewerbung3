# Programming Approach

Since the main tasks of this project are data-centric, and because we as students are more familiar with procedual programming when it comes to data analysis, we chose a procedual prorgramming approach.
Furthermore, we chose to avoid overhead and more layers of abstraction that would come hand in hand with programming object oriented for this project. 
And since the project shall have a simular scope to the first research software engineering project, we already are familiar and confident that procedual programming is sufficient and efficient for our tasks.
Also an encapsulation from the data is not necessary, as the data is publicly available anyways
and the direct control over the data is preferred. 

# Architecture

We chose to organize our code in a Model View Controller Architecture for the following main reasons:

1. Modularity: seperating the code that processes data and the code that plots data makes it easier for us to extend, organize and to maintain our code. 

2. Collaboration: Following the MVC architecture allows us as a team to easier maintain and work on our code files. It allowed us to work simultaneously without running into any conflicts.

3. Reusability: We could potentially reuse the model files in other project contexts that also want to operate on the same csv files.

With this architecture we tried covering criteria that come hand in hand with the FAIR guidelines, such as enabling better reusibility, making our code more accesibile through a better organization of code files and a proper structure of how the components interact with each other. 

## UML Package Diagram

![Package Architecture of EcoAnalyzerPy](/docs/EcoAnalyzerPy_Architecture_Package-Diagram.png "Package Architecture")

The package diagram depicts the interaction of our python library EcoAnalyzerPy and the Model, View and Controller directories.

The program is started by executing the main.py file. A command line interface starts running and parses arguments that the user can give. For each valid argument a corresponding controller method is being called. The controller file calls a method in the corresponding model file and starts reading the data by using a special "open_csv" method from our utilities module. The model file accesses the csv files from the data directory that is outside of our package, through the open_csv method. The processed and filtered data is returned to the controller method and the controller passes it to the corresponding view file. This view file takes the filtered dataframe object and creates the plot with the inbuilt functions of the imported python package matplotlib. 
