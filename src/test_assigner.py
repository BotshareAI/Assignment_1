# test_assigner.py
# ---------------------------------------------------------
# This module assigns each test data point to the best-matching
# ideal function based on deviation thresholding.
# The deviation must be within (max delta × √2) for a valid match.
# Only matched points are returned in the final DataFrame.
# ---------------------------------------------------------

import pandas as pd   # For structured tabular data handling
import numpy as np    # For fast numerical operations


def assign_test_points(test_df, ideal_df, training_df, best_match_dict):
    """
    Assigns test points to ideal functions based on deviation from known ideal values.

    Parameters:
    - test_df: pd.DataFrame
        Test dataset with columns ['x', 'y']
    - ideal_df: pd.DataFrame
        Dataset of 50 ideal functions, columns ['x', 'y1' ... 'y50']
    - training_df: pd.DataFrame
        Training dataset used to determine deviation bounds
    - best_match_dict: dict
        Maps training columns (e.g., 'y1') to best-fit ideal function columns (e.g., 'y17')

    Returns:
    - pd.DataFrame with matched test points only, including:
        ['x', 'y', 'delta_y', 'ideal_function']
    """

    results = []  # This will store all matched test point data

    # Iterate over each test point
    for idx, test_row in test_df.iterrows():
        x_test = test_row['x']   # x-coordinate of the test point
        y_test = test_row['y']   # observed y-value at x

        best_fit = None          # Placeholder for best match
        smallest_deviation = float('inf')  # Start with very high deviation

        # Try matching against each selected ideal function (via training mapping)
        for train_col, ideal_col in best_match_dict.items():
            # Calculate max delta between training and ideal function
            delta = np.max(np.abs(training_df[train_col] - ideal_df[ideal_col]))

            # Get y value of the ideal function at x_test
            try:
                y_ideal = ideal_df.loc[ideal_df['x'] == x_test, ideal_col].values[0]
            except IndexError:
                # x value not found in ideal_df; skip this row
                continue

            # Calculate deviation from the ideal function
            delta_y = np.abs(y_test - y_ideal)

            # Accept if deviation is within allowed threshold
            if delta_y <= np.sqrt(2) * delta:
                if delta_y < smallest_deviation:
                    smallest_deviation = delta_y
                    best_fit = {
                        'x': x_test,
                        'y': y_test,                  # use 'y' for consistency with DB schema
                        'delta_y': delta_y,
                        'ideal_function': ideal_col   # renamed to match DB schema
                    }

        # Store only if a valid match was found
        if best_fit:
            results.append(best_fit)

    # Create a DataFrame of only matched test points
    matched_df = pd.DataFrame(results)

    # Remove rows with no matched function (just for safety/clean output)
    matched_df = matched_df[matched_df["ideal_function"].notnull()]

    return matched_df  # Ready for DB insertion or visualization
