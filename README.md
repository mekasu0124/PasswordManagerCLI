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
