# SIR Model Simulation

## Overview

This project implements an SIR model to simulate the spread of an infectious disease through a population. The SIR model divides the population into three compartments:
- **Susceptible (S)**: Individuals who can contract the disease.
- **Infectious (I)**: Individuals who have contracted the disease and can spread it to susceptible individuals.
- **Recovered (R)**: Individuals who have recovered from the disease and are immune.

## Features

- **Simulation**: The model simulates the disease spread over time using differential equations.
- **Visualizations**: Graphs showing the number of susceptible, infectious, and recovered individuals over time.
- **Statistics**: Key metrics such as the peak number of infections and the time until the peak.

## Requirements

- Python 3.x
- Libraries: `numpy`, `scipy`, `matplotlib`, `pandas`

You can install the required libraries using pip:

    ```bash
    pip install numpy scipy matplotlib pandas
    ```

## How to Run

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/sir-model-simulation.git
    cd sir-model-simulation
    ```

2. Open the `sir_model.py` file and adjust the parameters if needed.

3. Run the simulation:

    ```bash
    python sir_model.py
    ```

4. The script will generate visualizations and print statistics to the console.

## Files

- **sir_model.py**: Main script to run the SIR model simulation.
- **plot_results.py**: Script to generate and save visualizations.
- **results.csv**: CSV file with the simulation results, including time steps, susceptible, infectious, and recovered counts.

## Code Explanation

1. **Initialization**: Parameters for the simulation are set, including the transmission rate, recovery rate, and initial conditions.
2. **Differential Equations**: The SIR model is implemented using ordinary differential equations (ODEs).
3. **Simulation**: The model is run over a specified time period, and the number of susceptible, infectious, and recovered individuals is recorded.
4. **Visualization**: Plots of the S, I, and R compartments are generated to visualize the dynamics of the disease spread.
5. **Statistics**: The model calculates and displays statistics such as the peak number of infections and the time at which the peak occurs.

## Results

After running the simulation, you will find:

- **Plots**: Graphs showing the progression of the disease over time.
- **Statistics**: Console output with details about the peak infection rate and other relevant metrics.
- **CSV File**: A file containing detailed simulation data for further analysis.

## Example Output

Here’s an example of what the plots might look like:

- **Susceptible, Infectious, and Recovered over Time**:
    ![SIR Plot](path/to/plot.png)

- **Peak Infection Statistics**:
    ```
    Peak number of infections: 150
    Time to peak: 30 days
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please contact [your.email@example.com](mailto:your.email@example.com).
