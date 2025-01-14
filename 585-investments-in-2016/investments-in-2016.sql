# Write your MySQL query statement below

select round(SUM(tiv_2016),2) AS tiv_2016
from insurance
where tiv_2015 IN (
    select tiv_2015
    from insurance
    GROUP BY tiv_2015
    HAVING COUNT(tiv_2015) > 1
)
AND (lat, lon) IN (
    SELECT lat, lon
    FROM insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
);
