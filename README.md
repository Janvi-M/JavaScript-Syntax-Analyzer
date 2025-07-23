# 🧠 JavaScript Syntax Parsers with PLY (Python Lex-Yacc)

This repository contains a collection of **mini-parsers** for different JavaScript syntax constructs, implemented using the [`ply`](https://github.com/dabeaz/ply) library in Python. PLY is a Pythonic re-implementation of the popular compiler construction tools **lex** and **yacc**.

---

## 📘 Introduction

Parsing is a crucial step in compilers and interpreters where a stream of tokens (produced by a lexer) is analyzed to determine its grammatical structure according to a formal grammar.

This project breaks down the complexity of **JavaScript parsing** into smaller, manageable components, each focusing on a specific syntax feature.

---

## ✨ Features

- 🧩 **Modular Design** – Each JavaScript construct is handled by a separate `ply` parser.
- 🏷️ **Lexical Analysis** – Uses `ply.lex` to tokenize JavaScript input (e.g., `ID`, `VAR`, `SEMICOLON`).
- 🧠 **Syntax Analysis** – Defines grammar rules via `ply.yacc` to validate and parse constructs.
- 🖥️ **Interactive Input** – Each script prompts for input, enabling real-time testing of JavaScript snippets.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your_username/javascript-ply-parsers.git
cd javascript-ply-parsers
```

### 2. Install Dependencies

```bash
pip install ply
```

---

## 🚀 Usage

Each `.py` file is a standalone parser for a JavaScript feature. To run:

```bash
python <parser_filename>.py
```

You will be prompted to enter JavaScript code.

---

## 🔍 Individual Parsers

### 📄 Variable Declaration and Assignment (`var_declaration_assignment.py`)

Handles basic `var`, `let`, `const` declarations and assignments.

#### ✅ Supported Syntax

```js
var x;
let y;
const z;
var a = 10;
let b = myVar;
const c = 20;
var x; x = 5;
```

#### ▶️ How to Run

```bash
python var_declaration_assignment.py
```

#### 💡 Example Input

```js
var myVariable = 123;
let anotherOne;
const PI = 3.14;
var test; test = 100;
```

---

### 📦 Array Declaration (`array.py`)

Focuses on literal and constructor-based array declarations.

#### ✅ Supported Syntax

```js
const myArray = [1, 2, "hello"];
let emptyArray = [];
var newArray = new Array();
let prefilledArray = new Array(1, "test", 3);
```

#### ▶️ How to Run

```bash
python array.py
```

#### 💡 Example Input

```js
const numbers = [1, 2, 3];
let names = ["Alice", "Bob"];
var data = new Array();
let mixed = new Array("apple", 123, "banana");
```

---

### ⏱️ `setTimeout` Function Call (`setTimeout.py`)

Parses `setTimeout` function calls with a callback and delay.

#### ✅ Supported Syntax

```js
setTimeout(myFunction, 1000);
setTimeout(anotherFunc, 500);
```

#### ▶️ How to Run

```bash
python setTimeout.py
```

#### 💡 Example Input

```js
setTimeout(callbackFunction, 2000);
setTimeout(animate, 500);
```

📌 *This parser prints lexed tokens before parsing.*

---

### 🔁 For Loop (`forloop.py`)

Handles basic `for` loops with optional `console.log` in the body.

#### ✅ Supported Syntax

```js
for (let i = 0; i < 10; i++) { console.log("Looping"); }
for (var x = 5; x > 0; x--) { console.log("Count"); }
```

#### ▶️ How to Run

```bash
python forloop.py
```

#### 💡 Example Input

```js
for (let i = 0; i < 5; i++) { console.log("Iteration"); }
for (var j = 10; j > 0; j--) { console.log("Countdown"); }
```
---
