


def write_exe(output_name, lines):

    #if user did specify name use that name
    if (output_name != None):
        with open (output_name, 'w') as write_output:
            for line in lines:
                write_output.write(' '.join(str(s) for s in line) + '\n')
    #else use a default name
    else:
        with open ('execute.out', 'w') as write_output:
            for line in lines:
                write_output.write(' '.join(str(s) for s in line) + '\n') 
    


