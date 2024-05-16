import streamlit as st
import pandas as pd
import ast
import plotly.express as px

# Load the CSV data
data_path = "C:\\Users\\user\\Desktop\\airbnb\\abnb_dataset.csv"
df = pd.read_csv(data_path)

# Convert string representation of dictionaries in certain columns to dictionaries
columns_to_convert = ['address', 'availability', 'review_scores', 'host']
for col in columns_to_convert:
    df[col] = df[col].apply(lambda x: ast.literal_eval(x))

# Streamlit app
st.title("Interactive Airbnb Data Visualization")

# Sidebar filters
st.sidebar.header("Filters")

# Property type filter
property_types = df['property_type'].unique()
selected_property_type = st.sidebar.selectbox("Select Property Type", property_types)

# Price range filter
min_price = st.sidebar.number_input("Minimum Price", min_value=float(df['price'].min()), max_value=float(df['price'].max()), value=float(df['price'].min()), step=1.0)
max_price = st.sidebar.number_input("Maximum Price", min_value=float(df['price'].min()), max_value=float(df['price'].max()), value=float(df['price'].max()), step=1.0)
st.sidebar.write(f"Min Price: {min_price}, Max Price: {max_price}")

# Bedrooms filter
min_bedrooms = st.sidebar.slider("Minimum Bedrooms", min_value=1, max_value=int(df['bedrooms'].max()), value=1)

# Cancellation policy filter
cancellation_policies = df['cancellation_policy'].unique()
selected_cancellation_policy = st.sidebar.selectbox("Select Cancellation Policy", cancellation_policies)

# Apply filters
filtered_df = df[(df['property_type'] == selected_property_type) &
                 (df['price'] >= min_price) &
                 (df['price'] <= max_price) &
                 (df['bedrooms'] >= min_bedrooms) &
                 (df['cancellation_policy'] == selected_cancellation_policy)]

# Display filtered data
st.subheader("Filtered Listings")
st.write(filtered_df)

# Visualization based on filtered data
st.subheader("Number of Listings by Neighborhood")
# Access 'suburb' key from each dictionary in the 'address' column
neighborhood_count = filtered_df['address'].apply(lambda x: x.get('suburb')).value_counts()
st.bar_chart(neighborhood_count)

# Additional interactive visualizations
st.sidebar.subheader("Additional Visualizations")
visualization_option = st.sidebar.selectbox("Select Visualization", ["Price Distribution", "Number of Listings Over Time", "Average Review Scores by Neighborhood"])

if visualization_option == "Price Distribution":
    st.subheader("Price Distribution Histogram with Tooltips")
    fig = px.histogram(filtered_df, x='price', nbins=20, labels={'price': 'Price'})
    fig.update_traces(marker_color='skyblue', marker_line_color='black',
                      marker_line_width=1, opacity=0.7, hoverinfo='y')
    fig.update_layout(title_text='Price Distribution', xaxis_title='Price', yaxis_title='Count')
    st.plotly_chart(fig)

elif visualization_option == "Number of Listings Over Time":
    st.subheader("Overall Number of Listings Over Time")
    df['last_scraped'] = pd.to_datetime(df['last_scraped'])
    df['year_month'] = df['last_scraped'].dt.to_period('M').dt.to_timestamp()
    overall_listings_over_time = df.groupby(df['year_month']).size()
    st.line_chart(overall_listings_over_time)

    st.subheader("Filtered Number of Listings Over Time")
    filtered_df['last_scraped'] = pd.to_datetime(filtered_df['last_scraped'])
    filtered_df['year_month'] = filtered_df['last_scraped'].dt.to_period('M').dt.to_timestamp()
    filtered_listings_over_time = filtered_df.groupby(filtered_df['year_month']).size()
    st.line_chart(filtered_listings_over_time)

elif visualization_option == "Average Review Scores by Neighborhood":
    st.subheader("Average Review Scores by Neighborhood")
    avg_review_scores = {}
    for index, row in filtered_df.iterrows():
        suburb = row['address'].get('suburb')
        review_scores = row['review_scores']
        if review_scores and 'review_scores_rating' in review_scores:
            rating = review_scores.get('review_scores_rating')
            if suburb in avg_review_scores:
                avg_review_scores[suburb].append(rating)
            else:
                avg_review_scores[suburb] = [rating]
    avg_review_scores = {suburb: sum(scores) / len(scores) for suburb, scores in avg_review_scores.items() if scores}
    fig = px.bar(x=list(avg_review_scores.keys()), y=list(avg_review_scores.values()), labels={'x': 'Neighborhood', 'y': 'Average Review Score'})
    fig.update_layout(xaxis={'categoryorder': 'total descending'}, title='Average Review Scores by Neighborhood')
    st.plotly_chart(fig)

# Detailed view for individual listings
if st.checkbox("Show Detailed View for Individual Listings"):
    selected_listing = st.selectbox("Select Listing", filtered_df['name'])
    selected_listing_info = filtered_df[filtered_df['name'] == selected_listing].iloc[0]
    st.subheader("Selected Listing Details")
    st.write(selected_listing_info)
