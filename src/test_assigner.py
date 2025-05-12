# test_assigner.py
# ---------------------------------------------------------
# This module assigns each test data point to one of the best-matched
# ideal functions using a thresholding rule.
# A point is accepted only if its deviation from the ideal value is within
# (max_delta × √2), where max_delta is the max deviation from training to ideal.
# ---------------------------------------------------------

import pandas as pd   # For DataFrame handling (tables of tabular data)
import numpy as np    # For efficient numeric computation (sqrt, abs, etc.)

def assign_test_points(test_df, ideal_df, training_df, best_match_dict):
    """
    Assign each test data point to a matched ideal function,
    based on a thresholded deviation rule.

    Parameters:
    ----------
    test_df : pd.DataFrame
        Test dataset with x and y values (e.g., from sensors or measurement).

    ideal_df : pd.DataFrame
        Ideal function dataset (columns: 'x', 'y1', ..., 'y50').

    training_df : pd.DataFrame
        Contains 'y1' to 'y4' training functions used to calculate deviation thresholds.

    best_match_dict : dict
        Mapping of training functions to their best-fit ideal functions.
        Example: {'y1': 'y14', 'y2': 'y8', ...}

    Returns:
    -------
    pd.DataFrame
        A filtered DataFrame with only matched points:
        Columns: ['x', 'y', 'delta_y', 'ideal_function']
    """

    results = []  # Initialize an empty list to store matching results

    # Automatically detect the y-column name (should be second column after 'x')
    y_column = [col for col in test_df.columns if col != 'x'][0]

    # Iterate through every test point (row-by-row in test_df)
    for idx, test_row in test_df.iterrows():
        x_test = test_row['x']         # Extract the x value
        y_test = test_row[y_column]    # Extract the measured y value (not necessarily named 'y')

        best_fit = None                    # Will hold the best match for this point
        smallest_deviation = float('inf') # Start with a very high deviation

        # Go through all training-to-ideal mappings
        for train_col, ideal_col in best_match_dict.items():

            # Calculate maximum allowed deviation between this training function and ideal function
            delta = np.max(np.abs(training_df[train_col] - ideal_df[ideal_col]))

            try:
                # Find the y_ideal value at the test x coordinate
                y_ideal = ideal_df.loc[ideal_df['x'] == x_test, ideal_col].values[0]
            except IndexError:
                # If no matching x value in ideal_df, skip this pair
                continue

            # Compute how far the test point's y is from the ideal
            delta_y = np.abs(y_test - y_ideal)

            # Accept only if deviation is within allowed limit (√2 * delta)
            if delta_y <= np.sqrt(2) * delta:
                # Keep the best match with the smallest deviation
                if delta_y < smallest_deviation:
                    smallest_deviation = delta_y
                    best_fit = {
                        'x': x_test,
                        'y': y_test,
                        'delta_y': delta_y,
                        'ideal_function': ideal_col
                    }

        # Save match if one was found
        if best_fit:
            results.append(best_fit)

    # Convert list of dictionaries to a DataFrame
    matched_df = pd.DataFrame(results)

    # Ensure all rows have a valid match
    matched_df = matched_df[matched_df['ideal_function'].notnull()]

    return matched_df
