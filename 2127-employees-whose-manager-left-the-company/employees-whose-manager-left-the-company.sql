SELECT employee_id
FROM Employees e1
WHERE salary < 30000
AND manager_id IS NOT NULL
AND manager_id NOT IN (SELECT employee_id FROM Employees)
ORDER BY employee_id;