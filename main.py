# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 08:10:37 2022

@author: Roger Hegstrom(rhegstrom@avc.edu)

For this exercise, write a dictionary that catalogs the classes you took last term - 
the keys should be the class CRN number (without the 'CRN' part), and the values should 
be the title of the class.
Then, write a function 'add class' that takes 2 arguments - a class number and a description - 
and adds the class to your dictionary.  Use this function to add the classes you’re taking this 
term to the dictionary.


Finally, write a function print classes that takes one argument - a Course CRN number  -
 and prints out all the classes you took in that have that CRN or a smaller CRN.


Example output:


>> print_classes(’77693’)
Introduction to Python

if you input a CRN that is not in your dictionary, say 
>> print_classes(’99999’) The print the message: 

No Course 99999 classes taken. numbers that you both did, and did not take! 
"""

classes = {}

def add_class(crn, name):
    classes[crn] = name

def print_classes(crn):
    if crn in classes:
        print(f'[CRN:{crn}] - {classes[crn]}')
    else:
        print(f'No course {crn} is being taken this semester.')




# Spring 2022
add_class(36783, 'CIS123 - Assem Lang & Computer Architecture')
add_class(36789, 'ELTE145 - Acceptability of Electronic Assemblies')

# Fall 2022
add_class(77693, 'CIS177 - Introduction to Python')
add_class(77896, 'ENGL101 - English Composition')



# Example of displaying classes ive taken this semester
print('Classes taken in fall 2022:')
print_classes(77693)
print_classes(77896)


# Print a non-existant class test case
print('\n\nNon-existant class test case:')
print_classes(1)
