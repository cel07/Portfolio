# Flight Delay Time Statistics Dashboard

This project provides an interactive dashboard to explore flight delay times by month for a specified year. 
The dashboard is built using [Dash](https://dash.plotly.com/) and [Plotly](https://plotly.com/) for data visualization.

## Features
- Interactive input for the year to filter data.
- Visualization of monthly flight delays based on user-selected year.
- Easy setup and deployment on local machines.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- `pandas`, `dash`, `plotly` libraries

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

3. Run the application:
   ```bash
   python flight_delay_enhanced.py
   ```

4. Open a web browser and go to `http://127.0.0.1:8050/` to view the dashboard.

## Project Structure
- `flight_delay_enhanced.py`: The main script for running the dashboard.
- `requirements.txt`: List of dependencies.
- `README.md`: Project documentation.

## Usage
1. Input a year in the input box.
2. The dashboard will display a histogram of flight delay times for each month of the selected year.

## Acknowledgments
Data for this dashboard was provided by IBM's Skills Network.

