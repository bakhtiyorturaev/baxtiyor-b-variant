import psycopg2

db_settings = {
    'dbname': 'postgres',
    'user': 'baxtiyor',
    'password': 1002,
    'host': 'localhost',
    'port': 5432
}

try:

    conn = psycopg2.connect(**db_settings)
    cur = connection.cursor("""
SELECT e.employee_id, e.employee_name, COUNT(p.project_id) AS project_count
FROM employees e
LEFT JOIN projects p ON e.employee_id = p.employee_id
GROUP BY e.employee_id, e.employee_name
ORDER BY project_count DESC
LIMIT 4""")