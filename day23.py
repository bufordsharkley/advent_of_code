PGM = """\
jio a, +16
inc a
inc a
tpl a
tpl a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
tpl a
tpl a
inc a
jmp +23
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
tpl a
inc a
inc a
tpl a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
tpl a
tpl a
inc a
jio a, +8
inc b
jie a, +4
tpl a
inc a
jmp +2
hlf a
jmp -7
"""


def fresh_registers():
    return {'a': 0, 'b': 0}


def run_program(registers, program_text):
    program = {ii: line for ii, line in enumerate(program_text.splitlines())}
    goto = 0
    while goto < len(program):
        instruction = program[goto]
        goto += run_instruction(registers, instruction)
    return registers


def run_instruction(registers, instruction):
    command, args = instruction.split(None, 1)
    jump = 1
    if command == 'inc':
        registers[args] += 1
    elif command == 'jio':
        reg, jmp = args.split(', ')
        if registers[reg] == 1:
            jump = int(jmp)
    elif command == 'tpl':
        registers[args] *= 3
    elif command == 'jmp':
        jump = int(args)
    elif command == 'jie':
        reg, jmp = args.split(', ')
        if not registers[reg] % 2:
            jump = int(jmp)
    elif command == 'hlf':
        registers[args] /= 2
    else:
        raise NotImplementedError(command)
    return jump


def main():
    registers = fresh_registers()
    registers = run_program(registers, PGM)
    print registers
    registers = fresh_registers()
    registers['a'] = 1
    registers = run_program(registers, PGM)
    print registers



if __name__ == "__main__":
    main()
