# Airbnb_Analysis_Project
Airbnb_Analysis_Project for the listings and reviews from mongo db sample dataset

## Introduction
Our solution to this project is a well-structured approach that encompasses MongoDB data retrieval, comprehensive data cleaning, and geospatial visualization. Through interactive pricing and availability analysis, location-based insights, and a user-friendly dashboard, we deliver a holistic understanding of the Airbnb dataset, ensuring transparency through meticulous documentation.

## Requirements for the project

    Python: Make sure you have Python installed on your system. The project is built using Python, and having Python installed is essential to run the code.
    
    GitHub: Ensure you have a GitHub account and know the basics of using Git version control. The project uses GitHub for versioning, collaboration, and sharing code.
    
    Mongo DB: Create a MongoDB Atlas Account,Set Up a Cluster,Load the Airbnb Sample Data and Import Sample Data.
    
    Required Libraries: Install the necessary Python libraries using pip install or any package manager. The essential libraries include:
    
      * pandas as pd
      * streamlit as st
      * numpy as np
      * matplotlib.pyplot as plt
      * plotly.express as px
      * ast 
      * seaborn as sns
      
      
      
Ensure all these libraries are installed before running the project code.

With these prerequisites in place, you'll be ready to explore and run the Airbnb project using Python, GitHub, and Mongo DB. Happy coding!

   
## Installation & Usage

To access the web app, simply open the provided URL in your web browser. Once there, you can start exploring the various features available on the app. The user-friendly interface allows you to interact with the app seamlessly. Provide the necessary inputs based on your specific needs, and in return, you'll receive insightful and interactive results. Enjoy the experience and gain valuable insights from the Airbnb Analysis Project.

    1. Clone the repository to your local machine using the following command: git clone https://github.com/preky777/Airbnb_Analysis_Project.git.
    2. Install the required libraries.
    3. Run the .py file.
    4. Connect to the mongo db atlas and retrieve the sample_airbnb dataaset.
    5. Open a terminal window and navigate to the directory where the app is located using the following command: cd C:\Users\Phoenix\Desktop\airbnb.
    6. Run the Streamlit app using the command [streamlit run abnb.py] and access the app through the local URL provided.
    7. The app should now be running on a local server. If it doesn't start automatically, you can access it by going to either the given Local URL or Network URL.
    8. Explore the Airbnb Analysis App, perform all sorts of filter and selection operators to view the desired data of listings and reviews of different places.
    
Our comprehensive solution transforms Airbnb data into actionable insights. From data retrieval and cleaning to immersive geospatial visualizations and a user-friendly dashboard, we've provided a roadmap for harnessing the dataset's full potential. This journey of analysis and presentation equips users with valuable knowledge about Airbnb listings, prices, and trends, ensuring informed decision-making and enhancing the overall Airbnb experience.


## Components of the Dashboard

    1.Home page
    
    2.Geospatial Visualization

    3.Price Analysis and Visualization

    4.Availability Analysis by Season

    5.Location-Based Insights

    6.Interactive Visualizations

    7.Dashboard Creation

    

1. Home page:
   This code defines the layout and content of the home page for the "Bizcard App." It provides a brief introduction to the app's functionality and prompts the user to click the "Get Started" button to proceed to the next page, which appears to be for extracting and modifying business card data using OCR.


         * st.title("Bizcard App"): Sets the title of the web application to "Bizcard App".

         * st.write(""" ... """, unsafe_allow_html=True): Writes the HTML content provided within triple quotes to the web application. This HTML content seems to define the layout and text displayed on the home page. The HTML content contains a heading, a couple of paragraphs, and a button.

         * The HTML content defines a <div> with a class of "home-text" to group the text elements together. It contains the following components:

               A large heading <h1> with the text "Welcome to BizCardX".
               A subheading <p> with the text "Extracting Business Card Data with OCR".
               A couple of paragraphs that provide introductory information about the app and its purpose.
               unsafe_allow_html=True: This parameter of the st.write() function tells Streamlit to allow rendering the provided HTML content. Without this parameter set to True, Streamlit would escape any HTML tags and display them as plain text.
         
         * if st.button("Get Started"): st.session_state['page'] = 'ext_mod': This line adds a button with the label "Get Started" to the home page. When the button is clicked, it sets a session state variable named 'page' to the value 'ext_mod'. The session state is a way to store and persist data across different pages of the application. By setting the 'page' variable to 'ext_mod', it likely serves as a signal to the application to navigate to another page, presumably the page for extracting and modifying business card data.
      


  2. Extraction and Modification process page:
     The ext_mod_page() function handles different aspects of the business card processing, depending on the option selected by the user. It offers features to upload, extract, modify, and delete business card data interactively.
  

           The function displays a title and a radio button group with three options: "Upload, Extract And Save Card To Database," "Update And Save Card To Database," and "Delete Card From The Database." Based on the selected option, different sections are shown.

            Section 1: Upload & Extract
         
            - Allows users to upload a business card image.
            - Displays the uploaded image and extracts contact information using OCR.
            - Shows the extracted data in a table.
            - Provides buttons to process the image further and save the data to a MySQL database.
     
            Section 2: Modify
         
            - Displays when "Update And Save Card To Database" is selected.
            - Allows users to select a card holder from a list and modify their information.
            - Provides a button to update the modified data in the database.
            - Shows a button to view all updated data in a DataFrame.
     
            Section 3: Delete
         
            - Displays when "Delete Card From The Database" is selected.
            - Allows users to select a card holder from a list for deletion.
            - Shows a warning message with an emoji for confirmation.
            - Provides a button to delete the selected card holder's information from the database.

  3.
      




## App Screenshots

