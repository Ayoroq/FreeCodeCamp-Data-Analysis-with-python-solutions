import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('data/fcc-forum-pageviews.csv', parse_dates=True, index_col='date')

# Clean data
df = df[(df['value'] <= df['value'].quantile(0.975))
        & (df['value'] >= df['value'].quantile(0.025))]


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(10, 5))
    plt.plot(df['value'], color='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['month'] = df.index.month
    df_bar['year'] = df.index.year
    df_bar = df_bar.groupby(['month', 'year'])['value'].mean().to_frame()
    df_bar = df_bar.reset_index()
    df_bar = df_bar.pivot('year', 'month', 'value')

    # Draw bar plot
    fig = df_bar.plot(kind='bar',
                      figsize=(8, 4),
                      xlabel='Years',
                      ylabel='Average Page Views').figure
    plt.legend([
        'January', 'February', 'March', 'April', 'May', 'June', 'July',
        'August', 'September', 'October', 'November', 'December'
    ],
               title='Months')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(11, 5))
    sns.boxplot(data=df_box, x='year', y='value', ax=ax[0])
    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_ylabel('Page Views')
    ax[0].set_xlabel('Year')

    sns.boxplot(data=df_box,
                x='month',
                y='value',
                ax=ax[1],
                order=[
                    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
                    'Sep', 'Oct', 'Nov', 'Dec'
                ])
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_ylabel('Page Views')
    ax[1].set_xlabel('Month')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

draw_line_plot()
draw_bar_plot()
draw_box_plot()
