#Assignments week 3, Python part 3.2P - Loïs van 't Wout, 12103977
#Import packages
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import datetime
import time

#Q3.2P.1
    #Generate data
uniform_data=np.random.uniform(low=-10,high=10,size=1000)
    #Generate boxplot 
plt.figure()
plt.boxplot(uniform_data)
    #Generate violinplot
plt.figure()
sns.violinplot(data=uniform_data)
    #Add jittered datapoints
sns.stripplot(data=uniform_data)
    #I think the boxplot is more insightful

#Q3.2P.2
    #Is a passenger's age associated with chance of survival?
    #Load data
titanic_data = pd.read_csv('https://raw.githubusercontent.com/hannesrosenbusch/schiphol_class/master/titanic.csv')
    #Generate plot
plt.figure()
    #Generates boxplot with group who survived vs who didn't and the spread of their ages
    #There appears to be no significant difference in age between groups
    #Therefore there is no apparent association betweeen age and survial
sns.boxplot(x="Survived", y="Age", data=titanic_data)

#Q3.2P.3
    #Load data
tips = sns. load_dataset("tips")
    #Generate scatterplot
plt.figure()
sns.regplot(data=tips,x="total_bill",y="tip",ci=None)
    #Set labels for axes
plt.xlabel("total_bill",fontsize=22)
plt.ylabel("tip",fontsize=22)

#plt.close('all')

#Q3.2P.4
    #Load data
diamonds=sns.load_dataset("diamonds")
    #Create subset of diamonds dataframe with only numeric variables
num_diamonds=diamonds[["carat","depth","table","price","x","y","z"]]
    #Create subplot window
fig, axs = plt.subplots(1,2)
    #Generate heatmap
    #Heatmap = index of correlations between numeric variables
    #Therefore include corr() to plot correlations
sns.heatmap(ax=axs[0],data=num_diamonds.corr())
    #Generate KDE plot
sns.kdeplot(ax=axs[1],data=num_diamonds,x="carat",y="price")

#Q3.2P.5
def my_plots(input_string):
    """
    returns an informative plot if input is yay, confusing plot if input is eww
    input_string: "eww" or "yay" 
    """
    #Return error/warning if input is not equal to yay or eww
    if not (input_string == "yay" or input_string == "eww") : 
        raise Exception("input must be either eww or yay: try again.")
    #If input is yay: informative plot
    if input_string == "yay":
        data=np.random.uniform(low=-10,high=10,size=(100))
        plt.figure()
        plt.title("beautiful informative boxplot")
        plt.boxplot(data)
    #If input is eww: confusing plot
    elif input_string == "eww":
        #Data to plot
        data=np.random.uniform(low=-10,high=10,size=(100,100))
        plt.figure()
        plt.title("total mess")
        plt.imshow(data)
    return plt.show()

#Q3.2P.6
#OLD BAD CODE

#Define (time) variables
t=datetime.datetime.now().time() #Get current time
midnight = datetime.time(00,00,00) #Define midnight
wakeup = datetime.time(5,00,00)
breakfast_start = datetime.time(7,00,00)
breakfast_stop = datetime.time(10,00,00)

#Function to check if current time lies within a time interval
def time_in_range(start, end, current):
    """Returns whether current is in the range [start, end]"""
    return start <= current <= end

#Check if it's bedtime / breakfast time yet
if(time_in_range(midnight,wakeup,t)):  #check if time is between midnight and 5am
  print("Go to sleep!") #if it is, print "Go to sleep!"
elif(time_in_range(breakfast_start,breakfast_stop,t)): #check if time is between 7am and 10am
   print("Eet je hagelslag!") #if it is, print a message
else:
   print("Gut gemacht!") #if the time is not within any of these intervals, print a message

#---------------------------------------------------------------------------------------------
#NEW GOOD CODE

#Define time variables
time_now = datetime.datetime.now().time() #Get current time
midnight = datetime.time(00,00,00) #Define midnight
wakeup = datetime.time(5,00,00) #Variable for 5AM
breakfast_start = datetime.time(7,00,00) #Variable for 7AM
breakfast_stop = datetime.time(10,00,00) #Variable for 10AM

#Function to check if current time lies within a time interval
def time_in_range(start, end, current):
    """Checks whether current time is in the range [start, end]
    start: start of the time range in datetime format
    end: end of the time range in datetime format
    current: current time in time format"""
    return start <= current <= end

#Check if it's bedtime / breakfast time yet and print message accordingly
if time_in_range(midnight,wakeup,time_now):  #check if time is between midnight and 5am #EDIT: removed unnecessary parentheses
    print("Go to sleep!") #if it is, print "Go to sleep!" #EDIT: bad indentation, changed from 2 spaces to 4
elif time_in_range(breakfast_start,breakfast_stop,time_now): #check if time is between 7am and 10am #EDIT: removed unnecessary parentheses
    print("Eet je hagelslag!") #if it is, print a message #EDIT: bad indentation, changed from 3 spaces to 4
else:
    print("Gut gemacht!") #if the time is not within any of these intervals, print a message #EDIT: bad indentation, changed from 3 spaces to 4


#Q3.2P.7
#There is discussion about naming constant variables: PEP8 wants constant variables to be named in UPPER_CASE
#However, the discussion is about how PEP8 detects constant variables and when to actually name them in UPPER_CASE 
    #(see: https://github.com/PyCQA/pep8-naming/issues/49)
#I had numerous suggestions from pylint to change variables into UPPER_CASE
#However, they were often not constant variables but would be changed later in the script
#I agree with people who say that "constant variables" are ones that never change in value throughout the script
#Therefore only those variables should be named in UPPER_CASE

#Q3.2P.8
#I chose to improve Michael's jellyfish() function:
    #Variable LineWidths (CamelCase) changed to line_widths (snake_case)
    #Variable "Colors" also doesn't conform to snake_case and isn't very informative. Changed to "colors_to_plot"

#---------------------------------------------------------------------------------------------
#Show plots
plt.show()
