# main.py
# Entry point for the Ideal Function Assignment project.
# Executes all major steps: data loading, LSQ matching, test assignment, and database storage.

import sys  # Required to exit the program on error

from data_loader import load_all_data                  # Module to load CSV datasets
from function_matcher import find_best_ideal_matches   # Finds best-fit ideal functions for training
from test_assigner import assign_test_points           # Assigns test data to matched ideal functions
from db_writer import write_to_database                # Writes the assigned results into SQLite


# -----------------------------------------------
# Step 1: Load all required CSV data files
# - training_data.csv: Contains x, y1–y4 (training set)
# - ideal_functions.csv: Contains x, y1–y50 (perfect functions)
# - test_data.csv: Contains x, y (unlabeled values to match)
# -----------------------------------------------
training_df, ideal_df, test_df = load_all_data(
    "data/training_data.csv",
    "data/ideal_functions.csv",
    "data/test_data.csv"
)

# -----------------------------------------------
# Step 2: Check if any file failed to load
# - If any DataFrame is None, exit gracefully
# -----------------------------------------------
if any(df is None for df in (training_df, ideal_df, test_df)):
    print("[ERROR] One or more datasets failed to load. Exiting.")
    sys.exit(1)  # Exit the program with error code 1


# -----------------------------------------------
# Step 3: Match training functions to ideal functions
# - For each training function y1–y4, find the best-fit ideal function (y1–y50)
# - Uses Least Squares Error (LSE) to evaluate similarity
# - Returns a dictionary like: {'y1': 'y13', 'y2': 'y27', ...}
# -----------------------------------------------
matched_functions = find_best_ideal_matches(training_df, ideal_df)


# -----------------------------------------------
# Step 4: Assign test points to the best-fit ideal functions
# - For each (x, y) in test set, compare against y_ideal(x)
# - Accept match if deviation <= max_delta × √2 (per assignment rules)
# - Returns a new DataFrame with matched test points
# -----------------------------------------------
assigned_df = assign_test_points(test_df, ideal_df, training_df, matched_functions)


# -----------------------------------------------
# Step 5: Save results to SQLite database
# - Stores assigned x, y, delta_y, and ideal_function
# - Creates table if it doesn't exist
# -----------------------------------------------
write_to_database(assigned_df, db_path="db/ideal_function.db")


# -----------------------------------------------
# Step 6: Optional visualization step (if implemented)
# -----------------------------------------------
# from visualizer import plot_matches
# plot_matches(training_df, ideal_df, matched_functions)


# Final confirmation
print("[INFO] Project execution complete. Matched test data saved to database.")
