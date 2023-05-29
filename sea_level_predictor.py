import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # Create scatter plot
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'],label='Historical Data')

    # Create first line of best fit
    line_1 = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    x_2050 = pd.Series(range(1880,2051))
    plot_line_1 = plt.plot(x_2050,line_1.intercept+line_1.slope*x_2050,label='Historical Rase of Sea Level Rise')
    plot_line_1
    # Create second line of best fit
    df2 = df[df['Year']>= 2000]
    x2 = pd.Series(range(2000,2051))
    line_2 = linregress(df2['Year'],df2['CSIRO Adjusted Sea Level'])
    plot_line_2 = plt.plot(x2,line_2.intercept+line_2.slope*x2,label='Current Rate of Sea Level Rise')
    plot_line_2
  
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()