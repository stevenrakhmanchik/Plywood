# Plywood Programming Language           
   
[![OSS Status: Healthy](https://img.shields.io/badge/OSS%20Status-Healthy-darkgreen.svg)](OSS_STATUS.md)
![GitHub issues](https://img.shields.io/github/issues-raw/stevenrakhmanchik/Pinewood-Programming-Language)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/stevenrakhmanchik/Pinewood-Programming-Language)

This is quite obviously a work in progress :)

## Goals:

The goal of Plywood is to give the user utmost freedom of structuring code in any way neccessary. This will be done via the use of a system of label and goto syntax that will allow going from one spot in the program to another.

The end product will be written completely in C or will be a Cython compiled version of the Python source code of the language.

## Join In!

I am currently looking for people to collaborate with on:

- Creating syntax highlighting and grammar rules via Tree-sitter for code editors to recognize Plywood <bold>(High Priority)</bold>
- Writing documentation and wiki
- Implementing more syntax features
- Developing libraries and a package system
- Literally anything else you want to suggest :)
- Need someone to help design a logo for the programming language so that we can be more "official" (blender, photoshop, or another tool?)
 
Contact info is in github bio.

## To Do:

- [X] Implement Numeric Arithmetic
- [X] Implement Output
- [ ] Implement Logic Arithmetic
- [ ] Implement if/then
- [X] Implement labels and goto to enable looping and recursive code when paired with if/then
- Adding more soon
- At some point: Try solving USACO Bronze problems with Plywood to see how it goes

## Sample Code Snippets:

#### Fibonacci:
Plywood program that spews out an infinte sequence of fibonacci numbers until it is terminated (this will clog up ur terminal given if/then/else haven't been implemented yet so be careful) you can stop the program as you normally would with CONTROL + C
```
# Clone the code and run the following command from inside the /src directory to test this program:
# python3 main.py testcode/fibonacci.wood

   0 -> A
   1 -> B
   1 -> C
   OUT 0 $ ', '

   LBL LOOP

   A -> C
   B -> A
   C + B -> B
   OUT B $ ', '
   B -> A
   C -> B
   
   GOTO LOOP 
```
