# Simple Weather App

## 📝 Description

This is a simple command-line Python application that fetches and displays current weather conditions for a user-specified city. It uses the WeatherAPI service to retrieve real-time data such as temperature, humidity, and wind speed.

## ✨ Features

- **Real-Time Data:** Fetches up-to-the-minute weather conditions.
- **Location-Based Search:** Allows the user to enter a city name to get a weather report.
- **Key Weather Metrics:** Displays temperature in Celsius, weather condition, humidity, and wind speed in kilometers per hour.
- **Error Handling:** Provides a clear message if weather data cannot be retrieved.

## 🛠️ Technologies Used

- **Language:** Python
- **Library:** `requests` for making API calls.
- **External API:** WeatherAPI.com

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system.
- An API key from **WeatherAPI.com**.

### Installation

1.  Clone this repository:
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  Install the required Python library:
    ```bash
    pip install requests
    ```

### Configuration

1.  Open the `weather.py` file.
2.  Replace the placeholder API key with your actual key from WeatherAPI.com:
    ```python
    API_KEY = "your_actual_api_key_here"
    ```

### Running the Application

To run the application, execute the following command in your terminal:

```bash
python weather.py
