# PHBS QPS 2024 HW1 - US Inflation Analysis Using CPI Data
## Repository Information

**GitHub Repository URL**:  
[https://github.com/jgz1433223/phbs-qps-2024](https://github.com/jgz1433223/phbs-qps-2024)

---
## How to Set Up and Run the Code

### Prerequisites
1. **GitHub Desktop** ([Download](https://desktop.github.com/))
2. **Visual Studio Code (VS Code)** ([Download](https://code.visualstudio.com/))
3. **Python** (3.8 or later) ([Download](https://www.python.org/))
4. **pip** (Python package manager)

---

### Steps to Run

#### Step 1: Clone the Repository
1. Open **GitHub Desktop**.
2. Clone the repository using the URL:  
   `https://github.com/jgz1433223/phbs-qps-2024`
3. Open the cloned repository in **VS Code**.

#### Step 2: Set Up the Environment
1. Open a terminal in VS Code:
   - On **Windows**: `Ctrl+`` (backtick)
   - On **Mac**: `Cmd+`` (backtick)
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate  # macOS/Linux
#### Step 3: Run the Script
1. Locate **scripts/fetch_cpi.py** in VS Code.
2. Run the script:
   ```bash
   python scripts/fetch_cpi.py
## Expected Output

1. **Terminal**:
   - Last 4 quarters of US inflation will be displayed.

2. **Graph**:
   - A graph showing the Consumer Price Index (CPI) trend will be generated.

### Example terminal output:

```plaintext
Last 4 Quarters of US Inflation:
Quarter      CPI  Quarterly Inflation
2023Q1    301.74             1.05
2023Q2    304.00             0.75
2023Q3    307.28             1.08
2023Q4    308.74             0.47
   

