import random
"""
The finally clause is optional however when present it is always executed, whether an exception has occurred or not.
The finally clause is important to do clean-up code
Python offer a else clause that is executed only if no exception is raised
"""


def read_file(file_name: str) -> str:
    """
  Simulate an operation to read a file
  :return: Fake content of a file
  """
    try:
        print("Open file:", file_name)
        for i in range(1, 11):
            rnd = random.randint(1, 11)
            if rnd <= 2:
                raise Exception("Error reading the file: " + file_name)
            else:
                print("Read a record =", i)
    except Exception as ex:
        print('Error processig file', ex)
    else:  # The else clause is executed only if no exception was raised
        print("No error reading the file")
    finally:  # The finally clause is always executed
        try:
            print("CLOSING FILE:", file_name)
        except:
            print("ERROR Closing file")

    return "File content"


try:
    file_content = read_file("my_file")
    print("File Content", file_content)
except Exception as error:
    print("ERROR PROCESSING THE FILE =>", error)
