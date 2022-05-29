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
- [X] Implement Logic Arithmetic
- [X] Implement if/then
- [X] Implement labels and goto to enable looping and recursive code when paired with if/then
- [ ] Implement lists
- [ ] Implement importing additional modules and libraries written in Plywood
- [X] Allow multiple lines of code to be put on one line separated by a vertical line delimiter ";"
- [ ] Build native Plywood library to create matrixes (will use lists to do this)

- [ ] Create chess engine using matrixes made in plywood (???)

- [ ] At some point: Try solving USACO Bronze problems with Plywood to see how it goes

## Sample Code Snippets:

#### Fibonacci:
Plywood program that spews out an fibonacci numbers until a certain number "n"
```
# Clone the code and run the following command from inside the /src directory:
# python3 main.py testcode/fibonacci2.wood

10 -> n
0 -> A; 1 -> B; 1 -> C; 1 -> i;
OUT 0 $ ' '
LBL fibonacciLoop
  GOTO helper
  LBL helperExit

  IF
  i == (n - 1)
  THEN
    GOTO exitFibonacciLoop
  ENDIF
  B -> A; C -> B; i + 1 -> i
GOTO fibonacciLoop

  LBL helper
    A -> C; B -> A; C + B -> B; OUT B $ ' '
  GOTO helperExit

  LBL exitFibonacciLoop
OUT '\n'
```
