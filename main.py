# Import required libraries
from multiprocessing import Pool  # This is used for parallel processing.
import collections  # This is used for convenient and efficient data structures.
import os  # This is used for interacting with the operating system, e.g., listing files.
from datetime import datetime

# Define constant values. These are global configurations for your script.
ROOT_PATH = r"C:\Users\HMala\OneDrive\Desktop\CaseStudy-Malak HOUSSAINI"  # The directory where your data resides, needs to change on each pc
SEPARATOR = "|"  # The character used to separate fields in your data.

# This function is responsible for processing an individual log file.
def process_log_file(file_path):
    data = collections.defaultdict(collections.Counter)  # This will hold the count of song plays for each country and user.
    try:
        # Open the file in read mode.
        with open(file_path, "r") as f:
            # Read the file line by line.
            for line in f:
                try:
                    # Split the line into song ID, user ID, and country.
                    sng_id, user_id, country = line.strip().split(SEPARATOR)
                    # Update the counters for the song ID for the corresponding country and user.
                    data[country][sng_id] += 1
                    data[user_id][sng_id] += 1
                except ValueError:  # This catches errors when a line does not have exactly three fields.
                    pass  # Ignore corrupted rows.
    except IOError:  # This catches errors when the file cannot be opened.
        # If the file can't be opened, print a message and continue to the next file.
        print(f"Failed to process {file_path}. Moving on to the next file...")
    return data  # Return the count data.

# This function is responsible for processing all log files in parallel.
def process_all_log_files(log_files):
    # Create a pool of worker processes.
    with Pool(processes=os.cpu_count()) as pool:
        # Process each log file in the pool. The map function applies the process_log_file function to each file.
        data_dicts = pool.map(process_log_file, log_files)
        
    # Combine the results from all processes.
    data = collections.defaultdict(collections.Counter)
    for d in data_dicts:
        for key, counter in d.items():
            data[key] += counter
            
    return data  # Return the combined count data.

# This function writes the top 50 songs for each key (country or user) to a file.
def write_top_50(data, filename):
    # Open a file to write the top 50 songs.
    with open(filename, "w") as f:
        for key, value in data.items():
            # Get the top 50 songs for this key.
            top_50 = value.most_common(50)
            # Write the top 50 songs to the file.
            f.write(f"{key}{SEPARATOR}{','.join([f'{k}:{v}' for k, v in top_50])}\n")


def get_subdirectories():
    subdirectories = []
    for dir in os.listdir(ROOT_PATH):
        dir_path = os.path.join(ROOT_PATH, dir)
        if os.path.isdir(dir_path):  # Check if it's a directory
            try:
                date_str = "-".join(dir.split('-')[1:4]).split('_')[0]  # Assume subdirectories are in 'sample_listen-YYYY-MM-DD_2Mlines' format.
                date = datetime.strptime(date_str, '%Y-%m-%d')  # Parse date from string.
                subdirectories.append((date, dir_path))
            except Exception as e:
                print(f"Failed to parse date from {dir}. Error: {e}")
                continue
    return subdirectories

def process_log_files():
    # Get all subdirectories in ROOT_PATH that match the date format in their names.
    dated_dirs = get_subdirectories()

    dated_dirs.sort(reverse=True)  # Sort in descending order so the latest dates come first.

    # Take only the last 7 directories.
    log_dirs = [dir for date, dir in dated_dirs[:7]]
    
    # Get all log files from selected directories.
    log_files = []
    for dir in log_dirs:
        log_files.extend([os.path.join(dir, f) for f in os.listdir(dir) if ".log" in f])

    # Process selected log files and get the count data.
    data = process_all_log_files(log_files)

    # Get the date from the last file
    last_file_date = dated_dirs[0][0].strftime("%Y-%m-%d")
    
    # Write top 50 songs for each country.
    country_file_name = f"country_top50_{last_file_date}.txt"
    write_top_50({k: v for k, v in data.items() if len(k) == 2}, country_file_name)
    
    # Write top 50 songs for each user.
    user_file_name = f"user_top50_{last_file_date}.txt"
    write_top_50({k: v for k, v in data.items() if len(k) > 2}, user_file_name)

# This is the entry point for your script.
if __name__ == "__main__":
    # Call the function to process the log files.
    process_log_files()


