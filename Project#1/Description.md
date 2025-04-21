# Final Project: Analyzing the Impact of AI on Industries Across Countries

## Overview

In this project, you will analyze a dataset that examines the influence of artificial intelligence (AI) on various industries across different countries and years. The dataset includes information about AI adoption rates, AI-generated content volume, job loss and revenue increase due to AI, human-AI collaboration rates, the top AI tools used, regulation status, consumer trust in AI, and market share of AI companies.

Your goal is to extract actionable insights from this dataset through an end-to-end data analytics workflow that involves data ingestion, cleaning, manipulation, descriptive and advanced statistical analysis, visualization, and reporting. You will make real-world interpretations that could be used by policymakers, business leaders, or technology strategists.

---

## Project Objectives

- **Data Loading & Cleaning:**  
  Load the dataset using Pandas and ensure data quality by inspecting, cleaning, and appropriately formatting the data.

- **Descriptive Statistical Analysis:**  
  Use Pandas and NumPy to calculate detailed descriptive statistics, including measures of central tendency (mean, median), dispersion (variance, standard deviation, interquartile range), and distribution shape (skewness, kurtosis). Identify trends and outliers.

- **Data Grouping & Aggregation:**  
  Group the data by key fields such as Country, Industry, Regulation Status, and Year to analyze performance differences and trends.

- **Advanced Numerical Analysis:**  
  Use NumPy for vectorized computations, correlation analysis, and computing derived metrics (e.g., percentage change, growth rates).

- **Data Visualization:**  
  Create various plots with Seaborn to visualize distributions, compare categorical variables, explore relationships via heatmaps, and observe trends over time.

- **Interpretation & Reporting:**  
  Summarize your findings in a detailed report, explaining the descriptive analysis, correlations, and any anomalies. Provide actionable recommendations based on your analysis.

---

## Tasks

### Task 1: Data Loading and Inspection

1. **Import Libraries:**
   - Import necessary libraries:
     - `pandas` as `pd`
     - `numpy` as `np`
     - `seaborn` as `sns`
     - `matplotlib.pyplot` as `plt`
   
2. **Load the Dataset:**
   - Load the CSV file using Pandas:
     - Example:  
       `df = pd.read_csv("ai_impact_dataset.csv")`
   - Convert the raw CSV data into a DataFrame:  
       `df = pd.DataFrame(pd.read_csv("ai_impact_dataset.csv"))`
   
3. **Inspect the Data:**
   - Display the first 10 rows using `df.head(10)`.
   - Print the dataset’s dimensions: `df.shape`.
   - Print column names using `df.columns` and data types with `df.dtypes`.
   - Check for missing values using `df.isnull().sum()`.
   - Questions to Consider:
     - What is the size and structure of the dataset?
     - Which columns are critical for your analysis, and do they have any missing or inconsistent values?
     - Are the percentage fields and numeric indicators stored correctly (as float or numeric types)?

4. Advanced data Inspection:
   - Use `df.info()` to get a concise summary of the DataFrame.
   - Use `df.describe()` to generate descriptive statistics for all numerical columns.
   - Use `df.isnull().sum()` to count the number of missing values in each column.
   - Use `df['Column_Name'].value_counts()` to get the frequency distribution of a categorical column.
   - Use `df['Column_Name'].unique()` to get the unique values in a categorical column.
   - Use `df['Column_Name'].nunique()` to get the number of unique values in a categorical column.
   - Use `df['Column_Name'].value_counts(normalize=True)` to get the frequency distribution of a categorical column as percentages.
   - Use `df['Column_Name'].value_counts().sort_values()` to get the frequency distribution of a categorical column in ascending order.
   - Use `df['Column_Name'].value_counts().sort_values(ascending=False)` to get the frequency distribution of a categorical column in descending order.
   - Use `df['Column_Name'].value_counts().sort_index()` to get the frequency distribution of a categorical column in alphabetical order.

---

### Task 2: Data Cleaning and Preparation

