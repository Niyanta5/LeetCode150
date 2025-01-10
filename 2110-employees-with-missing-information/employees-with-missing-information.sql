SELECT DISTINCT u.employee_id
FROM (
    SELECT employee_id FROM employees
    UNION ALL
    SELECT employee_id FROM salaries
) u
LEFT JOIN employees e ON e.employee_id = u.employee_id
LEFT JOIN salaries s ON s.employee_id = u.employee_id
WHERE e.name IS NULL OR s.salary IS NULL
ORDER BY u.employee_id;
