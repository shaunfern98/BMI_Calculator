# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 22:57:33 2024

@author: shaun
"""
# importing libraries
import turtle

# define function that takes height and weight as arguments
# calculates BMI and respective classification
def bmi_calculator(height,weight):
    bmi = (703*weight)/height**2
    statement = ""
    if bmi < 16:
        statement = "Underweight - Severe Thinness"
    elif bmi > 16 and bmi <= 16.9:
        statement = "Underweight - Moderate Thinness"
    elif bmi > 16.9 and bmi <= 18.4:
        statement = "Underweight - Mild Thinness"
    elif bmi > 18.4 and bmi <= 24.9:
        statement = "Normal Range"
    elif bmi > 24.9 and bmi <= 29.9:
        statement = "Overweight"
    elif bmi > 29.9 and bmi <= 34.9:
        statement = "Obese - Class 1"
    elif bmi > 34.9 and bmi <= 39.9:
        statement = "Obese - Class 2"
    else:
        statement = "Obese - Class 3"
    return print("You have a BMI of "+str(bmi)+" and are classified as "+statement)

# user inputs
height = int(turtle.textinput("User Height", "What is your height in inches?"))
weight = int(turtle.textinput("User Weight", "What is your weight in pounds (lbs)?"))

# calling on function using user inputted values
bmi_calculator(height,weight)