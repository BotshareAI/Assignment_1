# data_loader.py
# This module is responsible for reading and loading the training, ideal, and test datasets from CSV files.
# It uses the pandas library to convert CSV content into DataFrame objects for easy data handling.

import pandas as pd  # Import the pandas library, a powerful tool for data manipulation and analysis

# -------------------------
# Function: load_csv
# -------------------------
# Purpose: Reads a single CSV file and returns it as a pandas DataFrame.
# This is a reusable helper function for all types of datasets: training, test, and ideal.

def load_csv(file_path):
    """
    Loads a CSV file and returns it as a pandas DataFrame.
    
    Parameters:
    - file_path (str): The path to the CSV file (can be relative or absolute).
    
    Returns:
    - pd.DataFrame: The loaded dataset in table format.
    - None: If any error occurs (e.g., file not found or invalid format).
    """
    try:
        # Use pandas to read the CSV file located at file_path
        df = pd.read_csv(file_path)

        # Print a confirmation message showing the file loaded and its dimensions (rows x columns)
        print(f"[INFO] Loaded data from {file_path} with shape {df.shape}")

        # Return the loaded DataFrame to the caller
        return df

    except Exception as e:
        # If there's an error (e.g., missing file, permission error), print an error message
        print(f"[ERROR] Failed to load file: {file_path}. Reason: {e}")

        # Return None so the calling code knows the load failed
        return None


# -------------------------
# Function: load_all_data
# -------------------------
# Purpose: Loads all three required datasets for the project: training, ideal, and test datasets.
# This function calls load_csv() three times with the appropriate file paths.

def load_all_data(training_path, ideal_path, test_path):
    """
    Loads the required datasets: training data, ideal functions, and test data.

    Parameters:
    - training_path (str): Path to the training_data.csv file.
    - ideal_path (str): Path to the ideal_functions.csv file.
    - test_path (str): Path to the test_data.csv file.

    Returns:
    - Tuple (pd.DataFrame, pd.DataFrame, pd.DataFrame):
      (training_df, ideal_df, test_df)
    """
    # Load the training dataset
    training_df = load_csv(training_path)

    # Load the ideal functions dataset
    ideal_df = load_csv(ideal_path)

    # Load the test dataset
    test_df = load_csv(test_path)

    # Return all three datasets as a tuple
    return training_df, ideal_df, test_df
