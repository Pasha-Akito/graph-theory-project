Graph Theory 2021
Pavel Antonov
Student ID: G00373627

## Description

In this project we have made an algorithm to let the user search text files for a specific string input.
We use *Regular Expression* (Regex), *Shunting-yard algorithm*, *Thompson's Construction Algorithm* and *Nondeterministic Finite Automaton* (NFA) to achieve this.
The user will input a string to search for and the file path/name. 
This algorithm we have designed will return all matching strings from the text file.
We achieve this by changing the users' string input into Regex by using the Shunting-yard Algorithm.
We then input the Regex into Thompson's Construction Algorithm which outputs an NFA.
We use this NFA to match identical strings to what the user inputted and then output any matches to them.

-------------------------

## Instructions

- The user will need both python3 and Visual Studio Code. 
- Download and extract the zip.
- In the folder run command prompt.
- There will be a text file, you can edit it and add strings if you choose to but isn't necessary.
- In the command prompt type "python3 main.py"
- A menu will display.
- Press 1 to input a regular expression.
- - After pressing 1, input the file path/name to search that file for the string.
- - You will then be displayed all matching strings from the text file.
- Press 2 to exit the program

-------------------------

## Explanation of the Algorithm

When the user inputs a string, we first need to make sure it is ordered correctly for Thompson's Construction.
We use shuntingre.py to achieve this. shuntingre.py inputs an infix and returns a postfix. In shuntingre.py, if the users' string includes operators, those 
are pushed onto a stack while the rest of the string continues to be concatenated by character. Once shuntingre.py reaches the end of the string, it then takes the first operator 
that was pushed onto the stack and continues to concatenate to the string. After this process is finished, we now have a postfix from the string input the user gave us.

The postfix is in Regex, which we can use to search for specified text. Regex is a quick and short way of explaining Finite Automata. 
We input the postfix into thompson.py. This is Thompson's Construction which is an algorithm that turns Regexes into NFAs. We then use these NFAs to match strings.

-------------------------

## What is a Regular Expression?

- Regular Expression, or Regex, was proposed in the 1950s by Stephen Cole Kleene. 
Back then they would have state-based machines. These machines would need to be easily described when engineers were discussing about them between themselves.
They would draw diagrams to describes the states of these machines, but it was hard to describe a diagram over the phone. So, they at first used chomsky type 3 naming convention to describe these machines over the phone. Kleene thought there was a better and more compact way to talk about these finite automata. So, he proposed Regular Expression, which is the simpliest way to describe finite automaton and languages. Chomsky Type 3, Automaton Diagrams and Regex are all equivalent expressions and mean the same thing. 
- Regular Expressions is a way of defining patterns that are used to find and manage text. We use Regexes all the time without realising it, google and other search engines all utilize Regexes to help us find what we are looking for. Text editors like microsoft word also use Regexes. When a user does a simple search, the application uses regex to find that string of characters. If the user searches for all text files by typing `*.txt`, in the background what is actually being searched for in the text file is `^.*\.txt$`. The syntax of regexes seems confusing at first but are very useful and compact.

-------------------------

## How do regular expressions differ across implementations?

-------------------------

## Can all formal languages be encoded as regular expressions?

-------------------------

## Research done
- Thompsons Construction Algorithm
https://en.wikipedia.org/wiki/Thompson%27s_construction

- Shunting Yard Algorithm
https://en.wikipedia.org/wiki/Shunting-yard_algorithm

- Regular Expression
https://en.wikipedia.org/wiki/Regular_expression
https://www.computerhope.com/jargon/r/regex.htm
https://www.regular-expressions.info/
https://www.youtube.com/watch?v=528Jc3q86F8&t=874s&ab_channel=Computerphile
