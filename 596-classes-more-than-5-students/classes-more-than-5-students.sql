# Write your MySQL query statement below

select c.class from 
(select class, count(student) as student_count
from courses
group by class
having count(student)>=5 )c
