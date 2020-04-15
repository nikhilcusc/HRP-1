## Oracle SQL
### Notes:
1. To find the smallest, longest strings in tables, use:
    >select * from (SELECT CITY, LENGTH(CITY) FROM STATION WHERE LENGTH(CITY) IN (
    > SELECT MIN(LENGTH(CITY))
    > FROM STATION
    >) ORDER BY LENGTH(CITY),  CITY ASC) where ROWNUM<=1;

1. TO use REGEX :
    >select * from STATION where **REGEXP_LIKE(CITY,'^.**;