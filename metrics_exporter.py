from prometheus_client import start_http_server, Summary, Counter, Gauge, generate_latest
import time
import subprocess
import json
import sys
from flask import Flask, Response

app = Flask(__name__)

# Prometheus metrics
TEST_DURATION = Summary('pytest_execution_seconds', 'Time spent running pytest')
TEST_COUNT = Counter('pytest_total_tests', 'Total number of tests run')
TEST_PASSED = Counter('pytest_tests_passed', 'Number of tests passed')
TEST_FAILED = Counter('pytest_tests_failed', 'Number of tests failed')
TEST_SUCCESS_RATE = Gauge('pytest_success_rate', 'Test success rate percentage')

@TEST_DURATION.time()
def run_pytest():
    """Run pytest and capture metrics"""
    try:
        # Run pytest with JSON output
        result = subprocess.run([
            'pytest', '--tb=short', '--quiet', 
            '--json-report', '--json-report-file=test_results.json'
        ], capture_output=True, text=True, cwd='/app')
        
        # Parse results if JSON report exists
        try:
            with open('/app/test_results.json', 'r') as f:
                report = json.load(f)
                
            total_tests = report['summary']['total']
            passed_tests = report['summary'].get('passed', 0)
            failed_tests = report['summary'].get('failed', 0)
            
            # Update metrics
            TEST_COUNT.inc(total_tests)
            TEST_PASSED.inc(passed_tests)
            TEST_FAILED.inc(failed_tests)
            
            if total_tests > 0:
                success_rate = (passed_tests / total_tests) * 100
                TEST_SUCCESS_RATE.set(success_rate)
            
            print(f"Tests: {total_tests}, Passed: {passed_tests}, Failed: {failed_tests}")
            
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            print(f"Could not parse test results: {e}")
            # Fallback: just count based on exit code
            if result.returncode == 0:
                TEST_COUNT.inc(1)
                TEST_PASSED.inc(1)
                TEST_SUCCESS_RATE.set(100)
            else:
                TEST_COUNT.inc(1)
                TEST_FAILED.inc(1)
                TEST_SUCCESS_RATE.set(0)
        
        return result.returncode
        
    except Exception as e:
        print(f"Error running pytest: {e}")
        TEST_FAILED.inc(1)
        return 1

@app.route('/metrics')
def metrics():
    """Endpoint for Prometheus to scrape metrics"""
    return Response(generate_latest(), mimetype='text/plain')

@app.route('/health')
def health():
    """Health check endpoint"""
    return {'status': 'healthy', 'service': 'pytest-exporter'}

@app.route('/run-tests')
def run_tests_endpoint():
    """Endpoint to trigger test run"""
    exit_code = run_pytest()
    return {'exit_code': exit_code, 'status': 'completed'}

if __name__ == '__main__':
    print("Starting PyTest Prometheus Exporter...")
    print("Prometheus metrics available at: http://0.0.0.0:8000/metrics")
    print("Health check at: http://0.0.0.0:8000/health")
    print("Trigger tests at: http://0.0.0.0:8000/run-tests")
    
    # Run tests once on startup
    print("Running initial test suite...")
    run_pytest()
    
    # Start Flask server for metrics
    app.run(host='0.0.0.0', port=8000, debug=False)