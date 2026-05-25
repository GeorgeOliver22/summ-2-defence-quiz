# summ-2-defence-quiz
IFCS Summative 2 - Quiz

**Summative 2 IFCS** 

## Introduction

There are several different types of data classifications within the Consulting world. Data restrictions can be applied internally, to protect employee anonymity (such as personal information like age and gender), or there can be wider frameworks that dictate data handling, protection and distribution - these frameworks are often dictated by security clearance, with proper vetting completed for individuals to access specific data types. 

Working within the Defence Industry means that there is a need to handle several different classes of sensitive data. Each type of sensitive data comes with different security protocols and can only be handled/distributed in a specific manner due to confidentiality. There is an increased need for data protection within the Defence industry due to the wide-reaching consequences of improper data handling. For the most part, my project role involves the handling of confidential data marked as OFFICIAL-SENSITIVE (OS). OS data is a subset of information marked as 'OFFICIAL' within the UK. OS data is of a higher classification and therefore requires stricter and more careful handling - in terms of how data is stored and distributed. 

Data protection ensures that only personnel with the relevant security clearances have access to restricted data, whether this be internal clearance/approval to handle Sensitive Personal Information (SPI), or externally to handle classified information (such as information marked as OS or SECRET). 

For this project, I have created a quiz to test employee understanding of different types of classfiied data that they will come across while working in the Defence Industry (specifically within my project). To achieve this, I have created a quiz app as a 'MVP' (Minimum Viable Product) to test employee understanding and reinforce proper data protection practices. The quiz app presents questions on data restrictions/classifications in the format of Question, OptionA, OptionB, OptionC - meaning it is multiple choice for the respondent. 

## Requirements

The following are the defined requirements of the project. I have included details of both Functional and Non-Functional requirements. Functional requirements are the conditions which state what the quiz (app in Tkinter) must do to function as expected, whereas Non-Functional requirements are those that will define how well the app must perform. Essentially the difference is what the app must do versus how the app does it. 

### Functional Requirements 

- **Requirement 1**: The app (Tkinter) must read the questions from the quiz_data.csv file
- **Requirement 2**: The app (Tkinter) must provide a response to user answers immediately 
- **Requirement 3**: The user's responses must be exported to the results.csv file upon completion

### Non-Functional Requirements 

- **Requirement 4**: The app (Tkinter) must use exception handling when dealing with missing data files
- **Requirement 5**: The app will use Tkinter as its GUI - providing a polished application look

## Initial Design & Development

For the design of this assignment, I chose to utilise Python's built-in Tkinter framework as the Graphic User Interface (GUI). I chose this tool due to my familiarity with it and the ease of developing the framework for the quiz directly in Tkinter via VisualStudio - where I wrote the code. This allowed me to troubleshoot the design easily as it progressed, and make changes easily. During the initial design, I created the overall framework for the visual display of the quiz - I focussed on making it visually how I wanted the end product to be, rather than functionally (so just the interface was complete with an initial tester question). As a result, my initial design prototype included only the essential information and tools to allow a respondent to view a question and possible responses. 

To begin, I set up the Tkinter by importing the standard Tkinter framework and then coded to include the followiing 3 essential pieces of information:
    
- **Element 1**: Quiz Title at the top - 'Security Classifications Quiz'
- **Element 2**: Question - 'What does OS stand for?'
- **Element 3**: Drop-down box with possible answers - this would provide the respondent with 3 options in a drop-down box for how they could respond to the initial question

I chose to utilise a drop-down box as the answer type for this quiz to reinforce data integrity - a drop-down means that the user and only select an answer from a predetermined list of values. This eliminates the risk of user-error through spelling errors, or inputting an empty value. It will ensure that all users are able to respond with the same answers when completing the quiz - making it easy to analyse and catagorise once all answers from respondents are collated. To utilise a drop-down box in the Tkinter I imported the **'tk.OptionMenu'** widget - this allows for me to create values which will appear in the drop-dwon for the user and be selectable. 

Alongisde the physical question screen for the Tkinter, I also set-up an initial name screen where the respondent would be able to input their name prior to commencing the quiz. I added logic to the logic.py file to dictate that the respondent had to input a name greater than 2 characters in length. This would ensure that respondent names will be fully captured and transported into the **results.csv** file when I eventually built out the entire quiz app. The logic I added ensured that an error is returned if the respondent tried to skip the name screen, or not input their full name - it acts as a pre-requisite to start the actual quiz. To ensure that the user could not bypass the name element of the quiz, I utilised the **'messagebox'** library tool to cause an alert pop-up if the name inputted was <2 characters - it would return an error prompting the user to input a name that was >2 characters in order to proceed. Finally, I also utilised an f-string to link the name inputted on the first interface to the rest of the quiz. The f-string '**f"Employee{self.user_name}"**' meant that for all subsequent quetsions on the quiz, the Tkinter would present the user's inputted name at the top of the screen - allowing for a customised quiz experience for each user. 

Once the user inputs their full name, the logic verifies that it is greater than two characters and then allows the respondent to progress to the first question of the quiz. To transfer from the name page to the first question of the quiz, I utilised the **'clear_screen'** command - this is a command that allows from seamless transition from one slide to another of the quiz - it removes clutter as it just wipes the information on the inital screen and replaces it with the next - neatly moving from inputting a name to answering the first question. 

## Building Out The Quiz - Further Development

This phase of the development focused on shifting away from a simple visual prototype, to a polished quiz app that prompts the user to answer several different questions - moving through the list of questions within the **quiz_data.csv** file. I expanded on the development of the app in this phase of the development by integrating the **csv** files into the quiz's logic - this meant that the quiz app was now able to read all the questions directly from the **quiz_data.csv** file and save them into the quiz's memory as a list of questions which the user is able to move through. Alongside this, I added three tracking variables to the code, so that the quiz is able to track what question the user is on, who the user is and how they are performing in the quiz. The three variables were added within the **__init__** function: 

- **self.current_question_index = 0** - what question the user is on
- **self.user_name = ""** - who the user is
- **self.score = 0** - how the user is performing

These changes effectively provided the quiz app with a memory, being able to track performance and move through the list of questions in a cyclical nature. 

I also added a dictionary mapping for results within the app. The **csv** file stores the answer as a simple letter (A, B, C etc), whereas in the quiz the user clicks on an expanded answer, rather than a single letter. To ensure that the user's answer is able to be translated into a single letter which the **csv** file can store, I added the following - **mapping = {'A': 'OptionA', 'B': 'OptionB', 'C': 'OptionC'}**. This code ensures that when the quiz compares a user's selection to the possible answers (A, B, C etc), it is able to recognise which answer refers to which letter, removing any logic errors. 

The final core change I made in this development was completing the **clear_screen** loop. The completion of this loop ensured that when the user moves from one question to the next, it is a smooth transtiion as it deletes the exisiting screen (including text) and smoothly moves onto the new one.

This section of the development successfully moved the quiz from a simple dummy app, to a smart quiz that moved through a list of questions and kept track of user performance. 