1. **Data Type Conversion & Cleaning:**
   - Convert "Year" to a numeric or datetime format.
   - Ensure all percentage columns (e.g., `AI Adoption Rate (%)`, `Job Loss Due to AI (%)`) are stored as floats.
   - Standardize categorical fields such as `Regulation Status` and `Industry` (e.g., trim whitespace, uniform capitalization).
   - Document any corrections you apply.

2. **Handling Missing Data:**
   - Identify columns with missing values.
   - Decide whether to drop missing data or fill them using appropriate imputation methods (mean, median, or mode).
   - Record any assumptions made during imputation.

3. **Data Enrichment (Optional):**
   - Create derived columns if relevant (e.g., calculate total impact scores combining revenue increase and job loss, or a growth metric).
   - Questions to Consider:
     - How will missing values affect your descriptive statistics?
     - Are there any anomalies (extremely high or low values) that warrant further investigation?

4. **Additional Cleaning Tasks:**
   - Remove or correct any outliers or erroneous data entries.
   - Address any inconsistencies in data entry (e.g., inconsistent date formats, inconsistent spelling).
   - Questions to Consider:
     - How do outliers affect the distribution of your data?
     - Are there any data entry errors that could skew your analysis?

5. **Final Data Inspection:**
   - After cleaning, re-inspect the dataset to ensure it’s ready for analysis.
   - Check for any remaining missing values and outliers.

6. Add 2 more cleaning tasks and what questions would you ask? Answer them in the report.

---

### Task 3: Detailed Descriptive Statistical Analysis

1. **Overall Descriptive Statistics:**
   - Use `df.describe()` to compute summary statistics (mean, median, min, max, standard deviation) for numerical columns.
   - Calculate additional measures:
     - **Variance and Standard Deviation:** Understand the spread of each numerical feature.
     - **Interquartile Range (IQR):** To detect outliers.
     - **Skewness and Kurtosis:** To assess the symmetry and peakedness of distributions.
   - Questions to Consider:
     - What does the central tendency tell you about the typical AI adoption rate and revenue increase?
     - How dispersed are the values for job loss and content volume?
     - Are any distributions skewed or exhibit heavy tails?

2. **Correlation Analysis:**
   - Use `df.corr()` to compute the correlation matrix among numeric variables.
   - Apply NumPy functions if necessary to compute specific correlations.
   - Discuss any strong positive or negative correlations.
   - Questions to Consider:
     - How is AI adoption related to job losses or revenue increases?
     - Do higher AI-generated content volumes correlate with consumer trust?
     - What insights do the correlations provide for policymaking?

3. **Group-wise Analysis:**
   - **By Country and Industry:**  
     Group data by `Country` and `Industry` to compare AI metrics among different regions and sectors.
     - Example:  
       `grouped_stats = df.groupby(['Country', 'Industry']).agg({'AI Adoption Rate (%)': 'mean', 'Revenue Increase Due to AI (%)': 'mean', 'Job Loss Due to AI (%)': 'mean'})`
   - **By Regulation Status:**  
     Analyze differences in consumer trust and market share depending on how strictly AI is regulated.
   - **Temporal Analysis:**  
     If the dataset spans multiple years, analyze trends over time. Compute year-over-year changes.
   - Questions to Consider:
     - Which country/industry combination has the highest or lowest AI adoption rate?
     - How do regulation types impact key metrics like consumer trust?
     - Are there temporal trends that indicate improvements or declines over the years?

4. **Advanced Statistical Measures (Optional):**
   - **Percentile Analysis:**
     Calculate percentiles for key metrics to understand the distribution at specific points.
   - **Z-Scores:**
     Compute z-scores to identify outliers or unusual values.
   - **Regression Analysis:**
     If there are strong correlations, conduct a regression analysis to understand the relationship between variables.
   - Questions to Consider:
     - Are there any significant differences between countries or industries?
     - Can we predict future trends based on current data?
     
5. Add 2 more advanced statistical measures and what questions would you ask? Answer them in the report.

---

### Task 4: Data Visualization with Seaborn

1. **Distribution Plots:**
   - Create a **Histogram with KDE** for key variables, such as `AI Adoption Rate (%)` and `Job Loss Due to AI (%)`.  
     - *Short Example:*  
       `sns.histplot(df['AI Adoption Rate (%)'], bins=30, kde=True)`
   - Interpret what the distribution reveals: range, modality, and outliers.

