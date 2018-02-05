
from task import Task
#from connection import Connection
import sys






while (True):
	op = raw_input("Enter desired operation: ")
	if op == 'INSERT':
		name = raw_input('Enter task name: ')
		desc = raw_input('Enter task description: ')
		task_object = Task (name,desc)
		Task.insert_into_db(task_object)
		print("New element was added successfully")
	elif op == 'DELETE':
		name = raw_input('Enter task name: ')
		desc = raw_input('Enter task description: ')
		task_object = Task (name,desc)
		Task.del_from_db(task_object)
		print("Element was deleted successfully")
	elif op == 'UPDATE':
		old_name = raw_input('Enter task old name: ')
		old_desc = raw_input('Enter task old description: ')
		name = raw_input('Enter task new name: ')
		desc = raw_input('Enter task new description: ')
		old_task_object = Task(old_name,old_desc)
		new_task_object = Task (name,desc)
		Task.update_db_element(old_task_object, new_task_object)
		print("Element was updated successfully")
	elif op ==  'GET_ONE':
		id = raw_input('Enter id: ')
		task = Task('null','null')
		task.id = id
		task.get_by_id(id)
	elif op == 'GET_ALL':
		task = Task('Unknown','Unknown')
		task.get_all()
	else:
		print("WRONG OP, PLEASE TRY AGAIN")
		continue
	print 'IF DONE, ENTER -1, else enter any other integer'
	next_in = raw_input("prompt")
	if (next_in == -1):
		break

