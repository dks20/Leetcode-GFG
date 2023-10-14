# Write your MySQL query statement below
SELECT  Distinct author_id AS id
FROM Views
WHERE author_id = viewer_id
Order By id;