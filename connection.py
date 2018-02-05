import sqlite3
from sqlite3 import Error
import os



	
def create_connection():
	db = 'tasks.db'
	if not os.path.isfile(db):
		build_database(db)
	conn = sqlite3.connect(db)
	return conn



def build_database(db):

	conn = sqlite3.connect(r'tasks.db')
	c = conn.cursor()

	c.execute('''CREATE TABLE TODO
        (id Integer ASC , name varchar(100) NOT NULL, description )''')
	c. execute('''CREATE TABLE TODO_Mirror
        (id Integer ASC , name varchar(100) NOT NULL, description )''')

	c.execute('''CREATE TRIGGER IF NOT EXISTS insert_trigger 
		AFTER INSERT on TODO
		FOR each row
		BEGIN
			insert into TODO_Mirror (id,name, description)
			values (NEW.id,NEW.name,NEW.description);
		END;
				''')

	c.execute('''CREATE TRIGGER IF NOT EXISTS update_trigger 
		AFTER UPDATE on TODO
		FOR each row
		BEGIN
			update TODO_Mirror
			set id=NEW.id, name = NEW.name, description = NEW.description
			WHERE id = NEW.id;
		END;
		''')

	c.execute('''CREATE TRIGGER IF NOT EXISTS delete_trigger 
		AFTER DELETE on TODO
		FOR each row
		BEGIN
			delete from TODO_Mirror
			where id=OLD.id;
		END;
		''')


