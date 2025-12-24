from datetime import datetime
from tuvi_mcp.libs.can_chi import get_can_ngay, get_can_nam, get_chi_ngay, get_chi_nam, get_hanh_nam, get_hanh_ngay

# 1. QUAN HỆ NGŨ HÀNH (Sinh/Khắc)
NGU_HANH_RELATION = {
    "Kim": {"sinh": "Thủy", "khac": "Mộc", "bi_sinh": "Thổ", "bi_khac": "Hỏa"},
    "Mộc": {"sinh": "Hỏa", "khac": "Thổ", "bi_sinh": "Thủy", "bi_khac": "Kim"},
    "Thủy": {"sinh": "Mộc", "khac": "Hỏa", "bi_sinh": "Kim", "bi_khac": "Thổ"},
    "Hỏa": {"sinh": "Thổ", "khac": "Kim", "bi_sinh": "Mộc", "bi_khac": "Thủy"},
    "Thổ": {"sinh": "Kim", "khac": "Thủy", "bi_sinh": "Hỏa", "bi_khac": "Mộc"}
}

# 2. QUAN HỆ ĐỊA CHI (Xung/Hợp của 12 con giáp)
# Đây là phần quan trọng nhất
DIA_CHI_RELATION = {
    "Tý": {"nhi_hop": "Sửu", "tam_hop": ["Thân", "Thìn"], "xung": "Ngọ", "hai": "Mùi", "hinh": "Mão"},
    "Sửu": {"nhi_hop": "Tý", "tam_hop": ["Tỵ", "Dậu"], "xung": "Mùi", "hai": "Ngọ", "hinh": "Tuất"},
    "Dần": {"nhi_hop": "Hợi", "tam_hop": ["Ngọ", "Tuất"], "xung": "Thân", "hai": "Tỵ", "hinh": "Tỵ"},
    "Mão": {"nhi_hop": "Tuất", "tam_hop": ["Hợi", "Mùi"], "xung": "Dậu", "hai": "Thìn", "hinh": "Tý"},
    "Thìn": {"nhi_hop": "Dậu", "tam_hop": ["Thân", "Tý"], "xung": "Tuất", "hai": "Mão", "hinh": "Thìn"},
    "Tỵ": {"nhi_hop": "Thân", "tam_hop": ["Dậu", "Sửu"], "xung": "Hợi", "hai": "Dần", "hinh": "Thân"},
    "Ngọ": {"nhi_hop": "Mùi", "tam_hop": ["Dần", "Tuất"], "xung": "Tý", "hai": "Sửu", "hinh": "Ngọ"},
    "Mùi": {"nhi_hop": "Ngọ", "tam_hop": ["Hợi", "Mão"], "xung": "Sửu", "hai": "Tý", "hinh": "Tuất"},
    "Thân": {"nhi_hop": "Tỵ", "tam_hop": ["Tý", "Thìn"], "xung": "Dần", "hai": "Hợi", "hinh": "Dần"},
    "Dậu": {"nhi_hop": "Thìn", "tam_hop": ["Tỵ", "Sửu"], "xung": "Mão", "hai": "Tuất", "hinh": "Dậu"},
    "Tuất": {"nhi_hop": "Mão", "tam_hop": ["Dần", "Ngọ"], "xung": "Thìn", "hai": "Dậu", "hinh": "Sửu"},
    "Hợi": {"nhi_hop": "Dần", "tam_hop": ["Mão", "Mùi"], "xung": "Tỵ", "hai": "Thân", "hinh": "Hợi"}
}

# 3. QUAN HỆ THIÊN CAN (Hợp/Phá)
THIEN_CAN_RELATION = {
    "Giáp": {"hop": "Kỷ", "pha": ["Mậu", "Canh"]},
    "Ất": {"hop": "Canh", "pha": ["Kỷ", "Tân"]},
    "Bính": {"hop": "Tân", "pha": ["Canh", "Nhâm"]},
    "Đinh": {"hop": "Nhâm", "pha": ["Tân", "Quý"]},
    "Mậu": {"hop": "Quý", "pha": ["Nhâm", "Giáp"]},
    "Kỷ": {"hop": "Giáp", "pha": ["Quý", "Ất"]},
    "Canh": {"hop": "Ất", "pha": ["Giáp", "Bính"]},
    "Tân": {"hop": "Bính", "pha": ["Ất", "Đinh"]},
    "Nhâm": {"hop": "Đinh", "pha": ["Bính", "Mậu"]},
    "Quý": {"hop": "Mậu", "pha": ["Đinh", "Kỷ"]}
}

def get_can_relation(date_of_birth: datetime, forecast_day: datetime) -> str:
    """
    Get the can relation based on the date of birth and the forecast day
    :param date_of_birth: The date of birth in the format of datetime
    :param forecast_day: The day to forecast the fortune for, in the format of datetime
    :return: The can relation in the format of 2 (Hợp), -2 (Phá), 0 (Không hợp không phá)
    """
    can_tuoi = get_can_nam(date_of_birth)
    can_ngay = get_can_ngay(forecast_day)
    
    relation_can = THIEN_CAN_RELATION[can_tuoi]
    if can_ngay == relation_can["hop"]:
        return {
            "relation": 2,
            "description": f"Tương Hợp (Tốt): {can_tuoi} hợp {can_ngay}"
        }
    elif can_ngay in relation_can["pha"]:
        return {
            "relation": -2,
            "description": f"Tương Phá (Xấu): {can_tuoi} phá {can_ngay}"
        }
    else:
        return {
            "relation": 0,
            "description": f"Bình hòa: {can_tuoi} và {can_ngay} không có tương hợp hoặc tương phá"
        }
    

