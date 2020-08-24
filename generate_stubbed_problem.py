import sys
import subprocess


def create_template(function_name):
    coding_template = """
def """+function_name+"""():

    return None




if __name__ == "__main__":

    tests = [
        {"paramters": [], "expected": None}
    ]

    counter = 1
    for test in tests:
        results = """+function_name+"""(test['paramters'])
        print("Test {0} n={1}".format(counter, test['paramters']), test['expected'] == results, results )

        counter += 1
    
    """

    return coding_template


if __name__ == "__main__":

    if len(sys.argv) >= 2:
        stubb_name = sys.argv[1]
        name = stubb_name + "_problem.py"

        text_file = open(name, "w")
        text_file.write(create_template(stubb_name))
        text_file.close()

    else:
        print("Please enter stubb_name")




