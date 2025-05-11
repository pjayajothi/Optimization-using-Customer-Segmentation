# 🎯 Credit Card Targeting Optimization Using Customer Segmentation

## 🧠 Overview
This project analyzes customer behavior data to improve the targeting strategy for a fictional credit card product. The goal was to use clustering to identify high-value segments, simulate performance of a new campaign, and deliver data-driven recommendations.
Data Set - <a href ="https://www.kaggle.com/datasets/arjunbhasin2013/ccdata?resource=download&SSORegistrationToken=CfDJ8KvMat0eHzhGoPokVBGB7D3gy419ugFJ9BPG6Obi1qf88upUVSG6iaQZPZBT-6OfJ3NCM0Quowj-km4ANMlEd6YlMtC1z0nD84rdBgeOmt9iIUgJEU6BovFtF4JZx7Ql5RxMX-a5QmxuCKdddaEy91zGAobunsuWGMTNo7fsW9n6o1T6m-wYfUc2huhiUY20ZF0rlUvlexkfqWuHv-CUSsaqTSLVUoqfUIpIEX8LCUbU0PjzgqAnHWImKEtObVkfvu46Md5TCjvsL9byPXS4EDvvtLo5Hms5OhF7LkYDZwIWP7ZR-gr1YdLSj7Ahjm889qX02x7HUn8lULJ4yLHh3gkpgQ&DisplayName=rosy%20j"> Credit Card Dataset for Clustering </a> by Arjun Bhasin.
---

## 📊 Problem Statement
- Increase conversion rates of credit card offers by targeting the right customer segments.
- Reduce marketing spend on low-yield groups.

---

## 🛠️ Tools & Technologies
- **Python**, **Pandas**, **scikit-learn**, **Matplotlib**, **Seaborn**
- **SQL (PostgreSQL)** for data extraction and filtering
- **PowerPoint** for stakeholder presentation

---
## 🧠 Skills Demonstrated

- Data cleaning and preprocessing
- Exploratory data analysis and visualization
- Customer segmentation using unsupervised learning
- Business case communication using visuals

---

## 🔍 Key Steps

1. **Data Cleaning**  
   Used SQL and Pandas to preprocess 100K+ rows of customer data (demographics, credit scores, transaction behavior).

2. **Exploratory Data Analysis (EDA)**  
   Identified patterns in income, credit utilization, and product usage.

3. **Customer Segmentation**  
   Applied k-means clustering to find high-conversion potential groups based on:
   - Credit score
   - Annual income
   - Avg. monthly transaction volume
   - Number of products used

4. **Campaign Simulation**  
   Built A/B test scenario to estimate performance improvements. Found:
   - 18% projected increase in conversion
   - ~$150K potential annual revenue lift

5. **Presentation to Stakeholders**  
   Created a deck summarizing findings and recommended targeting strategy changes.

---

## 📈 Results
- Identified 3 high-potential customer segments.
- Proposed strategy with higher predicted ROI for direct marketing.
- Built reproducible pipeline for re-segmentation as new data arrives.

---

## 📂 Repository Contents
| File/Folder | Description |
|-------------|-------------|
| `raw_data.csv`| Raw dataset containing credit card usage data.
| `cleaned_data.csv`| Cleaned version of the dataset ready for analysis.
| `cluster_plot.png`| Visualization of customer clusters.
| `lift-chart.png` | Revenue comparison between targeting strategies
| `requirements.txt`| Python dependencies.
| `results_simulation_and_visuals.ipynb`| Revenue simulation, lift chart
| `data_cleaning_and_eda.ipynb` | Data cleaning and initial exploration
| `segmentation_modeling.ipynb`| KMeans clustering and PCA

---

## 🧪 Try It Yourself
1. Clone the repo
2. Install requirements: `pip install -r requirements.txt`
3. Run the notebooks in order

---

## ✍️ Author
Pujaa Jayajothi – Business/Data Analyst | Security-aware | Data-Driven Storyteller  



