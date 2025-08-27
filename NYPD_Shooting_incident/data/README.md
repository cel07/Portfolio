# Data Directory — NYPD Shooting Incident Analysis

This folder contains the source data used in the **NYPD Shooting Incident Data Analysis (2020–2024)** project. All files are publicly available through [NYC Open Data](https://data.cityofnewyork.us/Public-Safety/NYPD-Shooting-Incident-Data-Historic-/833y-fsy8).

## Files Included

- **`NYPD_Shooting_Incident_Data__Historic_.csv`**  
  The main dataset of shooting incidents reported by the NYPD.  
  - Each row represents a single shooting incident.  
  - Key fields include:  
    - `OCCUR_DATE`, `OCCUR_TIME`: Date and time of the incident  
    - `BORO`, `PRECINCT`: Location details  
    - `PERP_AGE_GROUP`, `PERP_SEX`, `PERP_RACE`: Perpetrator demographics  
    - `VIC_AGE_GROUP`, `VIC_SEX`, `VIC_RACE`: Victim demographics  
    - `STATISTICAL_MURDER_FLAG`: Whether the incident resulted in a death  
    - `X_COORD_CD`, `Y_COORD_CD`, `Latitude`, `Longitude`: Geographic coordinates  

- **`NYPD_Shootings_Historic_DataDictionary.xlsx`**  
  The official data dictionary explaining each field in the dataset. This file provides column descriptions, value definitions, and metadata to assist with interpreting the data.

## Notes on Data Use
- The dataset covers all reported NYPD shooting incidents since 2006.  
- For this project, the analysis focuses on the **years 2020–2024**.  
- Basic cleaning and preprocessing were performed in the analysis code (e.g., handling missing values, correcting data types, standardizing categories).  
- These raw files are kept unchanged to preserve the original source.

---

📊 For the full analysis report, see:  
👉 [NYPD Shooting History Data Analysis](https://clegarda.quarto.pub/nypd-shooting-history-data-analysis/)  

