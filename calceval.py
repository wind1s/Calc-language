import calc
import calcerror as cerr


def eval_condition(cond, table):
    """
    Evaluates a condition statement, piggybacks on python interpreter.
    """
    condopr = calc.condition_operator(cond)

    left = eval_expression(calc.condition_left(cond), table)
    right = eval_expression(calc.condition_right(cond), table)

    if condopr == "=":
        condopr += "="
    """
        return left == right
    elif condopr == "<":
        return left < right
    elif condopr == ">":
        return left > right
    """

    return eval(f"{left}{condopr}{right}")


def eval_expression(expr, table):
    """
    Evaluates a expression.
    """
    if calc.is_constant(expr):
        return expr

    elif calc.is_binaryexpr(expr):
        return eval_binary_expression(expr, table)

    elif calc.is_variable(expr):
        return eval_variable(expr, table)

    else:  # Expression is not defined in the calc language.
        cerr.error_expression(expr)


def eval_binary_expression(bin_expr, table):
    """
    Evaluates a binary expression, (+, -, /, *)
    """
    bin_op = calc.binaryexpr_operator(bin_expr)
    left = eval_expression(calc.binaryexpr_left(bin_expr), table)
    right = eval_expression(calc.binaryexpr_right(bin_expr), table)

    return eval(f"{left}{bin_op}{right}")


def eval_variable(variable, table):
    """
    Evaluats a variable, if it is declared.
    """
    cerr.check_declared(variable, table)
    return table[variable]
