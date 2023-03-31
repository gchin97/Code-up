with open("EmployeeDemographic.csv", "w") as report_file:
    report_file.write(
        "'EmployeeID', 'FirstName', 'LastName', 'Age', 'Gender'")
    report_file.write("\n1001, 'Jim', 'Halpert', 30, 'Male'")
    report_file.write("\n1002, 'Pam', 'Beasley', 30, 'Female'")
    report_file.write("\n1003, 'Dwight', 'Schrute', 29, 'Male'")
    report_file.write("\n1004, 'Angela', 'Martin', 31, 'Female'")
    report_file.write("\n1005, 'Toby', 'Flenderson', 32, 'Male'")
    report_file.write("\n1006, 'Michael', 'Scott', 35, 'Male'")
    report_file.write("\n1007, 'Meredith', 'Palmer', 32, 'Female'")
    report_file.write("\n1008, 'Stanley', 'Hudson', 38, 'Male'")
    report_file.write("\n1009, 'Kevin', 'Malone', 31, 'Male'")

with open("EmployeeDemographic.csv", "r") as report_file:
    filedata = report_file.read()
filedata = filedata.replace("'", "")

# with open("EmployeeDemographic.csv", "w") as report_file:
#     report_file(filedata)

with open("EmployeeSalary.csv", "w") as report_files:
    report_files.write("'EmployeeID', 'JobTitle', 'Salary'")
    report_files.write("\n1001, 'Salesman', 45000")
    report_files.write("\n1002, 'Receptionist', 36000")
    report_files.write("\n1003, 'Salesman', 63000")
    report_files.write("\n1004, 'Accountant', 47000")
    report_files.write("\n1005, 'HR', 50000")
    report_files.write("\n1006, 'Regional Manager', 65000")
    report_files.write("\n1007, 'Supplier Relations', 41000")
    report_files.write("\n1008, 'Salesman', 48000")
    report_files.write("\n1009, 'Accountant', 42000")

with open("EmployeeSalary.csv", "r") as report_files:
    filesdata = report_files.read()
filesdata = filesdata.replace("'", "")

with open('EmployeeSalary.csv', 'w') as report_files:
    report_files.write(filesdata)
