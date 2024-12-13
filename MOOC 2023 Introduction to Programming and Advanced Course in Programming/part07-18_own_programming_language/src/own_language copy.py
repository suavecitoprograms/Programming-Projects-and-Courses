# Write your solution here
from string import *
def run(program : list):
    ## handles the initializing each variable to a value of 0
    assignment = {}
    time_jump = {}
    for letter in ascii_uppercase:
        assignment[letter] = 0
    index = 0
    current = len(program)
    placeholder = []
    return handle(program, assignment, time_jump, index, current, placeholder)
    

def handle(program : list, assignment : dict, time_jump : dict, index : int, current : int, placeholder : list):
    ## handles assigning of each
    result = []
    for command in program[index:current]:
        info = command.split()
        if info[0] in "MOV_ADD_SUB_MUL":
            arithmetic(info, assignment)
            
        elif info[0] == "JUMP": ## format JUMP [location]
            location = info[1]
            jump(time_jump, program, command, location, assignment, placeholder)
        
        elif info[0] == "IF": ## "IF C == A JUMP error" -> operand = info[2]
            operation = False
            value1 = assignment[info[1]]
            value2 = assignment[info[3]] if info[3] in ascii_uppercase else int(info[3])
       
            if "=" in info[2]:
                if "<" in info[2]:
                    match = True if value1 <= value2 else False
     
                elif ">" in info[2]:
                    match = True if value1 >= value2 else False
                elif "!" in info[2]:
                    match = True if value1 != value2 else False
                else:
                    match = True if value1 == value2 else False
            elif "<" in info[2]:
                match = True if value1 < value2 else False
            else:
                match = True if value1 > value2 else False
                        
            if match:
                location = info[5]
                jump(time_jump, program, command, location, assignment, placeholder)
                index = program.index(command)
                handle(program, assignment, time_jump, index-1, current, placeholder)
        
        elif info[0] == "END":
            return placeholder
        
        elif info[0] == "PRINT":
            placeholder.append(assignment[info[1]])
            
        else: ## handles [location]:
            time_jump[info[0][:-1]] = program.index(command) + 1
    if current == len(program):
        return placeholder
            
def jump(time_jump, program, command, location, assignment, placeholder):
    index = time_jump[location]
    current = program.index(command) - 1
    
    handle(program, assignment, time_jump, index, current, placeholder)

def arithmetic(info : list, assignment : dict):
    ## info is in the format : ["[operation]", "[variable]", "[value]"]
    operation = info[0]
    var = info[1]
    val = info[2]
    
    
    if operation == "MOV":
        assignment[var] = int(assignment[val]) if val in ascii_uppercase else int(val)

    elif operation == "ADD":
        assignment[var] += int(assignment[val]) if val in ascii_uppercase else int(val)

    elif operation == "SUB":
        assignment[var] -= int(assignment[val]) if val in ascii_uppercase else int(val)
        
    else: ## handles mul
        assignment[var] *= int(assignment[val]) if val in ascii_uppercase else int(val)

if __name__ == "__main__":
    program3 = ['MOV A 1', 'MOV B 1', 'start:', 'MUL A 2', 'ADD B 1', 'IF B != 101 JUMP start', 'PRINT A']
    result = run(program3)
    print(result)