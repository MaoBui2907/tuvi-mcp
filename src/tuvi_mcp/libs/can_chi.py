from lunar_python import Lunar, LunarYear
from datetime import datetime

CAN = {
    "甲": "Giáp",
    "乙": "Ất",
    "丙": "Bính",
    "丁": "Đinh",
    "戊": "Mậu",
    "己": "Kỷ",
    "庚": "Canh",
    "辛": "Tân",
    "壬": "Nhâm",
    "癸": "Quý",
}

CHI = {
    "子": "Tý",
    "丑": "Sửu",
    "寅": "Dần",
    "卯": "Mão",
    "辰": "Thìn",
    "巳": "Tỵ",
    "午": "Ngọ",
    "未": "Mùi",
    "申": "Thân",
    "酉": "Dậu",
    "戌": "Tuất",
    "亥": "Hợi",
}

LUC_DIEU_LIST = ["先胜", "友引", "先负", "佛灭", "大安", "赤口"]

LUC_DIEU = {
    "先胜": "Đại An",
    "友引": "Lưu Niên",
    "先负": "Tốc Hỷ",
    "佛灭": "Xích Khẩu",
    "大安": "Tiểu Cát",
    "赤口": "Không Vong",
}

HANH = {"金": "Kim", "木": "Mộc", "水": "Thủy", "火": "Hỏa", "土": "Thổ"}

TRUC = {
    "建": "Kiến",
    "除": "Trừ",
    "满": "Mãn",
    "平": "Bình",
    "定": "Định",
    "执": "Chấp",
    "破": "Phá",
    "危": "Nguy",
    "成": "Thành",
    "收": "Thu",
    "开": "Khai",
    "闭": "Bế",
}

NHI_THAP_BAT_TU = {
    # Phương Đông (Thanh Long)
    "角": "Giác",
    "亢": "Cang",
    "氐": "Đê",
    "房": "Phòng",
    "心": "Tâm",
    "尾": "Vĩ",
    "箕": "Cơ",
    # Phương Bắc (Huyền Vũ)
    "斗": "Đẩu",
    "牛": "Ngưu",
    "女": "Nữ",
    "虚": "Hư",
    "危": "Nguy",
    "室": "Thất",
    "壁": "Bích",
    # Phương Tây (Bạch Hổ)
    "奎": "Khuê",
    "娄": "Lâu",
    "胃": "Vị",
    "昴": "Mão",
    "毕": "Tất",
    "觜": "Chủy",
    "参": "Sâm",
    # Phương Nam (Chu Tước)
    "井": "Tỉnh",
    "鬼": "Quỷ",
    "柳": "Liễu",
    "星": "Tinh",
    "张": "Trương",
    "翼": "Dực",
    "轸": "Chẩn",
}

HUONG = {
    "震": "Đông",
    "巽": "Đông Nam",
    "离": "Nam",
    "坤": "Tây Nam",
    "兑": "Tây",
    "乾": "Tây Bắc",
    "坎": "Bắc",
    "艮": "Đông Bắc",
    "中": "Trung Cung",
}

TIET_KHI = {
    # Mùa Xuân
    "立春": "Lập Xuân (Bắt đầu mùa Xuân)",
    "雨水": "Vũ Thủy (Mưa ẩm)",
    "惊蛰": "Kinh Trập (Sâu nở)",
    "春分": "Xuân Phân (Giữa xuân)",
    "清明": "Thanh Minh (Trong sáng)",
    "谷雨": "Cốc Vũ (Mưa rào)",
    # Mùa Hạ
    "立夏": "Lập Hạ (Bắt đầu mùa Hè)",
    "小满": "Tiểu Mãn (Lũ nhỏ)",
    "芒种": "Mang Chủng (Chòm sao tua rua)",
    "夏至": "Hạ Chí (Giữa hè - Ngày dài nhất)",
    "小暑": "Tiểu Thử (Nắng nhẹ)",
    "大暑": "Đại Thử (Nắng oi)",
    # Mùa Thu
    "立秋": "Lập Thu (Bắt đầu mùa Thu)",
    "处暑": "Xử Thử (Mưa ngâu)",
    "白露": "Bạch Lộ (Nắng nhạt)",
    "秋分": "Thu Phân (Giữa thu)",
    "寒露": "Hàn Lộ (Mát mẻ)",
    "霜降": "Sương Giáng (Sương mù)",
    # Mùa Đông
    "立冬": "Lập Đông (Bắt đầu mùa Đông)",
    "小雪": "Tiểu Tuyết (Tuyết nhẹ)",
    "大雪": "Đại Tuyết (Tuyết dày)",
    "冬至": "Đông Chí (Giữa đông - Đêm dài nhất)",
    "小寒": "Tiểu Hàn (Rét nhẹ)",
    "大寒": "Đại Hàn (Rét đậm)",
}

