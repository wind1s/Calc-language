class CalcVariableError(Exception):
    """
    Represents a calc variable error, such as not declared.
    """

    def __init__(self, err):
        super().__init__(err)
        self.err = err

    def __str__(self):
        return "Variable error, " + self.err


class CalcSyntaxError(Exception):
    """
    Represents a calc syntax error such as writing "for" instead of "while".
    """

    def __init__(self, err):
        super().__init__(err)
        self.err = err

    def __str__(self):
        return "Syntax error, " + self.err


class CalcProgramError(Exception):
    """
    Represents the error when a program is not a calc program.
    """

    def __init__(self, err):
        super().__init__(err)
        self.err = err

    def __str__(self):
        return "Program error, " + self.err
