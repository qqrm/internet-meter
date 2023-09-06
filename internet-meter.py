import speedtest
import os
from datetime import datetime


def human_readable_size(nbytes: float) -> str:
    """Convert bytes to human-readable units."""
    suffixes = ["B", "KB", "MB", "GB", "TB", "PB"]
    i = 0
    while nbytes >= 1024 and i < len(suffixes) - 1:
        nbytes /= 1024.0
        i += 1
    size = f"{nbytes:.2f}".rstrip("0").rstrip(".")
    return f"{size} {suffixes[i]}"


def get_current_datetime() -> str:
    """Get the current date and time as a formatted string."""
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")


def main():
    """Main function to perform speed tests and log the results."""
    # Initialize Speedtest API
    speed_test = speedtest.Speedtest()

    # Generate a unique log file name based on the current date and time
    current_datetime_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file_name = f"speed_log_{current_datetime_str}.txt"

    # Check and remove existing log file if it exists
    if os.path.exists(log_file_name):
        os.remove(log_file_name)

    # Open a new log file for writing using 'with' for automatic file management
    with open(log_file_name, "w") as log_file:
        while True:
            # Perform download and upload speed tests
            download_speed = speed_test.download()
            upload_speed = speed_test.upload()

            # Convert speeds to human-readable format
            download_str = human_readable_size(download_speed)
            upload_str = human_readable_size(upload_speed)

            # Generate and print the log entry
            log_entry = f"[{get_current_datetime()}] {download_str} / {upload_str}"
            print(log_entry)

            # Write the log entry to the file and flush the buffer
            log_file.write(f"{log_entry}\n")
            log_file.flush()


if __name__ == "__main__":
    main()
