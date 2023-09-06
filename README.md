# Internet Meter

## Overview
The `internet-meter` repository contains a Python script (`speedtest_logger.py`) for monitoring internet speed. It performs speed tests at regular intervals and logs the results. The script uses Ookla's Speedtest CLI to gauge download and upload speeds and saves them along with the current timestamp to a uniquely named log file.

## Requirements

- Python 3.x
- Speedtest CLI by Ookla

## Installation Steps

### Clone the Repository

First, clone the `internet-meter` repository.

```bash
git clone https://github.com/qqrm/internet-meter.git
```

### Install Required Packages

After cloning the repo, navigate to the directory containing the script. Install the required Python packages using the following command:

```bash
pip install -r requirements.txt
```

This assumes that you have a `requirements.txt` file in the repository listing `speedtest-cli`. If not, you can manually install the required package using:

```bash
pip install speedtest-cli
```

## Usage

Navigate to the directory containing `speedtest_logger.py` and execute the script:

```bash
python speedtest_logger.py
```

This will begin the speed tests, logging each result to a new file in the same directory. Each log file is named `speed_log_YYYYMMDD_HHMMSS.txt`, where `YYYYMMDD` is the current date and `HHMMSS` is the current time.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.