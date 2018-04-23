# http://book.pythontips.com/en/latest/args_and_kwargs.html
# *args is used to send a non-keyworded variable
# length argument list to the function.
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)


test_var_args('yasoob', 'python', 'eggs', 'test')
