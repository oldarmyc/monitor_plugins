#!/usr/bin/python

"""
Copyright 2016 Dave Kludt

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

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
