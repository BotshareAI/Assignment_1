# main.py
# Entry point for the Ideal Function Assignment project.
# Executes all major steps: data loading, LSQ matching, test assignment, and database storage.

from data_loader import load_all_data            # Module to load CSV datasets
from function_matcher import find_best_ideal_matches  # Finds best-fit ideal functions for training
from test_assigner import assign_test_points     # Assign test data to matched ideal functions
from db_writer import write_to_database          # Writes the assigned results into SQLite

# 1. Load all required CSV data files (training, ideal, test)
training_df, ideal_df, test_df = load_all_data(
    "data/training_data.csv",
    "data/ideal_functions.csv",
    "data/test_data.csv"
)

# Safety check: if any file failed to load, exit the program gracefully
if None in (training_df, ideal_df, test_df):
    print("Error loading one or more datasets. Exiting.")
    exit(1)

# 2. Match each training function (y1–y4) to the best ideal function using least squares
# Returns: dict with keys like 'y1', values like 'y12' (ideal function name)
matched_functions = find_best_ideal_matches(training_df, ideal_df)

# 3. Use test data and find closest matching ideal function (from matched list)
# Only assign if deviation is within 1.1 * max deviation from training
assigned_df = assign_test_points(test_df, ideal_df, matched_functions)

# 4. Persist the assigned matches (x, y, delta_y, ideal_function) to SQLite database
write_to_database(assigned_df, db_path="db/ideal_function.db")

# 5. (Optional) You can call a visualization here (if implemented)
# from visualizer import plot_matches
# plot_matches(training_df, ideal_df, matched_functions)

# Final confirmation
print("Project execution complete. Matched data saved to SQLite.")
