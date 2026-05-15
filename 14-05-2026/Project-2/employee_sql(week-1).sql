-- Create Database
CREATE DATABASE employee_tracker;
USE employee_tracker;

-- Employee Table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    joining_date DATE
);

-- Attendance Table
CREATE TABLE attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    clock_in DATETIME,
    clock_out DATETIME,
    FOREIGN KEY (employee_id)
    REFERENCES employees(employee_id)
);

-- Tasks Table
CREATE TABLE tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    tasks_completed INT,
    task_date DATE,
    FOREIGN KEY (employee_id)
    REFERENCES employees(employee_id)
);

-- INSERT
INSERT INTO employees VALUES
(1,'Arun','IT','2024-01-01');

-- READ
SELECT * FROM employees;

-- UPDATE
UPDATE employees
SET department='HR'
WHERE employee_id=1;

-- DELETE
DELETE FROM employees WHERE employee_id=1;
DELIMITER //

CREATE PROCEDURE total_work_hours(IN emp INT)
BEGIN
    SELECT employee_id,
    SUM(TIMESTAMPDIFF(HOUR, clock_in, clock_out)) AS total_hours
    FROM attendance
    WHERE employee_id = emp
    GROUP BY employee_id;
END //

DELIMITER ;
-- Call procedure:
CALL total_work_hours(1);

