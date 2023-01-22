import calc
import calcexception as cexcep

# Error messages for respective errors.
PROGRAM_ERROR = "not a calc program: {0}"
STATEMENT_ERROR = "invalid calc statement: {0}"
CONDITION_ERROR = "invalid calc condition: {0}"
EXPRESSION_ERROR = "invalid calc expression: {0}"
DECLARED_ERROR = "variable {0} is not declared"


def error_statement(statement):
    """
    Throws error that statement is an invalid calc statement.
    """
    raise cexcep.CalcSyntaxError(STATEMENT_ERROR.format(statement))


def error_program(prog):
    """
    Throws error that prog is an invalid calc statement.
    """
    raise cexcep.CalcProgramError(PROGRAM_ERROR.format(prog))


def error_condition(condition):
    """
    Throws error that condition is an invalid calc condition.
    """
    raise cexcep.CalcSyntaxError(CONDITION_ERROR.format(condition))


def error_expression(expr):
    """
    Throws error that expr is an invalid calc expression.
    """
    raise cexcep.CalcSyntaxError(EXPRESSION_ERROR.format(expr))


def error_declared(variable):
    """
    Throws error that variable is not declared.
    """
    raise cexcep.CalcVariableError(DECLARED_ERROR.format(variable))


def check_statement(statement):
    """
    Throws error that statement is an invalid calc statement.
    """
    if not calc.is_statement(statement):
        error_statement(statement)


def check_program(prog):
    """
    Throw error if prog is not a calc program.
    """
    if not calc.is_program(prog):
        error_program(prog)


def check_condition(condition):
    """
    Throw error if condoper is not a calc condition.
    """
    if not calc.is_condition(condition):
        error_condition(condition)


def check_declared(variable, table):
    """
    Throw error if variable is not declared.
    """
    if not variable in table:
        error_declared(variable)
