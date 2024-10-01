import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    X = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(X, y, label="Data Points")


    # Create first line of best fit
    result = linregress(X, y)
    X_extended = list(range(X.min(), 2051))
    first_best_fit = [result.slope * xi + result.intercept for xi in X_extended]
    ax.plot(X_extended, first_best_fit, 'r', label="1st Line of Best Fit")

    # Create second line of best fit
    X2 = X[X >= 2000]
    y2 = y[X >= 2000]
    result2 = linregress(X2, y2)
    X2_extended = list(range(X2.min(), 2051))
    second_best_fit = [result2.slope * xi + result2.intercept for xi in X2_extended]
    ax.plot(X2_extended, second_best_fit, 'g', label="2nd Line of Best Fit")

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title('Rise in Sea Level')
    ax.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()