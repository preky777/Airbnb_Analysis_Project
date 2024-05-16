import streamlit as st

# Page titles
page_titles = [
    "Distribution of Property Types",
    "Distribution of Room Types",
    "Average Price by Property Type",
    "Average Price by Room Type",
    "Distribution of Cancellation Policies",
    "Top Neighborhoods by Number of Listings",
    "Average Review Scores by Neighborhood",
    "Availability Trends Over Time",
    "Price Trends Over Time",
    "Correlation between Price and Number of Reviews",
    "Geospatial Distribution of Listings"
]

# Display each page as an image
for title in page_titles:
    st.subheader(title)
    image_path = f"{title}.png"  # Update with the correct file extension (e.g., .pdf if exporting as PDF)
    st.image(image_path)