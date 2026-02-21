import pandas as pd
import sqlite3

# TASK 1: The Insight Filter
conn=sqlite3.connect("C:/Users/abdul/Desktop/database/internship.db")
af = pd.read_sql_query("SELECT * FROM interns WHERE stipend>5000 AND track='Data Science'",conn)
print("Interns from Data Science Track who's stipend is greater than 5000\n",af)
bf = pd.read_sql_query("SELECT track,avg(stipend) FROM interns GROUP BY track",conn)
print("Average stipend of each track:\n",bf)
cf = pd.read_sql_query("SELECT track,count(id) FROM interns GROUP BY track", conn)
print("Count of interns in each track:\n",cf)

#Task 2: The Data Connector (JOINs & Python Integration)

df = pd.read_sql_query("SELECT interns.name,mentors.mentor_name FROM interns INNER JOIN mentors ON interns.track=mentors.mentor_track", conn)
print("Mentors of each intern are:\n",df)