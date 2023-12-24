import random
import multiprocessing

def clean_employees_chunk(chunk):
    # Create a set to store unique combinations of employee attributes
    unique_employees = set()
    cleaned_employees = []
    
    # Iterate through the employees list
    for emp in chunk:
        # Create a unique index combining all three fields
        emp_index = (emp["department"], emp["name"], emp["age"])
        # Check if the combination is unique, if yes, add it to the cleaned list
        if emp_index not in unique_employees:
            unique_employees.add(emp_index)
            cleaned_employees.append(emp)
    
    return cleaned_employees

def clean_employees_parallel(employees, processes=4):
    pool = multiprocessing.Pool(processes=processes)
    chunk_size = len(employees) // processes
    chunks = [employees[i:i + chunk_size] for i in range(0, len(employees), chunk_size)]
    cleaned_chunks = pool.map(clean_employees_chunk, chunks)
    pool.close()
    pool.join()

    # Merge the results from all chunks
    cleaned_employees = []
    for chunk in cleaned_chunks:
        cleaned_employees.extend(chunk)
    
    return cleaned_employees

def dwarf_giant_pairs(employees):
    cleaned_employees = clean_employees_parallel(employees)
    # Shuffle the employees to randomize the order
    random.shuffle(cleaned_employees)
    
    pairs = []
    num_employees = len(cleaned_employees)
    
    # Create pairs by iterating through the employees
    for i in range(num_employees):
        dwarf = cleaned_employees[i]
        # Find the index for the giant, making sure it's not the same as the dwarf
        giant_index = (i + num_employees // 2) % num_employees
        
        # Ensure the giant index is not the same as the dwarf index or its reversed pair
        while giant_index == i or (cleaned_employees[giant_index]["name"], dwarf["name"]) in pairs:
            giant_index = (giant_index + 1) % num_employees
        
        giant = cleaned_employees[giant_index]
        pairs.append((dwarf["name"], giant["name"]))
    
    return pairs

if __name__ == "__main__":
    # Given employee data
    employees = [
        {"department": "R&D", "name": "emp1", "age": 46},
        {"department": "Sales", "name": "emp2", "age": 28},
        {"department": "R&D", "name": "emp3", "age": 33},
        {"department": "R&D", "name": "emp4", "age": 29}
    ]

    # Generate the dwarf-giant pairs
    output = dwarf_giant_pairs(employees)
    print(output)