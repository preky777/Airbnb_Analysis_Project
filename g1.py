import streamlit as st
import pandas as pd
import plotly.express as px
import ast  # Import the ast module for literal evaluation

# Load your DataFrame with the address information
# Assuming your DataFrame is named df
df=pd.read_csv("C:\\Users\\Phoenix\\Desktop\\airbnb\\abnb_dataset.csv")

# Assuming your DataFrame is named df
df['_id'] = df['_id'].astype(str)

# Parse the "address" column to convert the string representation into a dictionary
df['address'] = df['address'].apply(ast.literal_eval)

# Parse the "review_scores" column to convert the string representation into a dictionary
df['review_scores'] = df['review_scores'].apply(ast.literal_eval)

# Extract latitude and longitude coordinates from the "location" field
df['latitude'] = df['address'].apply(lambda x: x['location']['coordinates'][1])
df['longitude'] = df['address'].apply(lambda x: x['location']['coordinates'][0])

# Extract "review_scores_rating" from the nested "review_scores" dictionary
df['review_scores_rating'] = df['review_scores'].apply(lambda x: x.get('review_scores_rating', None))

# Streamlit App
st.title("Interactive Geospatial Visualization")

# Create a map to display the listings' locations
st.header("Map of Airbnb Listings")
fig = px.scatter_geo(df, 
                     lat="latitude", 
                     lon="longitude", 
                     hover_name="name", 
                     custom_data=["price", "review_scores_rating"],  # Use "custom_data" for hover data
                     title="Airbnb Listings")

# Define the hovertemplate to customize the hover text
fig.update_traces(hovertemplate="<b>%{hovertext}</b><br>Price: %{customdata[0]:.2f}<br>Rating: %{customdata[1]}")

st.plotly_chart(fig)

# Filter and Interact with Data
st.sidebar.header("Filter Options")
min_price = st.sidebar.number_input("Minimum Price", min_value=0)
max_price = st.sidebar.number_input("Maximum Price", min_value=0)
min_rating = st.sidebar.number_input("Minimum Rating", min_value=0, max_value=10, step=1)  # Change step to an integer


# Apply filters to the DataFrame
filtered_df = df[(df["price"] >= min_price) & (df["price"] <= max_price) & (df["review_scores_rating"] >= min_rating)]

# Display filtered data on the map
st.header("Filtered Airbnb Listings")
fig_filtered = px.scatter_geo(filtered_df, 
                              lat="latitude", 
                              lon="longitude", 
                              hover_name="name", 
                              custom_data=["price", "review_scores_rating"],  # Use "custom_data" for hover data
                              title="Filtered Airbnb Listings")

# Define the hovertemplate for the filtered map
fig_filtered.update_traces(hovertemplate="<b>%{hovertext}</b><br>Price: %{customdata[0]:.2f}<br>Rating: %{customdata[1]}")

st.plotly_chart(fig_filtered)

# Display a table with detailed information about the selected listing
if st.checkbox("Show Detailed Listing Information"):
    selected_listing = st.selectbox("Select a Listing", filtered_df["name"])
    listing_details = filtered_df[filtered_df["name"] == selected_listing]
    st.dataframe(listing_details)
