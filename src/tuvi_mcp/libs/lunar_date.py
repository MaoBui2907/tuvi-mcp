from datetime import datetime
from lunar_python import Lunar

# Leap month will have a (-) - negative value

def get_lunar_date(solar_date: datetime) -> str:
    """
    Get the lunar date based on the solar date
    :param solar_date: The solar date in the format of YYYY-MM-DD
    :return: The lunar date string in the format of YYYY-MM-DD
    """
    lunar_date = Lunar.fromDate(solar_date)
    lunar_date_string = f"{lunar_date.getYear()}-{lunar_date.getMonth()}-{lunar_date.getDay()}"
    return lunar_date_string


def get_solar_date(lunar_date: str) -> datetime:
    """
    Get the solar date based on the lunar date
    :param lunar_date: The lunar date in the format of YYYY-MM-DD or YYYY-(-MM)-DD
    :return: The solar date in the format of datetime
    """
    # Handle both formats: YYYY-MM-DD and YYYY-(-MM)-DD
    if lunar_date.count("(") > 0:
        # Leap month format: YYYY-(-MM)-DD
        import re
        match = re.match(r"(\d{4})-\((-?\d{1,2})\)-(\d{1,2})", lunar_date)
        if match:
            year = int(match.group(1))
            month = int(match.group(2))  # Negative for leap month
            day = int(match.group(3))
        else:
            raise ValueError(f"Invalid leap month format: {lunar_date}")
    else:
        # Regular format: YYYY-MM-DD
        parts = lunar_date.split("-")
        if len(parts) != 3:
            raise ValueError(f"Invalid lunar date format: {lunar_date}")
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])

    lunar = Lunar.fromYmd(year, month, day)
    return lunar.getSolar()

if __name__ == "__main__":
    today = datetime.now()
    lunar_date = get_lunar_date(today)

    print(today)
    print(lunar_date)
    print(get_solar_date(lunar_date))

