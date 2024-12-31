import json
import os


class JsonEngine:
    def check_exists(self):
        curr_dir = os.getcwd()
        app_dir = os.path.join(curr_dir, "app")
        data_dir = os.path.join(app_dir, ".data")

        if not os.path.isdir(data_dir):
            os.mkdir(data_dir)

        config_file = os.path.join(data_dir, "config.json")

        if not os.path.isfile(config_file):
            def_dict = {
                "setup": False,
                "agree": False
            }

            with open(config_file, 'w+', encoding="utf-8-sig") as f:
                json.dump(def_dict, f, indent=2)

            return config_file
        
        return config_file
    
    def update_setup(self, value: bool) -> bool:
        file_path = self.check_exists()

        with open(file_path, 'r', encoding="utf-8-sig") as f:
            data = json.load(f)
            
            try:
                data["setup"] = True

                with open(file_path, 'w+', encoding="utf-8-sig") as new:
                    json.dump(data, new, indent=4)

                return True
            except Exception as e:
                print(e)
                return False
    
    def update_agree(self, value: bool) -> bool:
        file_path = self.check_exists()

        with open(file_path, 'r', encoding="utf-8-sig") as f:
            data = json.load(f)
            
            try:
                data["agree"] = True

                with open(file_path, 'w+', encoding="utf-8-sig") as new:
                    json.dump(data, new, indent=4)

                return True
            except Exception as e:
                print(e)
                return False
