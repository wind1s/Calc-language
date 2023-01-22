import calc
import calcerror as cerr
import calceval as ceval


def exec_statements(statements, table):
    """
    Executes the first calc statement and continues to execute the rest of the statements.
    """
    first = calc.first_statement(statements)
    cerr.check_statement(first)

    new_table = exec_statement(first, table)
    rest = calc.rest_statements(statements)

    if not calc.empty_statements(rest):
        new_table = exec_statements(rest, new_table)

    return new_table


def exec_statement(statement, table):
    """
    Executes a calc statement.
    """
    new_table = {}

    if calc.is_selection(statement):
        new_table = exec_selection(statement, table)

    elif calc.is_input(statement):
        new_table = exec_input(statement, table)

    elif calc.is_output(statement):
        exec_output(statement, table)
        new_table = table

    elif calc.is_assignment(statement):
        new_table = exec_assignment(statement, table)

    elif calc.is_repetition(statement):
        new_table = exec_repetition(statement, table)

    else:  # Sstatement is not defined in the calc language.
        cerr.error_statement(statement)

    return new_table


def exec_selection(selection, table):
    """
    # Executes a selection statement (if statement).
    """
    new_table = {}

    condition = calc.selection_condition(selection)
    cerr.check_condition(condition)

    if ceval.eval_condition(condition, table):
        true_statement = calc.selection_true_branch(selection)
        cerr.check_statement(true_statement)
        new_table = exec_statement(true_statement, table)

    # If the condition is false execute the false branch, if it exists.
    elif calc.selection_has_false_branch(selection):
        false_statement = calc.selection_false_branch(selection)
        cerr.check_statement(false_statement)
        new_table = exec_statement(false_statement, table)

    return new_table


def exec_input(inp, table):
    """
    Executes a input statement and saves the value to a variable.
    """
    new_table = table.copy()
    variable = calc.input_variable(inp)
    new_table[variable] = int(input(f"Enter value for {variable}: "))
    return new_table


def exec_output(output, table):
    """
    Executes a output statement.
    """
    expr = calc.output_expression(output)
    val = ceval.eval_expression(expr, table)

    if calc.is_variable(expr):
        print(f"{expr} = {val}")
    else:
        print(val)


def exec_assignment(assignment, table):
    """
    Executes a assignment statement, evalutates eventual expressions.
    """
    new_table = table.copy()
    variable = calc.assignment_variable(assignment)
    expression = calc.assignment_expression(assignment)

    new_table[variable] = ceval.eval_expression(expression, table)
    return new_table


def exec_repetition(statement, table):
    """
    Executes a repetition statement (while statement).
    """
    new_table = table.copy()

    condition = calc.repetition_condition(statement)
    cerr.check_condition(condition)

    while ceval.eval_condition(condition, new_table):
        new_table = exec_statements(
            calc.repetition_statements(statement), new_table)

    return new_table
