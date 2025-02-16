import pybreaker
import requests

# Create a circuit breaker
breaker = pybreaker.CircuitBreaker(fail_max=3, reset_timeout=60)

@breaker
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

try:
    data = fetch_data("https://api.example.com/data")
    print(data)
except pybreaker.CircuitBreakerError:
    print("Service is currently unavailable. Please try again later.") 