# JavaScript-Syntax-Analyzer

This project uses Python's PLY library to parse and validate various JavaScript constructs. It includes tokenization and parsing rules for:

Variable Declarations: Supports var, let, and const.
Array Declarations: Handles literal arrays, arrays created with new Array(), and nested arrays.
For Loops: Validates standard JavaScript for loop syntax.
setTimeout Statements: Parses setTimeout function calls with different arguments.

The lexer identifies JavaScript keywords, identifiers, numbers, strings, and various punctuation marks, while the parser ensures the correct syntax for each construct. This tool is ideal for basic JavaScript code validation and educational purposes.
