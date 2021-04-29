Graph Theory 2021
Pavel Antonov
Student ID: G00373627

## Description

In this project we have made an algorithm to let the user search text files for a specific string input.
We use *Regular Expression* (regex), *Shunting-yard algorithm*, *Thompson's Construction Algorithm* and *Nondeterministic Finite Automaton* (NFA) to achieve this.
The user will input a string to search for and the file path/name. 
This algorithm we have designed will return all matching strings from the text file.
We achieve this by changing the users' string input into regex by using the Shunting-yard Algorithm.
We then input the regex into Thompson's Construction Algorithm which outputs an NFA.
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

The postfix is in regex, which we can use to search for specified text. regex is a quick and short way of explaining Finite Automata. 
We input the postfix into thompson.py. This is Thompson's Construction which is an algorithm that turns regexes into NFAs. We then use these NFAs to match strings.

-------------------------

## What is a Regular Expression?

- Regular Expression, or regex, was theorised in the early 1950s by Stephen Cole Kleene. 
Back then they would have state-based machines. These machines would need to be easily described.
It was hard to describe diagrams over the phone, so notion that can be read easily needed to be used. They at first used chomsky type 3 naming convention to describe these machines over the phone. Kleene thought there was a better and more compact way to talk about these finite automata. He proposed Regular Expression, which is the simplest way to describe finite automaton and languages. Chomsky Type 3, Finite Automaton and Regex are all equivalent expressions and mean the same thing. In the 1960s Ken Thompson implemented pattern matching using Kleene's regex notion.
- A Regular Expression is a string that helps you search for text. Search engines use regexes to find matches from the string we entered. Many text editors also use regexes. There are special characters that can be used to help us refine our searches, an example of this would be wildcard asterix `*`. If we are looking for all mp4 files on our system, we can input `*.mp4` in the file directory. The asterisk `*` wildcard indicates anything ending in `.mp4` will result in a match and will display all the mp4 files we have. This is a basic example of regexes. 
- Regular Expressions are a notation for describing sets of strings. When a string is in the set described by a regex, the regex matches the string. We are able to concatenate two different regexes to form a new regex. This would work similiar to *Logic OR Function* and we would use a vertical bar to denote this `|`. `dog | cog` can match with `dog` or `cog`. Another way to describe sets of strings is with Finite Automata. They are also known as state-based machines. 

-------------------------

## How do regular expressions differ across implementations?

- There are many implementations of regexes from how the engine runs and to the language itself. There are two different types of using regexes in engines. The first being regex-directed  We first introduce a regex token to a regex engine. The engine then tries the regex on every single character in the text file and tries to find a match. If a match is found, it will continue through the regex and the matched string. 

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
https://www.regular-expressions.info/tutorial.html
https://programminghistorian.org/en/lessons/understanding-regular-expressions
https://www.youtube.com/watch?v=528Jc3q86F8&t=874s&ab_channel=Computerphile
https://www.cs.rochester.edu/u/nelson/courses/csc_173/fa/re.html#:~:text=Concatenation%3A%20If%20R1%20and%20R2,R1R2%20(also%20written%20as%20R1.&text=Kleene%20closure%3A%20If%20R1%20is,is%20also%20a%20regular%20expression.

- Finite Automata
https://www.javatpoint.com/automata-regular-expression