# toyproject_flask_api

Toyproject which sets up a simple flask api.

## Tests

Test of GET request (address and port may vary):

curl http://127.0.0.1:5000/

Test of POST request (address and port may vary):

curl -v -H "Content-Type: application/json" -X POST -d "{\"LSTAT\": \"10\"}" http://127.0.0.1:5000/predict

(LSTAT=5 should give 29.80359411, LSTAT=10 should give 25.05334734)
