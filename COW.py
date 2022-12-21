class COW:

    def __init__(self, code):
        self.memory = [0,]
        self.code = code
        self.code_pos = 0
        self.mem_pos = 0

        self.COMMANDS = {
            0: 'moo',
            1: 'mOo',
            2: 'moO',
            3: 'mOO',
            4: 'Moo',
            5: 'MOo',
            6: 'MoO',
            7: 'MOO',
            8: 'OOO',
            9: 'MMM',
            10: 'OOM',
            11: 'oom'
        }

        # можно было бы хранить и начало, и конец, но по примеру
        # из документации OOO MOO moo moo должен перенести ко второму MOO
        self.loop_starts = [] 


    def get_next_three_symblos(self):
        return self.code[self.code_pos:self.code_pos + 3]


    def read_code(self):
        while True:
            command = self.get_next_command()
            self.exec_command(command)


    def get_next_command(self):
        if self.code_pos + 3 >= len(self.code):
            print('')
            exit()
        command = self.get_next_three_symblos()
        while command not in self.COMMANDS.values():
            if self.code_pos >= len(self.code):
                print('')
                exit()
            self.code_pos += 1
            command = self.get_next_three_symblos()
        self.code_pos += 3
        return command
    

    def search_moo(self, _command):
        while _command != 'moo':
            _command = self.get_next_three_symblos()
            self.code_pos += 1
            if _command == 'MOO':
                self.search_moo(_command)

    
    def exec_command(self, command):
        if command == 'moo':
            self.code_pos = self.loop_starts[-1]
        
        elif command == 'MOO':
            if self.memory[self.mem_pos] == 0:
                if self.loop_starts[-1] == self.code_pos - 3:
                    self.loop_starts.pop()  
                self.code_pos += 6 # + 3 + 3
                _command = self.get_next_three_symblos()
                self.search_moo(_command)
                self.code_pos += 3
            else:
                if len(self.loop_starts) == 0 or self.loop_starts[-1] != self.code_pos - 3: 
                    self.loop_starts.append(self.code_pos - 3)
        
        elif command == 'MoO':
            self.memory[self.mem_pos] += 1
        elif command == 'MOo':
            self.memory[self.mem_pos] -= 1
        elif command == 'moO':
            self.mem_pos += 1
            if self.mem_pos >= len(self.memory):
                self.memory.append(0)
        elif command == 'mOo':
            self.mem_pos -= 1
        elif command == 'OOM':
            print(self.memory[self.mem_pos], end='')
        elif command == 'oom':
            self.memory[self.mem_pos] = int(input())
        elif command == 'mOO':
            self.exec_command(self.COMMANDS[self.mem[self.mem_pos]])
        elif command == 'OOO':
            self.memory[self.mem_pos] = 0
        elif command == 'Moo':
            if self.memory[self.mem_pos] == 0:
                self.memory[self.mem_pos] = ord(input())
            else:
                print(chr(self.memory[self.mem_pos]), end='')
        