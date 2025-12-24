from fastmcp import FastMCP
from datetime import datetime
from tuvi_mcp.libs.lunar_date import get_lunar_date
from tuvi_mcp.libs.can_chi import (
    get_can_nam,
    get_can_ngay,
    get_chi_nam,
    get_chi_ngay,
    get_hanh_nam,
    get_huong_tai_than,
    get_huong_hy_than,
    get_huong_quy_nhan,
    get_truc_day,
    get_tiet_khi,
    get_tinh_tu,
    get_luc_dieu,
    get_nap_am_year,
    get_nap_am_month,
    get_nap_am_day,
    get_gua,
)
from tuvi_mcp.libs.xung_khac import get_xung_khac
from tuvi_mcp.libs.khuyen import (
    PENGZU_CAN,
    PENGZU_CHI,
    NHI_THAP_BAT_TU_KHUYEN,
    PHAT_BAN_MENH,
    THAP_NHI_KIEN_TRU_KHUYEN,
    LUC_DIEU_KHUYEN,
    CUNG_PHI,
)
import argparse
import sys

mcp = FastMCP("TuVi MCP")


@mcp.tool()
def get_date_of_birth_detail(
    date_of_birth: str,
    gender: int = 1,
    format: str = "text"
) -> str:
    """
    Get the detail of the date of birth
    :param date_of_birth: The date of birth in the format of YYYY-MM-DD
    :param gender: The gender of the person, 1 for male, 0 for female
    :param format: The format to return the detail in, either "text" or "json", default is "text"
    :return: The detail of the date of birth in the format of text or json
    """
    try:
        date_of_birth = datetime.fromisoformat(date_of_birth)
        lunar_date = get_lunar_date(date_of_birth)
        can_tuoi = get_can_nam(date_of_birth)
        chi_tuoi = get_chi_nam(date_of_birth)
        ngu_hanh_tuoi = get_hanh_nam(date_of_birth)
        nap_am_tuoi = get_nap_am_year(date_of_birth)
        gua = get_gua(date_of_birth, gender)
        phat_do_mang = PHAT_BAN_MENH[chi_tuoi]
        cung_phi = CUNG_PHI[gua]

        if format == "text":
            return f"Sinh ngày {date_of_birth.strftime('%Y-%m-%d')} tức ngày {lunar_date} \nTuổi: {can_tuoi} {chi_tuoi} \nMệnh: {ngu_hanh_tuoi} ({nap_am_tuoi}) \nQuái: {cung_phi['ten']} \nPhật Đồ Mạng: {phat_do_mang} \nCung Phi: {cung_phi['nhom']} hướng tôt: {cung_phi['tot']}"
        elif format == "json":
            return {
                "lunar_date": lunar_date,
                "cung_phi": cung_phi,
                "phat_do_mang": phat_do_mang,
                "can_tuoi": can_tuoi,
                "chi_tuoi": chi_tuoi,
                "ngu_hanh_tuoi": ngu_hanh_tuoi,
                "nap_am_tuoi": nap_am_tuoi
            }
        else:
            return "Invalid format"
    except ValueError:
        return "Invalid date of birth"

@mcp.tool()
def get_daily_fortune(
    date_of_birth: str, 
    forecast_day: str = datetime.now().strftime("%Y-%m-%d"), 
    format: str = "text"
) -> str:
    """
    Get a daily fortune based on the date of birth and the forecast day
    :param date_of_birth: The date of birth in the format of YYYY-MM-DD
    :param forecast_day: The day to forecast the fortune for, in the format of YYYY-MM-DD, default is today
    :param format: The format to return the fortune in, either "text" or "json", default is "text"
    :return: A daily fortune based on the date of birth and the forecast day in the format of text or json
    """
    try:
        date_of_birth = datetime.fromisoformat(date_of_birth)
        forecast_day = datetime.fromisoformat(forecast_day)
        xung_khac = get_xung_khac(date_of_birth, forecast_day)
        if format == "text":
            output_text = f"Ngày {forecast_day.strftime('%Y-%m-%d')}"
            output_text += f"\n{xung_khac['total_relation']['description']}"
            output_text += f"\n{xung_khac['can_relation']['description']}"
            output_text += f"\n{xung_khac['chi_relation']['description']}"
            output_text += f"\n{xung_khac['ngu_hanh_relation']['description']}"
            return output_text
        elif format == "json":
            return xung_khac
        else:
            return "Invalid format"
    except ValueError:
        return "Invalid date of birth or forecast day"


