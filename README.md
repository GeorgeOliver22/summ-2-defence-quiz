# summ-2-defence-quiz
IFCS Summative 2 - Quiz

**George Oliver - Summative 2 IFCS** 

## Introduction

There are several different types of data classifications within the Consulting world. Data restrictions can be applied internally, to protect employee anonymity (such as personal information like age and gender), or there can be wider frameworks that dictate data handling, protection and distribution - these frameworks are often dictated by security clearance, with proper vetting completed for individuals to access specific data types. 

Working within the Defence Industry means that there is a need to handle several different classes of sensitive data. Each type of sensitive data comes with different security protocols and can only be handled/distributed in a specific manner due to confidentiality. There is an increased need for data protection within the Defence industry due to the wide-reaching consequences of improper data handling. For the most part, my project role involves the handling of confidential data marked as OFFICIAL-SENSITIVE (OS). OS data is a subset of information marked as 'OFFICIAL' within the UK. OS data is of a higher classification and therefore requires stricter and more careful handling - in terms of how data is stored and distributed. 

Data protection ensures that only personnel with the relevant security clearances have access to restricted data, whether this be internal clearance/approval to handle Sensitive Personal Information (SPI), or externally to handle classified information (such as information marked as OS or SECRET). 

For this project, I have created a quiz to test employee understanding of different types of classfiied data that they will come across while working in the Defence Industry (specifically within my project). To achieve this, I have created a quiz app as a 'MVP' (Minimum Viable Product) to test employee understanding and reinforce proper data protection practices. The quiz app presents questions on data restrictions/classifications in the format of Question, OptionA, OptionB, OptionC - meaning it is multiple choice for the respondent. 

## Requirements

The following are the defined requirements of the project. I have included details of both Functional and Non-Functional requirements. Functional requirements are the conditions which state what the quiz (app in Tkinter) must do to function as expected, whereas Non-Functional requirements are those that will define how well the app must perform. Essentially the difference is what the app must do versus how the app does it. 

### Functional Requirements 

- Requirement 1: The app (Tkinter) must read the questions from the quiz_data.csv file
- Requirement 2: The app (Tkinter) must provide a response to user answers immediately 
- Requirement 3: The user's responses must be exported to the results.csv file upon completion

### Non-Functional Requirements 

- Requirement 4: The app (Tkinter) must use exception handling when dealing with missing data files
- Requirement 5: The app will use Tkinter as its GUI - providing a polished application look

