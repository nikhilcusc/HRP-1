## Oracle SQL
### Notes:
1. To find the smallest, longest strings in tables, use:
    >select * from (SELECT CITY, LENGTH(CITY) FROM STATION WHERE LENGTH(CITY) IN (
    > SELECT MIN(LENGTH(CITY))
    > FROM STATION
    >) ORDER BY LENGTH(CITY),  CITY ASC) where ROWNUM<=1;

1. To use REGEX :
    >select * from STATION where **REGEXP_LIKE(CITY,'^.**;

1. Replace:
    >REPLACE(SALARY,0,'')

1. The CAST() function converts a value (of any type) into a specified datatype.
    vs
    The CONVERT() function converts a value (of any type) into a specified datatype.

1. Euclidean distance:
    > select ROUND(SQRT( POWER( (MAX(LAT_N) - MIN(LAT_N)),2 ) + POWER( (MAX(LONG_W) - MIN(LONG_W)),2) ),4) from STATION;

1. Joins:
   
    1. (INNER) JOIN: Returns records that have matching values in both tables. 
    1. LEFT (OUTER) JOIN: Returns all records from the left table, and the matched records from the right table. 
    1. RIGHT (OUTER) JOIN: Returns all records from the right table, and the matched records from the left table.
    1. FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table.
    
     > SELECT * FROM Orders INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID;