# EC601---Project-2

OPEN SOURCE API “Airbnb Locator in Paris”
By,
Avantika Kothandaraman

EC601 - Product Design - PROJECT 2

Acknowledgements: <br>
Kaggle and the original creators of the Airbnb’s European Cities dataset,
https://zenodo.org/records/4446043#.Y9Y9ENJBwUE <br>
ChatGPT for assisting in fine tuning my ideas and debugging the code.

Mission Statement: <br>
The aim of this product is to help travelers to Paris, particularly foreign travelers, find locations to Airbnbs in various parts of the city. The map would include the location of the 
Airbnb, the rating, number of bedrooms and the price for 2 nights, 2 people. This is to help travelers easily locate lodging spots without having to rely on potentially false/misleading 
information. This is done to provide a seamless way to locate, explore and evaluate various Airbnb properties.

User Stories:
1. As a traveler, I want to search for Airbnb properties in Paris to find suitable accommodation quickly. (MVP)
2. As a traveler, I want to visualize the location of every available Airbnb in Paris. (MVP)
3. As a traveler, I want to know the number of bedrooms, the price for 1 night and customer
ratings to make an informed decision. (MVP)
4. As a user, I want to be able to write reviews on different properties.
5. As a traveler, I want to be able to read reviews written by other travelers.
6. As a traveler, I want to be able to make bookings by directly contacting the host through
this service.
7. As a foreign traveler, I want the option to view the listed price in different currencies.
8. As an app user, I want the service to be available on both mobile and desktop settings.
9. As an avid traveler, I want to be able to use the same service for more European cities.
 
Minimum Viable Product:
The first 3 points discussed previously are the MVP.
1. As a traveler, I want to search for Airbnb properties in Paris to find suitable accommodation quickly. (MVP)
2. As a traveler, I want to visualize the location of every available Airbnb in Paris. (MVP)
3. As a traveler, I want to know the number of bedrooms, the price for 1 night and customer ratings to make an informed decision. (MVP)

Demonstration of the MVP using third-party APIs:
1. The dataset https://zenodo.org/records/4446043#.Y9Y9ENJBwUE must be downloaded and saved as parisbnb2.csv
2. The code Airbnb_paris.py must also be saved in the same directory.
3. The Flask API can be run through the command line terminal.
4. Use python3 -m pip install folium to install folium.
5. The app has 3 routes:
/ - which leads to the homepage,
/listings - which produces a text script of the price, number of bedrooms, ratings, latitude and longitude
/map - which produces a map with the locations plotted (the popup of the map displays the price, number of bedrooms and rating)
6. This app makes use of Flask API.
7. The dataset of the locations and Airbnb property details was downloaded from Kaggle in
.csv format (credits have been provided to the original authors of the dataset).
8. Runs on http://127.0.0.1:5000
9. The map is developed as a .html file, which must be saved in the same directory as the
other files in a folder named “templates”
10. Finally the API can be run from the command line terminal.

[EC601-Project2-Avantika.pdf](https://github.com/avantika747/EC601---Project-2/files/13540883/EC601-Project2-Avantika.pdf)
