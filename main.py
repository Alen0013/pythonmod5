from modules.module1 import report_origin as report_module1
from modules.module2 import report_origin as report_module2
from my_package.folder1.file1 import report_origin as report_file1
from my_package.folder1.file2 import report_origin as report_file2
from my_package.folder2.file3 import report_origin as report_file3
from my_package.folder2.file4 import report_origin as report_file4
from my_package.folder3.file5 import report_origin as report_file5
from my_package.folder3.file6 import report_origin as report_file6

if __name__ == "__main__":
    print(report_module1())
    print(report_module2())
    print(report_file1())
    print(report_file2())
    print(report_file3())
    print(report_file4())
    print(report_file5())
    print(report_file6())