# config-server-example

## Overview
This project consists of two Flask-based microservices:

1. **Config Server (Service 1)**: Serves configuration data based on service names.
2. **Application Server (Service 2)**: Fetches configurations from the Config Server and updates its local cache. It also serves an HTML page based on the retrieved configuration.

## How It Works

### Service 1: Config Server
- Hosts a JSON-based configuration file (`config.json`).
- Exposes an endpoint: `/getConfig/<service_name>` to return configurations for a given service.
- Runs on port `5000`.

### Service 2: Application Server
- Fetches configuration from the Config Server.
- Exposes:
  - `/refreshConfig?service_name=<service_name>`: Updates the local cache by fetching the config for the given service.
  - `/homepage`: Serves an HTML page based on the config.
- Runs on port `5001`.

## How to Run

### Prerequisites
Ensure you have Python installed and Flask available:
```sh
pip install flask requests
```

### Running the Services

1. Start the Config Server:
   ```sh
   python config_server.py
   ```
2. Start the Application Server:
   ```sh
   python app_server.py
   ```

### Testing the Endpoints

1. Fetch a service configuration:
   ```sh
   curl http://localhost:5001/getConfig/example3
   ```

2. Refresh the config for a service:
   ```sh
   curl "http://localhost:5002/refreshConfig?service_name=example2"
   ```

3. Access the homepage:
   ```sh
   curl http://localhost:5002/homepage
   ```

### HTML Page
A simple HTML page (`index.html`) is included. It provides a form where users can enter a service name and submit it to `/refreshConfig`.
