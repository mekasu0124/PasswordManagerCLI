import sqlite3 as sql
import os



class DbEngine:
    def check_exists(self) -> tuple:
        curr_dir = os.getcwd()
        app_dir = os.path.join(curr_dir, "app")
        data_dir = os.path.join(app_dir, ".data")

        if not os.path.isdir(data_dir):
            os.mkdir(data_dir)

        db_file = os.path.join(data_dir, "main.db")

        if not os.path.isfile(db_file):
            is_created = self.create_db_file(db_file)

            if not is_created:
                return (False, is_created[1])
            
            return (True, db_file)
        
        return (True, db_file)
    
    def create_db_file(self, file_name: str) -> tuple:
        try:
            with sql.connect(file_name) as mdb:
                cursor = mdb.cursor()
        except sql.Error as e:
            raise e
        

if __name__ == '__main__':
    engine = DbEngine()
    engine.create_db_file("john_doe.db")