import calcexec as cexec
import calc
import calcerror as cerr


def exec_program(prog, table={}):
    """
    Executes a calc program.
    """
    try:
        cerr.check_program(prog)
        return cexec.exec_statements(
            calc.program_statements(prog), table)

    except Exception as err:
        print(err)
