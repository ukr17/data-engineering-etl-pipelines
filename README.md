# Data Engineering ETL Pipelines

This repository showcases automated ETL (Extract, Transform, Load) pipelines designed to process, clean, and analyze datasets. It includes Python-based data manipulation, SQL Server database integration, and automated logging for process monitoring.

## Projects Included

### 1. Global Market Capitalization ETL
*   **Description:** Automates the extraction of global bank market capitalization data and performs currency conversion across USD, GBP, EUR, and INR.
*   **Key Files:** `Largest_banks_data.csv` (contains processed market cap data).
*   **Database Structure:** Data is structured in SQL Server with the `Largest_banks` table containing columns for Name, MC_USD, MC_GBP, MC_EUR, and MC_INR.

### 2. Data Cleaning & Normalization
*   **Description:** Demonstrates standard data cleaning procedures using Pandas.
*   **Key Files:** `messy.csv` (raw data before cleaning).
*   **Process:** Handles missing values and standardizes data formats for production-ready analysis.

## Pipeline Logging
The ETL processes are fully logged, tracking the lifecycle from data extraction through to final database loading. 

**Example Log Extract:**
- `Data extraction started` -> `Data transformation complete` -> `SQL Connection initiated` -> `ETL Job Ended`

## Technical Stack
*   **Language:** Python (Pandas, NumPy, BeautifulSoup).
*   **Database:** SQL Server.
*   **Task:** Data Transformation, Cleaning, and Automated ETL Logging.

## How to use
1.  **Environment:** Ensure you have Python installed with the `pandas` and `numpy` libraries.
2.  **Database:** Set up a SQL Server instance to handle the table schema defined in `Largest_banks`.
3.  **Execution:** Run the ETL scripts to generate the output files and load them into your SQL database.
