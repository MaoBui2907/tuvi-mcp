from datetime import datetime
from libs.lunar_date import get_lunar_date
from libs.can_chi import get_tinh_tu, get_truc_day, get_luc_dieu, get_nap_am_year, get_nap_am_month, get_nap_am_day
from libs.khuyen import NHI_THAP_BAT_TU_KHUYEN, THAP_NHI_KIEN_TRU_KHUYEN, LUC_DIEU_KHUYEN

if __name__ == "__main__":
    # day_date = datetime.fromisoformat("2026-02-04")
    day_date = datetime.now()
    lunar_date = get_lunar_date(day_date)
    print(lunar_date)
    print(get_nap_am_year(day_date))
    print(get_nap_am_month(day_date))
    print(get_nap_am_day(day_date))