# Travel Planner
Welcome to the Travel Planner project! This web application helps users plan their trips by providing features such as itinerary creation, weather forecasts, and points of interest recommendations.


Trip Planning: Users can create and manage their travel itineraries, including specifying the destination, departure date, and activities.
Weather Forecast: Get real-time weather forecasts for the chosen destination to better plan your activities.
Points of Interest: Explore nearby attractions, restaurants, and landmarks at the destination.
User Authentication: Secure user authentication system to protect user data and trip information.
API Integration: Integration with Google Places API for points of interest and OpenWeather API for weather forecasts.
Setup
Clone the repository to your local machine:


```bash
git clone https://github.com/Gasimzade04/TrikTrippers.git
```
Navigate to the project directory:

```bash
Copy code
cd TrikTrippers
```
Install dependencies:

```bash
pip install -r requirements.txt
```
Set up environment variables:

Create a .env file in the project root directory.
Add the required environment variables for API keys (e.g., GOOGLE_API_KEY, OPENAI_API_KEY, OPEN_WEATHER_API_KEY).
Usage
Run the Django development server:

```bash
python manage.py runserver 0.0.0.0:80 
```
Access the application in your web browser at http://localhost:80.

Dependencies
Django: Web framework for building the application.
Django REST Framework: Toolkit for building Web APIs.
Requests: HTTP library for making API requests.
Other dependencies are listed in the requirements.txt file.
Contributing
Contributions are welcome! If you would like to contribute to the project, please follow these steps:

Create a new branch (git checkout -b feature/improvement).
Make your changes and commit them (git commit -am 'Add new feature').
Push to the branch (git push origin feature/improvement).
Create a new Pull Request.
