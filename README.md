Simulation User Manual
Overview
The provided Python code simulates a queuing system where cars arrive based on a specified lambda and undergo service with different service time distributions. The simulation is implemented using the SimPy library.
Usage
Code Structure
The program has two main functions:
1.	simulate(arrivalfile, servicefile): This function performs the simulation based on the specified arrival and service time files.
2.	simulate_and_format(arrival_file, service_file, description): This function formats the simulation results for display.
Input Files
The simulation requires two input files:
•	Arrival File (arrivalfile): Contains the arrival times for cars.
•	Service File (servicefile): Contains the service times for cars.
Running the Simulation
1.	Provide the arrival and service files in the designated format.
2.	Execute the script, and the simulation results will be printed.
Results
The simulation results include the average queuing time for each scenario. The output is displayed in a tabular format, providing insights into the system performance under different conditions.
