"""
Source: https://scool.larc.nasa.gov/lesson_plans/CloudCoverSolarRadiation.pdf (NASA)
"""

# Conversion table for cloud coverage to percentage (average %)
TO_PERCENTAGE = {
    1: 0.03,
    2: 0.125,
    3: 0.25,
    4: 0.375,
    5: 0.5,
    6: 0.625,
    7: 0.75,
    8: 0.875,
    9: 0.97,
}


def cloudcoverage_to_solarradiation(cloud_coverage: int) -> float:
    """
    Converts cloud coverage from 7timer to solar radiation in Watts/m2
    Using the formula P = 990*(1-0.75F^3)
    Arguments:
        cloud_coverage: 7timer cloud coverage integer
    Returns:
        solar_radiation: Watts per m2
    """

    cloud_percentage = TO_PERCENTAGE[cloud_coverage]
    # Calculate solar radiation
    solar_radiation = 990 * (1 - 0.75 * cloud_percentage**3)
    return solar_radiation
