"""
FastAPI application calling 7timer to fetch weather information
Author: Luuk Dijkhuizen
e-mail: luuk@lddata.nl
"""

import httpx
import uvicorn
from fastapi import FastAPI, Query, Depends
from fastapi.responses import JSONResponse

from config import UNIT, OUTPUT
from responses import weather_response


URL = "https://www.7timer.info/bin/astro.php"

app = FastAPI()


async def get_client():
    """
    Creates new client for each request and yields it to get_weather
    Automatically closes the client after response.
    """
    async with httpx.AsyncClient() as client:
        yield client


@app.get("/weather")
async def get_weather(
    lon: float = Query(ge=-90, le=90),
    lat: float = Query(ge=-180, le=180),
    client: httpx.AsyncClient = Depends(get_client),
) -> JSONResponse:
    """
    API endpoint receiving coordinates and returning a JSON with weather info
    Arguments:
        lon: longitude (WGS84), allows float between -90 and 90
        lat: latitude (WGS84), allows float -180 and 180
        client: httpx client for connection, FastAPI Dependency
    """
    # API call to 7timer
    response = await client.get(
        URL,
        params={"lon": lon, "lat": lat, "unit": UNIT, "output": OUTPUT},
    )
    # Transform API response into required time series
    time_series = weather_response(response.json())

    return JSONResponse(content=time_series)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
