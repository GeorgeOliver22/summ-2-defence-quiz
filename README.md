# summ-2-defence-quiz
IFCS Summative 2 - Quiz

**Summative 2 IFCS** 

## Introduction

Data restrictions can be applied internally, to protect employee anonymity, or there can be wider frameworks that dictate data handling, protection and distribution.

Working within the Defence Industry means that there is a need to handle several different classes of sensitive data. Each type of sensitive data comes with different security protocols. There is an increased need for data protection within the Defence industry due to the wide-reaching consequences of improper data handling. For the most part, my project role involves the handling of confidential data marked as OFFICIAL-SENSITIVE (OS). OS data is of a higher classification and therefore requires stricter and more careful handling - in terms of how data is stored and distributed. 

Data protection ensures that only personnel with the relevant security clearances have access to restricted data.

## Requirements

Functional requirements are the conditions which state what the quiz (app in Tkinter) must do to function as expected, whereas Non-Functional requirements are those that will define how well the app must perform. Essentially the difference is what the app must do versus how the app does it. 

### Functional Requirements 

- **Requirement 1**: The app (Tkinter) must read the questions from the quiz_data.csv file
- **Requirement 2**: The app (Tkinter) must provide a response to user answers immediately 
- **Requirement 3**: The user's responses must be exported to the results.csv file upon completion

### Non-Functional Requirements 

- **Requirement 4**: The app (Tkinter) must use exception handling when dealing with missing data files
- **Requirement 5**: The app will use Tkinter as its GUI - providing a polished application look

## Initial Design & Development

I chose to utilise Python's built-in Tkinter framework as the Graphic User Interface (GUI). I chose this tool due to my familiarity with it and the ease of developing the framework for the quiz directly in Tkinter via VisualStudio. This allowed me to troubleshoot the design easily as it progressed, and make changes easily. I created the overall framework for the visual display of the quiz - I focussed on making it visually how I wanted the end product to be, rather than functionally. As a result, my initial design prototype included only the essential information.

To begin, I set up the Tkinter by importing the standard Tkinter framework and then coded to include the following pieces of information:
    
- **Element 1**: Quiz Title - 'Security Classifications Quiz'
- **Element 2**: Question - 'What does OS stand for?'
- **Element 3**: Drop-down box - this would provide the respondent with 3 options for how they could respond to the initial question

I chose to utilise a drop-down box as the answer type for this quiz to reinforce data integrity - a drop-down means that the user can only select an answer from a predetermined list of values. This eliminates the risk of user-error through spelling errors, or inputting an empty value. It will ensure that all users are able to respond with the same answers when completing the quiz - making it easier to analyse and catagorise. To utilise a drop-down box in the Tkinter I imported the **'tk.OptionMenu'** widget - this allows for me to create values which will appear in the drop-dwon for the user and be selectable. 

Alongisde the physical question screen for the Tkinter, I also set-up an initial name screen. I added logic to the **logic.py** file to dictate that the respondent had to input a name greater than 2 characters. This ensured that respondent names will be fully captured and transported into the **results.csv** file. The logic I added ensured that an error is returned if the respondent tried to skip the name screen, or not input their full name. To ensure that the user could not bypass the name element of the quiz, I utilised the **'messagebox'** library tool to cause an alert pop-up if the name inputted was <2 characters - it would return an error prompting the user to input a name that was >2 characters. Finally, I also utilised an f-string to link the name inputted on the first interface to the rest of the quiz. The f-string '**f"Employee{self.user_name}"**' meant that for all subsequent quetsions on the quiz, the Tkinter would present the user's inputted name at the top of the screen - allowing for a customised quiz experience for each user. 

Once the user inputs their full name, the logic verifies that it is greater than two characters and then allows the respondent to progress to the first question of the quiz. To transfer from the name page to the first question of the quiz, I utilised the **'clear_screen'** command - this is a command that allows from seamless transition from one slide to another of the quiz - neatly moving from inputting a name to answering the first question. 

## Building Out The Quiz - Further Development

This phase focused on shifting away from a simple visual prototype, to a polished quiz app that prompts the user to answer several different questions - moving through the list of questions within the **quiz_data.csv** file. I expanded on the development by integrating the **csv** files into the quiz's logic - this meant that the quiz app was now able to read all the questions directly from the **quiz_data.csv** file and save them into the quiz's memory as a list of questions which the user is able to move through. Alongside this, I added three tracking variables to the code. The three variables were added within the **__init__** function: 

- **self.current_question_index = 0** - what question the user is on
- **self.user_name = ""** - who the user is
- **self.score = 0** - how the user is performing

