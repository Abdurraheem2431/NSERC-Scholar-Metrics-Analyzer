# NSERC Scholar Metrics Analyzer

A Python data analysis project that evaluates the relationship between NSERC Discovery Grant (Computer Science) recipients and academic impact using Google Scholar publication/citation metrics, then publishes results as charts and a static website.

## Live website
https://www.cs.torontomu.ca/tneves/website/Cito.html

## Features
- Parses NSERC awards data from Excel to extract Discovery Grants Program winners (name + fiscal year).
- Uses Google Scholar (via the `scholarly` library) to compute per-award-year:
  - Publication count
  - Total citations
- Generates visualizations:
  - Publications per researcher (bar chart + average baseline)
  - Citations per researcher (bar chart + average baseline)
  - Citations vs publications (scatter plot + trendline + Pearson correlation; r ≈ 0.59)

## Tech stack
Python, Pandas, OpenPyXL, Matplotlib, scholarly, HTML/CSS

## How to run
```bash
cd Code
pip install -r requirements.txt
python scripts/getNames.py
python scripts/charts.py
