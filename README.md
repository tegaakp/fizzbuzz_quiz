# Fizzbuzz quiz written tutorial

This is for the summative quiz for IF1 using Fizzbuzz for TDD

# Introduction

This README file will walk you through:

+ FizzBuzz and its code 
+ Test Driven Development and pytest
+ CI/CD using GitHub actions

 **FizzBuzz** is a classic beginner‑friendly programming challenge that tests your ability to use loops, conditionals, and basic logic.
 
 You’re will need to print a sequence of numbers, usually from 1 to 100, but with a twist:

+ If a number is divisible by 3, print “Fizz”

+ If it’s divisible by 5, print “Buzz”

+ If it’s divisible by both 3 and 5, print “FizzBuzz”

+ Otherwise, print the number itself


The code for this is:

     for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        elif i % 3 == 0:
        print("Fizz")
        elif i % 5 == 0:
        print("Buzz")
        else:
            print(i)

##Test Driven Development and Pytest 

🧪 Test‑Driven Development (TDD)

TDD is a software development approach where you write tests before writing the actual code. The cycle is simple:

+ Write a failing test
  
+ Write the minimum code needed to make the test pass

+ Refactor the code while keeping tests green

**Pytest** is a python testing framework that is run in the terminal 

To install the pytest library, follow these steps ( these instructions are specifically for **MacOS** and for **python 3.9 onwards**:

 1. Create a virtual environment( to download this intro a specific environment rather than downloading it globally)

         python3 -m venv venv

 2. Activate the environment

        source venv/bin/activate



