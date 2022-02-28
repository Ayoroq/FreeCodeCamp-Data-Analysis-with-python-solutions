import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column

df['overweight'] = np.where(df['weight']/((df['height']/100)**2) > 25, 1,0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = np.where(df['cholesterol'] <= 1, 0,1)
df['gluc'] = np.where(df['gluc'] <= 1, 0,1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df,id_vars=['cardio'],value_vars= ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']).sort_values('variable')

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat['total'] = 0
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index = False).count() 

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x = 'variable',
                      y = 'total',
                      hue = 'value',
                      col= 'cardio',
                      data= df_cat, 
                      kind= 'bar').figure

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

    # Filtering out teh data 
    

# Draw Heat Map
def draw_heat_map():

    # Cleaning of the data to remove values with diastolic pressure higher than systolic, 
    # height less than the 2.5th percentile, height more than the 97.5th percentile, 
    # weight less than the 2.5th percentile, weight more than the 97.5th percentile
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) 
    & 
    (df['height'] >= df['height'].quantile(0.025)) & 
    (df['height'] <= df['height'].quantile(0.975)) & 
    (df['weight'] >= df['weight'].quantile(0.025)) & 
    (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr,dtype = bool))



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))

    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, mask=mask, vmax= .3,center=0, annot= True,square=False, linewidths=.5, cbar_kws={"shrink": .5, 'ticks':[-0.08,0.00,0.08,0.16,0.24]}, fmt = '.1f')

    
    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

draw_cat_plot()
draw_heat_map()