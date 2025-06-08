from prometheus_client import start_http_server, Summary
import time
import subprocess

# Metric to capture test execution time
TEST_DURATION = Summary('pytest_execution_seconds', 'Time spent running pytest')

@TEST_DURATION.time()
def run_pytest():
    # Run pytest and return exit code
    return subprocess.call(['pytest'])

if __name__ == '__main__':
    # Start Prometheus metrics server on port 8000
    start_http_server(8000)
    print("Prometheus exporter running on http://0.0.0.0:8000")

    # Run tests once and keep the container alive for Prometheus to scrape
    code = run_pytest()
    while True:
        time.sleep(10)  # Keeps container alive to serve metrics
