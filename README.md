<div align="center">
  <img src="./app/images/app-icon.jpeg" width="150" height="150" />

  # Mek's Hub - Password Manager - CLI Version
</div>

<div align="center">

[Introduction](#introduction) ... [How To Use](#how-to-use) ... [Installation](#installation) ... [Issues](#issues) ... [Licensing](#licensing) ... [Contributing](#contributing)
</div>

### Introduction

Welcome to **Mek's Hub Password Manager - CLI Version**. This project was inspired by the need for a simple, lightweight, and efficient password manager. Built with [Click](https://click.palletsprojects.com/en/stable/) and enhanced with [Rich](https://rich.readthedocs.io/en/stable/), this CLI application provides a seamless and visually appealing experience for managing your passwords.

[<a href="#top">Top</a>]

### How To Use

| Command  | Usage                                                                 | Description                                                                 |
|----------|-----------------------------------------------------------------------|-----------------------------------------------------------------------------|
| `help`   | `pwm --help`                                                         | Displays a help screen for assistance with the application.                |
| `hello`  | `pwm hello --name "Your Name"`                                       | Displays a greeting. **Name is optional**.                                 |
| `add`    | `pwm add --link your_link --username your_username --password your_password` | Saves the given information. **All inputs are required**.                  |
| `update` | `pwm update --link your_link --username your_username --password your_password --new-username new_username --new-password new_password` | Updates the stored entry with the new values. **Link, username, and password are required**. |
| `delete` | `pwm delete --link your_link --username your_username`               | Deletes the given entry after user confirmation. **Link and username are required**. |
| `list`   | `pwm list`                                                           | Displays all saved entries in a beautifully formatted table.               |

[<a href="#top">Top</a>]

### Installation

#### Regular Users
1. **Clone the GitHub repository**:
   ```bash
   git clone https://github.com/mekasu0124/PasswordManagerCLI.git
   ```
2. **Navigate into the project directory**:
   ```bash
   cd PasswordManagerCLI
   ```
3. **Create a virtual environment**:
   - **Windows**:
     ```bash
     python.exe -m venv env
     ```
   - **Linux**:
     ```bash
     python3 -m venv env
     ```
4. **Activate the virtual environment**:
   - **Windows**:
     ```bash
     env\Scripts\activate
     ```
   - **Linux**:
     ```bash
     source env/bin/activate
     ```
5. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
6. **Run the application**:
   ```bash
   pwm --help
   ```

#### Contributors
1. **Fork the repository**.
2. Follow the steps for **Regular Users** starting from step 2.

[<a href="#top">Top</a>]

### Issues

If you encounter any issues, please [create a new issue](https://github.com/mekasu0124/PasswordManagerCLI/issues) on the GitHub repository. For guidance on creating issues, refer to the [GitHub documentation](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue).

[<a href="#top">Top</a>]

### Licensing

This project is licensed under the **GNU GPLv3 License**. It is a free and open-source software (FOSS) project that anyone is welcome to use, modify, and distribute.

> **Note**: This application is not permitted to be used for personal financial gain, reproduction for sales and services, or any other methods/forms of earning revenue/income based on this application.

[<a href="#top">Top</a>]

### Contributing

Contributors are required to adhere to the same licensing terms as above. Fork the repository, make your changes, and submit a pull request. Ensure your code follows the project's style and guidelines.

> **Note**: This application is not permitted to be used for personal financial gain, reproduction for sales and services, or any other methods/forms of earning revenue/income based on this application.

[<a href="#top">Top</a>]
