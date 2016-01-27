#!/usr/bin/python


import sys
import os


def check_file_system_read_write(file_system_path):
    test_file_path = '%s/temp_test' % (file_system_path)
    try:
        file = open(test_file_path, 'w')
        file.close()
        os.remove(test_file_path)
    except:
        return 'RO'
    else:
        return 'RW'


def main():
    status = 'RO'
    if len(sys.argv) != 2:
        print('Usage: %s <filePath>' % (sys.argv[0]))
        sys.exit(0)

    file_system_path = sys.argv[1]
    status = check_file_system_read_write(file_system_path)
    print('metric writestatus string %s' % (status))
    sys.exit(0)


if __name__ == '__main__':
    main()