NAP_AM = {
    "海中金": "Hải Trung Kim",
    "炉中火": "Lư Trung Hỏa",
    "大林木": "Đại Lâm Mộc",
    "路旁土": "Lộ Bàng Thổ",
    "剑锋金": "Kiếm Phong Kim",
    "山头火": "Sơn Đầu Hỏa",
    "涧下水": "Giản Hạ Thủy",
    "城头土": "Thành Đầu Thổ",
    "白蜡金": "Bạch Lạp Kim",
    "杨柳木": "Dương Liễu Mộc",
    "泉中水": "Tuyền Trung Thủy",
    "屋上土": "Ốc Thượng Thổ",
    "霹雳火": "Tích Lịch Hỏa",
    "松柏木": "Tùng Bách Mộc",
    "长流水": "Trường Lưu Thủy",
    "沙中金": "Sa Trung Kim",
    "山下火": "Sơn Hạ Hỏa",
    "平地木": "Bình Địa Mộc",
    "壁上土": "Bích Thượng Thổ",
    "金箔金": "Kim Bạch Kim",
    "覆灯火": "Phúc Đăng Hỏa",
    "天河水": "Thiên Hà Thủy",
    "大驿土": "Đại Trạch Thổ",
    "钗钏金": "Thoa Xuyến Kim",
    "桑柘木": "Tang Đố Mộc",
    "大溪水": "Đại Khê Thủy",
    "沙中土": "Sa Trung Thổ",
    "天上火": "Thiên Thượng Hỏa",
    "石榴木": "Thạch Lựu Mộc",
    "大海水": "Đại Hải Thủy"
}

QUAI_SO = {
    "坎": "Khảm",
    "坤": "Khôn",
    "震": "Chấn",
    "巽": "Tốn",
    "乾": "Càn",
    "兑": "Đoài",
    "艮": "Cấn",
    "离": "Ly",
}

def get_can_ngay(solar_date: datetime) -> str:
    """
    Get the can based on the solar date
    :param solar_date: The solar date in the format of YYYY-MM-DD
    :return: The can of the day in the format of CAN
    """
    lunar = Lunar.fromDate(solar_date)
    return CAN[lunar.getDayGan()]


def get_can_thang(solar_date: datetime) -> str:
    """
    Get the can based on the solar date
    :param solar_date: The solar date in the format of YYYY-MM-DD
    :return: The can of the month in the format of CAN
    """
    lunar = Lunar.fromDate(solar_date)
    return CAN[lunar.getMonthGan()]


def get_can_nam(solar_date: datetime) -> str:
    """
    Get the can based on the solar date
    :param solar_date: The solar date in the format of YYYY-MM-DD
    :return: The can of the year in the format of CAN
    """
    lunar = Lunar.fromDate(solar_date)
    return CAN[lunar.getYearGan()]


def get_chi_ngay(solar_date: datetime) -> str:
    """
    Get the chi based on the solar date
    :param solar_date: The solar date in the format of YYYY-MM-DD
    :return: The chi in the format of CHI
    """
    lunar = Lunar.fromDate(solar_date)
    return CHI[lunar.getDayZhi()]


