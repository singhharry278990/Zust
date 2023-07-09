// Check if the Geolocation API is supported by the browser
if (navigator.geolocation) {
  // Get the user's current position
  navigator.geolocation.getCurrentPosition(getWeatherData, handleLocationError);
} else {
  // Geolocation is not supported by the browser
  console.log("Geolocation is not supported by this browser.");
}

// Callback function to handle the retrieved position
function getWeatherData(position) {
  // Retrieve the latitude and longitude coordinates
  var latitude = position.coords.latitude;
  var longitude = position.coords.longitude;

  // Call the weather API with the coordinates
  var apiUrl = `https://api.weatherapi.com/v1/current.json?key=310670bf6c2e4165a1b132750230907&q=${latitude},${longitude}&aqi=no`;

  // Make an HTTP request to the weather API
  fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
      // Process the weather data
      console.log("Weather data:", data);
      displayWeatherData(data);
    })
    .catch(error => {
      console.log("Error fetching weather data:", error);
    });
}

// Function to display weather data in a container
function displayWeatherData(weatherData) {
  // Get the container element
  var container = document.getElementById('weather-container1');

  // Create elements to display the weather information
  var locationElement = document.createElement('div');
  locationElement.textContent = `${weatherData.location.name}, ${weatherData.location.country}`;
  container.appendChild(locationElement);

  var temperatureElement = document.createElement('div');
  temperatureElement.textContent = weatherData.current.temp_c + '°C';
  container.appendChild(temperatureElement);

  // Example styling
  container.style.backgroundColor = '#f2f2f2';
  container.style.padding = '20px';
  container.style.borderRadius = '10px';
  container.style.fontSize = '24px';
  container.style.fontWeight = 'bold';

  // You can add more CSS properties to customize the styling
}

