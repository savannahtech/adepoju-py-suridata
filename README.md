# Dwarf-Giant Game Solution

## Introduction

This Python solution simulates the Dwarf-Giant game, where unique pairs of employees are created, adhering to specific game rules.

## Problem Statement

The goal is to create pairs of employees where each employee gets a chance to be a Dwarf once and a Giant once. Constraints include:

- Cleaning duplicates: Removing duplicate entries based on a unique combination of three fields.
- Randomization: Ensuring randomness in pair selection.
- Pair uniqueness: Avoiding duplicate pairs or reversed pairs.
- Multi-process implementation: Utilizing multiprocessing for handling large datasets efficiently.

## Solution Overview

### `clean_employees_chunk` function

- Cleans a chunk of employee data by identifying and removing duplicates.
- Uses a unique index based on department, name, and age to validate uniqueness.

### `clean_employees_parallel` function

- Splits the input into chunks and processes them in parallel using multiprocessing.
- Utilizes `clean_employees_chunk` for cleaning each chunk and merges the results.

### `dwarf_giant_pairs` function

- Generates dwarf-giant pairs following the game rules:
  - Randomizes the order of cleaned employees.
  - Iterates through employees to form pairs ensuring fairness and uniqueness.

## Usage

1. Input: Provide a list of dictionaries, each containing "department," "name," and "age" fields for employees.
2. Run the code.
3. Output: Receive a list of tuples representing unique Dwarf-Giant pairs.

## Implementation Details

- Multiprocessing: Utilizes the `multiprocessing` module to parallelize the cleaning process and enhance performance.
- Randomization: Randomizes employee order for pair creation.
- Avoiding duplicates: Ensures pair uniqueness by preventing reversed pairs or duplicate pairs.

## How to Run

1. Ensure Python 3.x is installed.
2. Execute the code in the specified environment.
3. Update the `employees` list to include employee data in the desired format.
4. Run the script and observe the generated Dwarf-Giant pairs.

## Bonus: Multithreading

The solution is optimized for handling large datasets through multi-processing, enhancing efficiency and scalability.
