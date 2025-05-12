# Function to find the best ideal function (from ideal_df) for each training function (in training_df)
# using the Least Squares method.
def find_best_ideal_matches(training_df, ideal_df):
    # Dictionary to store the best matching ideal function for each training function
    # Format: {'y1': 'y12', 'y2': 'y7', ...}
    best_fit_mapping = {}

    # Loop over each column (function) in the training dataset
    for train_col in training_df.columns:
        # Skip the 'x' column, we only want to compare function values (y1, y2, etc.)
        if train_col == "x":
            continue

        # Initialize the minimum least squares error with a very large number
        min_error = float("inf")

        # Variable to store the best-matching ideal function name for this training function
        best_ideal_col = None

        # Now compare current training function to all ideal functions
        for ideal_col in ideal_df.columns:
            # Again, skip the 'x' column, we only care about y-values
            if ideal_col == "x":
                continue

            # Calculate the least squares error between training and ideal function
            # Both columns must correspond to the same x values
            lsq_error = calculate_lsq(training_df[train_col], ideal_df[ideal_col])

            # If this ideal function has a smaller error, it's a better match
            if lsq_error < min_error:
                min_error = lsq_error             # Update minimum error found so far
                best_ideal_col = ideal_col        # Update the best matching ideal function name

        # Once all ideal functions have been checked for this training function,
        # store the best match in the dictionary
        best_fit_mapping[train_col] = best_ideal_col

    # After all training functions are processed, return the final mapping dictionary
    return best_fit_mapping
