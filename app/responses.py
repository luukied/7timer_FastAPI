"""
Function extracting values from API response
"""
from datetime import datetime, timedelta

from transformations.solar_radiation import cloudcoverage_to_solarradiation
from config import TIME_SERIES_HOURS, VALUES


# Keys from 7timer response
INIT = "init"
DATASERIES = "dataseries"

# Custom datapoint variables
TIMEPOINT = "timepoint"
START_PERIOD_UTC = "start_period_utc"
END_PERIOD_UTC = "end_period_utc"
CLOUD_COVER = "cloudcover"
SOLAR_RADIATION = "solar_radiation"


def weather_response(response: dict) -> list:
    """
    Extracts the relevant values from the 7timer response and
    transforms it to a desireable result
    Aruments:
        response: API response from 7timer API
    Returns:
        time_series: time series with required values for API call
    """

    time_series = []
    series_start_time = datetime.strptime(response[INIT], "%Y%m%d%H")

    for item in response[DATASERIES]:
        # Check if the time series already contains required time interval
        if item[TIMEPOINT] > TIME_SERIES_HOURS:
            break

        # Calculate end- and start period of time series interval
        end_period_utc = series_start_time + timedelta(hours=item[TIMEPOINT])
        start_period_utc = end_period_utc - timedelta(hours=3)

        # Get the relevant literal data from API response
        series = {key: item[key] for key in VALUES}

        # Update series with periods & append to list
        series.update(
            {
                START_PERIOD_UTC: start_period_utc.strftime("%Y%m%d%H"),
                END_PERIOD_UTC: end_period_utc.strftime("%Y%m%d%H"),
                SOLAR_RADIATION: cloudcoverage_to_solarradiation(
                    item[CLOUD_COVER]
                ),
            }
        )
        time_series.append(series)
    return time_series
