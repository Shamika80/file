def parse_temperature(text):
  """Parses a temperature string (e.g., "5°C") and returns the numerical value."""
  return float(text.split("°")[0])  

def calculate_average_temperature(data):
  """Calculates the average temperature from a list of temperature data."""
  if not data:
    return None  
  temperatures = [parse_temperature(entry) for entry in data]
  return sum(temperatures) / len(temperatures)

def analyze_weather_data(filenames):
  """Analyzes weather data from multiple files, calculates average temperatures, and identifies the year with the highest average."""
  year_averages = {}
  highest_average_year = None
  highest_average = float('-inf')  

  for filename in filenames:
    year = filename.split("_")[1]  
    temperatures = []
    try:
      with open(filename, 'r') as file:
        for line in file:
          data = line.strip().split(",")  
          if len(data) == 2:  
            temperatures.append(data[1])  
    except FileNotFoundError:
      print(f"Error: File not found: {filename}")
      continue

    average_temp = calculate_average_temperature(temperatures)
    year_averages[year] = average_temp

    if average_temp > highest_average:
      highest_average = average_temp
      highest_average_year = year

  return year_averages, highest_average_year, highest_average

if __name__ == "__main__":
  filenames = ["weather_2020.txt", "weather_2021.txt", ...]  
  print("Average Temperatures by Year:")
  for year, average in "year_averages.items()":
    print(f"{year}: {average:.2f}°C")

  print(f"\nYear with Highest Average Temperature: {"highest_average_year"} ("{highest_average:.2f}°C)")