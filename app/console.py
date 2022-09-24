"""This must be run as a module not a script to find the dependencies. 
AKA run with python3 -m app.console"""

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.api.v1.endpoints.plant:app", host="0.0.0.0", port=8000)
