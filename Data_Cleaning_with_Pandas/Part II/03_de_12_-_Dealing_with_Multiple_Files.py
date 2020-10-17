"""
DATA CLEANING WITH PANDAS
Dealing with Multiple Files
Often, you have the same data separated out into multiple files.

Let’s say that we have a ton of files following the filename structure: 'file1.csv', 'file2.csv', 'file3.csv', and so on. The power of pandas is mainly in being able to manipulate large amounts of structured data, so we want to be able to get all of the relevant information into one table so that we can analyze the aggregate data.

We can combine the use of glob, a Python library for working with files, with pandas to organize this data better. glob can open multiple files by using regex matching to get the filenames:

import glob

files = glob.glob("file*.csv")

df_list = []
for filename in files:
  data = pd.read_csv(filename)
  df_list.append(data)

df = pd.concat(df_list)

print(files)
This code goes through any file that starts with 'file' and has an extension of .csv. It opens each file, reads the data into a DataFrame, and then concatenates all of those DataFrames together.
"""
import codecademylib3_seaborn
import pandas as pd
import glob

"""
We have 10 different files containing 100 students each. These files follow the naming structure:

exams0.csv
exams1.csv
… up to exams9.csv
We are going to import each file using pandas, and combine all of the entries into one DataFrame.

First, create a variable called student_files and set it equal to the glob() of all of the csv files we want to import.
"""
student_files = glob.glob("exams*.csv")
print("student_files: \n" + str(student_files))

"""
Create an empty list called df_list that will store all of the DataFrames we make from the files exams0.csv through exams9.csv.
"""
df_list = []

"""
Loop through the filenames in student_files, and create a DataFrame from each file. Append this DataFrame to df_list.
"""
for i in student_files:
  df = pd.read_csv(i)
  df_list.append(df)
print("df_list: \n" + str(df_list))

"""
Concatenate all of the DataFrames in df_list into one DataFrame called students.
"""
students = pd.concat(df_list)

"""
Print students and the length of students. Did we get all of them?
"""
print("students: \n" + str(students))
print("lenght of students dataframe: \n" + str(len(students)))



