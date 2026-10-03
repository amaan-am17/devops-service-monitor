# DevOps Service Monitor

A simple Python-based monitoring tool that checks both system connectivity and API health.

## Features

- Checks system connectivity using `ping`
- Checks API availability using HTTP requests
- Handles command execution errors
- Handles API/network errors
- Uses a 5-second API timeout
- Provides individual system and API health status
- Calculates an overall health status

## Technologies

- Python
- subprocess
- requests
- HTTP APIs

## How to Run

Install the required dependency:

```bash
pip install requests