def get_chi_thang(solar_date: datetime) -> str:
    """
    Get the chi based on the solar date
    :param solar_date: The solar date in the format of YYYY-MM-DD
    :return: The chi of the month in the format of CHI
    """
    lunar = Lunar.fromDate(solar_date)
    return CHI[lunar.getMonthZhi()]


def get_chi_nam(solar_date: datetime) -> str:
    """
    Get the chi based on the solar date
    :param solar_date: The solar date in the format of YYYY-MM-DD
    :return: The chi of the year in the format of CHI
    """
    lunar = Lunar.fromDate(solar_date)
    return CHI[lunar.getYearZhi()]


def get_hanh_ngay(solar_date: datetime) -> str:
    """
    Get the hanh based on the solar date
    :param solar_date: The solar date in the format of YYYY-MM-DD
    :return: The hanh in the format of HANH
    """
    lunar = Lunar.fromDate(solar_date)
    return HANH[lunar.getDayNaYin()[-1]]

def get_hanh_thang(solar_date: datetime) -> str:
    """
    Get the hanh based on the solar date
    :param solar_date: The solar date in the format of YYYY-MM-DD
    :return: The hanh in the format of HANH
    """
    lunar = Lunar.fromDate(solar_date)
    return HANH[lunar.getMonthNaYin()[-1]]

def get_hanh_nam(solar_date: datetime) -> str:
    """
    Get the hanh based on the solar date
    :param solar_date: The solar date in the format of YYYY-MM-DD
    :return: The hanh in the format of HANH
    """
    lunar = Lunar.fromDate(solar_date)
    return HANH[lunar.getYearNaYin()[-1]]

def get_truc_day(solar_date: datetime) -> str:
    """
    Get the truc based on the solar date
    :param solar_date: The solar date in the format of YYYY-MM-DD
    :return: The truc in the format of TRUC
    """
    lunar = Lunar.fromDate(solar_date)
    return TRUC[lunar.getZhiXing()]


def get_huong_tai_than(solar_date: datetime) -> str:
    """
    Get the huong tai than based on the solar date
    :param solar_date: The solar date in the format of YYYY-MM-DD
    :return: The huong tai than in the format of HUONG
    """
    lunar = Lunar.fromDate(solar_date)
    return HUONG[lunar.getDayPositionCai()]


def get_huong_hy_than(solar_date: datetime) -> str:
    """
    Get the huong hy than based on the solar date
    :param solar_date: The solar date in the format of YYYY-MM-DD
    :return: The huong hy than in the format of HUONG
    """
    lunar = Lunar.fromDate(solar_date)
    return HUONG[lunar.getDayPositionXi()]


def get_huong_quy_nhan(solar_date: datetime) -> str:
    """
    Get the huong quy nhan based on the solar date
    :param solar_date: The solar date in the format of YYYY-MM-DD
    :return: The huong quy nhan in the format of HUONG
    """
    lunar = Lunar.fromDate(solar_date)
    return HUONG[lunar.getDayPositionYangGui()]


def get_tiet_khi(solar_date: datetime) -> str:
    """
    Get the tiet khi based on the solar date
    :param solar_date: The solar date in the format of YYYY-MM-DD
    :return: The tiet khi name
    """
    lunar = Lunar.fromDate(solar_date)
    tiet_khi = lunar.getCurrentJieQi()
    if tiet_khi is None:
        tiet_khi = lunar.getPrevJieQi()
        if tiet_khi is None:
            return "None"
        return "Đang trong tiết " + TIET_KHI[tiet_khi.getName()]
    return "Chính ngày " + TIET_KHI[tiet_khi.getName()]


def get_tinh_tu(solar_date: datetime) -> str:
    """
    Get the tinh tu based on the solar date
    :param solar_date: The solar date in the format of YYYY-MM-DD
    :return: The tinh tu in the format of NHI_THAP_BAT_TU
    """
    lunar = Lunar.fromDate(solar_date)
    return NHI_THAP_BAT_TU[lunar.getXiu()]


