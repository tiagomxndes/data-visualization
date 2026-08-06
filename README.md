# Data Visualization

Exercises from Python Crash Course, 3rd Edition, working with matplotlib and Plotly to turn plain numbers and real weather data into charts.

## Files

**Basic plotting with matplotlib**
- `mpl_squares.py` - simple line plot of square numbers
- `scatter_squares.py` - same idea as a scatter plot, colored by value
- `try_by_myself.py` - cubic numbers, same pattern applied on my own

**Random walks**
- `random_walk.py` - a `RandomWalk` class that generates a random path, one step at a time, rejecting steps that don't actually move
- `rw_visual.py` - plots the walk with matplotlib, colors the start and end points, regenerates a new walk on each run if you want to keep going

**Dice simulation with Plotly**
- `die.py` - a `Die` class, rolls a random number between 1 and however many sides it has
- `die_visual.py` - rolls two dice 50,000 times and charts the frequency of each result as a bar chart

**Weather data (CSV)**
- `sitka_highs.py` - reads a year of Sitka weather data, plots daily high temperatures
- `sitka_highs_lows.py` - same, but plots high and low together with the gap between them shaded in
- `sitka_rainfall.py` - reads the same location's full dataset, this time plotting rainfall, with a try/except to skip rows where that value is missing
- `death_valley_highs_lows.py` - same high/low pattern applied to a different climate, Death Valley, for comparison against Sitka

## What I actually practiced here

- Reading real CSV data and parsing it into usable Python values, dates, temperatures, rainfall
- Handling bad or missing rows in a dataset without crashing the whole script
- The visual language of matplotlib, styling axes and titles, choosing colors, shading between two lines, formatting date labels so they don't overlap
- Building small classes to hold reusable state (`Die`, `RandomWalk`) instead of writing one-off scripts
- A first look at Plotly, mainly for the interactive bar chart on the dice results

## Setup

pip install matplotlib plotly

Weather scripts expect their CSV files inside `weather_data/`. Run any script directly, e.g. `python sitka_highs.py`.
