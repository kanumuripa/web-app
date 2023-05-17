# import time

filepath = 'testdata.txt'
def get_testdata():
    with open(filepath, 'r') as file:
        r = file.readlines()
    return r


def apnd_testdata(v_args):
    with open(filepath, 'a') as file1:
        file1.writelines(v_args)


def wrt_testdata(r_args):
    with open(filepath, 'w') as file2:
        file2.writelines(r_args)

# print(get_testdata())
# print(time.strftime("Date of Execution: %d/%M/%Y %H:%m"))