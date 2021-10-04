import random

"""
The finally clause is optional however when present it is always executed, whether an exception has occurred or not.
The finally clause is important to do clean-up code
I tis possible
"""


def read_file(file_name: str) -> str:
    """
    Simulate an operation to read a file
    :return: Fake content of a file
    """
    try:
        print("Open file:", file_name)
        for i in range(1, 15):
            rnd = random.randint(1, 20)
            if rnd <= 5:
              raise Exception("Error reading the file: " + file_name)
            else:
              print("Read a record =", i)                
        return "File content"
    finally:
        print("CLOSING FILE:", file_name)

try:
    file_content = read_file("my_file")
    print("File Content", file_content)
except Exception as error:
    print("ERROR PROCESSING THE FILE =>", error)