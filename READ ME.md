This project focuses on processing log data containing user song streaming activities and generates daily statistics. These statistics are the top 50 songs most listened to in each country and by each user within the last 7 days.

## Table of Contents
- [Environment Setup](#environment-setup)
- [Project Setup](#project-setup)
- [Implementation](#implementation)
- [How to Run](#how-to-run)
- [Output](#output)
- [Schedule the Code](#schedule-the-code)
- [Additional Information](#additional-information)
- [Limitations](#limitations)
- [Support](#support)
- [Contributions](#contributions)

## Environment Setup
1. Download and install Python: Visit the official [Python website](https://www.python.org/) to download the latest version and follow the installation instructions for your operating system.
2. Download and install Visual Studio Code: Visit the [VS Code website](https://code.visualstudio.com/) to download and install it. VS Code is a powerful, lightweight code editor.

## Project Setup
1. **Create a new directory**: Open a terminal or command prompt, navigate to the desired location, and create a new directory using the `mkdir` command.
2. **Initialize a new Git repository**: Inside the project directory, run the command `git init` to initialize a new Git repository. This will allow us to track changes and easily upload our code to GitHub.
3. **Create a new Python virtual environment**: Navigate to the project directory and run the command `python -m venv env` to create a new virtual environment.
4. **Activate the virtual environment**: Use the appropriate command based on your operating system:
    - Windows: `env\Scripts\activate`
    - macOS/Linux: `source env/bin/activate`
5. **Create a Python script**: Using VS Code, create a new Python file in your project directory. For example: `main.py`.

Note: Virtual environments are crucial for isolating project-specific dependencies and mitigating version conflicts between different projects.

## Implementation
This Python script leverages multiprocessing, collections and file handling techniques to process large amounts of data efficiently. It reads data from log files, each of which contains listening data for songs from various users and countries. It calculates the top 50 most listened songs for each user and country for the last 7 days.

Please refer to `main.py` for detailed code comments and function descriptions.

## How to Run
1. Clone the repository or download the project files.
2. Update the `ROOT_PATH` variable in `main.py` to point to your directory containing the daily log files.
3. Open the terminal/command prompt.
4. Navigate to the directory containing `main.py`.
5. Run the following command: `python main.py`
6. The script will process all ".log" files in the `ROOT_PATH` directory and generate two output files: `top50_songs_per_country.txt` and `top50_songs_per_user.txt`.

## Output
The script generates two output files:
1. `top50_songs_per_country.txt`: Lists the top 50 songs listened in each country.
2. `top50_songs_per_user.txt`: Lists the top 50 songs listened to by each user.

## Schedule the Code
You can automate the script to run daily at a specific time. The method varies between Windows and Linux systems.

- **Windows**: Use the Task Scheduler. Please follow [these instructions](#windows-task-scheduler).

- **Linux**: Use Cron jobs. Please follow [these instructions](#linux-cron-jobs).

### Windows Task Scheduler
- Open Task Scheduler. Search for 'Task Scheduler' in the start menu.
- Click on 'Create Basic Task'.
- Enter a name and a description for the task. Click 'Next'.
- Choose the trigger frequency (daily). Click 'Next'.
- Set the start time and date. Click 'Next'.
- In the 'Action' field, select 'Start a program'. Click 'Next'.
- In the 'Program/script' field, enter the path to the Python executable.
- In the 'Add arguments' field, enter the name of your Python script with the .py extension.
- In the 'Start in' field, enter the path to the directory where your Python script is located.
- Click 'Next', then 'Finish'.

### Linux Cron Jobs
- Open Terminal.
- To open the crontab configuration file, enter `crontab -e`.
- In the editor, enter a new line at the end of the file in this format: `* * * * * /usr/bin/python3 /path/to/your/script.py`.
- Save and close the file.

## Additional Information
- The script is designed to ignore corrupted rows in the input data. It will print a message and continue to the next file if a file cannot be opened.
- The script is designed


