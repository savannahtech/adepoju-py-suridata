import multiprocessing
import itertools
import random

# Example list of employees (replace this with your actual list)
employees = [
    {"name": "Alice", "department": "Sales", "id": 1},
    {"name": "Bob", "department": "IT", "id": 2},
    {"name": "Alice", "department": "Sales", "id": 1},  # Duplicate
    {"name": "Charlie", "department": "HR", "id": 3},
    {"name": "Dave", "department": "Finance", "id": 4},
    # Add more employees here
]

# Function to clean and validate employee list
def clean_and_validate(employees):
    # Remove duplicates based on a combination of fields
    unique_employees = {tuple(employee.values()) for employee in employees}
    cleaned_employees = [dict(zip(("name", "department", "id"), employee)) for employee in unique_employees]
    return cleaned_employees

# Function to generate unique pairs of employees
def generate_pairs(employees):
    random.shuffle(employees)
    pairs = list(zip(employees[::2], employees[1::2]))
    return [(pair[0]["name"], pair[1]["name"]) if pair[0]["id"] < pair[1]["id"] else (pair[1]["name"], pair[0]["name"]) for pair in pairs]

# Splitting the input into chunks for parallel processing
def chunks(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]

if __name__ == '__main__':
    # Clean and validate employee list
    cleaned_employees = clean_and_validate(employees)

    # Split employees into chunks for parallel processing
    if len(cleaned_employees) < 100:
        num_processes = 1
    else:
        num_processes = multiprocessing.cpu_count()
    employee_chunks = chunks(cleaned_employees, len(cleaned_employees) // num_processes + 1)

    # Create a pool of processes to handle the chunks
    with multiprocessing.Pool(processes=num_processes) as pool:
        # Generate pairs for each chunk in parallel
        results = pool.map(generate_pairs, employee_chunks)

    # Flatten the results from different processes
    all_pairs = list(itertools.chain.from_iterable(results))

    # Remove duplicate pairs
    unique_pairs = list(set(all_pairs))

    # Print the unique pairs of Dwarf-Giant
    print(unique_pairs)