# function_matcher.py
# This module finds the best matching ideal functions for each training function
# using the Least Squares Error (LSE) method.

import numpy as np  # NumPy is used for efficient numerical calculations

def calculate_lsq(y_train, y_ideal):
    """
    Calculates the Least Squares Error (LSE) between two series of y-values.
    
    Parameters:
    - y_train (pd.Series): The training function's y-values
    - y_ideal (pd.Series): The ideal function's y-values

    Returns:
    - float: The total squared error (a measure of how well the ideal matches the training)
    """
    # Compute the sum of squared differences between each corresponding y-value
    return np.sum((y_train - y_ideal) ** 2)

# Function to find the best ideal function (from ideal_df) for each training function (in training_df)
def find_best_ideal_matches(training_df, ideal_df):
    """
    Finds the best-matching ideal function for each training function using LSE.

    Parameters:
    - training_df (pd.DataFrame): DataFrame with training functions (y1–y4)
    - ideal_df (pd.DataFrame): DataFrame with 50 ideal functions (y1–y50)

    Returns:
    - dict: Mapping like {'y1': 'y13', 'y2': 'y27', ...} showing the best-matching ideal for each training function
    """
    # Create a dictionary to store the best match for each training function
    best_fit_mapping = {}

    # Loop through each column in the training dataset
    for train_col in training_df.columns:
        # Skip the 'x' column because we are only interested in matching y-values
        if train_col == "x":
            continue

        # Set a high initial value for the minimum LSE
        min_error = float("inf")
        best_ideal_col = None  # Variable to track the best-matching ideal function

        # Compare the current training function to each ideal function
        for ideal_col in ideal_df.columns:
            if ideal_col == "x":
                continue  # Skip the 'x' column

            # Compute the least squares error between the training and ideal y-values
            lsq_error = calculate_lsq(training_df[train_col], ideal_df[ideal_col])

            # Update the best match if the current ideal function gives a lower error
            if lsq_error < min_error:
                min_error = lsq_error
                best_ideal_col = ideal_col

        # After checking all ideal functions, store the best match for this training function
        best_fit_mapping[train_col] = best_ideal_col

    # Return the final dictionary of best matches
    return best_fit_mapping
