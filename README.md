# Airbnb Analysis Project

## Project Overview

 This project aims to analyze Airbnb data using MongoDB Atlas, perform data cleaning and preparation, develop interactive geospatial visualizations, and create dynamic plots to gain insights into pricing variations, availability      patterns, and location-based trends.

## Objectives

    1.  Establish a MongoDB connection, retrieve the Airbnb dataset, and ensure efficient data retrieval for analysis.
    2.  Clean and prepare the dataset, addressing missing values, duplicates, and data type conversions for accurate analysis.
    3.  Develop a Streamlit web application with interactive maps showcasing the distribution of Airbnb listings, allowing users to explore prices, ratings, and other relevant factors.
    4.  Conduct price analysis and visualization, exploring variations based on location, property type, and seasons using dynamic plots and charts.
    5.  Analyze availability patterns across seasons, visualizing occupancy rates and demand fluctuations using suitable visualizations.
    6.  Investigate location-based insights by extracting and visualizing data for specific regions or neighborhoods.
    7.  Create interactive visualizations that enable users to filter and drill down into the data.
    8.  Build a comprehensive dashboard using Tableau or Power BI, combining various visualizations to present key insights from the analysis.

## Repository Structure
    .
    ├── 1_Geospatial_Visualization.py
    ├── pages
    │   ├── 2_Price_Analysis_and_Visualization.py
    │   ├── 3_Availability_Analysis_by_Season.py
    │   ├── 4_Location_Based_Insights_1.py
    │   ├── 5_Location_Based_Insights_2.py
    │   ├── 6_Interactive_Visualizations.py
    │   ├── 7_Dashboard_Creation_Using_Power_BI.py
    ├── README.md
    └── requirements.txt

# Project Approach

## 1. MongoDB Connection and Data Retrieval

    •Establish a connection to the MongoDB Atlas database.
    •Retrieve the Airbnb dataset.
    •Perform queries and data retrieval operations to extract the necessary information for analysis.

## 2. Data Cleaning and Preparation

    •Handle missing values and remove duplicates.
    •Transform data types as necessary.
    •Prepare the dataset for EDA and visualization tasks, ensuring data integrity and consistency.

## 3. Geospatial Visualization

    •Develop a Streamlit web application.
    •Utilize geospatial data to create interactive maps.
    •Visualize the distribution of listings across different locations, allowing users to explore prices, ratings, and other relevant factors.

## 4. Price Analysis and Visualization

    •Analyze and visualize how prices vary across different locations, property types, and seasons.
    •Create dynamic plots and charts that enable users to explore price trends, outliers, and correlations with other variables.

## 5. Availability Analysis by Season

    •Analyze the availability of Airbnb listings based on seasonal variations.
    •Visualize the occupancy rates, booking patterns, and demand fluctuations throughout the year using line charts, heatmaps, or other suitable visualizations.

## 6. Location-Based Insights

    •Investigate how the price of listings varies across different locations.
    •Use MongoDB queries and data aggregation techniques to extract relevant information for specific regions or neighborhoods.
    •Visualize these insights on interactive maps or create dashboards in tools like Tableau or Power BI.

## 7. Interactive Visualizations

    •Develop dynamic and interactive visualizations that allow users to filter and drill down into the data based on their preferences.
    •Enable users to interact with the visualizations to explore specific regions, property types, or time periods of interest.

## 8. Dashboard Creation

    •Utilize Tableau or Power BI to create a comprehensive dashboard that presents key insights from your analysis.
    •Combine different visualizations, such as maps, charts, and tables, to provide a holistic view of the Airbnb dataset and its patterns.

## Installation

To run this project locally, follow these steps:

    1. Clone the repository:
        git clone https://github.com/your_username/airbnb-analysis.git

    2. Navigate to the project directory:
        cd airbnb-analysis

    3. Install the required libraries:
        pip install -r requirements.txt

## Usage

    1. Run the Streamlit application:
        streamlit run 1_Geospatial_Visualization.py
    
    2. Open your web browser and navigate to the local host URL provided by Streamlit.

## Requirements

The required Python libraries for this project are listed in the requirements.txt file.

## App Screenshots

<img width="1251" alt="Screenshot 2024-05-17 033832" src="https://github.com/preky777/Airbnb_Analysis_Project/assets/107749942/a6b28fe1-ef3a-4bd3-9869-ee2bf2df8ce4">
<img width="1249" alt="Screenshot 2024-05-17 033922" src="https://github.com/preky777/Airbnb_Analysis_Project/assets/107749942/432a6432-ee14-4df6-a164-95a83447e678">
<img width="1250" alt="Screenshot 2024-05-17 033951" src="https://github.com/preky777/Airbnb_Analysis_Project/assets/107749942/c84f58a1-7b96-4c39-b786-62fb8841b2ff">
<img width="1250" alt="Screenshot 2024-05-17 034033" src="https://github.com/preky777/Airbnb_Analysis_Project/assets/107749942/3936656c-6817-4a07-b499-f24ec6e44605">
<img width="1248" alt="Screenshot 2024-05-17 034128" src="https://github.com/preky777/Airbnb_Analysis_Project/assets/107749942/d731e690-117d-49df-a138-580e7a7c3631">
<img width="1250" alt="Screenshot 2024-05-17 034248" src="https://github.com/preky777/Airbnb_Analysis_Project/assets/107749942/93d68777-8b54-40a0-b6df-42b8a92de96b">
<img width="1247" alt="Screenshot 2024-05-17 034307" src="https://github.com/preky777/Airbnb_Analysis_Project/assets/107749942/0d8d6f26-8ea4-41f0-85a9-737a8b5c1cb9">
<img width="1250" alt="Screenshot 2024-05-17 034330" src="https://github.com/preky777/Airbnb_Analysis_Project/assets/107749942/3c4ff035-8a24-4413-a790-173fca585815">
<img width="1250" alt="Screenshot 2024-05-17 034351" src="https://github.com/preky777/Airbnb_Analysis_Project/assets/107749942/fd5fc31b-0ad1-49cc-baa0-8b3f4d7df2b6">
