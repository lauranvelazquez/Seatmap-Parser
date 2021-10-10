from xml_file import *
from json_file import *
import sys


def principal():
    file = str(sys.argv[1])
    seats = read_xml(file)
    file_name = json_generate(seats, file)
    print(file_name)


if __name__ == '__main__':
    principal()
