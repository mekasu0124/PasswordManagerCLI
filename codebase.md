# .gitignore

```
env/
password_manager.egg-info
.pytest_cache/
__pycache__/
build/
run.py
.env
app/.data/

```

# app\__init__.py

```py

```

# app\commands\__init__.py

```py

```

# app\commands\general\__init__.py

```py

```

# app\commands\general\hello.py

```py
import click


@click.command(name="hello")
@click.option("--name", default="User", help="Enter the name you want the system to greet you by")
def hello_command(name: str) -> None:
    """
    Greets the user with the provided name, otherwise, as User
    """

    msg = (
        f"Hello, {name}!\n"
        "This message shows that your installation worked! Yay!\n"
        "\n"
        "App Name: Mek's Hub Password Manager - CLI\n"
        "App Version: 1.0.0\n"
        "App Description: A light-weight cli application to assist in storing your passwords for easier use and lookup. Most password managers are behind multiple screen options, so why not have one that is just as simple as pwm lookup --link your_link_here or pwm add --link your_link --username your_username --password your_password to have your information readily available."
    )
    return click.echo(msg)
```

# app\commands\general\list_all.py

```py
from app.utilities.json import JsonEngine

import click


@click.command(name="list")
def list_entries():
    json_engine = JsonEngine()

    all_entries = json_engine.list_all_entries()

    
```

# app\commands\management\__init__.py

```py

```

# app\commands\management\add.py

```py
from app.utilities.json import JsonEngine

import click


@click.command(name="add")
@click.option("--link", required=True, help="The link associated with the password.")
@click.option("--username", required=True, help="The username associated with the password.")
@click.option("--password", required=True, help="The password you want to save.")
def add_entry(link: str, username: str, password: str):
    """
    Allows the user to save their desired link, username, and password
    """

    json_engine = JsonEngine()

    data_to_save = {
        "link": link,
        "username": username,
        "password": password
    }

    result = json_engine.save_entry(data_to_save)
    return click.echo(result)

```

# app\commands\management\delete.py

```py
from app.utilities.json import JsonEngine

import click


@click.command(name="delete")
@click.option("--link", required=True, help="The link of the entry to delete")
@click.option("--username", required=True, help="The username of the entry to delete")
def delete_entry(link: str, username: str):
    """
    Allows the user to delete an existing entry from the given link and username.
    """

    json_engine = JsonEngine()

    all_entries = json_engine.list_all_entries()

    entry_to_delete = None

    for index, entry in enumerate(all_entries):
        if entry["link"] == link and entry["username"] == username:
            entry_to_delete = entry
            break
        
    if entry_to_delete:
        click.echo(f"Found Entry:\n\nLink: {entry_to_delete["link"]}\nUsername: {entry_to_delete["username"]}\nPassword: {entry_to_delete["password"]}")
            
        user_agree = input("\nAre You Sure You Want To Delete This Entry? (Y/N): ")

        while not user_agree.lower() in ["y", "n"]:
            click.echo("Invalid Input. Enter 'Y' for Yes or 'N' for No")
            user_agree = input("Are You Sure You Want To Delete This Entry? (Y/N): ")

            if user_agree.lower() in ["y", "n"]:
                break

        if user_agree.lower() == 'n':
            return click.echo("You Elected To Keep This Entry.")
        
        result = json_engine.delete_entry(entry_to_delete)

        return click.echo(result)

```

# app\commands\management\update.py

```py
from app.utilities.json import JsonEngine
import click


@click.command(name="update")
@click.option("--link", required=True, help="The link currently saved")
@click.option("--username", required=True, help="The username currently saved")
@click.option("--password", required=True, help="The new password currently saved.")
@click.option("--new-username", required=False, help="The new username you want to set")
@click.option("--new-password", required=False, help="The new password you want to set")
def update_entry(link: str, username: str, password: str, new_username: str, new_password: str):
    """
    Allows the user to update an existing entry for a given link and username.
    The link will remain unchanged, but the username and/or password can be updated.
    """

    json_engine = JsonEngine()

    current_data = json_engine.list_all_entries()

    entry_to_update = None
    
    for entry in current_data:
        if entry["link"] == link and entry["username"] == username:
            entry_to_update = entry
            break

    if entry_to_update:
        # Check if the new username already exists for the given link
        if new_username:
            for entry in current_data:
                if entry["link"] == link and entry["username"] == new_username:
                    click.echo("That Username Already Exists")
                    return

            # If the username doesn't exist, update it
            entry_to_update["username"] = new_username

        if new_password:
            entry_to_update["password"] = new_password

        # Save the updated entry
        result = json_engine.update_entry(entry_to_update, current_data)
        click.echo(result)
    else:
        click.echo("Entry not found.")

```

