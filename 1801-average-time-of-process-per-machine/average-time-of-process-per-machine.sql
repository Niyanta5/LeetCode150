# Write your MySQL query statement below
/*
id processid end start   

0.   0.      1.5    0.7
0.   1.     4.1     3.1

0    0    null.  0.7
0.   0    1.5.   null

id processid ems
0     0.       0.8
0.     1       0.9

select id, sum(ems) as processing_time  from Activity group by id

*/

select machine_id, round(avg(end_minus_start), 3) as processing_time from(
select machine_id, process_id, (max(case when activity_type = 'end' then timestamp end) - max(case when activity_type = 'start' then timestamp end)) as end_minus_start
from Activity group by machine_id, process_id) m group by machine_id
