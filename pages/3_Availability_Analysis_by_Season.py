import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv("C:\\Users\\user\\Desktop\\airbnb\\abnb_dataset.csv")

# Function to parse availability values from the JSON-like string
def parse_availability(avail_str, interval):
    avail_dict = eval(avail_str)  # Evaluate the string as a dictionary
    return avail_dict.get(interval, 0)

# Define time intervals
intervals = ['availability_30', 'availability_60', 'availability_90', 'availability_365']

# Apply the parsing function to each time interval
for interval in intervals:
    df[interval] = df['availability'].apply(lambda x: parse_availability(x, interval))

# Convert 'last_scraped' column to datetime format
df['last_scraped'] = pd.to_datetime(df['last_scraped'])

# Extract month from 'last_scraped' column
df['month'] = df['last_scraped'].dt.month

# Define seasons based on months
def get_season(month):
    if month in [12, 1, 2]:  # Winter: December, January, February
        return 'Winter'
    elif month in [3, 4, 5]:  # Spring: March, April, May
        return 'Spring'
    elif month in [6, 7, 8]:  # Summer: June, July, August
        return 'Summer'
    else:  # Fall: September, October, November
        return 'Fall'

# Apply the season function to the 'month' column
df['season'] = df['month'].apply(get_season)

# Group by month and calculate average availability for each time interval
availability_by_month = df.groupby('month')[intervals].mean().reset_index()

# Group by season and calculate average availability for each time interval
availability_by_season = df.groupby('season')[intervals].mean().reset_index()

# Title for the app
st.title('Airbnb Availability Analysis')

# Plotting availability trends by month and by season side by side
st.subheader('Availability Analysis')

# Plot monthly availability trends
st.subheader('Monthly Availability Trends')
for interval in intervals:
    fig = px.line(availability_by_month, x='month', y=interval, 
                  labels={'month': 'Month', 'availability': f'Average {interval} Availability'}, 
                  title=f'Monthly {interval} Availability Trend')
    st.plotly_chart(fig, use_container_width=True)

# Plot seasonal availability trends
st.subheader('Seasonal Availability Trends')
for interval in intervals:
    fig = px.bar(availability_by_season, x='season', y=interval, 
                 labels={'season': 'Season', 'availability': f'Average {interval} Availability'}, 
                 title=f'Seasonal {interval} Availability Trend', color='season')
    st.plotly_chart(fig, use_container_width=True)




import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

# Load the CSV data
csv_path = "C:\\Users\\user\\Desktop\\airbnb\\abnb_dataset.csv"
data = pd.read_csv(csv_path)

# Convert relevant columns to datetime
date_columns = ['last_scraped', 'calendar_last_scraped', 'first_review', 'last_review']
for col in date_columns:
    data[col] = pd.to_datetime(data[col], errors='coerce')

# Convert 'availability' column to JSON format
data['availability'] = data['availability'].apply(lambda x: json.loads(x.replace("'", "\"")))

# Extract availability values
data['availability_30'] = data['availability'].apply(lambda x: x['availability_30'])
data['availability_60'] = data['availability'].apply(lambda x: x['availability_60'])
data['availability_90'] = data['availability'].apply(lambda x: x['availability_90'])
data['availability_365'] = data['availability'].apply(lambda x: x['availability_365'])

# Calculate overall availability
data['overall_availability'] = (data['availability_30'] + data['availability_60'] + 
                                data['availability_90'] + data['availability_365']) / 4

# Extract year and month from the 'last_scraped' column
data['year_month'] = data['last_scraped'].dt.to_period('M')

# Calculate occupancy rates
occupancy_rates = data.groupby('year_month')['overall_availability'].mean()

# Streamlit app
st.title('Airbnb Occupancy Rates Visualization')

# Debugging
st.write("Occupancy Rates DataFrame:")
st.write(occupancy_rates)

# Line chart
st.subheader('Occupancy Rates Over Time')
if not occupancy_rates.empty:
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x=occupancy_rates.index.astype(str), y=occupancy_rates.values, ax=ax)
    plt.xticks(rotation=45)
    plt.xlabel('Year-Month')
    plt.ylabel('Occupancy Rate')
    st.pyplot(fig)
else:
    st.write("No data available for occupancy rates over time.")



import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv("C:\\Users\\user\\Desktop\\airbnb\\abnb_dataset.csv")

