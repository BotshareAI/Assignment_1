# Project Requirements: Ideal Function Matching System

## 🧱 Technologies to Use

- **Python 3.8+**
- **SQLite** for storing matches and test evaluations
- **Pandas** for data manipulation
- **NumPy** for numerical operations and error computation
- **Bokeh** for visualization
- **Unittest** for simple module testing

---

## 📁 Folder and File Structure

IdealFunction/
│
├── data/ # CSV files provided
│ ├── training_data.csv
│ ├── ideal_functions.csv
│ └── test_data.csv
│
├── src/ # Python modules
│ ├── main.py # Script to execute all steps
│ ├── data_loader.py # Functions to load CSV and DB
│ ├── function_matcher.py # Matching and evaluation logic
│ ├── test_matcher.py # Test file with unit tests
│ └── visualizer.py # Plotting using Bokeh
│
├── db/
│ └── ideal_function.db # Generated database
│
├── README.md # Project overview and task
└── requirements.md # Requirements and expectations

---

## ✅ Functional Requirements

- Load 4 training functions, 50 ideal functions, and 1 test dataset.
- Match each training function to its best-fitting ideal function.
- Identify which test points can be explained by the chosen ideal functions.
- Store matches in a structured SQLite database.
- Create readable, labeled plots of all data and mappings.

---

## 📚 OOP Concepts to Apply

- **Abstraction:** Use well-defined modules (`data_loader.py`, `function_matcher.py`, etc.)
- **Encapsulation:** Each module should manage its own logic (data loading, matching, etc.)
- **Inheritance:** If creating subclasses for data sources or visualization extensions
- **Polymorphism:** Potential use in visualization or data processing interfaces

---

## ⚙️ Installation Instructions

To install required packages in GitHub Codespaces or locally:

```bash
pip install pandas numpy bokeh