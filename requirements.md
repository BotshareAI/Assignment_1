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
├── data/
│   └── .gitkeep
│
├── src/
│   ├── main.py
│   ├── data_loader.py
│   ├── function_matcher.py
│   ├── test_matcher.py
│   └── visualizer.py
│
├── db/
│   └── .gitkeep
│
├── tests/
│   └── __init__.py
│
├── README.md
└── requirements.md

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