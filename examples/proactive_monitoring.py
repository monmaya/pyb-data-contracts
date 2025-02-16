import time
import random

def collect_metrics():
    # Simulate collecting metrics
    return {
        "latency": random.uniform(0.1, 0.5),
        "error_rate": random.uniform(0.0, 0.1),
        "throughput": random.randint(100, 500)
    }

def analyze_metrics(metrics):
    if metrics["latency"] > 0.3:
        print("Warning: High latency detected!")
    if metrics["error_rate"] > 0.05:
        print("Warning: High error rate detected!")
    if metrics["throughput"] < 150:
        print("Warning: Low throughput detected!")

def monitor_service():
    while True:
        metrics = collect_metrics()
        analyze_metrics(metrics)
        time.sleep(5)

if __name__ == "__main__":
    monitor_service() 