--  Copy Paste the Following Commands to create and Insert data into tables 

-- Create the Employee Table
create Table Employee(emp_no varchar(10),emp_name varchar(255),dept_name varchar(100),salary int,doj date,branch varchar(100));

-- Create the EmployeeDetails Table
CREATE TABLE EmployeeDetails(emp_no varchar(10),emp_name varchar(255),designation varchar(255),dept_name varchar(100));

-- Insert all entries in Employee Table
INSERT INTO Employee(emp_no,emp_name,dept_name,salary,doj,branch) 
VALUES ('E101','Vivek','R&D',145000,'2009-06-11','Nagpur'), 
('E102','Vishal','Marketing',90000,'2012-03,15','Pune'), 
('E103','Priyal','Product Development',120000,'2018-07-20','Banglore'), 
('E104','Srushti','Product Development',80000,'2019-09-19','Nagpur'), 
('E105','Pranay','Product Development',100000,'2018-10-22','Mumbai');


-- Insert all entries in EmployeeDetails Table
 INSERT INTO EmployeeDetails(emp_no,emp_name,designation) 
 VALUES ('E101','Vivek','Project Manager'), 
 ('E102','Vishal','Sales Manager'), 
 ('E103','Priyal','Design Architect'), 
 ('E104','Srushti','Software Developer'), 
 ('E105','Pranay','Project Lead');

-- Display all entries from the Employee Table
SELECT * FROM Employee;

-- Display the number of employees 
SELECT COUNT(*) as EmployeeCount FROM Employee;

-- Retriving the Employee_no with their respective salary
SELECT emp_no, salary FROM Employee;

-- Total Salary Of All Employees 
SELECT SUM(salary) AS SumOfAllEmployeeSalary FROM Employee;

-- Average Salary Of Employee 
SELECT AVG(salary) AS AverageSalaryOfEmployee FROM Employee;

-- Displaying the name of the Employees in the Descending Order 
SELECT emp_name AS NamesInDescOrder FROM Employee ORDER BY emp_name DESC;

-- Retrieve the name of employees and their dept name 

-- Update the EmployeeDetails tables, replace all NULL values in the dept_name 

-- Rec-01 
UPDATE EmployeeDetails 
SET dept_name='IT'
WHERE emp_no='E101';

-- Rec-02 
UPDATE EmployeeDetails 
SET dept_name='Digital Marketing' 
WHERE emp_no='E102';

-- Rec-03 
UPDATE EmployeeDetails
SET dept_name="UI/UX"
WHERE emp_no='E103';

-- Rec-04 
UPDATE EmployeeDetails
SET dept_name="App Tester"
WHERE emp_no='E104';

UPDATE EmployeeDetails
SET dept_name="SDE-3"
WHERE emp_no="E105";


-- Simple Liner Code 
SELECT  CONCAT('{"emp_name":"',Employee.emp_name, ',"emp_no":"',Employee.emp_no,'",', '"dept_name":"',Employee.dept_name,'",', '"salary":"',Employee.salary,'",', '"doj":"',Employee.doj,'",', '"branch":"',Employee.branch,'"},')AS EmployeeDBInJSON from Employee JOIN EmployeeDetails ON Employee.emp_no=EmployeeDetails.emp_no;


-- Printing the table content in JSON Format 
SELECT  CONCAT( GROUP_CONCAT('{"emp_name":"',Employee.emp_name,'","dept_name":"',EmployeeDetails.dept_name,'"}' ) ) AS EmployeeNameAndDeptInJSON FROM Employee JOIN EmployeeDetails ON Employee.emp_no = EmployeeDetails.emp_no;
