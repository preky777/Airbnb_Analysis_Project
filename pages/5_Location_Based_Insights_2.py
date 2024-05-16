import streamlit as st
import pandas as pd
import plotly.express as px
from pymongo import MongoClient
import base64
from io import BytesIO

# Streamlit app title
st.title('Airbnb Price Insights by Location')

# MongoDB connection details
client = MongoClient("mongodb+srv://rp:7654@cluster0.eu7csqt.mongodb.net/")
db = client['abnb']
collection = db['collect']

# Use Streamlit's new caching mechanism to store the unique locations
@st.cache_data
def get_unique_locations():
    pipeline = [
        {"$group": {"_id": "$address.market"}}
    ]
    results = list(collection.aggregate(pipeline))
    locations = [result['_id'] for result in results if result['_id'] is not None]
    return locations



# Get unique locations for the select box
unique_locations = get_unique_locations()

# User input for location using a select box with a unique key
location = st.selectbox('Select a location:', unique_locations, key='unique_location_selectbox')

def get_price_insights(location):
    # MongoDB aggregation pipeline
    pipeline = [
        {"$match": {"address.market": location}},
        {"$group": {
            "_id": "$address.suburb",
            "average_price": {"$avg": "$price"},
            "latitude": {"$first": {"$arrayElemAt": ["$address.location.coordinates", 1]}},
            "longitude": {"$first": {"$arrayElemAt": ["$address.location.coordinates", 0]}}
        }},
        {"$sort": {"average_price": -1}}
    ]
    # Execute the aggregation query
    results = list(collection.aggregate(pipeline))
    return results

# Initialize session state for the DataFrame
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame()

# Button to trigger the MongoDB query
if st.button('Get Insights'):
    # Get the price insights
    insights = get_price_insights(location)
    
    # Convert the results to a DataFrame and store it in session state
    st.session_state.df = pd.DataFrame(insights)
    
    # Rename columns for better readability
    st.session_state.df.rename(columns={'_id': 'Suburb', 'average_price': 'Average Price'}, inplace=True)
    
    # Display the DataFrame
    st.write(st.session_state.df)
    
    # Plot the results on a bar chart
    bar_fig = px.bar(st.session_state.df, x='Suburb', y='Average Price', title=f'Average Airbnb Prices in {location}')
    st.plotly_chart(bar_fig)
    
    # Plot the results on a map
    map_fig = px.scatter_mapbox(st.session_state.df, lat='latitude', lon='longitude', size='Average Price',
                                color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
                                mapbox_style="carto-positron", title=f'Airbnb Prices Map in {location}',
                                hover_name='Suburb')
    st.plotly_chart(map_fig)

# Function to convert DataFrame to CSV and encode it for download
def to_csv(df):
    # Convert DataFrame to CSV string
    csv_string = df.to_csv(index=False)
    # Convert CSV string to bytes
    csv_bytes = csv_string.encode()
    # Encode bytes to base64
    b64 = base64.b64encode(csv_bytes).decode()
    return b64

# Streamlit button to download the DataFrame as CSV
if st.button('Download CSV'):
    # Check if the DataFrame in session state exists and is not empty
    if not st.session_state.df.empty:
        # Convert DataFrame to base64 encoded CSV
        b64 = to_csv(st.session_state.df)
        # Create a link for downloading
        href = f'<a href="data:file/csv;base64,{b64}" download="airbnb_prices_{location}.csv">Download CSV File</a>'
        st.markdown(href, unsafe_allow_html=True)
    else:
        # Inform the user that there is no data to download
        st.error('No data available to download.')