2. **Categorical Plots:**
   - **Box Plots and Violin Plots:**  
     Compare metrics like `Revenue Increase Due to AI (%)` across different industries and countries.
   - **Swarm/Strip Plots:**  
     Visualize individual data points for variables such as `Consumer Trust in AI (%)` segmented by `Regulation Status`.
   - Questions to Consider:
     - What patterns emerge when comparing industries? Are certain sectors significantly outperforming others?
     - How do strict regulations compare against lenient ones in terms of consumer trust and market share?

3. **Matrix Plot (Heatmap):**
   - Plot a heatmap for the correlation matrix using:  
     `sns.heatmap(df.corr(), annot=True, cmap="coolwarm")`
   - Interpret which variables have strong correlations and discuss potential causal relationships.

4. **Time Series/Trend Analysis (If Applicable):**
   - Create line or area plots to show how key metrics change over the years.
   - Questions to Consider:
     - Are there trends indicating that AI adoption is improving or declining?
     - How do job loss and revenue increase evolve over time?

5. **Pair Plot:**
   - Generate a pair plot for the numerical variables, with points colored by a categorical feature such as `Industry` or `Regulation Status`.
   - Discuss any apparent clusters or outliers.

6. Add 2 more plots to the report.
---

### Task 5: Reporting and Interpretation

1. **Summary Report(Report #1 which include both data Interpretation and analysis):**
   - Write a detailed report that explains:
     - The data cleaning and transformation steps.
     - Descriptive statistics, key aggregated findings, and visualizations.
     - Any anomalies, trends, or significant correlations.
     - Include answers to guiding questions from the previous tasks.

2. **Interpretation:**
   - Use your findings to make real-world interpretations:
     - How does AI adoption affect revenue and job loss?
     - What are the implications for policymakers, businesses, and technology companies?
     - How can industries leverage AI to enhance productivity and collaboration?
   - Consider how these insights could be used to inform policy decisions and business strategies.

3. **Report #2(Data Interpretation):**
   - Write a detailed report that explains:
     - The data cleaning and transformation steps.
     - Descriptive statistics, key aggregated findings, and visualizations.
     - Any anomalies, trends, or significant correlations.
     

2. **Actionable Recommendations:**
   - Based on your analysis, suggest recommendations for key stakeholders:
     - How can policymakers design balanced regulations to optimize revenue without causing excessive job loss?
     - What strategies might companies employ to improve consumer trust in AI?
     - How might industries leverage high AI adoption rates to enhance productivity and collaboration?
   - Consider writing a conclusion that summarizes the overall insights and suggests avenues for further research or data collection.

3. **Presentation :**
   - Prepare highlighting:
     - Key findings and visualizations.
     - Recommendations and the potential impact on policy and business strategy.

---

## Deliverables

- **Code:**  
  A well-documented Python script or Jupyter Notebook that includes:
  - Data ingestion and cleaning steps.
  - Detailed descriptive and advanced statistical analysis using Pandas and NumPy.
  - Comprehensive visualizations created with Seaborn.

- **Final Report#1 & #2:**  
  A written report (in PDF or Markdown format) that outlines:
  - Your methodology.
  - Key findings, insights, and interpretations.
  - Actionable recommendations based on your analysis.

- **Optional Presentation:**  
  A slide deck summarizing your project for an executive audience.

---

## Evaluation Criteria

- **Completeness:**  
  All tasks have been thoroughly addressed, including detailed descriptive analysis, grouping, and visualization.

- **Technical Accuracy:**  
  Code runs without errors, and the analysis is statistically sound and replicable.

- **Clarity and Documentation:**  
  The code and final report are well-organized and commented, making it easy to follow your logic and methods.

- **Depth of Analysis:**  
  The project demonstrates deep understanding through advanced statistical measures, clear visualizations, and insightful interpretations.

- **Real-World Relevance:**  
  The recommendations and conclusions are connected to practical challenges and scenarios in the real world.

- **Creativity and Initiative:**  
  Any additional analyses, visualizations, or innovative insights beyond the prescribed tasks will be considered positively.

