import calcexception as cex
from io import StringIO
from contextlib import redirect_stdout
from calcprogram import exec_program
import calcerror as cerr


# ----- Correct examples ----- #
fibonacci = ["calc",
             ["read", "n"],
             ["set", "n1", 0],
             ["set", "n2", 1],
             ["set", "count", 0],
             ["if", ["n", "<", 1],
              ["print", "Only positive integers."],
                 ["while", ["count", "<", "n"],
                  ["print", "n1"],
                  ["set", "n3", ["n1", "+", "n2"]],
                  ["set", "n1", "n2"],
                  ["set", "n2", "n3"],
                  ["set", "count", ["count", "+", 1]]
                  ]]]

exponential = [
    "calc", ["read", "base"],
    ["read", "exponent"],
    ["set", "result", 1],
    ["while", ["exponent", ">", 0],
     ["set", "result", ["result", "*", "base"]],
     ["set", "exponent", ["exponent", "-", 1]]
     ],
    ["print", "result"]]

factorial = [
    "calc", ["read", "n"], ["set", "result", 1],
    ["while", ["n", ">", 0],
     ["set", "result", ["result", "*", "n"]],
     ["set", "n", ["n", "-", 1]]],
    ["print", "result"]]
"""
print("Calc program that calculates the n-th fibonacci number.")
exec_program(fibonacci)
print("\n")
print("Calc program that calculates an exponential expression given base and exponent.")
exec_program(exponential)
print("\n")
print("Calc program that calculates n!")
exec_program(factorial)
"""
# ----- Incorrect Examples ----- #


def assert_calc_error_msg(expected_err_msg, *inp):
    with redirect_stdout(StringIO()) as f:
        exec_program(*inp)

    err_msg = f.getvalue().rstrip("\n")
    assert str(err_msg) == str(expected_err_msg)


# Program error.
incorrect_program1 = ["calc"]
incorrect_program2 = ["prog", []]

assert_calc_error_msg(cex.CalcProgramError(cerr.PROGRAM_ERROR.format(
    incorrect_program1)), incorrect_program1)
assert_calc_error_msg(cex.CalcProgramError(cerr.PROGRAM_ERROR.format(
    incorrect_program2)), incorrect_program2)

# Statement error.
statement_error1 = ["calc", ["set", "i", 2], [
    "for", ["i", ">", 0], ["set", "i", ["i", "-", 1]]]]
statement_error2 = ["calc", ["func", ["a"], ["print", "a"]], ["func", ["a"]]]

assert_calc_error_msg(cex.CalcSyntaxError(cerr.STATEMENT_ERROR.format(
    statement_error1[2])), statement_error1)
assert_calc_error_msg(cex.CalcSyntaxError(cerr.STATEMENT_ERROR.format(
    statement_error2[1])), statement_error2)

# Expression error
modulo_err = ["calc", ["set", "n", 5], ["print", ["n", "%", 2]]]
list_err = ["calc", ["print", [2, 2]]]

assert_calc_error_msg(
    cex.CalcSyntaxError(cerr.EXPRESSION_ERROR.format(["n", "%", 2])),
    modulo_err)
assert_calc_error_msg(cex.CalcSyntaxError(
    cerr.EXPRESSION_ERROR.format(list_err[1][1])), list_err)


# Variable not declared error.
output_str_err = ["calc", ["print", "hello world!"]]

assert_calc_error_msg(
    cex.CalcVariableError(
        cerr.DECLARED_ERROR.format(output_str_err[1][1])),
    output_str_err)

# Condition error.
condition_err1 = ["calc", ["set", "a", 2],
                  ["if", [2, ">=", 2], ["print", "a"]]]
condition_err2 = ["calc", ["set", "k", 2], [
    "if", [0, "<=", 2, "<", 4], ["print", "k"]]]

assert_calc_error_msg(cex.CalcSyntaxError(cerr.CONDITION_ERROR.format(
    condition_err1[2][1])), condition_err1)
assert_calc_error_msg(cex.CalcSyntaxError(cerr.CONDITION_ERROR.format(
    condition_err2[2][1])), condition_err2)
