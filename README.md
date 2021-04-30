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

- A Regular Expression is a string that helps you search for text. Regular Expressions are a notation for describing sets of strings. When a string is in the set described by a regex, the regex matches the string. Search engines use regexes to find matches from the string we entered. Many text editors also use regexes. There are special characters that can be used to help us refine our searches, an example of this would be wildcard asterix `*`. If we are looking for all mp4 files on our system, we can input `*.mp4` in the file directory. The asterisk `*` wildcard indicates anything ending in `.mp4` will result in a match and will display all the mp4 files we have. This is a basic example of regexes. We are able to concatenate two different regexes to form a new regex. This would work similiar to *Logic OR Function* and we would use a vertical bar to denote this `|`. `dog | cog` can match with `dog` or `cog`. Concatenating helps us compact our work easier, instead of having two seperate regexes we are able to put them into one. This is incredibly important when dealing with Finite Automata.

- What are Finite Automata? They are another way to describe sets of strings. They are also known as state-based machines and are used to help us find matches. Finite automata have a start state and then accept states. When we input a string into a Finite Automata, if the string reaches the accept state then we have a match. Lets have `dog` as a regex, we now need to make a finite automata which helps us match that regex. Preferably you would have to use a diagram to describe them but thankfully `dog` would be a simple finite automata. This Automata would have four states and will be a basic example. s1, s2, s3 and s4. s1 is the start state and s4 is the accept state. To go from s1 to s2 you would need `d`, to go from s2 to s3 you would need `o` and finally to get to s4 the accept state you would need `g`. By inputting all possible sets of string in this infite automata the only thing it will accept will be `dog` giving us a match. When we want to describe all possible string in a set we use Kleene's star denoted by `*`. This is what we call a *Deterministic Finite Automata*, or DFA. It is a DFA because no matter the string, it will always be in the one state and not in multiple at once. *Nondeterministic Finite Automata* or NFA are the opposite and there can be more than one possible transition from one state to another, leaving you in multiple states at once. 

- Every regex has an equivalent NFA. To be able to search for text we need to get the NFA equivalent. There are many ways to change regex into NFA but in this project we are using Thompson's method with his algorithm. By using his method we can change any regex into a NFA which we use to match text and then output it to the user.

-------------------------

## How do regular expressions differ across implementations?

- There are many implementations of regex that differ lightly or dramatically in both how they work and their syntax but they are only two sort of engines. A regex engine is an application that can understand regexes and match the given string. These regex engines are usually part of a larger application and we have no access to engine but we can invoke it. The two types of regex engines are *regex-directed engine* and a *text-directed engine*. Modern regex engines are mostly *regex-directed* engines because they have more features that are avalible to the user and most importantly what distingushes them from text-directed engines is *backtracking*. Both types always return the leftmost match. Lets use `h(a|e)ir`  as our regex token and `She changed her hairdo, perfect for an heir` as our string to match in both engine examples. 

- When our regex-directed engines search through the string, it tries to match `h` first, if it doesn't match, it checks the next component of the string for a match. It does this until it reaches `h` and then goes down to the next part of the NFA and tries to first match `a` in `hair`, if `a` fails then it checks for `e` in `heir`. It always attempts the first alternative and then the next. The engine tries to match the first token in the regex and checks the first character `S`, this is not a match and goes to the second character and matches `h`. The engine tries to match the second token `a` with the third character `e` and fails, but we alternated our token, the engine backtracks to the second token again because there are alternatives. It checks the third character again but with `e` and matches. The engine goes to the next third component of the token and tries to match `i` with the fourth character which is a blank space ` ` and fails the match. Because there are no alternatives at the third part of the token it backtracks all the way to the first part of the token and tries to search for `h` again. The 17th upto the 20th character contain a match. The engine goes through the regex token and the string and gives us a match of `hair` from `hairdo`. This might not be the result we were expecting as hairdo is a different string from hair and maybe we were expecting heir to match first. But like I mentioned earlier on, the engine always returns the leftmost match first, it therefore reports the first four letters of `hairdo` as a valid match and doesn't proceed further on to find 'better' matches. Perl uses a regex-directed engine and has additional features like backtracking and more.

- A *text-directed engine* doesn't have backtracking or these additional features. For the most part it is the same and in most cases both engines find the same matches. When the text-directed engine searches strings, it keeps track of all matches that are currently possible. The regex-directed engine, when it failed to match `a` on the third character, it backtracked and searched for `e` on the third character straight away. The text-directed engine when it checks the third character is checking for both `a` and `e`. Up until that point, the engine had two `h` in memory as they were at that point matching with the regex. When the engine sees `e` and no `a`, it removes one of the `h` results and before looking at the fourth character which is a blank space ` ` the engine keeps track of `he` and removes it once trying to match the blank space.

- I've touched mostly on engines, but plenty of languages have regular expressions which although look the same vary largely on syntax and functionality.

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
https://swtch.com/~rsc/regexp/regexp1.html

- Finite Automata
https://www.javatpoint.com/automata-regular-expression
https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton
https://en.wikipedia.org/wiki/Deterministic_finite_automaton

- Regular Expression Engine
https://www.regular-expressions.info/engine.html
https://se.ifmo.ru/~ad/Documentation/Mastering_RegExp/mastregex2-CHP-4-SECT-3.html