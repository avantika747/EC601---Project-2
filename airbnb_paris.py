import pandas as pd
import folium
from flask import Flask, request, jsonify, render_template, Response
import os

app = Flask(__name__)

# Load the dataset from parisbnb.csv
paris_dataset = pd.read_csv('parisbnb2.csv')

# Select and include only the specific columns you want
selected_columns = ['realSum', 'bedrooms', 'guest_satisfaction_overall', 'lat', 'lng']
filtered_paris_dataset = paris_dataset[selected_columns]

# Initialize the listings data
paris_listings = None  # Initialize it as None here

@app.route('/', methods=['GET'])
def welcome_page():
    return """
    <html>
    <head>
        <title>Welcome to My Paris Airbnb Listings App</title>
    </head>
    <body>
        <h1>Welcome to My Paris Airbnb Listings App</h1>
        <p>Explore Airbnb listings in Paris:</p>
        <ul>
            <li><a href="/listings">View Listings</a></li>
            <li><a href="/map">View Map</a></li>
        </ul>
    </body>
    </html>
    """

@app.route('/listings', methods=['GET'])
def get_paris_airbnb_listings():
    global paris_listings  # Use the global variable
    # Convert the filtered dataset to a list of dictionaries
    paris_listings = filtered_paris_dataset.to_dict(orient='records')
    text_output = ""
    for listing in paris_listings:
        text_output += f"Price (2 nights, 2 people): €{listing['realSum']}, Rating: {listing['guest_satisfaction_overall']}, Bedrooms: {listing['bedrooms']}\n"

    response = Response(text_output, content_type='text/plain; charset=utf-8')
    return response
    #return jsonify(paris_listings)

@app.route('/map', methods=['GET'])
def display_paris_map():
    if paris_listings is None:
        return "No data available. Please fetch listings first."

    # Define the absolute path to the HTML file
    html_file_path = '/Users/avantikak/Desktop/templates/paris_airbnb_map.html'

    # Check if the HTML file exists and delete it if it does
    if os.path.exists(html_file_path):
        os.remove(html_file_path)

    # Create a map centered at Paris
    m = folium.Map(location=[48.8566, 2.3522], zoom_start=12)  # Paris coordinates

    # Add markers for Paris Airbnb listings with additional information
    for listing in paris_listings:
        content = f"Price (2N, 2P): €{listing['realSum']}, Rating: {listing['guest_satisfaction_overall']}, Bedrooms: {listing['bedrooms']}"
        folium.Marker(
            location=[listing['lat'], listing['lng']],
            popup=content
        ).add_to(m)

    # Save the map to the HTML file with the specified path
    m.save(html_file_path)

    return render_template('paris_airbnb_map.html')


if __name__ == '__main__':
    app.run(debug=True)
