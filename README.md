
# Facebook Automation using Python Selenium

This project automates various Facebook functionalities such as logging in, logging out, and password recovery using Python and Selenium WebDriver. It demonstrates the power of browser automation for specific use cases while addressing the limitations of Selenium by incorporating PyAutoGUI where necessary.

## Features
- **Login Automation**: Automatically log into Facebook with provided credentials.
- **Logout Automation**: Log out of the Facebook account.
- **Password Recovery**: Automate the process of recovering a forgotten password.
- **Mail Handling with PyAutoGUI**: Navigate and copy security codes from emails for password recovery.

## Prerequisites
- Python 3.7+
- Google Chrome (or the browser you wish to automate)
- ChromeDriver (version compatible with your Chrome browser)
- Required Python libraries:
  - Selenium
  - PyAutoGUI

## Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/ChathuraJayakody/facebook-automation-selenium.git
   ```
2. Navigate to the project directory:
   ```bash
   cd facebook-automation-selenium
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Update the `config.py` file (if applicable) with your Facebook credentials and other necessary configurations.

## Usage
1. Run the `forgot_password.py` script to test the password recovery functionality:
   ```bash
   python forgot_password.py
   ```
2. Use the `test.py` script to perform automated tests:
   ```bash
   python test.py
   ```

## Folder Structure
- `forgot_password.py`: Script for automating the password recovery process.
- `login.py`: Script for automating login functionality.
- `main.py`: Main script to orchestrate automation tasks.
- `requirements.txt`: Python dependencies for the project.

## Notes
- Ensure that you have a stable internet connection and that the browser window remains in focus during automation.
- Adjust screen resolution settings if using PyAutoGUI on different monitors.

## Disclaimer
This project is for educational purposes only. Use it responsibly and do not violate Facebook's terms of service.
