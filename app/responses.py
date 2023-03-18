"""
Function extracting values from API response
"""
from datetime import datetime, timedelta

from transformations.solar_radiation import cloudcoverage_to_solarradiation
from config import TIME_SERIES_HOURS, VALUES


def weather_response(weather_data: dict) -> list:
    """
    Extracts the relevant values from the 7timer response and
    transforms it to a desireable result
    Aruments:
        response: API response from 7timer API
    Returns:
        time_series: time series with required values for API call
    """

    time_series = []
    series_start_time = datetime.strptime(weather_data["init"], "%Y%m%d%H")

    for measurement in weather_data["dataseries"]:
        # Check if the time series already contains required time interval
        if measurement["timepoint"] > TIME_SERIES_HOURS:
            break

        # Calculate end- and start period of time series interval
        end_period_utc = series_start_time + timedelta(hours=measurement["timepoint"])
        start_period_utc = end_period_utc - timedelta(hours=3)

        # Get the relevant literal data from API response
        series = {key: measurement[key] for key in VALUES}

        # Update series with periods & append to list
        series.update(
            {
                "start_period_utc": start_period_utc.strftime("%Y%m%d%H"),
                "end_period_utc": end_period_utc.strftime("%Y%m%d%H"),
                "solar_radiation": cloudcoverage_to_solarradiation(
                    measurement["cloudcover"]
                ),
            }
        )
        time_series.append(series)
    return time_series
