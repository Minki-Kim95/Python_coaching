# Python coaching program

This is SKKU's teaching program for learning how to do coding more practical and efficially.

## Purpose of repository

This repository is used for submission of assignments.

### Week 1

* How to do unit test and do a little assignments

Assignment1

```
Write code to reverse a given string  (without python reverse fuction)

ex) input: abc  //   return: cba,
```

Assignment2

```
When two strings are given, print the common characters from both strings 
(all the characters possible involved in ASCII possible)

ex) input: aflji, sefoh   //  output: f 
```


### Week2

* learn how to use flask and understand HTTP protocol and HTML

Assignment1

```
1. install Flask
2. make a web server code which return "Hello world" by flask
3. learn about requirements.txt and put the moduls in there
4. use pylint to check style of code
```

Assignment2

```
1. Ask the name of vistor and attach that behind the Hello world and return it

ex) input: Gil-dong -> return: Hello world Gil-dong
2. use pylint to check code style
```

Assignment3

```
Implement a web service that returns a yard when you enter a meter.
(error handling when client typing non-numeric value)
ex) input: 3 -> 3.28084
input: face -> reload with alert "please type number"
```


### Week3

* Edit hangman game code and store the score by RDBMS
* hangmen code from (https://github.com/keeyong/hangman)

Assignment1

```
1. read words in file (words1.txt)
2. store highest score in file (highest_score1.txt)
standard of highest score: Least number of missed letter
```

Assignment2

```
1. Use database (not file)
2. Use Sqlite
```



### Week4

* Lanch on server by EC2 (AWS)

Assignment

```
make hangman game code can run on website by flask
```


## Final

* Enron email problem

Assignment1

```
How many emails did each person receive each day?
```

Assignment2

```
Let's label an email as "direct" if there is exactly one recipient and "broadcast" 
if it has multiple recipients. Identify the person (or people) 
who received the largest number of direct emails and the person (or people) 
who sent the largest number of broadcast emails.
```

Assignment3 (bonus question)

```
Find the five emails with the fastest response times. 
(A response is defined as a message from one of the recipients to the original sender 
whose subject line contains all of the words from the subject of the original email, 
and the response time should be measured as the difference between 
when the original email was sent and when the response was sent.). 
```
## Mentor

* **Han Keeyong** - *Code Reviewer* - [Account](https://github.com/keeyong)
