#!/usr/bin/env python
# coding: utf-8

# # Pymaceuticals Inc.
# ---
# 
# ### Analysis
# 
# - Add your analysis here.
#  

# In[1]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st

# Study data files
mouse_metadata_path = "data/Mouse_metadata.csv"
study_results_path = "data/Study_results.csv"

# Read the mouse data and the study results
mouse_metadata = pd.read_csv(mouse_metadata_path)
study_results = pd.read_csv(study_results_path)

# Combine the data into a single DataFrame
mouse_data = pd.merge(mouse_metadata,study_results, on='Mouse ID')

# Display the data table for preview
mouse_data.head()


# In[2]:


# Checking the number of mice.
mouse_count = len(mouse_data.groupby('Mouse ID').count())
print(f'The number of mice is: ', mouse_count)


# In[19]:


# Our data should be uniquely identified by Mouse ID and Timepoint
# Get the duplicate mice by ID number that shows up for Mouse ID and Timepoint. 
duplicates = mouse_data[mouse_data.duplicated(['Mouse ID', 'Timepoint'])]
duplicates = duplicates['Mouse ID'].unique()
print(f'The duplicate mice have the following ID(s): ',duplicates)


# In[4]:


# Optional: Get all the data for the duplicate mouse ID. 
duplicates = mouse_data.loc[mouse_data['Mouse ID'] == 'g989']
duplicates


# In[5]:


# Create a clean DataFrame by dropping the duplicate mouse by its ID.
clean_data = mouse_data[mouse_data['Mouse ID'] != 'g989']
clean_data


# In[6]:


# Checking the number of mice in the clean DataFrame.
clean_count = len(clean_data.groupby('Mouse ID').nunique())
print(f'The number of mice is: ', clean_count)


# ## Summary Statistics

# In[22]:


# Generate a summary statistics table of mean, median, variance, standard deviation, and SEM of the tumor volume for each regimen
# Use groupby and summary statistical methods to calculate the following properties of each drug regimen: 
# mean, median, variance, standard deviation, and SEM of the tumor volume. 

mean = clean_data.groupby(['Drug Regimen']).mean()['Tumor Volume (mm3)']
median = clean_data.groupby(['Drug Regimen']).median()['Tumor Volume (mm3)']
variance = clean_data.groupby(['Drug Regimen']).var()['Tumor Volume (mm3)']
std_dev = clean_data.groupby(['Drug Regimen']).std()['Tumor Volume (mm3)']
std_error = clean_data.groupby(['Drug Regimen']).sem()['Tumor Volume (mm3)']

# Assemble the resulting series into a single summary DataFrame.

summary = pd.DataFrame ({'Mean' : mean,
                        'Median' : median,
                        'Variance' : variance,
                        'Std. Deviation' : std_dev,
                        'SEM' : std_error})
summary


# ## Bar and Pie Charts

# In[37]:


# Generate a bar plot showing the total number of rows (Mouse ID/Timepoints) for each drug regimen using Pandas.

counts = clean_data['Drug Regimen'].value_counts()
pandas_bar_chart = counts.plot(kind="bar", figsize=[7,3.5])

#Label Chart Title, Axes
plt.xlabel('Drug Regomen')
plt.ylabel('No. of Mouse Timepoints')
plt.title('No. of Mouse Timepoints by Drug Regimen')

#Create Bar Plot
plt.show()


# In[58]:


# Generate a bar plot showing the total number of rows (Mouse ID/Timepoints) for each drug regimen using pyplot.
drug = clean_data['Drug Regimen'].unique()
counts2 = clean_data['Drug Regimen'].value_counts()


#Define X- and Y-axes
x_axis = drug
y_axis = counts2

#Label Chart Title, Axes
plt.xlabel('Drug Regomen')
plt.xticks(rotation='vertical')
plt.ylabel('No. of Mouse Timepoints')
plt.title('No. of Mouse Timepoints by Drug Regimen')

#Create a PyPlot Bar Chart
plt.bar(x_axis, y_axis)
plt.show()


# In[59]:


# Generate a pie plot showing the distribution of female versus male mice using Pandas
pie_counts = clean_data['Sex'].value_counts()
pandas_pie_chart = pie_counts.plot(kind="pie", autopct='%1.1f%%')

#Label Chart Title, Axes
plt.ylabel('Sex')
plt.title('No. of Mice by Sex')

#Create Bar Plot
plt.show()


# In[61]:


# Generate a pie plot showing the distribution of female versus male mice using pyplot
pie_counts2 = clean_data['Sex'].value_counts()

#Define Y-axis
y_axis = pie_counts2

#Label Chart Title, Axes
plt.ylabel('Sex')
plt.title('No. of Mice by Sex')

#Create a PyPlot Bar Chart
plt.pie(y_axis,autopct='%1.1f%%')
plt.show()


# ## Quartiles, Outliers and Boxplots

# In[13]:


# Calculate the final tumor volume of each mouse across four of the treatment regimens:  
# Capomulin, Ramicane, Infubinol, and Ceftamin

# Start by getting the last (greatest) timepoint for each mouse


# Merge this group df with the original DataFrame to get the tumor volume at the last timepoint


# In[14]:


# Put treatments into a list for for loop (and later for plot labels)


# Create empty list to fill with tumor vol data (for plotting)


# Calculate the IQR and quantitatively determine if there are any potential outliers. 

    
    # Locate the rows which contain mice on each drug and get the tumor volumes

    
    # add subset 

    
    # Determine outliers using upper and lower bounds


# In[15]:


# Generate a box plot that shows the distrubution of the tumor volume for each treatment group.


# ## Line and Scatter Plots

# In[16]:


# Generate a line plot of tumor volume vs. time point for a single mouse treated with Capomulin


# In[17]:


# Generate a scatter plot of mouse weight vs. the average observed tumor volume for the entire Capomulin regimen


# ## Correlation and Regression

# In[18]:


# Calculate the correlation coefficient and a linear regression model 
# for mouse weight and average observed tumor volume for the entire Capomulin regimen


# In[ ]:




