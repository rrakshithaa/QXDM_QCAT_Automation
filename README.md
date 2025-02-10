# QXDM Logs Automation - HDF to PCAP Conversion using QCat

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Code Workflow](#code-workflow)
- [Logging](#logging)
- [Error Handling](#error-handling)
- [License](#license)

## Introduction

This Python project automates the process of converting Qualcomm eXtensible Diagnostic Monitor (QXDM) logs from `.hdf` format to `.pcap` format using the QCat application. It includes functionalities for handling QCat GUI operations, reading `.hdf` files, and moving the converted `.pcap` files to a separate destination folder.

## Project Structure

```
QXDM_Automation
├── qxdm_qcat.py            # Main automation script
├── Qxdm_operations
│   ├── hdf_operation.py     # Handles reading of HDF files
│   └── keyboard_functions.py # Automates keyboard interactions
└── utils
    └── logger.py            # Custom logging module
```

## Prerequisites

Ensure the following software and packages are installed:

1. **Python 3.13.0 or higher**
2. **QCat Application (Installed on your system)**
3. **Required Python Packages:**

```bash
pip install AppOpener keyboard
```

## Installation

1. Clone this repository to your local system:

   ```bash
   git clone https://github.com/rrakshithaa/QXDM_QCAT_Automation.git
   cd QXDM_Automation
   ```

2. Install the required dependencies as mentioned above.

3. Ensure that the paths in `hdf_operation.py` and `qxdm_qcat.py` are updated to match your file locations.

## Usage

### Step 1: Prepare Input Files

Place your `.hdf` logs in the folder `C:\Users\Downloads\QXDM_Logs\qxdm_file`.

### Step 2: Execute the Script

Run the main Python script:

```bash
python qxdm_qcat.py
```

### Step 3: Output

The converted `.pcap` files containing `TheadX_IP` will be moved to the folder `C:\Users\Downloads\QXDM_Logs\output_threadx`.

## Code Workflow

### 1. **Initialization**

- The `Qxdm_operations` class initializes objects for reading `.hdf` files and handling keyboard events.

### 2. **Opening QCat and Loading Logs**

- Opens QCat using `AppOpener` and maximizes the window.
- Navigates the GUI to open the specified `.hdf` log file.

### 3. **Handling Popups and Alerts**

- Closes any unexpected popups using keyboard shortcuts.

### 4. **Conversion to PCAP**

- Selects the option to convert logs to `.pcap` files.

### 5. **File Processing**

- Moves `.pcap` files containing `TheadX_IP` to the output directory.

## Logging

Logs for the execution process are recorded using a custom logger located in `utils/logger.py`. Key events and errors are logged for easy debugging.

## Error Handling

- **File Errors:** Captured and logged when files are not found or cannot be moved.
- **QCat Application Errors:** Exceptions are caught and logged during QCat operations.

## License

This project is free to use for educational, research, and personal learning purposes. Any commercial usage, redistribution, or modification without prior permission is prohibited.

