import streamlit as st
import pandas as pd
import ast
import folium
import matplotlib.pyplot as plt
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster
import seaborn as sns

# Read the CSV file
df = pd.read_csv("C:\\Users\\user\\Desktop\\airbnb\\abnb_dataset.csv")

# Define a function to convert string to dictionary
def parse_address(address):
    try:
        return ast.literal_eval(address)
    except (SyntaxError, ValueError):
        return {}

# Convert 'address' column from string to dictionary
df['address'] = df['address'].apply(parse_address)

# Define a function to extract 'suburb' and 'government_area' values
def extract_suburb_and_government_area(address_dict):
    try:
        suburb = address_dict.get('suburb', None)
        government_area = address_dict.get('government_area', None)
        return suburb, government_area
    except AttributeError:
        return None, None

# Apply the function to extract 'suburb' and 'government_area' values
df['suburb'], df['government_area'] = zip(*df['address'].apply(extract_suburb_and_government_area))


# Streamlit app
def main():
    st.title('Airbnb Listing Prices by Location')

    # Sidebar for location selection and price filter
    location_options = ['suburb', 'government_area']
    selected_location = st.sidebar.selectbox('Select Location Type', location_options)

    # Determine the minimum price dynamically from the dataframe
    min_price = int(df['price'].min())

    # Text indicating min and max price values
    st.sidebar.write("Enter Price Range:")
    st.sidebar.write("Min Price: $", min_price)
    st.sidebar.write("Max Price: $", int(df['price'].max()))

    # Sidebar for price filter
    max_price = st.sidebar.number_input('Enter Max Price', min_value=min_price, max_value=int(df['price'].max()), value=int(df['price'].max()), step=10)

    # Filtered dataframe based on location and price range
    filtered_df = df[(df['price'] <= max_price)]

    # Reset index of filtered DataFrame
    filtered_df.reset_index(drop=True, inplace=True)

    # Display title
    st.write('## Listing Price Statistics')

    # Display filtered dataframe
    st.write("Total locations available:", len(filtered_df))
    st.write(filtered_df)

    # Create map for filtered dataframe
    st.write('## Map of Listing Prices by Location (Filtered)')
    m = folium.Map(location=[41.1413, -8.61308], zoom_start=12)

    marker_cluster = MarkerCluster().add_to(m)

    for i in range(len(filtered_df)):
        if filtered_df['address'].iloc[i]:
            loc = filtered_df['suburb'].iloc[i] if selected_location == 'suburb' else filtered_df['government_area'].iloc[i]
            folium.Marker(
                location=[filtered_df['address'].iloc[i]['location']['coordinates'][1], filtered_df['address'].iloc[i]['location']['coordinates'][0]],
                popup="Location: {}\nPrice: ${}".format(loc, filtered_df['price'].iloc[i]),
                icon=None,
            ).add_to(marker_cluster)

    # Display map
    folium_static(m)

    # Price distribution box plot for each location
    st.write('## Price Distribution')

    if selected_location in filtered_df.columns:  # Check if the selected location exists in the dataframe
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.boxplot(data=filtered_df, x=selected_location, y='price', ax=ax)
        ax.set_xlabel('Location')
        ax.set_ylabel('Price ($)')
        ax.tick_params(axis='x', rotation=45)
        st.pyplot(fig)
    else:
        st.write(f"No data available for {selected_location}")

if __name__ == "__main__":
    main()
