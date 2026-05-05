Data Visualization with Pandas & Matplotlib
📌 Project Overview

This project focuses on loading, cleaning, and visualizing real-world datasets using pandas and matplotlib.
It demonstrates how to transform raw CSV data into structured DataFrames and generate meaningful visualizations.

Features
ex00
Load CSV datasets safely with error handling
Convert raw data into structured DataFrames


ex01
Handle missing values (NaN)
Filter and clean data


ex02
Convert non-numeric values (e.g., k, M) into usable numbers


ex03
Compare datasets (e.g., population, GDP, life expectancy)
Generate clear and readable graphs


Key Concepts Used in panda 
DataFrame: 2D structure with rows and columns
Parsing: converting raw CSV data into structured format
.set_index(): for easier data access
.loc[]: label-based data selection
.notna(): identify missing values
.intersection(): find common data between datasets
.astype(): convert data types

Matplotlib Features used in this Project
plt.figure() → create a new figure (graph window)
plt.plot() → plot line graphs (e.g., population, life expectancy)
plt.scatter() → create scatter plots (e.g., GDP vs life expectancy)
plt.title() → add a title to the graph
plt.xlabel() → label the x-axis
plt.ylabel() → label the y-axis
plt.legend() → display labels for plotted data
plt.xticks() → control x-axis tick values and formatting
plt.yticks() → control y-axis tick values and formatting
plt.xlim() → set x-axis range
plt.grid() → display grid lines
plt.tight_layout() → adjust spacing for better readability
plt.show() → display the graph