@mcp.tool()
def get_general_fortune(
    forecast_day: str = datetime.now().strftime("%Y-%m-%d"), format: str = "text"
) -> str:
    """
    Get a general fortune for everyone based on the forecast day
    :param forecast_day: The day to forecast the fortune for, in the format of YYYY-MM-DD, default is today
    :param format: The format to return the fortune in, either "text" or "json", default is "text"
    :return: A general fortune for everyone based on the forecast day in the format of text or json
    """
    forecast_day = datetime.fromisoformat(forecast_day)
    lunar_date = get_lunar_date(forecast_day)
    can_ngay = get_can_ngay(forecast_day)
    chi_ngay = get_chi_ngay(forecast_day)
    huong_tai_than = get_huong_tai_than(forecast_day)
    huong_hy_than = get_huong_hy_than(forecast_day)
    huong_quy_nhan = get_huong_quy_nhan(forecast_day)
    truc_day = get_truc_day(forecast_day)
    tiet_khi = get_tiet_khi(forecast_day)
    tinh_tu = get_tinh_tu(forecast_day)
    luc_dieu = get_luc_dieu(forecast_day)
    pengzu_can = PENGZU_CAN[can_ngay]
    pengzu_chi = PENGZU_CHI[chi_ngay]
    nhi_thap_bat_tu = NHI_THAP_BAT_TU_KHUYEN[tinh_tu]
    thap_nhi_kien_tru = THAP_NHI_KIEN_TRU_KHUYEN[truc_day]
    luc_dieu = LUC_DIEU_KHUYEN[luc_dieu]
    nap_am_year = get_nap_am_year(forecast_day)
    nap_am_month = get_nap_am_month(forecast_day)
    nap_am_day = get_nap_am_day(forecast_day)
    if format == "text":
        return f"""Ngày {lunar_date} là ngày {can_ngay} {chi_ngay} {tiet_khi} {nap_am_day}
        Huớng Tài Thần: {huong_tai_than}
        Huớng Hỷ Thần: {huong_hy_than}
        Huớng Quý Nhân: {huong_quy_nhan}
        Trực: {truc_day}
        Phận can: {pengzu_can}
        Phận chi: {pengzu_chi}
        Nhi thập bát tụ: {nhi_thap_bat_tu}
        Thập nhi kiến trừ: {thap_nhi_kien_tru}
        Lực diệu: {luc_dieu}"""
    elif format == "json":
        return {
            "lunar_date": lunar_date,
            "can_ngay": can_ngay,
            "chi_ngay": chi_ngay,
            "tiet_khi": tiet_khi,
            "huong_tai_than": huong_tai_than,
            "huong_hy_than": huong_hy_than,
            "huong_quy_nhan": huong_quy_nhan,
            "truc_day": truc_day,
            "nap_am_year": nap_am_year,
            "nap_am_month": nap_am_month,
            "nap_am_day": nap_am_day,
            "tinh_tu": tinh_tu,
            "pengzu_can": pengzu_can,
            "pengzu_chi": pengzu_chi,
            "nhi_thap_bat_tu": nhi_thap_bat_tu,
            "thap_nhi_kien_tru": thap_nhi_kien_tru,
            "luc_dieu": luc_dieu,
        }
    else:
        return "Invalid format"


def main():
    """Entry point for the MCP server"""
    parser = argparse.ArgumentParser(
        description='VNStock MCP Server - Vietnam Stock Market Data Access via MCP',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
            Examples:
            %(prog)s                              # Run with default stdio transport
            %(prog)s --transport stdio            # Explicitly use stdio transport
            %(prog)s --transport sse              # Use Server-Sent Events transport
            %(prog)s --transport streamable-http  # Use HTTP streaming transport
            
            Transport Modes:
            stdio          : Standard input/output (default, for MCP clients like Claude Desktop)
            sse            : Server-Sent Events (for web applications)
            streamable-http: HTTP streaming (for HTTP-based integrations)
        """
    )
    
    parser.add_argument(
        '--transport', '-t',
        choices=['stdio', 'sse', 'streamable-http'],
        default='stdio',
        help='Transport protocol to use (default: stdio)'
    )

    parser.add_argument(
        '--host',
        type=str,
        default='0.0.0.0',
        help='Host address to bind to (default: 0.0.0.0)'
    )

    parser.add_argument(
        '--port',
        type=int,
        default=8000,
        help='Port to bind to (default: 8000)'
    )
    try:
        args = parser.parse_args()
        
        if args.transport == 'stdio':
            mcp.run(transport=args.transport)
        else:
            # HTTP-based transports (sse, streamable-http)
            print(f"Server running on http://{args.host}:{args.port}", file=sys.stderr)
            mcp.run(
                transport=args.transport,
                host=args.host,
                port=args.port,
            )
    except KeyboardInterrupt:
        print("\nServer stopped by user.", file=sys.stderr)
        sys.exit(0)
    except Exception as e:
        print(f"Error starting server: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    # For testing, you can uncomment the line below
    # print(get_date_of_birth_detail("1998-07-19", 1, "text"))
    # For running the server, use:
    main()