def get_luc_dieu(solar_date: datetime) -> str:
    """
    Get the luc dieu based on the solar date
    :param solar_date: The solar date in the format of YYYY-MM-DD
    :return: The luc dieu in the format of LUC_DIEU
    """
    lunar = Lunar.fromDate(solar_date)
    month = lunar.getMonth()
    year = lunar.getYear()
    day = lunar.getDay( )  
    
    # 1. Lấy thông tin năm âm lịch xem có nhuận tháng nào không
    nam_am = LunarYear.fromYear(year)
    thang_nhuan = nam_am.getLeapMonth() # Trả về 0 nếu không nhuận, trả về số tháng (ví dụ 6) nếu nhuận
    
    # 2. Tính số thứ tự thực tế của tháng
    # Mặc định số thứ tự = số tháng
    thang_thuc_te = month
    
    if thang_nhuan > 0:
        # Nếu tháng hiện tại lớn hơn tháng nhuận 
        # (Ví dụ: Nhuận tháng 6, đang là tháng 11 -> Thực tế là tháng thứ 12)
        if month > thang_nhuan:
            thang_thuc_te = month + 1
        
        # Nếu đang là chính cái tháng nhuận đó (Ví dụ đang ở tháng 6 nhuận)
        # Thì tùy phái, nhưng đa số các web sẽ tính là tháng tiếp theo (+1)
        elif month == thang_nhuan and lunar.isLeap():
            thang_thuc_te = month + 1

    # 3. Áp dụng công thức với tháng thực tế
    index = (thang_thuc_te + day - 2) % 6
    
    if index < 0:
        index += 6

    return LUC_DIEU[LUC_DIEU_LIST[index]]


def get_nap_am_year(solar_date: datetime) -> str:
    """
    Get the nap am based on the solar date
    :param solar_date: The solar date in the format of YYYY-MM-DD
    :return: The nap am in the format of NAP_AM
    """
    lunar = Lunar.fromDate(solar_date)
    return NAP_AM[lunar.getYearNaYin()]


def get_nap_am_month(solar_date: datetime) -> str:
    """
    Get the nap am based on the solar date
    :param solar_date: The solar date in the format of YYYY-MM-DD
    :return: The nap am in the format of NAP_AM
    """
    lunar = Lunar.fromDate(solar_date)
    return NAP_AM[lunar.getMonthNaYin()]


def get_nap_am_day(solar_date: datetime) -> str:
    """
    Get the nap am based on the solar date
    :param solar_date: The solar date in the format of YYYY-MM-DD
    :return: The nap am in the format of NAP_AM
    """
    lunar = Lunar.fromDate(solar_date)
    return NAP_AM[lunar.getDayNaYin()]

def get_gua(solar_date: datetime, gender: int = 1) -> str:
    """
    Get the gua based on the solar date
    :param solar_date: The solar date in the format of YYYY-MM-DD
    :param gender: The gender of the person, 1 for male, 0 for female
    :return: The gua in the format of GUA
    """
    lunar = Lunar.fromDate(solar_date)
    nam_sinh = lunar.getYear()
        
    # 1. Tính số thành
    while nam_sinh > 9:
        nam_sinh = sum(int(d) for d in str(nam_sinh))
    
    # 2. Tính quái số theo giới tính
    if gender == 1: # Nam
        quai_so = 11 - nam_sinh
    else: # Nữ
        quai_so = 4 + nam_sinh
        
    quai_so = sum(int(d) for d in str(quai_so))
    
    # 3. Xử lý trường hợp Trung Cung (Số 5)
    if quai_so == 5:
        if gender == 1: 
            quai_so = 2
        else: 
            quai_so = 8
        
    map_so_han = {
        1: "坎", 2: "坤", 3: "震", 4: "巽", 
        6: "乾", 7: "兑", 8: "艮", 9: "离"
    }
    
    return QUAI_SO[map_so_han.get(quai_so, "")]