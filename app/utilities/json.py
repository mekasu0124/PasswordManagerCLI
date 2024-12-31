import json
import os


class JsonEngine:
    def check_exists(self):
        curr_dir = os.getcwd()
        app_dir = os.path.join(curr_dir, "app")
        data_dir = os.path.join(app_dir, ".data")

        if not os.path.isdir(data_dir):
            os.mkdir(data_dir)

        db_file = os.path.join(data_dir, "db.json")

        if not os.path.isfile(db_file):
            with open(db_file, 'w+', encoding="utf-8-sig") as new:
                json.dump([], new, indent=2)

            return db_file
        
        return db_file
    
    def save_entry(self, new_entry: dict):
        file_path = self.check_exists()

        with open(file_path, 'r', encoding="utf-8-sig") as f:
            data = json.load(f)

            if not data:
                data.append(new_entry)

                with open(file_path, 'w+', encoding="utf-8-sig") as new:
                    json.dump(data, new, indent=2)

                return "Entry Saved Successfully"

            for saved_entry in data:
                link = saved_entry["link"]
                username = saved_entry["username"]
                password = saved_entry["password"]

                if new_entry["link"] == link and new_entry["username"] == username:
                    return f"\nEntry Already Exists!\n\nUsername: {username}\nLink: {link}\nPassword: {password}"
                
                data.append(new_entry)

                with open(file_path, 'w+', encoding="utf-8-sig") as new:
                    json.dump(data, new, indent=4)

                return "Entry Saved Successfully"
            
    def update_entry(self, updated_entry: dict, current_data: list):
        file_path = self.check_exists()

        for i, entry in enumerate(current_data):
            if entry["link"] == updated_entry["link"] and entry["username"] == updated_entry["username"]:
                current_data[i] = updated_entry
                break

        with open(file_path, 'w+', encoding="utf-8-sig") as new:
            json.dump(current_data, new, indent=2)

        return "Entry Updated Successfully"
            
    def list_all_entries(self):
        file_path = self.check_exists()

        with open(file_path, 'r', encoding="utf-8-sig") as f:
            data = json.load(f)

            return data if data else None
