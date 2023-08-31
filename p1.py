import streamlit as st
import pandas as pd
import plotly.express as px
import ast
import datetime

# Load your DataFrame
# Assuming your DataFrame is named df
df = pd.read_csv("C:\\Users\\Phoenix\\Desktop\\airbnb\\abnb_dataset.csv")

# Assuming your DataFrame is named df
df['_id'] = df['_id'].astype(str)

# Parse the "address" column to convert the string representation into a dictionary
df['address'] = df['address'].apply(ast.literal_eval)

# Extract latitude and longitude coordinates from the "location" field
df['latitude'] = df['address'].apply(lambda x: x['location']['coordinates'][1])
df['longitude'] = df['address'].apply(lambda x: x['location']['coordinates'][0])

# Convert 'last_scraped' column to datetime
df['last_scraped'] = pd.to_datetime(df['last_scraped'])

# Define a function to map dates to seasons
def get_season(date):
    if date.month in [3, 4, 5]:
        return 'Spring'
    elif date.month in [6, 7, 8]:
        return 'Summer'
    elif date.month in [9, 10, 11]:
        return 'Fall'
    else:
        return 'Winter'

# Apply the function to create the 'season' column
df['season'] = df['last_scraped'].apply(get_season)

# Convert 'review_scores' column to dictionaries
df['review_scores'] = df['review_scores'].apply(ast.literal_eval)

# Extract 'review_scores_rating' from the nested 'review_scores' dictionary
df['review_scores_rating'] = df['review_scores'].apply(lambda x: x.get('review_scores_rating', None))

# Streamlit App
st.title("Price Analysis and Visualization")

# Filter Options
st.sidebar.header("Filter Options")
property_types = st.sidebar.multiselect("Select Property Types", df['property_type'].unique())
seasons = st.sidebar.multiselect("Select Seasons", df['season'].unique())

# Filter DataFrame based on selected options
filtered_df = df[(df['property_type'].isin(property_types)) & (df['season'].isin(seasons))]

# Line Chart for Price Trends Over Time
st.header("Price Trends Over Time")
line_chart = px.line(
    filtered_df,
    x="last_scraped",
    y="price",
    color="property_type",
    title="Price Trends Over Time"
)
line_chart.update_layout(
    xaxis_title="Date",
    yaxis_title="Price",
    legend_title="Property Type"
)
st.plotly_chart(line_chart)

# Scatter Plot for Price vs. Ratings
st.header("Price vs. Ratings")
scatter_plot = px.scatter(
    filtered_df,
    x="review_scores_rating",
    y="price",
    color="property_type",
    title="Price vs. Ratings"
)
scatter_plot.update_layout(
    xaxis_title="Review Scores (Rating)",
    yaxis_title="Price",
    legend_title="Property Type"
)
st.plotly_chart(scatter_plot)

# Box Plot for Price Distribution by Property Type
st.header("Price Distribution by Property Type")
box_plot = px.box(
    filtered_df,
    x="property_type",
    y="price",
    title="Price Distribution by Property Type"
)
box_plot.update_layout(
    xaxis_title="Property Type",
    yaxis_title="Price"
)
st.plotly_chart(box_plot)

# Location-Based Analysis: Scatter Plot on a Map
st.header("Location-Based Price Analysis")
if 'latitude' in df.columns and 'longitude' in df.columns:
    map_plot = px.scatter_mapbox(
        filtered_df,
        lat="latitude",
        lon="longitude",
        color="price",
        title="Price Variation by Location",
        mapbox_style="carto-positron",  # You can choose other mapbox styles
        zoom=10  # Adjust the zoom level as needed
    )
    st.plotly_chart(map_plot)
else:
    st.write("Latitude and longitude columns not found for location-based analysis.")


# Seasonal Analysis
st.header("Seasonal Analysis")
seasonal_df = filtered_df.groupby('season')['price'].mean().reset_index()
bar_chart = px.bar(
    seasonal_df,
    x="season",
    y="price",
    title="Average Price by Season"
)
bar_chart.update_layout(
    xaxis_title="Season",
    yaxis_title="Average Price"
)
st.plotly_chart(bar_chart)

# Correlation Analysis
st.header("Correlation Analysis")

# Select numeric columns for correlation analysis
numeric_columns = filtered_df.select_dtypes(include=['number'])

if not numeric_columns.empty:
    correlation_matrix = numeric_columns.corr()
    st.write("Correlation Matrix:")
    st.write(correlation_matrix)
else:
    st.write("No numeric columns available for correlation analysis.")

# Price Outliers
st.header("Price Outliers")
price_outliers = filtered_df[(filtered_df['price'] > filtered_df['price'].quantile(0.95)) |
                             (filtered_df['price'] < filtered_df['price'].quantile(0.05))]
st.write("Outliers:")
st.write(price_outliers)

# Table with Detailed Information
if st.checkbox("Show Detailed Information"):
    st.write(filtered_df)

# User Interaction
st.sidebar.header("User Interaction")

if not filtered_df.empty:
    min_price = min(filtered_df['price'])
    max_price = max(filtered_df['price'])
else:
    min_price, max_price = 0, 100  # Set default values or adjust as needed

average_price = st.sidebar.slider("Select Average Price Range", min_price, max_price)
selected_properties = st.sidebar.multiselect("Select Properties", df['property_type'].unique())

# Filter based on user interaction
filtered_df = df[(df['price'] <= average_price) & (df['property_type'].isin(selected_properties))]

# Display filtered data
st.header("Filtered Data")
st.write(filtered_df)
