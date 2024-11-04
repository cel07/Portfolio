
# Flight Delay Time Statistics Dashboard (Matplotlib Version)

This project provides a dashboard to explore flight delay times by month for a specified year, using Matplotlib for data visualization in a Jupyter Notebook. This version replaces the original interactive dashboard with static charts, making it easy to view directly on GitHub.

## Features
- Input for selecting a year to filter data.
- Visualizations of monthly flight delays for different types of delays.
- Easy to set up and view in Jupyter Notebook.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- `pandas`, `matplotlib` libraries

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/cel07/Portfolio.git
   cd Portfolio
   ```

2. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. Open the Jupyter Notebook:

   ```bash
   jupyter notebook flight_delay_analysis_matplotlib.ipynb
   ```

## Project Structure
- `flight_delay_analysis_matplotlib.ipynb`: The main notebook with Matplotlib visualizations.
- `requirements.txt`: List of dependencies.
- `README.md`: Project documentation.

## Usage
1. Open the notebook in Jupyter Notebook.
2. Select a year in the code cell where `year` is defined, and then run all cells to generate plots.
3. The notebook will display line plots for different types of delays (carrier, weather, NAS, security, and late aircraft) based on the selected year.

## Acknowledgments
Data for this dashboard was provided by IBM's Skills Network.
