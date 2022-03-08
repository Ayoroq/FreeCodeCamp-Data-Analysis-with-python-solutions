import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('data/epa-sea-level.csv')
    
        # getting equation of line from linegress
    (slope, intercept, rvalue, pvalue, stdrr) = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    
    years_from_2000 = df['Year'][df['Year']>=2000]
    (b_slope, b_intercept, b_rvalue, b_pvalue, b_stdrr) = linregress(years_from_2000,df['CSIRO Adjusted Sea Level'][df['Year'] >= 2000])
    
    # Creating a new year series from 1880 that extends to 2050
    new_year = []
    for i in range(1880,2051):
        new_year.append(i)
    new_year = pd.Series(new_year)
    
    # Creating a new year series from 2000 that extends to 2050
    new_year_b = []
    for i in range(2000,2051):
        new_year_b.append(i)
    new_year_b = pd.Series(new_year_b)
    
    y_predict = slope*new_year + intercept
    y_predict_b = b_slope*new_year_b + b_intercept
    
    plt.figure()
    # Original scatter plot
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'], label = 'Original Data')
    # First predictions with equation of line from 1880
    plt.plot(new_year, y_predict)
    # Second prediction with equation of line from 2000
    plt.plot(new_year_b, y_predict_b)
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    #plt.show()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()