// Error handling function for geolocation errors
function handleLocationError(error) {
  switch (error.code) {
    case error.PERMISSION_DENIED:
      console.log("User denied the request for Geolocation.");
      break;
    case error.POSITION_UNAVAILABLE:
      console.log("Location information is unavailable.");
      break;
    case error.TIMEOUT:
      console.log("The request to get user location timed out.");
      break;
    case error.UNKNOWN_ERROR:
      console.log("An unknown error occurred.");
      break;
  }
}

  document.getElementById('weather-btn').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent the default form submission behavior
  
    // Get the input values
    var country = document.getElementById('country').value;
    var forecastDays = document.getElementById('forecast_days').value;
    var temperatureUnit = document.getElementById('temperature').value;
    $.ajax({
      url: 'https://api.weatherapi.com/v1/forecast.json',
      data: {
        key: '310670bf6c2e4165a1b132750230907',
        q: country,
        days: forecastDays,
        units: temperatureUnit
      },
      dataType: 'json',
      success: function(apiResponse) {
        console.log(apiResponse)
        // Create weather display HTML structure dynamically
        var weatherDisplay = document.createElement('div');
        weatherDisplay.className = 'weather_animated';
  
        var locationElement = document.createElement('div');
        locationElement.className = 'location';
        var locationSpan = document.createElement('span');
        locationSpan.dataset.api = 'location';
        locationSpan.textContent = apiResponse.location.name;
        locationElement.appendChild(locationSpan);
        weatherDisplay.appendChild(locationElement);

        var locationElement1 = document.createElement('div');
        locationElement1.className = 'location';
        var locationSpan1 = document.createElement('span');
        locationSpan1.dataset.api = 'location';
        locationSpan1.textContent = apiResponse.location.country;
        locationElement1.appendChild(locationSpan1);
        weatherDisplay.appendChild(locationElement1);
  
        var mainLeftElement = document.createElement('div');
        mainLeftElement.className = 'main_left';
        var mainIcon = document.createElement('i');
        mainIcon.dataset.api = 'current_icon';
        mainIcon.className = apiResponse.current.condition.code;
        var mainDescr = document.createElement('span');
        mainDescr.dataset.api = 'current_main_descr';
        mainDescr.textContent = apiResponse.current.condition.text;
        mainLeftElement.appendChild(mainIcon);
        mainLeftElement.appendChild(mainDescr);
        weatherDisplay.appendChild(mainLeftElement);
  
        var mainRightElement = document.createElement('div');
        mainRightElement.className = 'main_right';
        var windSpeed = document.createElement('span');
        windSpeed.className = 'wind';
        windSpeed.dataset.api = 'current_wind_speed';
        windSpeed.textContent = 'Wind: ' + apiResponse.current.wind_kph + ' km/h';
        var precip = document.createElement('span');
        precip.className = 'precip';
        precip.dataset.api = 'current_precip';
        precip.textContent = 'Precip: ' + apiResponse.current.precip_mm + ' mm';
        var pressure = document.createElement('span');
        pressure.className = 'pressure';
        pressure.dataset.api = 'current_pressure';
        pressure.textContent = 'Pressure: ' + apiResponse.current.pressure_mb + ' mb';
        var temperature = document.createElement('span');
        temperature.className = 'temperature';
        temperature.dataset.api = 'current_temperature';
        temperature.textContent = apiResponse.current.temp_c + '°C';
        mainRightElement.appendChild(windSpeed);
        mainRightElement.appendChild(precip);
        mainRightElement.appendChild(pressure);
        mainRightElement.appendChild(temperature);
        weatherDisplay.appendChild(mainRightElement);
  
        var forecastWeekElement = document.createElement('div');
        forecastWeekElement.dataset.api = 'forecast_week';
        forecastWeekElement.className = 'week';
        apiResponse.forecast.forecastday.forEach(function(forecastDay) {
          var dayElement = document.createElement('div');
          dayElement.className = 'day';
  
          var nameElement = document.createElement('span');
          nameElement.className = 'name';
          nameElement.textContent = forecastDay.date;
          dayElement.appendChild(nameElement);
  
          var iconElement = document.createElement('i');
          iconElement.className = forecastDay.day.condition.code;
          dayElement.appendChild(iconElement);
  
          var temperatureElement = document.createElement('span');
          temperatureElement.className = 'temperature';
          temperatureElement.textContent = forecastDay.day.avgtemp_c + '°C';
          dayElement.appendChild(temperatureElement);
  
          forecastWeekElement.appendChild(dayElement);
        });
        weatherDisplay.appendChild(forecastWeekElement);
        var styleElement = document.createElement('style');
        styleElement.textContent = `
        .weather_animated {
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          background-color: #f2f2f2;
          padding: 20px;
          border-radius: 10px;
        }
        
        .location-name {
          font-size: 24px;
          font-weight: bold;
          margin-bottom: 10px;
        }
        
        .main_left {
          display: flex;
          flex-direction: column;
          align-items: center;
          margin-bottom: 20px;
        }
        
        .main_left i {
          font-size: 50px;
        }
        
        .main_left span {
          font-size: 16px;
          margin-top: 10px;
        }
        
        .main_right span {
          display: block;
          font-size: 16px;
          margin-bottom: 10px;
        }
        
        .week {
          display: flex;
          justify-content: space-between;
        }
        
        .day {
          display: flex;
          flex-direction: column;
          align-items: center;
          text-align: center;
        }
        
        .day .name {
          font-size: 16px;
          font-weight: bold;
          margin-bottom: 5px;
        }
        
        .day i {
          font-size: 30px;
          margin-bottom: 5px;
        }
        
        .day .temperature {
          font-size: 16px;
        }
        
          `;
        weatherDisplay.appendChild(styleElement);
  
  
        // Append the weather display to a container element
        var container = document.getElementById('weather-container');
        container.innerHTML = ''; // Clear previous weather display
        container.appendChild(weatherDisplay);
        
      }
    });
  });
  