# Convert 'last_scraped' column to datetime format
df['last_scraped'] = pd.to_datetime(df['last_scraped'])

# Extract month and year from 'last_scraped' column
df['month'] = df['last_scraped'].dt.month
df['year'] = df['last_scraped'].dt.year

# Group by month, year, and count the number of listings
occupancy_data = df.groupby(['year', 'month']).size().reset_index(name='count')

# Define the Streamlit app
def main():
    st.title('Airbnb Occupancy and Demand Analysis')

    # Visualize booking patterns using an interactive bar chart
    st.subheader('Booking Patterns Over the Year (Bar Chart)')
    booking_bar_chart = px.bar(occupancy_data, x='month', y='count', color='year', 
                               labels={'count': 'Number of Bookings', 'month': 'Month'},
                               title='Booking Patterns Over the Year (Bar Chart)',
                               hover_data={'year': True, 'count': True})
    st.plotly_chart(booking_bar_chart, use_container_width=True)

    # Visualize booking patterns using a scatter plot
    st.subheader('Booking Patterns Over the Year (Scatter Plot)')
    booking_scatter_plot = px.scatter(occupancy_data, x='month', y='count', color='year', 
                                      labels={'count': 'Number of Bookings', 'month': 'Month'},
                                      title='Booking Patterns Over the Year (Scatter Plot)',
                                      hover_data={'year': True, 'count': True})
    st.plotly_chart(booking_scatter_plot, use_container_width=True)

    # Visualize booking patterns using a line graph
    st.subheader('Booking Patterns Over the Year (Line Graph)')
    booking_line_chart = px.line(occupancy_data, x='month', y='count', color='year', 
                                 labels={'count': 'Number of Bookings', 'month': 'Month'},
                                 title='Booking Patterns Over the Year (Line Graph)')
    st.plotly_chart(booking_line_chart, use_container_width=True)

# Execute the main function
if __name__ == '__main__':
    main()


import streamlit as st
import pandas as pd
import plotly.express as px
import json

# Load the data from the CSV file
data_path = "C:\\Users\\user\\Desktop\\airbnb\\abnb_dataset.csv"
df = pd.read_csv(data_path)

# Add a new column for 'month'
df["month"] = pd.to_datetime(df["last_scraped"]).dt.month_name()

# Function to extract availability values from JSON string
def extract_availability(data):
    availability_dict = json.loads(data.replace("'", "\""))
    return (
        availability_dict["availability_30"],
        availability_dict["availability_60"],
        availability_dict["availability_90"],
        availability_dict["availability_365"],
    )


# Extract availability values and add them as new columns
availability_values = df["availability"].apply(extract_availability)
df[["availability_30", "availability_60", "availability_90", "availability_365"]] = pd.DataFrame(availability_values.tolist(), index=df.index)

# Streamlit App
st.title("Airbnb Demand Fluctuations")

# Select Month for Visualization
selected_month = st.selectbox("Select Month", df["month"].unique())

# Filter data by month
df_filtered = df.loc[df["month"] == selected_month]

# Calculate average monthly availability
avg_monthly_availability = df_filtered[["availability_30", "availability_60", "availability_90", "availability_365"]].mean().mean()
st.write(f"Average Monthly Availability: {int(avg_monthly_availability)}")

# Create separate line charts for each availability metric
availability_metrics = ["availability_30", "availability_60", "availability_90", "availability_365"]
for metric in availability_metrics:
    # Optional: Add hover_data for individual charts (list column names)
    hover_data = [metric] if st.checkbox(f"Enable Hover for {metric.replace('_', ' ')} Availability?") else []
    fig = px.line(
        df_filtered,
        x=df_filtered.index,
        y=metric,
        labels={"value": "Availability"},
        title=f"{metric.replace('_', ' ')} Availability for {selected_month}",
        hover_data=hover_data,  # Include hover_data if enabled
        width=800,
        height=300,
    )
    st.plotly_chart(fig)

# Create a line chart for the average availability (without hover_data)
fig_avg = px.line(
    x=[0],  # Dummy data for x-axis (just a single point)
    y=[avg_monthly_availability],
    labels={"value": "Availability"},
    title=f"Average Availability for {selected_month}",
    width=800,
    height=200,
)
fig_avg.add_hline(y=avg_monthly_availability, line_dash="dash", line_color="orange", annotation_text=f"Average ({int(avg_monthly_availability)})", annotation_position="top right")
st.plotly_chart(fig_avg)