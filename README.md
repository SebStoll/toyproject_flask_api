# toyproject_flask_api

Toyproject which sets up a simple flask api.

## Tests

Test of GET request:

curl <server address>

Test of POST request:

curl -v -H "Content-Type: application/json" -X POST -d "{\"LSTAT\": \"10\"}" <server address>/predict

(LSTAT=5 should give 29.80359411, LSTAT=10 should give 25.05334734)
