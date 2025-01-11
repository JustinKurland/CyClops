# CyCAD

## Overview
CyCAD is a Python-based project for threat intelligence and analytics.

## Setup
1. Clone the repository.
2. Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Structure
- `docs/`: Documentation for the project.
- `tests/`: Unit and integration tests.
- `src/cycad/`: Source code, including modules and the orchestrator.

## Running
To run the orchestrator:
```bash
python src/cycad/orchestrator.py
