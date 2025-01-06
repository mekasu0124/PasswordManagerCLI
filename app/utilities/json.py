import json
import os


class JsonEngine:
    def check_exists(self):
        curr_dir = os.path.dirname(os.path.abspath(__file__))
        app_dir = os.path.dirname(curr_dir)
        data_dir = os.path.join(app_dir, ".data")

        if not os.path.isdir(data_dir):
            os.makedirs(data_dir, exist_ok=True)

        db_file = os.path.join(data_dir, "db.json")

        if not os.path.isfile(db_file):
            with open(db_file, 'w+', encoding="utf-8-sig") as new:
                json.dump([], new, indent=2)

        return db_file

    def list_all_entries(self):
        file_path = self.check_exists()

        with open(file_path, 'r', encoding="utf-8-sig") as f:
            data = json.load(f)

            return data if data else None

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
                if new_entry["link"] == saved_entry["link"] and new_entry["username"] == saved_entry["username"]:
                    return "\nEntry Already Exists!\n"

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

    def delete_entry(self, entry_to_delete: dict):
        file_path = self.check_exists()

        with open(file_path, 'r', encoding="utf-8-sig") as f:
            data = json.load(f)

            for i, entry in enumerate(data):
                if entry["link"] == entry_to_delete["link"] and entry["username"] == entry_to_delete["username"]:
                    data.pop(i)

                    with open(file_path, 'w+', encoding="utf-8-sig") as new:
                        json.dump(data, new, indent=2)

                    return "Entry Deleted Successfully"
                
    
