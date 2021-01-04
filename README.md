# Benford's Law Application

This application asks the user for a file and a column header and plots the distribution
of the leading digit for the specified column.

# To build the application run the following commands:

cd src
docker image build -t benford-app .
docker run -p 5001:5000 -d benford-app

# Accessing the application

Navigate to http://localhost:5001/ to access the application.