def get_chi_relation(date_of_birth: datetime, forecast_day: datetime) -> str:
    """
    Get the chi relation based on the date of birth and the forecast day
    :param date_of_birth: The date of birth in the format of datetime
    :param forecast_day: The day to forecast the fortune for, in the format of datetime
    :return: The chi relation in the format of 2 (Nhị Hợp, Tam Hợp), -2 (Lục Xung), -1 (Hại, Hình), 0 (Không hợp không phá)
    """
    chi_tuoi = get_chi_nam(date_of_birth)
    chi_ngay = get_chi_ngay(forecast_day)
    relation_chi = DIA_CHI_RELATION[chi_tuoi]
    if chi_ngay == relation_chi["nhi_hop"]:
        return {
            "relation": 2,
            "description": f"Nhị Hợp (Rất Tốt): {chi_tuoi} nhị hợp {chi_ngay}"
        }
    elif chi_ngay in relation_chi["tam_hop"]:
        return {
            "relation": 2,
            "description": f"Tam Hợp (Rất Tốt): {chi_tuoi} tam hợp {chi_ngay}"
        }
    elif chi_ngay == relation_chi["xung"]:
        return {
            "relation": -2,
            "description": f"Lục Xung (Xấu): {chi_tuoi} lục xung {chi_ngay}"
        }
    elif chi_ngay == relation_chi["hai"]:
        return {
            "relation": -1,
            "description": f"Lục Hại (Xấu): {chi_tuoi} hại {chi_ngay}"
        }
    elif chi_ngay == relation_chi["hinh"]:
        return {
            "relation": -1,
            "description": f"Tương Hình (Xấu): {chi_tuoi} hình {chi_ngay}"
        }
    else:
        return {
            "relation": 0,
            "description": f"Bình hòa: {chi_tuoi} và {chi_ngay} không có tương hợp, tương phá, tương hình hoặc tương hại"
        }

def get_ngu_hanh_relation(date_of_birth: datetime, forecast_day: datetime) -> str:
    """
    Get the ngu hanh relation based on the date of birth and the forecast day
    :param date_of_birth: The date of birth in the format of datetime
    :param forecast_day: The day to forecast the fortune for, in the format of datetime
    :return: The ngu hanh relation in the format of 2 (Sinh), -2 (Khắc), 0.5 (Khắc xuất), -0.5 (Sinh xuất), 0 (Không sinh khắc)
    """
    ngu_hanh_tuoi = get_hanh_nam(date_of_birth)
    ngu_hanh_ngay = get_hanh_ngay(forecast_day)
    relation_ngu_hanh = NGU_HANH_RELATION[ngu_hanh_tuoi]
    if ngu_hanh_ngay == relation_ngu_hanh["bi_sinh"]:
        return {
            "relation": 2,
            "description": f"Tương Sinh (Rất Tốt): hành {ngu_hanh_ngay} sinh dưỡng cho mệnh {ngu_hanh_tuoi}"
        }
    elif ngu_hanh_ngay == relation_ngu_hanh["bi_khac"]:
        return {
            "relation": -2,
            "description": f"Tương Khắc (Rất Xấu): hành {ngu_hanh_ngay} khắc mệnh {ngu_hanh_tuoi}"
        }
    elif ngu_hanh_ngay == relation_ngu_hanh["sinh"]:
        return {
            "relation": -0.5,
            "description": f"Sinh Xuất (Hơi Xấu): mệnh {ngu_hanh_tuoi} sinh dưỡng cho hành {ngu_hanh_ngay}"
        }
    elif ngu_hanh_ngay == relation_ngu_hanh["khac"]:
        return {
            "relation": 0.5,
            "description": f"Khắc Xuất (Trung Bình): mệnh {ngu_hanh_tuoi} chế ngự hành {ngu_hanh_ngay}"
        }
    else:
        return {
            "relation": 0,
            "description": f"Tỷ hòa (Bình thường): mệnh {ngu_hanh_tuoi} và hành {ngu_hanh_ngay} không có tương sinh khắc"
        }
    
def get_xung_khac(date_of_birth: datetime, forecast_day: datetime) -> str:
    """
    Get the xung khac based on the date of birth and the forecast day
    :param date_of_birth: The date of birth in the format of YYYY-MM-DD
    :param forecast_day: The day to forecast the fortune for, in the format of YYYY-MM-DD
    :return: The xung khac in the format of XUNG_KHAC
    """
    can_relation = get_can_relation(date_of_birth, forecast_day)
    chi_relation = get_chi_relation(date_of_birth, forecast_day)
    ngu_hanh_relation = get_ngu_hanh_relation(date_of_birth, forecast_day)
    total_relation = can_relation["relation"] + chi_relation["relation"] + ngu_hanh_relation["relation"]
    total = {}
    if total_relation >= 3:
        total = {
            "relation": total_relation,
            "description": "Đại Cát (Rất Tốt)"
        }
    elif total_relation > 0:
        total = {
            "relation": total_relation,
            "description": "Tiểu Cát (Tốt)"
        }
    elif total_relation == 0:
        total = {
            "relation": total_relation,
            "description": "Bình Hòa"
        }
    elif total_relation < -3:
        total = {
            "relation": total_relation,
            "description": "Đại Hung (Rất Xấu)"
        }
    else:
        total = {
            "relation": total_relation,
            "description": "Tiểu Hung (Hơi Xấu)"
        }
    return {
        "can_relation": can_relation,
        "chi_relation": chi_relation,
        "ngu_hanh_relation": ngu_hanh_relation,
        "total_relation": total
    }