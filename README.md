# Advent-of-Code-2024
My solutions for the Advent of Code 2024 challenges. Not all of them will be coding solutions. Documentation of solution strategy will be done in the README (hopefully).

## Process Overview
A lot of my other attempts at the Advent of Codes last year have ended with me getting roadblocked becuase I wanted to approach everything as a coding challenge. My goal this year is just to get 15 stars (the amount my Computer Science teacher challenges us to get) by any means possible. I'm treating this more as a porblem solving chanllenge than a coding one. I will still code solutions as necissary, but spreadsheets, diagrams, brute foce logic, and all other approaches are fair game.

## Table of Contents
- [Advent-of-Code-2024](#advent-of-code-2024)
  - [Table of Contents](#table-of-contents)
  - [Day 1](#day-1)
    - [Part 1](#part-1)
    - [Part 2](#part-2)

## Day 1
### Part 1
Though this sounded like an interesting enough coding challenge, I concluded the easiest approach would be to use a spreadsheet. After copy-pasting the input, formatting the data to split on spaces, reordering each column to arrange themselves "alphabetically" (in this case it would sort numerically since it was only dealing with numbers), finding the absolute difference of the columns and summing them were two easy Excel functions.

[Day 1 Part 1 Solution](link)

### Part 2
This is just above my Excel skills. Though I'm sure some cool function exists for it, I do not know them and didn't know the best way to search them up [if I had to guess, the key words would be "repetition" or "duplicates"]. Advent of Code also provides a great excuse to practice languages I'm out of practice with and, given I've been learning C++ in school for the past four months, I decided to take a break and program in Python. I quickly discovered I am gratefully out of practice with Python; a fact that is sure to make the future challenges a lot more fun.

Reading in the file was as simple as remembering my roots, and internalizing that .csv files are read in as arrays line by line so I could access them by element. The only thing that caused issues in this part was having to make sure it was reading in each element as an integer. I didn't do this until the very end and it caused a lot of annoying errors later. I guess an advantage of languages like C++ is that they force you to think about situations like this initially so you couldn't run into these errors, even if you wanted to. 
Gathering the similarity score was another simple double for-loop. I am confident I could do this in an nlogn format by at least sorting the list and if I had to guess, extensions like numpy could help remove the second for loop entirely with a fancy function, but, alas, here we are. Here is also where Python interpreting the input as strings came to bite me. I believe it was somehow interpreting the ASCII values of each number leading to ridiculously higher numbers than wanted. 
Summing the terms was done in another simple function at the bottom of the code.

[Day 1 Part 2 Solution](link)