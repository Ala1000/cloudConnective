import sqlite3
from sqlite3 import Error
import connection
#from connection import Connection


class Task():

	name= "Unknown"
	desc = "Unknown"
	id = -1

	def __init__(self, name, desc):
		self.name = name
		self.desc = desc

	#def __init__(self, id):
		#self.id = id

	def create_task(name,desc):
		task = Task(name,desc)
		insert_into_db(task)


	def insert_into_db(new_task):
		values = [new_task.name, new_task.desc]
		conn = connection.create_connection()
		c = conn.cursor()
		c.execute('''INSERT INTO TODO(name,description) VALUES(?,?)''',values)
		conn.commit()
		c.close()
		conn.close()

	def del_from_db(task):
		values = [task.name, task.desc]
		conn = connection.create_connection()
		c = conn.cursor()
		c.execute('''DELETE FROM TODO WHERE name =?''',(task.name,))
		conn.commit()
		c.close()
		conn.close()

	def update_db_element(old_task, new_task):
		conn = connection.create_connection()
		c = conn.cursor()
		id = c.execute('''UPDATE TODO SET name= ?, description = ? WHERE name = ? and description = ?''',(new_task.name,new_task.desc,old_task.name, old_task.desc))
		c.commit()
		c.close()
		conn.close()

	def get_by_id(self,id):
		conn = connection.create_connection()
		c = conn.cursor()
		c.execute('''SELECT * FROM TODO WHERE id =?''',(id,))
		print(c.fetchall())
		c.close()
		conn.close()

	def get_all(self):
		conn = connection.create_connection()
		c = conn.cursor()
		c.execute('''SELECT * FROM TODO''')
		print(c.fetchall())
		c.close()
		conn.close()