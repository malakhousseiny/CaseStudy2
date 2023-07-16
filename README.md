# Case Study - Top 50 Songs Per Country and Per User over the Last 7 Days 

## Table of Contents

- [Project Overview](#project-overview)
- [Downloading the Project](#downloading-the-project)
- [Environment Setup](#environment-setup)
- [Project Setup](#project-setup)
- [Installing Required Packages](#installing-required-packages)
- [Running the Project](#running-the-project)
- [Project Structure](#Project-Structure)
- [Code Functionality](#Code-Functionality)
- [Adherence to Constraints](#Adherence-To-Constraints)
- [Additional Information](#Additional-Information)
- [Support](#Support)
- [Contributions](#Contributions)

## Project Overview

This Python-based project processes song listening log data to find the top 50 songs listened to in each country and by each user over the last 7 days. Each daily log file contains the logs of all listening streams made on that date, formatted as `sng_id|user_id|country`.

The solution leverages Python's built-in multiprocessing and collections libraries to efficiently process large volumes of data. The script processes each log file in parallel using Python's multiprocessing module, and for each file, it processes each line one by one to minimize memory usage.

## Downloading the Project

Clone the project from the GitHub repository to your local machine using the following command in your terminal or command prompt:

```bash
git clone <your_repository_url>
```

Replace `<your_repository_url>` with the URL of your GitHub repository.

## Environment Setup

Follow these steps to prepare your environment for running the project:

1. **Python Installation**: Download and install the latest version of Python from the [official Python website](https://www.python.org/). Make sure to follow the installation instructions that are specific to your operating system.

2. **Visual Studio Code**: Download and install Visual Studio Code from the [official site](https://code.visualstudio.com/). This is a powerful and lightweight code editor that we recommend for this project.

## Project Setup

Next, set up the project directory and prepare it for development:

1. **Navigate to the Project Directory**: Open a terminal (or Command Prompt on Windows) and navigate to the directory of the cloned project.

2. **Python Virtual Environment**: While in the project directory, create a new virtual environment for project-specific dependency management. This is separate from your global Python environment and helps avoid potential conflicts between dependencies. Run the command `python -m venv env` on Linux, or `py -m venv env` on Windows.

3. **Activating the Virtual Environment**: To activate the virtual environment, run the appropriate command based on your operating system:
    - For Windows: `env\Scripts\activate`
    - For Linux: `source env/bin/activate`

## Installing Required Packages

Before running the code, ensure that all required packages listed in the `requirements.txt` file are installed in your virtual environment. If any are missing, you can install them with pip using the following command:

```bash
pip install -r requirements.txt
```

Make sure the `requirements.txt` file is in the same directory where you will run the script.

## Running the Project

1. Update the `ROOT_PATH` variable in the Python script to point to your directory containing the daily log files.
2. To run the project, navigate to the directory containing `main.py` and execute the command `python main.py`.

## Project Structure

The main script, `main.py`, processes the log files and generates two output files: `top50_songs_per_country.txt` and `top50_songs_per_user.txt`.

## Code Functionality

Let's break down the main functions of the script:

    process_log_file(file_path): Reads a log file, storing how many times each song has been played by each user and in each country. It employs the collections.defaultdict for easy and efficient counting of song plays. The function gracefully handles potential errors, such as corrupt lines or inaccessible files.

    process_all_log_files(log_files): Utilizes the multiprocessing module to process multiple log files concurrently. This function creates a pool of worker processes and distributes the log files among them. The resultant data from all processes is combined into one dictionary.

    write_top_50(data, filename): Accepts the processed data and writes the top 50 most listened songs for each key (country or user) to a file. The most_common method from the Counter class in the collections module helps identify the top 50 songs.

    get_subdirectories(): Lists all subdirectories within a predefined root directory (ROOT_PATH). Each subdirectory's name is parsed to extract a date (assuming a format 'sample_listen-YYYY-MM-DD_2Mlines'). This function generates a list of tuples, each containing a datetime object of the parsed date and the corresponding directory's path. It handles errors encountered during date parsing effectively.

    process_log_files(): Orchestrates the whole process. It first retrieves the list of log files from a specified root directory, sorts them by date in descending order to process the last 7 days of files. The above functions are then used to process the log files and write the results to output files. Separate files for each country and user are created. Any errors in date parsing are gracefully handled.

## Adherence to Constraints

The script was designed and implemented adhering to the following constraints:

1. Handling Corrupted Rows: Any corrupted lines in the log files are gracefully ignored.

2. No Third-Party Systems: The script is designed with Python's built-in libraries and does not rely on any third-party systems.

3. Limited RAM Usage: By processing each log file and line one by one, the script minimizes the RAM usage.

4. Writing Intermediate Files: No need for intermediate files during the processing. All data is processed in a memory efficient way

5. Linux Compatibility: The script should run without issues on Linux, as it uses platform-independent Python built-in libraries.

6. Maintainability: The script is organized into small, single-purpose functions, enhancing its maintainability.

7. Performance: The use of multiprocessing for concurrent log file processing and collections.Counter for fast counting, improves the overall performance of the script.

## Code Output

This script processes the 7 most recent listening logs to find the top 50 songs listened to in each country and by each user. The logs should be text files located in a specified directory, with each line in the format "song ID | user ID | country". The script processes each log file in parallel using Python's built-in multiprocessing module, and for each file, it processes each line one by one to minimize memory usage. It handles corrupted rows by skipping them. The results are written to two output files: "country_top50_2021-12-01.txt" and "user_top50_2021-12-01.txt". Each line in the output files is in the format "country/user | song1:count1, song2:count2, ...". The script does not rely on any third-party systems or libraries and is compatible with Linux. The script is organized into small, single-purpose functions and uses comments to explain the purpose of each function and important parts of the code. The performance can be limited by disk I/O speed and by the speed of counting songs when the number of unique songs is very large.

## Scheduling the Script
# Running the Code Automatically Daily

To make the script production ready, it can be set to run automatically at a certain time each day. This section provides instructions on how to set this up on Windows and Linux systems.

## Windows

On Windows, you can use the Task Scheduler to run the Python script at prescribed times. Here's how you do it:

1. Open Task Scheduler (you can find it by searching for 'Task Scheduler' in the start menu).
2. Click on 'Create Basic Task'.
3. Enter a name and a description for the task and click 'Next'.
4. Choose the trigger frequency (daily in our case) and click 'Next'.
5. Set the start time and date (e.g., 12:30 AM daily), and click 'Next'.
6. In the 'Action' field, select 'Start a program' and click 'Next'.
7. In the 'Program/script' field, enter the path to the Python executable. This might look something like "C:\Python311\python.exe", but it will depend on where Python is installed on your system.
8. In the 'Add arguments' field, enter the name of your Python script with .py extension.
9. In the 'Start in' field, enter the path to the directory where your Python script is located.
10. Click 'Next', then 'Finish'.

A few things to remember:

- Make sure your script has the right permissions to run (i.e., it's executable).
- Always use absolute paths in your crontab file or Task Scheduler, not relative paths.
- Make sure Python is correctly installed and that your script runs without issues.
- You need to provide the correct path to the Python interpreter and the script in the Task Scheduler.

## Linux

On Linux, you can use `cron` to schedule tasks (called cron jobs). Here's a guide to setting this up:

1. Open Terminal.
2. To open the crontab configuration file, enter the following command: `crontab -e`.
3. This will open the crontab file in your default text editor. If this is your first time running the `crontab -e` command, you may be asked to select a text editor (such as nano, vim, etc.).
4. In the editor, add a new line at the end of the file, structured as follows:

```bash
30 0 * * * /usr/bin/python3 /path/to/your/script.py
```
This line will schedule your script to run every day at 12:30 AM.

5. Save and close the file. If you're using nano, you can do this by pressing `Ctrl+X` to exit, then `Y` to confirm that you want to save changes, and then `Enter` to confirm the file name.
6. Your crontab has now been updated, and the scheduled task should run at your specified intervals.

Remember to replace `/usr/bin/python3` and `/path/to/your/script.py` with the paths to your Python interpreter and your Python script respectively. You can find the path to your Python interpreter by running `which python3` in the terminal.

## Additional Information

- The script is designed to ignore corrupted rows in the input data. If a file cannot be opened, it will print a message and continue to the next file.
- The script is designed to use a limited amount of RAM (less than 1 GB).

## Support

If you have any questions or face any issues while running the script, please raise an issue in this repository.

## Contributions

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



