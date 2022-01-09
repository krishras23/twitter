
SELECT *
FROM tweet
JOIN followers
ON tweet.username = followers.following
order by createdAt;

ALTER TABLE employee.info
DROP COLUMN DOB;


create database employee

create table employee.info (
    employeeID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	f_name VARCHAR(20) NOT NULL,
	l_name VARCHAR(20) NOT NULL,
	DOB DATE,
	age INT
);

select * from employee.info
select * from employee.about

INSERT INTO employee.info (f_name, l_name, age) values ("hikaru","nakamura",83);

create table employee.about (
    employeeID INT,
	sports VARCHAR(20),
	hobbies VARCHAR(20),
	address VARCHAR(90)
);


INSERT INTO employee.about (employeeID, sports, hobbies, address) values (1,"jackhammer","running", "3230 John Dr, New Mexico");

SELECT *
FROM employee.info
JOIN employee.about
ON employee.info.employeeID = employee.about.employeeID;



SELECT *
FROM employee.info
LEFT JOIN employee.about
ON employee.info.employeeID = employee.about.employeeID;


SELECT *
FROM employee.info
RIGHT JOIN employee.about
ON employee.info.employeeID = employee.about.employeeID;

SELECT *
FROM employee.info
INNER JOIN employee.about
ON employee.info.employeeID = employee.about.employeeID;



SELECT *
FROM employee.info
CROSS JOIN employee.about
ON employee.info.employeeID = employee.about.employeeID;

-- cross join (maps each row)
-- left join (first table)
-- right join (second table)
