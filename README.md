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

 3. Download the pytest library

         pip install pytest

In the video tutorial, I run pytest after every line of code. This is because I want to ensure every line of code works, rather than creating a snowball effect of errors that have to be debugged at the end of code execution.

To test whether pytest is working correctly, it is beneficial to use the simplest line of code to run:

       def test_example():
           assert 1 == 1

It is vital to name the module and function with **test**, as it allows pytest to know that this is a test when run in the terminal. This is explained more in the [video](https://northeastern-my.sharepoint.com/personal/akpobi_o_northeastern_edu/_layouts/15/stream.aspx?id=%2Fpersonal%2Fakpobi%5Fo%5Fnortheastern%5Fedu%2FDocuments%2Fsumative%201%20video%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2Ebd448d5a%2D741e%2D4584%2Da8be%2Daeeefedfc033) tutorial, this is a brief overview.



## CI/CD using GitHub actions.

Continuous Integration is the practice of:

+ Frequently merging code changes into a shared repository

+ Automatically running tests each time code is pushed

CD — Continuous Delivery / Continuous Deployment is the practice of:

Continuous Delivery:  
 + Code that passes tests is automatically prepared for release, but a human decides when to deploy.

Continuous Deployment:  
 + Every change that passes the pipeline is deployed to production automatically.


**GitHub actions** 

GitHub Actions is an automation platform built into GitHub. It lets you create workflows that run automatically when something happens in your repository, such as:

+ pushing code

+ opening a pull request

+ creating a release

GitHub Actions can automatically run tasks on your Python applications.



This is the final code shown at the end of the video.

       def fizzbuzz(n):
           if n % 15 == 0:
             return "FizzBuzz"
           elif n % 3 == 0:
             return "Fizz"
           elif n % 5 ==0:
             return "Buzz"
                else:
                return n 

       if __name__ == "__main__": # this means that only when this file in run directly, it returns values 
            for i in range(1,101):
              print(fizzbuzz(i))

## Conclusion

This is a brief overview of the integration of pytest and CI/CD with the fizzbuzz python program. For an indepth tutorial and overview you can access the video [here](https://northeastern-my.sharepoint.com/personal/akpobi_o_northeastern_edu/_layouts/15/stream.aspx?id=%2Fpersonal%2Fakpobi%5Fo%5Fnortheastern%5Fedu%2FDocuments%2Fsumative%201%20video%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2Ebd448d5a%2D741e%2D4584%2Da8be%2Daeeefedfc033)

