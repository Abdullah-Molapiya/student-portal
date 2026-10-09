from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

myapp = Flask(__name__)
REQUEST_COUNT = Counter(
    'student_app_request_total',
    'Total number of request to Student Portal',
    ['endpoint']
)

@myapp.route('/')
def home_page():
    REQUEST_COUNT.labels(endpoint='/').inc()
    return """
    <h1>Welcome to Student Portal Home Page</h1>
    """

@myapp.route('/about')
def home_page():
    REQUEST_COUNT.labels(endpoint='/about').inc()
    return """
    <h1>Welcome to About Page</h1>
    """

@myapp.route('/contact')
def contact():
    REQUEST_COUNT.labels(endpoint='/').inc()
    return """
    <h1>Welcome to Student Portal Home Page</h1>
    """

@myapp.route('/metrics')
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )


if __name__ == '__main__':
    myapp.run('0.0.0.0', port=5000)
    