# app\images\app-icon.jpeg

This is a binary file of the type: Image

# app\images\Blue - Stone Color Palette - color-hex.com.png

This is a binary file of the type: Image

# app\main.py

```py
from app.commands.general.hello import hello_command
from app.commands.management.add import add_entry
from app.commands.management.update import update_entry
from app.commands.management.delete import delete_entry

import click


@click.group()
def cli():
    """
    A Password Manager CLI Application

    Use the commands below to interact with the application
    """
    pass

cli.add_command(hello_command)
cli.add_command(add_entry)
cli.add_command(update_entry)
cli.add_command(delete_entry)


if __name__ == '__main__':
    cli()
```

# app\utilities\__init__.py

```py

```

# app\utilities\json.py

```py
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

```

# changelog.txt

```txt
Project Started: 12/31/2024 @ 09:35 hours.

12/31/2024
  - Project Instantiated
  - Created
    - venv
    - setup.py
      - if contributing to the code, you can run pip install -e ./ in the root directory of the project and it will install it in development mode. It goes from running one command to another. It's better. trust me
        - Go From: python3 app/main.py hello --name Mek
        - Go To: pwm hello --name Mek
    - all the init files per sub-folder from app down
    - requirements.txt
    - app/utils/json/engine.py
      - the engine class that interacts with the config.json file
    - hello test command
    - hello command
  - Started
    - README.md
    - app/commands/management/add.py
      - The command to add a new password to the database
  - Imported
    - app icon
  - Installed
    - click
```

# README.md

```md
<label id="top"></label>

<div align="center">
  <img src="./app/images/app-icon.jpeg" width="150" height="150" />

  # Mek's Hub - Password Manager - CLI Version
</div>

<div align="center">

[Introduction](#introduction) ... [How To Use](#how-to-use) ... [Installation](#installation) ... [Issues](#issues) ... [Licensing](#licensing) ... [Contributing](#contributing)
</div>


### Introduction

Welcome To Mek's Hub Password Manager - CLI Version. This project was inspired by the mere fact that I consistently have a password manager of some sort (from desktop apps, to websites, and on my phone) always popping up and I figured I'd try and re-create one myself. This application uses [click](https://click.palletsprojects.com/en/stable/) as the framework for executing commands and yielding results.

[<a href="#top">Top</a>]

### How To Use

|commands|usage|description|
|---------|-----|-----------|
| help | pwm --help | displays a help screen to the user for assistance with the application.|
| hello | pwm hello --name "Your Name" | displays a greeting of Hello, Your Name! **Name is optional |
| add | pwm add --link your_link --username your_username --password your_password | Saves the given information. **All Inputs Required |
| update | pwm update --link your_link --username your_username --password your_password --new-username new_username --new-password new_password | Updates the stored entry with the new values given one or both exists. ** link, username, and password are required to accurately locate your matching saved entry |
| delete | pwm delete --link your_link --username your_username --password your_password | Deletes the given entry after user confirmation ** link, username, password are required to accurately locate your matching saved entry |

[<a href="#top">Top</a>]

### Installation

- Regular Users
   - <b><u>Clone the github repository</u></b>
     - <code>git clone https://github.com/mekasu0124/PasswordManagerCLI.git</code> 
   - <b><u>CD into the project</u></b>
     - <code>cd PasswordManagerCLI</code>
   - <b><u>Create the virtual environment</u></b>
     - <b><u>Windows</u></b>
       - <code>python.exe -m venv env</code>
     - <b><u>Linux</u></b>
       - <code>python3 -m venv env</code>
   - <b><u>Activate the virtual environment</u></b>
     - <b><u>Windows</u></b>
       - <code>env\Scripts\activate</code>
     - <b><u>Linux</u></b>
       - <code>source env/bin/activate</code>
   - <b><u>Install UV and UVLoop (Optional)</u></b>
     - <code>pip install uv uvloop</code>
   - <b><u>Install Requirements</u></b>
     - prefix pip with uv if using UV and UVLoop. Example: <code>uv pip ...</code>
     - <code>pip install -r requirements.txt</code>
   - <b><u>Running the package</u></b>
     - <b><u>Short vs Long Command Name</u></b>
       - <b><u>pwm --help</u></b>
         - prefix with uv if using UV and UVLoop
         - <code>pip install -e ./</code>
       - <b><u>python3 app/main.py --help</u></b>
         - change python3 to python on Windows

- Contributors
  - Instead of cloning the repository, fork the repo and the follow from the second step down for <b><u>Regular Users</u></b> above

[<a href="#top">Top</a>]

### Issues

If at any time you experience issues using this application, please head over to the [issues page](https://github.com/mekasu0124/PasswordManagerCLI/issues) and post a new issue. If you don't know how to create an issue on a GitHub repository, [click here](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue)

[<a href="#top">Top</a>]

### Licensing

This application follows the GNULPv3 license. It is a FOSS (Free Open Souce Software) project that
anyone is welcome to clone and create as their own.

> NOTE: This application is not permitted to be used for personal financial gain, reproduction for sales and services, or any other methods/forms of earning a revenue/income based off this application in any manor possible.

[<a href="#top">Top</a>]

### Contributing

Contributors are required to follow the same licensing as above. 

> NOTE: This application is not permitted to be used for personal financial gain, reproduction for sales and services, or any other methods/forms of earning a revenue/income based off this application in any manor possible.

[<a href="#top">Top</a>]

```

