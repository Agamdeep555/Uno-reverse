

import sys

def print_statements(problem_statements):
    for statement in problem_statements:
        print(statement)

if __name__ == "__main__":
   
    problem_statements = sys.argv[1:]

    
    print_statements(problem_statements)
