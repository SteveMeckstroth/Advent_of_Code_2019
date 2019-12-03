class GravityAssist:

    def __init__(self, n, v):
        self.program_storage = [int(i) for i in open('input.txt', 'r').read().split(',')]
        self.program = self.program_storage[:]
        self.program[1] = n
        self.program[2] = v
        self.processing = True
        self.idx = 0

    @property
    def int_code_switch(self):
        return {1: lambda x, y: x + y, 2: lambda x, y: x * y}

    def int_code_program(self, program, opcode, n, v, position):
        try:
            program[position] = self.int_code_switch[opcode](self.program[n], self.program[v])
        except KeyError:
            self.processing = False

    def run(self, program):
        while self.processing:
            self.int_code_program(program, *self.program[self.idx:self.idx + 4])
            self.idx += 4

        self.set_default_states()
        return program[0]

    def set_default_states(self):
        self.program = self.program_storage[:]
        self.processing = True
        self.idx = 0


if __name__ == '__main__':
    g = GravityAssist(12, 2)
    print(g.run(g.program))

    for verb in range(99):
        for noun in range(99):
            g.program[1] = noun
            g.program[2] = verb
            if g.run(g.program) == 19690720:
                print(100 * noun + verb)
