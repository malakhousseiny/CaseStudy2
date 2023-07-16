## Step 1: Environment Setup

1. Download and install Python: Visit the official Python website (https://www.python.org/) and download the latest version of Python. Follow the installation instructions for your operating system.

2. Install VS Code: Download and install Visual Studio Code (https://code.visualstudio.com/), a lightweight and powerful code editor.

## Step 2: Project Setup

1. Create a new directory for our project: Open a terminal or command prompt, navigate to the desired location, and create a new directory using the `mkdir` command.

2. Initialize a new Git repository: Inside the project directory, run the command `git init` to initialize a new Git repository. This will allow us to track changes and easily upload our code to GitHub.

3. Create a new Python virtual environment: In the terminal, navigate to the project directory and run the command `python -m venv env` to create a new virtual environment.

   - By using a virtual environment, you can create a controlled and reproducible environment for your project, ensuring that it runs consistently across different systems. Additionally, relying on a text editor or command line interface allows for flexibility and simplicity, making it easier to maintain and run the solution in a Linux production environment.

4. Activate the virtual environment:

   - For Windows: Run the command `env\Scripts\activate`.
   - For macOS/Linux: Run the command `source env/bin/activate`.

   (In case of encountering the "cannot be loaded because running scripts is disabled" error, refer to the provided instructions for Windows and Linux to resolve the issue.)

## Step 3: Coding and Adherence to Constraints

This Python script leverages multiprocessing, collections, and file handling techniques to process large amounts of data efficiently. The script reads data from log files that contain listening data for songs from various users and countries, then calculates the top 50 most listened songs for each user and country for the last 7 days.

### Functions:

- `process_log_file(file_path)`: This function reads a log file and records how many times each song has been played by each user and in each country. The data is stored in a defaultdict from the collections module, which allows easy and efficient counting of song plays. Any errors, such as corrupt lines or inaccessible files, are handled and do not stop the script from running.

- `process_all_log_files(log_files)`: This function leverages the multiprocessing module to process multiple log files concurrently. It creates a pool of worker processes and distributes the log files among them. After processing, it combines the data from all processes into one dictionary.

- `write_top_50(data, filename)`: This function takes in the processed data and writes the top 50 most listened songs for each key (country or user) to a file. It uses the `most_common` method from the Counter class in the collections module to get the top 50 songs for each key.

- `get_subdirectories()`: This function lists all subdirectories within a predefined root directory (`ROOT_PATH`). It parses each subdirectory's name to extract a date, assuming a specific format ('sample_listen-YYYY-MM-DD_2Mlines'). A list of tuples is generated, with each tuple containing a `datetime` object of the parsed date and the corresponding directory's path. If the function encounters an error while parsing the date, it logs an error message and moves on to the next directory.

- `process_log_files()`: This is the main function that orchestrates the whole process. It retrieves the list of log files from a specified root directory, sorts them by date in descending order to process the last 7 days of files, and uses the above functions to process the log files and write the results to output files. It creates separate files for each country and user. Any errors in date parsing are handled and do not stop the script from running.

### Adherence to Constraints:

- **Handling Corrupted Rows**: The script handles corrupted rows by using a `try`/`except` block in the `process_log_file()` function. When a line does not split into exactly three parts (song ID, user ID, and country), a `ValueError` is raised, and the script ignores this line and moves on to the next one.

- **No Third-Party Systems**: This script does not rely on any third-party systems. It only uses Python's built-in libraries (`os`, `collections`, and `multiprocessing`).

- **Limited RAM Usage**: The script processes each log file one by one, and for each file, it processes each line one by one. This means the script never needs to load an entire file into memory at once. Moreover, it uses `collections.Counter` to store counts, which is memory efficient. However, if the number of unique songs or unique countries/users is very large, memory usage can still be high. In such cases, additional techniques such as disk-based storage or data compression may be needed.

- **Writing Intermediate Files**: This script doesn't write any intermediate files. It processes all data in memory. If needed, you could modify the script to store intermediate counts to disk (for example, you could write the `data` dictionary to a file after processing each log file).

- **Linux Compatibility**: This script should be compatible with Linux, as it uses only Python's built-in libraries, which are platform independent. It does not have any Windows-specific code.

- **Maintainability**: The script is organized into small, single-purpose functions, which improves maintainability. Comments are used to explain the purpose of each function and important parts of the code. The script is also robust because it handles errors and exceptions in file reading, date parsing, and data processing.

- **Performance**: The script uses `multiprocessing` to process log files in parallel, which can greatly improve performance on multi-core systems. It uses `collections.Counter` for counting, which is fast. However, the performance can still be limited by disk I/O speed and the speed of the `most_common()` method when the number of unique songs is very large.

## Project
### Functions:

- `process_log_file(file_path)`: This function reads a log file and records how many times each song has been played by each user and in each country. The data is stored in a defaultdict from the collections module, which allows easy and efficient counting of song plays. Any errors, such as corrupt lines or inaccessible files, are handled and do not stop the script from running.

- `process_all_log_files(log_files)`: This function leverages the multiprocessing module to process multiple log files concurrently. It creates a pool of worker processes and distributes the log files among them. After processing, it combines the data from all processes into one dictionary.

- `write_top_50(data, filename)`: This function takes in the processed data and writes the top 50 most listened songs for each key (country or user) to a file. It uses the `most_common` method from the Counter class in the collections module to get the top 50 songs for each key.

- `get_subdirectories()`: This function lists all subdirectories within a predefined root directory (`ROOT_PATH`). It parses each subdirectory's name to extract a date, assuming a specific format ('sample_listen-YYYY-MM-DD_2Mlines'). A list of tuples is generated, with each tuple containing a `datetime` object of the parsed date and the corresponding directory's path. If the function encounters an error while parsing the date, it logs an error message and moves on to the next directory.

- `process_log_files()`: This is the main function that orchestrates the whole process. It retrieves the list of log files from a specified root directory, sorts them by date in descending order to process the last 7 days of files, and uses the above functions to process the log files and write the results to output files. It creates separate files for each country and user. Any errors in date parsing are handled and do not stop the script from running.

### Adherence to Constraints:

- **Handling Corrupted Rows**: The script handles corrupted rows by using a `try`/`except` block in the `process_log_file()` function. When a line does not split into exactly three parts (song ID, user ID, and country), a `ValueError` is raised, and the script ignores this line and moves on to the next one.

- **No Third-Party Systems**: This script does not rely on any third-party systems. It only uses Python's built-in libraries (`os`, `collections`, and `multiprocessing`).

- **Limited RAM Usage**: The script processes each log file one by one, and for each file, it processes each line one by one. This means the script never needs to load an entire file into memory at once. Moreover, it uses `collections.Counter` to store counts, which is memory efficient. However, if the number of unique songs or unique countries/users is very large, memory usage can still be high. In such cases, additional techniques such as disk-based storage or data compression may be needed.

- **Writing Intermediate Files**: This script doesn't write any intermediate files. It processes all data in memory. If needed, you could modify the script to store intermediate counts to disk (for example, you could write the `data` dictionary to a file after processing each log file).

- **Linux Compatibility**: This script should be compatible with Linux, as it uses only Python's built-in libraries, which are platform independent. It does not have any Windows-specific code.

- **Maintainability**: The script is organized into small, single-purpose functions, which improves maintainability. Comments are used to explain the purpose of each function and important parts of the code. The script is also robust because it handles errors and exceptions in file reading, date parsing, and data processing.

- **Performance**: The script uses `multiprocessing` to process log files in parallel, which can greatly improve performance on multi-core systems. It uses `collections.Counter` for counting, which is fast. However, the performance can still be limited by disk I/O speed and the speed of the `most_common()` method when the number of unique songs is very large.

## Project
Step 1: Environment Setup

    Download and install Python: Visit the official Python website (https://www.python.org/) and download the latest version of Python. Follow the installation instructions for your operating system.

1-I chose Python because it is the most common language used in data engineering projects

    Install VS Code: Download and install Visual Studio Code (https://code.visualstudio.com/), a lightweight and powerful code editor.

Step 2: Project Setup


2-Create a new directory for our project: Open a terminal or command prompt, navigate to the desired location, and create a new directory using the mkdir command.
3-Initialize a new Git repository: Inside the project directory, run the command 'git init' to initialize a new Git repository. This will allow us to track changes and easily upload our code to GitHub.
4-Create a new Python virtual environment: In the terminal, we can navigate to the project directory and run the command python -m venv env to create a new virtual environment.
"This allows us to manage project-specific dependencies separately from the global Python environment. This isolation ensures that the installed packages and libraries are contained within the virtual environment,allowing us to have full control over the environment without affecting other projects or the system-wide Python installation.This approach maintains a consistent and reproducible development environment, facilitating collaboration and ensuring the project runs reliably across different systems."

 **By using a virtual environment, you can create a controlled and reproducible environment for your project, ensuring that it runs consistently across different systems. Additionally, relying on a text editor or command line interface allows for flexibility and simplicity, making it easier to maintain and run the solution in a Linux production environment.**


5- Activate the virtual environment: we run the appropriate command to activate the virtual environment based on our operating system:

**For Windows: env\Scripts\activate**
    **For macOS/Linux: source env/bin/activate**


(in case of having this error message : cannot be loaded because running scripts is disabled 
on this system. For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
+ env\Scripts\activate
+ ~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess

To resolve this issue:
    In windows: 
            we can change the execution policy to allow script execution. Follow these steps:

            Open a new PowerShell session with administrator privileges.
            Run the command Set-ExecutionPolicy RemoteSigned. This command sets the execution policy to allow running local scripts.
            When prompted to confirm the change, type Y and press Enter.

            After changing the execution policy, you should be able to activate the virtual environment using the env\Scripts\activate command without encountering the "running scripts is disabled" error.

            Note: Changing the execution policy can have security implications. It's recommended to set it back to a more restrictive policy after you're done working with the virtual environment. You can use the command Set-ExecutionPolicy Restricted to restore the default policy.
    In Linux: 
            

            In Linux, you won't encounter the same error message because Linux does not have PowerShell as the default shell. Instead, Linux typically uses Bash or another shell.

            However, in Linux, you may encounter permission-related issues when trying to execute scripts. To resolve such issues, you can use the chmod command to give the script executable permissions. For example, you can use the following command to make a script executable:


            'chmod +x script_name.sh'

            After making the script executable, you can run it using ./script_name.sh.

8-Create a Python script: Using VS Code, create a new Python file in your project directory, here it is: main.py.

# Step 3: Coding and adherence to constraints: 

This Python script leverages multiprocessing, collections and file handling techniques to process large amounts of data efficiently. The script reads data from log files which contain listening data for songs from various users and countries, then it calculates the top 50 most listened songs for each user and country for the last 7 days.

Let's go through each function and describe why and how they are used.

- `process_log_file(file_path)`: This function reads a log file and records how many times each song has been played by each user and in each country. The data is stored in a defaultdict from the collections module, which allows easy and efficient counting of song plays. Any errors, such as corrupt lines or inaccessible files, are handled and do not stop the script from running.

- `process_all_log_files(log_files)`: This function leverages the multiprocessing module to process multiple log files concurrently. It does this by creating a pool of worker processes and distributing the log files among them. After processing, it combines the data from all processes into one dictionary.

- `write_top_50(data, filename)`: This function takes in the processed data and writes the top 50 most listened songs for each key (country or user) to a file. It uses the 'most_common' method from the Counter class in the collections module to get the top 50 songs for each key.

- `get_subdirectories()`: This function is tasked with listing all subdirectories within a predefined root directory (`ROOT_PATH`). It parses each subdirectory's name to extract a date, assuming a specific format ('sample_listen-YYYY-MM-DD_2Mlines'). A list of tuples is generated, with each tuple containing a `datetime` object of the parsed date and the corresponding directory's path. If the function encounters an error while parsing the date, it will log an error message and move on to the next directory. This function is a fundamental part of the script's flow, as it establishes the data set for the subsequent analysis by identifying the relevant directories to be processed. The design ensures robust error handling, allowing the script to continue running even when faced with unexpected directory names.
- 
- `process_log_files()`: This is the main function that orchestrates the whole process. It first gets the list of log files from a specified root directory and then sorts them by date in descending order to process the last 7 days of files. It then uses the above functions to process the log files and write the results to output files. It creates separate files for each country and user. Any errors in date parsing are handled and do not stop the script from running.

This script is efficient because it splits the processing of log files into separate processes, which can run on separate cores of a CPU and thus speed up the processing. It's also very scalable and can handle increasing numbers of log files and rows of data.

In terms of readability and maintainability, the script is divided into functions each with a specific task, which makes the code easier to understand and modify. The script is also robust because it handles errors and exceptions in file reading, date parsing, and data processing.

As for memory efficiency, the script does not store all the raw data in memory but only counts of song plays. Also, by processing each file separately and then combining the results, it avoids having to load all data into memory at once.

Adherance to constraints :
1. **Handling Corrupted Rows**: The script handles corrupted rows by using a `try`/`except` block in the `process_log_file()` function. When a line does not split into exactly three parts (song ID, user ID, and country), a `ValueError` is raised, and the script ignores this line and moves on to the next one.

2. **No Third-Party Systems**: This script does not rely on any third-party systems. It only uses Python's built-in libraries (`os`, `collections`, and `multiprocessing`).

3. **Limited RAM Usage**: The script processes each log file one by one, and for each file, it processes each line one by one. This means the script never needs to load an entire file into memory at once. Moreover, it uses `collections.Counter` to store counts, which is memory efficient. However, if the number of unique songs or unique countries/users is very large, memory usage can still be high. In such cases, additional techniques such as disk-based storage or data compression may be needed.

4. **Writing Intermediate Files**: This script doesn't write any intermediate files. It processes all data in memory. If needed, you could modify the script to store intermediate counts to disk (for example, you could write the `data` dictionary to a file after processing each log file).

5. **Linux Compatibility**: This script should be compatible with Linux, as it uses only Python's built-in libraries which are platform independent. It does not have any Windows-specific code.

6. **Maintainability**: The script is organized into small, single-purpose functions, which improves maintainability. Comments are used to explain the purpose of each function and important parts of the code. However, the script lacks error checking and logging, which could be improved.

7. **Performance**: The script uses `multiprocessing` to process log files in parallel, which can greatly improve performance on multi-core systems. It uses `collections.Counter` for counting, which is fast. But, the performance can still be limited by disk I/O speed, and by the speed of the `most_common()` method when the number of unique songs is very large.

What does the code do?
This script processes song listening logs to find the top 50 songs listened in each country and by each user. The logs should be text files located in a specified directory, with each line in the format "song ID | user ID | country". The script processes each log file in parallel using Python's built-in multiprocessing module, and for each file, it processes each line one by one to minimize memory usage. It handles corrupted rows by skipping them. The results are written to two output files: "top50_songs_per_country.txt" and "top50_songs_per_user.txt". Each line in the output files is in the format "country/user | song1:count1, song2:count2, ...". The script does not rely on any third-party systems or libraries, and it should be compatible with Linux. The script is organized into small, single-purpose functions, and uses comments to explain the purpose of each function and important parts of the code. The performance can be limited by disk I/O speed, and by the speed of counting songs when the number of unique songs is very large.

![Alt text](image.png) RAM before running the code
![Alt text](image-1.png) RAM after running the code




```markdown
# Project Description

The main task is to process log data containing user song streaming activities and generate daily statistics. The statistics produced are the top 50 songs most listened to in each country and by each user within the last 7 days.

Each daily log file contains the logs of all listening streams made on that date, formatted as `sng_id|user_id|country`.

## Implementation

The solution is implemented in Python using core libraries only. The implementation uses the Python's multiprocessing and collections libraries to efficiently process large amounts of data.

## File Structure

The main script of this project is `top_songs.py`. The script processes the log files and generates two output files: `top50_songs_per_country.txt` and `top50_songs_per_user.txt`.

The structure of the project files is as follows:
```
/
│
└───top_songs.py
└───top50_songs_per_country.txt (Generated after execution)
└───top50_songs_per_user.txt (Generated after execution)
```

## How to Run

To run this script, you need to have Python 3 installed on your system. 

1. Clone the repository or download the project files.
2. Update the `ROOT_PATH` variable in `top_songs.py` to point to your directory containing the daily log files.
3. Open the terminal/command prompt.
4. Navigate to the directory containing `top_songs.py`.
5. Run the following command:
    ```sh
    python top_songs.py
    ```
6. The script will process all ".log" files in the `ROOT_PATH` directory, and generate two output files: `top50_songs_per_country.txt` and `top50_songs_per_user.txt`.

## Output

The output of the script are two text files:

1. `top50_songs_per_country.txt`: Each row in this file represents the top 50 songs listened in a specific country, in the following format:
`country|sng_id1:n1,sng_id2:n2,sng_id3:n3,...,sng_id50:n50`
    * `country` is the country ISO code (2 characters long)
    * `sng_id1:n1` the identifier of the song the most listened to with the related number of streams, and so on for the 50 top songs.

2. `top50_songs_per_user.txt`: Each row in this file represents the top 50 songs listened to by a specific user, in the same format as the per country file.


##How to Run the Code Automatically Daily at a certain time so that it can be production ready (here I took 2am as an example):

For Windows:

    Task Scheduler
        To schedule a Python script to run at prescribed times, you use the Task Scheduler GUI that comes with Windows. Follow the steps below to set up the task.
        -Open Task Scheduler. You can find it by searching for 'Task Scheduler' in the start menu.
        -Click on 'Create Basic Task'.
        -Enter a name and a description for the task and click 'Next'.
        -Choose the trigger frequency ( daily in our case) and click 'Next'.
        -Set the start time and date, and click 'Next'. (00:30 daily)
        -In the 'Action' field, select 'Start a program' and click 'Next'.
        -In the 'Program/script' field, enter the path to the Python executable. his will be something like "C:\Python311\python.exe", but it will depend on where Python is installed on your system.
        -In the 'Add arguments' field, enter the name of your Python script with .py extension. ("C:\Users\HMala\OneDrive\Desktop\CaseStudy-Malak HOUSSAINI\main.py")
        -In the 'Start in' field, enter the path to the directory where your Python script is located. ("C:\Users\HMala\OneDrive\Desktop\CaseStudy-Malak HOUSSAINI")
        -Click 'Next', then 'Finish'.
        Your task is now set up and your script will run at the time(s) you specified.

A couple of things to remember:

    Make sure your script has the right permissions to run (i.e., it's executable).
    Always use absolute paths in your crontab file or Task Scheduler, not relative paths.
    Make sure Python is correctly installed and that your script runs without issues.
    You need to provide the correct path to the Python interpreter and the script in the Task Scheduler.

Linux: 

    Cron Jobs
     Here is a step-by-step guide for scheduling your Python script with `cron`.

    First, make sure your Python script has the correct permissions to be executable. You can do this by navigating to the script's directory and running `chmod +x script.py`.

    Here's the guide:

    1. Open Terminal.

    2. To open the crontab configuration file, enter the following command:

    ```bash
    crontab -e
    ```

    3. This will open the crontab file in your default text editor. If this is your first time running the `crontab -e` command, you may be asked to select a text editor (such as nano, vim, etc.).

    4. In the editor, enter a new line at the end of the file following this format:

    ```bash
    * * * * * /usr/bin/python3 /path/to/your/script.py
    ```

    The five asterisks at the beginning of the line represent different date parts in the following order: 

    - Minute (from 0 to 59)
    - Hour (from 0 to 23)
    - Day of month (from 1 to 31)
    - Month (from 1 to 12)
    - Day of week (from 0 to 7) (0 or 7 is Sunday, or use names)

    A `*` in a field is used to indicate "every". For example, if you wanted your script to run every day at 00:30 (12:30 AM), you would configure the line like this:

    ```bash
    30 0 * * * /usr/bin/python3 /path/to/your/script.py

    ```
    5. Once you've entered the line, save and close the file. If you're using nano, you can do this by pressing `Ctrl+X` to exit, then `Y` to confirm that you want to save changes, and then `Enter` to confirm the file name.

    6. Your crontab has now been updated, and the scheduled task should run at your specified intervals.

    Remember to replace `/usr/bin/python3` and `/path/to/your/script.py` with the paths to your Python interpreter and your Python script respectively. You can find the path to your Python interpreter by running `which python3` in the terminal.


## Additional Information

- The script is designed to ignore corrupted rows in the input data. It will print a message and continue to the next file if a file cannot be opened.
- It is designed to use a limited amount of RAM (less than 1 GB), writing intermediate information to the disk as necessary.

## Limitations

Currently, the script needs to be run manually every day. For automatic daily execution, you could schedule the script using a task scheduler that is appropriate for your operating system (such as cron jobs on Linux).

## Support

If you have any questions or face any issues while running the script, please raise an issue in this repository.

## Contributions

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.








```
