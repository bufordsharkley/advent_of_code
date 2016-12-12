TEST = """\
cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a"""

def resolve(regs, instructions):
    ii = 0
    while ii < len(instructions):
        instruction = instructions[ii].split()
        if instruction[0] == 'cpy':
            src, dst = instruction[1:]
            try:
                regs[dst] = int(src)
            except:
                regs[dst] = regs[src]
        elif instruction[0] == 'jnz':
            test, src = instruction[1:]
            if test == '0':
                pass
            elif test in 'abcd' and regs[test] == 0:
                pass
            else:
                offset = int(src)
                ii += offset - 1
        elif instruction[0] == 'inc':
            regs[instruction[1]] += 1
            pass
        elif instruction[0] == 'dec':
            regs[instruction[1]] -= 1
            pass
        else:
            raise Exception(instruction)
        ii += 1
    return regs

if __name__ == "__main__":
    instructions = [x.strip() for x in TEST.splitlines()]
    instructions = [x.strip() for x in open('input/12.txt').readlines()]
    regs = {x: 0 for x in 'abcd'}
    regs['c'] = 1
    regs = resolve(regs, instructions)
    print regs
