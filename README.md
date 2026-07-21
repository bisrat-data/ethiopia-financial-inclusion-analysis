# Ethiopia Financial Inclusion Analysis

## Project Overview

This project analyzes Ethiopia's Financial Inclusion dataset to understand trends in financial access, usage, and inclusion.

The project focuses on:

- Data exploration
- Data enrichment
- Exploratory Data Analysis (EDA)
- Financial inclusion insights
- Preparation for forecasting and impact modeling

---

## Dataset Description

The dataset follows a unified schema and contains four main record types:

### Observation
Measured values for financial inclusion indicators.

### Event
Policy, market, or technology events that may affect financial inclusion outcomes.

### Target
Desired future values for financial inclusion indicators.

### Impact Link
Relationships connecting events to indicators and estimating expected impacts.

---

## Project Structure

```
ethiopia-financial-inclusion-analysis/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── 01_data_exploration.ipynb
│
├── reports/
│   └── interim_report.md
│
├── src/
│
├── data_enrichment_log.md
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Installation

Create and activate the virtual environment:

```bash
python -m venv .venv-1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Notebook

Open:

```
notebooks/01_data_exploration.ipynb
```

and run all cells.

---

## Data Sources

- Ethiopia Financial Inclusion Dataset
- Reference Codes Dataset
- Supplementary financial inclusion references used during enrichment

---

## Key Findings

- Account ownership increased significantly over time.
- Growth slowed between 2021 and 2024.
- Digital financial services are important drivers of inclusion.
- Data quality varies across indicators.
- Several indicators have limited temporal coverage.

---

## Author

Netsanet Gebrekidan