# requirements.txt

```txt
click==8.1.8
contourpy==1.3.1
cycler==0.12.1
fonttools==4.55.3
iniconfig==2.0.0
kiwisolver==1.4.8
markdown-it-py==3.0.0
mdurl==0.1.2
numpy==2.2.1
packaging==24.2
-e file:///home/mekasu0124/Documents/Programming/Current/CLI/PasswordManager
pillow==11.0.0
pip==24.0
pluggy==1.5.0
pygments==2.18.0
pyparsing==3.2.0
pytest==8.3.4
python-dateutil==2.9.0.post0
python-dotenv==1.0.1
rich==13.9.4
setuptools==75.6.0
six==1.17.0
uv==0.5.13
uvloop==0.21.0

```

# setup.py

```py
from setuptools import setup, find_packages

setup(
    name='password_manager',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'Click',  # Ensure Click is listed as a dependency
    ],
    entry_points={
        'console_scripts': [
            'pwm=app.main:cli',  # Replace 'cli' with the name of your Click command function
        ],
    },
)

```

# tests\__init__.py

```py

```

# tests\test_add_command.py

```py
from click.testing import CliRunner
from app.commands.management.add import add_command

def test_add_command():
    runner = CliRunner()

    # Correctly pass all arguments and options in a single list
    result = runner.invoke(
        add_command,
        ["--link", "https://google.com", "--username", "mekasu0124", "--password", "Test123!"],
        input="y"
    )

    assert result.exit_code == 0
    assert "Entry Saved" in result.output or "\nEntry Already Exists" in result.output

```

# tests\test_hello.py

```py
from click.testing import CliRunner
from app.commands.general.hello import hello_command


def test_hello_command():
    runner = CliRunner()

    result = runner.invoke(hello_command, ["--name", "Mek"])

    assert result.exit_code == 0
    assert "Hello, Mek!" in result.output

```

# tests\test_update_command.py

```py
from click.testing import CliRunner
from app.commands.management.update import update_command

def test_update_command():
    runner = CliRunner()

    result = runner.invoke(
        update_command,
        ["--link", "https://google.com", "--username", "mekasu012444", "--password", "Test123!", "--new-username", "mekasu0124", "--new-password", "Test1234!"]
    )

    assert result.exit_code == 0
    assert "Entry Updated" in result.output or "Entry not found" in result.output
```

