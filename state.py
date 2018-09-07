class State:
    def __init__(self, value, operation=None, parent=None):
        self.value = value
        self.operation = operation
        self.parent = parent

    def __repr__(self):
        return f"{self.operation or ''}={self.value}"
    
    def reverse_op(self):
        if self.operation[0] == '/':
            self.operation = self.operation.replace('/', '*')
        elif self.operation[0] == '*':
            self.operation = self.operation.replace('*', '/')
        elif self.operation[0] == '+':
            self.operation = self.operation.replace('+', '-')
        elif self.operation[0] == '-':
            self.operation = self.operation.replace('-', '+')