# My solutions for some of the simple python coding challanges available online.
I had done these challenges a long time ago in Python 2.x. The programs are re-written them in Python 3.x for reference.<br />
Courtesy: I have solved only some of the question created by https://github.com/zhiwehu<br />
Link to the original challenges: <br />
https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt <br />
The solutions are uploaded as .py files with the same name is the question. For example. Solution for Question 6 is Q6.py <br />
Question 6,7,8,18,19,20,21,22 <br />
## These question are of Level 3 in the original challenges list. <br />
* __Q6 : Write a program that calculates and prints the value according to the given formula__:
Q = Square root of [(2 * C * D)/H]<br />
* __Q7 : Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.__  <br />
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
* __Q8: Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.__
Suppose the following input is supplied to the program: <br />
without,hello,bag,world <br />
Then, the output should be: <br />
bag,hello,without,world <br />
* __Q18:A website requires the users to input username and password to register. Write a program to check the validity of password input by users.__  <br />
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
* __Question 19__
Level 3

Question:
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80 <br />
John,20,90 <br />
Jony,17,91 <br />
Jony,17,93 <br />
Json,21,85 <br />
Then, the output of the program should be: <br />
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use itemgetter to enable multiple sort keys.

* __Question 20__

Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield

* __Question 21__
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5 <br />
DOWN 3 <br />
LEFT 3 <br />
RIGHT 2 <br />
¡­ <br />
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example: <br />
If the following tuples are given as input to the program: <br />
UP 5 <br />
DOWN 3 <br />
LEFT 3 <br />
RIGHT 2 <br />
Then, the output of the program should be: <br />
2 <br />

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

* __Question 22__

Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:<br />
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3. <br />
Then, the output should be: <br />
2:2 <br />
3.:1 <br />
3?:1 <br />
New:1 <br />
Python:5 <br />
Read:1 <br />
and:1 <br />
between:1 <br />
choosing:1 <br />
or:2 <br />
to:1 <br />

Hints <br />
In case of input data being supplied to the question, it should be assumed to be a console input. <br />

