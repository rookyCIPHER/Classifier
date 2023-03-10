# -*- coding: utf-8 -*-
"""Classifier_Rohan_Manro_till_handling_binsize

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1thTYiQOw1Ka8E27z7m0BsFCmh-ec0hgx

First of all giving permission to google colab so that it can access the files
"""

# Commented out IPython magic to ensure Python compatibility.
from google.colab import drive
drive.mount('/content/drive')
# %cd /content/drive/MyDrive

import csv

"""Reading the data

"""

#Dividing the data in test and training data but first getting total number of rows, then only adding 90% of it to training data.
data=[]
number_of_rows=0
with open('A_Z Handwritten Data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      number_of_rows+=1
      data.append(list(row))

"""Segregating the data"""

# segregating the read data
# train_data=[]
# test_data=[]
# counter=0
# for i in data:
#   counter+=1
#   if counter<=(0.9*number_of_rows):
#     train_data.append(i)
#   else: 
#     test_data.append(i)

#THIS IS COMMENTED OUT FOR THE REASON EXPLAINED IN BELOW COMMENTS

# #Now the next step is to calculate p(y=k) where k belongs to [0,25]
# dict1={}
# counter_list=[]  
# #will store the first column of each row and then we will use counter to count number of times a particular one appears and then divide by total number to get probability by favourable/total

# for i in train_data:
#   counter_list.append(i[0])

# #Now our next step is to assign the number and the probability of each as key value pair in dictionary, we are using dictionary because it uses hash mapping ang take less time to fetch data
# counter_set=set(counter_list)   #just to remove the duplicates and see all the labels that have been covered in the training data
# print(counter_set)
# #OUTPUT=['0', '1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '21', '3', '4', '5', '6', '7', '8', '9']
# #so we can see if we use training data then not all the labels between 0 to 25 are covered. So for calculating P(Y=k) we need to first shuffle the data and then segregate it and that's why above part was commented out

import random
random.shuffle(data)

#segregating the read data
train_data=[]
test_data=[]
counter=0
for i in data:
  counter+=1
  if counter<=(0.9*number_of_rows):
    train_data.append(i)
  else: 
    test_data.append(i)

"""Calculation P(Y=k)"""

#Now the next step is to calculate p(y=k) where k belongs to [0,25]
dict1={}
counter_list=[]  
#will store the first column of each row and then we will use counter to count number of times a particular one appears and then divide by total number to get probability by favourable/total

for i in train_data:
  counter_list.append(i[0])

#Now our next step is to assign the number and the probability of each as key value pair in dictionary, we are using dictionary because it uses hash mapping ang take less time to fetch data
counter_set=set(counter_list)   #just to remove the duplicates and see all the labels that have been covered in the training data. These will help in adding keys to the dictionary

#Calculating P(y=k) and adding to dictionary
for i in counter_set:
  probability=counter_list.count(i)/len(counter_list)
  dict1[i]=round(probability,6)

print(dict1)

"""Addressing the problems of creation of bins, initially taking it be bin size of 8. """

bin_dict={}  #again using dictionary for associating

key=0
for i in range(0,256):
  if 32*key<=i and i<32*(key+1):
    bin_dict[i]=key
  else:
    bin_dict[i]=key+1 #because otherwise numbers such as 32,64 where if statements are not satisfied would never be added to dictionary.
    key+=1
#so we are creating a bin size of 8 i.e. all the pixels which were taking values between 0 to 255 will now be scaled down to take values between 0 to 7
#so that means the scaling will take 32 numbers at a time to divide 256 over 8 parts, so numbers in range 0 to 31 will come to 0 then between 32 to 63 to 1 and so on...

print(bin_dict)

"""Now once we have done this we need to change all the data in our training set according to our bin size."""

#so in the train_data list each element is a list which has 785 entries where the first entry is the label and remaining 784 as pixels and we can verify that
print(len(train_data[1]))

#so to convert all 784 pixels according to our bin size, we will take all data by iterating through them and replace them with their corresponding value in the bin dictionary

for i in train_data:
  for j in range(1,785): #starting from index 1 as index 0 is label and we only need to change the pixel data
    i[j]=bin_dict[int(i[j])]