These changes effectively provided the quiz app with a memory, being able to track performance and move through the list of questions in a cyclical nature. 

I also added a dictionary mapping for results within the app. The **csv** file stores the answer as a simple letter (A, B, C etc), whereas in the quiz the user clicks on an expanded answer, rather than a single letter. To ensure that the user's answer is able to be translated into a single letter which the **csv** file can store, I added the following - **mapping = {'A': 'OptionA', 'B': 'OptionB', 'C': 'OptionC'}**. This code ensures that when the quiz compares a user's selection to the possible answers (A, B, C etc), it is able to recognise which answer refers to which letter, removing any logic errors. 

Finally I completed the **clear_screen** loop. The completion of this loop ensured that when the user moves from one question to the next, it is a smooth transtiion as it deletes the exisiting screen (including text) and smoothly moves onto the new one.

## Testing The Quiz App

To test functionality, I created an automated testing suite that could be run directly from the terminal. The code within the **test_logic.py** file tests the core logic functions of my quiz app. There are two primary areas that it tests:

- User Name - I added three validation checks to ensure that the user's name is correctly recorded. It ensures that a user is not able to input a single letter name or a blank value. This ensures that the user's name is full and recorded for their quiz. 
- Correct Answers - I added two new code elements to verfiy whether a users answer is correct or not. The code added contains two " " values within the line - if they are the same, it will return a **TRUE** value, whereas if there is a mismatch it will return a **FALSE** value, showing that the user's answer is incorrect.

When I run these tests in the terminal, using the **python3 -m unittest tests/test_logic.py** command it verifies that the code I have written is functioning correctly - proviign instant techincal evidence that my app is configured properly and can be used as intended by the user. Furthermore, running these tests in the terminal and returning an **OK** value, shows the systematic testing of my app and evidence that I tested the app's functionality as I designed/created it. 

I also completed a series of manual tests. The table below shows the tests and their results:

| Test | Expected Behaviour | Actual Result | Pass/Fail |
| User name blank | Error pop-up and user cannot continue test | Alert triggered and user cannot continue | PASS |
| User name too short | Error pop-up and user cannot continue test | Alert triggered and user cannot continue | PASS |
| Dropdown validation | User unable to move to next question if no answer selected | Alert triggered and user cannot continue | PASS |
| Quiz termination | Upon submission of final answer, quiz provides user score and clears page | Page cleared and score presented | PASS |

The tests above verify the physical GUI interface is perfoming as expected. I needed to couple the automated tests with manual testing because the unittests are unable to actually verify the physical quiz app pop-up behaviour - i.e. ensuring errors present when necessary etc. Therefore, by doing manual testing as well I am able to verfiy both the app's code and the app's physical behaviour. 

## User Documentation - End-user

The following instructions are for employees who are completing the test:

- Launch test - run **python3 main.py** in the terminal
- Login - enter full name and click **start**
- Answers - click the dropdown menu and select the correct answer and press **submit**
- End Test - upon completion of final question you will be presented with your score, just click the cross in the corner to close app and end the test

## User Documentation - Testing

The following instructions are for employees who want to verify the app logic:

- Ensure you have python installed
- Ensure the **quiz.data.csv** file is set up within the **data** folder
- In the terminal, type **python3 -m unittest tests/test_logic.py**
- To confirm GUI operation, launch the quiz using **python3 main.py** in the terminal 

## Evaluation 

I was pleased with the overall creation of my quiz app. There were a few key decisions that I made during the design phase that I believe contributed to a clean and functional app. Firstly, the decision to separate the physical app code (within **main.py**) and the core validation logic (within **logic.py**) allowed for a clean automated testing suite that did not affect the core app's code stability. Also, by storing the quiz question data in an external **csv** file, it means that the quiz's questions are separate from the app logic - so this means that the quiz could be easily scaled by a non-techincal person by simply adding questions to the **csv** file, while not having to alter the core logic at all. 

While largely content, I faced several troubleshooting issues along the way - ranging from simple formatting and indentation errors, to more complex syntax errors. Troubleshooting these errors helped to improve my code's quality and also ensure that I was fully focussed throughout the development. The troubleshooting I completed along the way was the most important part of the project as it provided the opportunity for specific targetted learning and improvements of my coding quality control. I also realised at the end during my reflection that I had not added the code within the **main.py** file to save the user responses and record them into the **results.csv** file. This was a good catch and I was then able to add in the relevant code within the Quiz App section of the main code body. 

One future enhancement I would make to the app would be to add a timing element to the quiz. I could use Tkinter's incorporated **.after()** feature to crate a visual timer for the user so that there is a time-pressured element to the quiz, meaning questions must be answered within a specific window of time. 