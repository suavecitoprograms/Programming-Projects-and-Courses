# Write your solution here
from string import *
def run(program : list):
    ## handles the initializing each variable to a value of 0
    assignment = {}
    time_jump = {}
    
    for command in program:
        if command not in "MOV_ADD_SUB_MUL_JUMP_IF_END_PRINT":
            info = command.split()
            time_jump[info[0][:-1]] = program.index(command)
            
    for letter in ascii_uppercase:
        assignment[letter] = 0

    placeholder = []
    handle(program, assignment, time_jump, placeholder)
    return placeholder
    

def handle(program : list, assignment : dict, time_jump : dict, placeholder : list):
    ## handles assigning of each
    index = 0
    while index < len(program):
        command = program[index]
        info = command.split()
        if info[0] in "MOV_ADD_SUB_MUL":
            arithmetic(info, assignment)
            
        elif info[0] == "JUMP": ## format JUMP [location]
            location = info[1]
            index = int(time_jump[location])
        
        elif info[0] == "IF": ## "IF C == A JUMP error" -> operand = info[2]
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
                index = int(time_jump[location])
        
        elif info[0] == "END" or index == len(program):
            return 
        
        elif info[0] == "PRINT":
            printo = info[1]
            if printo in digits:
                placeholder.append(int(printo))
            else:
                placeholder.append(assignment[info[1]])
            
        else: ## handles [location]:
            pass
            
        index += 1

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
    program2 = ['MOV N 100', 'PRINT 2', 'MOV A 3', 'start:', 'MOV B 2', 'MOV Z 0', 'test:', 'MOV C B', 'new:', 'IF C == A JUMP virhe', 'IF C > A JUMP pass_by', 'ADD C B', 'JUMP new', 'virhe:', 'MOV Z 1', 'JUMP pass_by2', 'pass_by:', 'ADD B 1', 'IF B < A JUMP test', 'pass_by2:', 'IF Z == 1 JUMP pass_by3', 'PRINT A', 'pass_by3:', 'ADD A 1', 'IF A <= N JUMP start']
    result = run(program2)
    print(result)