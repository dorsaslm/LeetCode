CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE off INT;

IF N IS NULL OR N < 1 THEN
    RETURN NULL;
  END IF;

 # if N = 1 SET off = 1 else SET off = N - 1;
 SET off = N - 1;

  RETURN (

    select t.salary from (
      # Write your MySQL query statement below.
    select distinct salary 
    from employee
    order by salary desc
    limit off,1 ) as t
  );
END