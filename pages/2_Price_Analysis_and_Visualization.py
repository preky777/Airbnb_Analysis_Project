import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from streamlit_folium import folium_static  # Importing folium_static for Streamlit compatibility

# Load the Airbnb dataset
file_path = "C:\\Users\\user\\Desktop\\airbnb\\abnb_dataset.csv"
df = pd.read_csv(file_path)

# Convert string representations of dictionaries in 'address' column to actual dictionaries
df['address'] = df['address'].apply(eval)

# Extract latitude and longitude coordinates from the 'address' column
df['latitude'] = df['address'].apply(lambda x: x['location']['coordinates'][1] if 'location' in x else None)
df['longitude'] = df['address'].apply(lambda x: x['location']['coordinates'][0] if 'location' in x else None)

# Create separate columns for location details
df['suburb'] = df['address'].apply(lambda x: x.get('suburb'))
df['government_area'] = df['address'].apply(lambda x: x.get('government_area'))
df['market'] = df['address'].apply(lambda x: x.get('market'))

# Visualize average price by property type
st.title('Price Analysis and Visualization')

# Average price by property type
avg_price_by_property_type = df.groupby('property_type')['price'].mean().sort_values(ascending=False)
st.subheader('Average Price by Property Type')
st.bar_chart(avg_price_by_property_type)

# Interactive map showing price distribution by location
st.subheader('Price Distribution by Location')
map_center = [df['latitude'].mean(), df['longitude'].mean()]  # Center the map around the average location
map_data = df[['latitude', 'longitude', 'price', 'suburb']].dropna()
m = folium.Map(location=map_center, zoom_start=12)

for index, row in map_data.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=5,  # Adjust the size of the pointers
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity=0.6,
        tooltip=f"Location: {row['suburb']}<br>Price: ${row['price']}"  # Include location name in tooltip
    ).add_to(m)

# Add fullscreen mode
folium.plugins.Fullscreen().add_to(m)

# Render the map
folium_static(m)

# Interactive filtering by location details
selected_location = st.selectbox('Select Location Detail', ['suburb', 'government_area', 'market'])
if selected_location:
    avg_price_by_location_detail = df.groupby(selected_location)['price'].mean().sort_values(ascending=False)
    st.bar_chart(avg_price_by_location_detail)

# Price trend analysis
if 'calendar_last_scraped' in df.columns:
    df['calendar_last_scraped'] = pd.to_datetime(df['calendar_last_scraped'])
    df['month'] = df['calendar_last_scraped'].dt.month

    # Define seasons based on months
    seasons = {
        1: 'Winter',
        2: 'Winter',
        3: 'Spring',
        4: 'Spring',
        5: 'Spring',
        6: 'Summer',
        7: 'Summer',
        8: 'Summer',
        9: 'Autumn',
        10: 'Autumn',
        11: 'Autumn',
        12: 'Winter'
    }
    df['season'] = df['month'].map(seasons)

    st.subheader('Average Price by Season')
    avg_price_by_season = df.groupby('season')['price'].mean().sort_index()
    st.bar_chart(avg_price_by_season)


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("C:\\Users\\user\\Desktop\\airbnb\\abnb_dataset.csv")

# Convert date columns to datetime
df['last_scraped'] = pd.to_datetime(df['last_scraped'])

# Title for the app
st.title('Airbnb Price Trend Analysis')

# Plotting price trends
st.subheader('Price Trend Over Time')

# Set the style
plt.style.use('ggplot')

# Plot price over time
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x=df['last_scraped'], y=df['price'], marker='o', linewidth=2, color='blue', ax=ax)
ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Price (USD)', fontsize=12)
ax.set_title('Price Trend Over Time', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()

# Display the plot in the Streamlit app
st.pyplot(fig)


# Price trend analysis
if 'calendar_last_scraped' in df.columns:
    df['calendar_last_scraped'] = pd.to_datetime(df['calendar_last_scraped'])
    df['month_year'] = df['calendar_last_scraped'].dt.to_period('M').dt.to_timestamp()  # Extract year-month information

    st.subheader('Price Trend Over Time')

    # Add granularity selector
    granularity = st.selectbox('Select Granularity', ['Daily', 'Weekly', 'Monthly'], index=2)  # Default to Monthly
    if granularity == 'Daily':
        time_period = 'D'
    elif granularity == 'Weekly':
        time_period = 'W'
    else:
        time_period = 'M'

    avg_price_trend = df.resample(time_period, on='month_year')['price'].mean()
    
    # Plot the trend line
    st.write("Average Price Trend:")
    fig, ax = plt.subplots(figsize=(10, 6))
    avg_price_trend.plot(ax=ax, marker='o', linestyle='-')
    ax.set_xlabel('Time')
    ax.set_ylabel('Average Price')
    ax.set_title('Average Price Trend Over Time')
    st.pyplot(fig)

    # Add data table showing average price for each time period
    st.write("Average Price for Each Time Period:")
    st.write(avg_price_trend.reset_index().rename(columns={'price': 'Average Price'}))

# Additional analysis
st.subheader('Additional Analysis')

# Explore price distribution
st.write("Price Distribution:")
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(df['price'], bins=30, edgecolor='black')
ax.set_xlabel('Price')
ax.set_ylabel('Frequency')
st.pyplot(fig)

# Explore correlations (numeric columns only)
st.subheader('Correlation Analysis')
correlation_columns = st.multiselect('Select columns for correlation analysis', df.select_dtypes(include=['number']).columns)
if correlation_columns:
    correlation_matrix = df[correlation_columns].corr()
    st.write("Correlation Heatmap:")
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)
    st.pyplot(fig)

# Explore outliers
st.subheader('Outlier Analysis')
outlier_column = st.selectbox('Select column for outlier analysis', df.select_dtypes(include=['number']).columns)
if outlier_column:
    st.write("Outliers:")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(x=df[outlier_column], ax=ax)
    ax.set_xlabel(outlier_column)
    st.pyplot(fig)