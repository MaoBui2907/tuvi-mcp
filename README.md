# TuVi MCP - Máy Bói Toán Việt Nam

Một MCP (Model Context Protocol) server cung cấp các công cụ bói toán dựa trên lịch âm Việt Nam, sử dụng các yếu tố như Can Chi, Ngũ Hành, Xung Khắc, và các phương pháp bói toán truyền thống.

## Tính năng

### 1. Chi Tiết Ngày Sinh (get_date_of_birth_detail)
Phân tích chi tiết ngày sinh bao gồm:
- Ngày âm lịch
- Tuổi Can Chi (Can + Chi)
- Ngũ Hành mệnh
- Nạp Âm
- Quái số
- Phật Đồ Mạng
- Cung Phi (hướng tốt)

### 2. Dự Đoán Vận Hạn Hàng Ngày (get_daily_fortune)
Dự đoán vận hạn dựa trên tương quan giữa ngày sinh và ngày cần xem:
- Quan hệ tổng thể
- Quan hệ Can
- Quan hệ Chi
- Quan hệ Ngũ Hành

### 3. Dự Đoán Vận Hạn Chung (get_general_fortune)
Thông tin vận hạn chung cho mọi người trong ngày:
- Ngày âm lịch và tiết khí
- Can Chi ngày
- Hướng Tài Thần, Hỷ Thần, Quý Nhân
- Trực ngày
- Phận Can, Phận Chi
- Nhi thập bát tú
- Thập nhị kiến trừ
- Lục diệu

## Cài đặt

### Yêu cầu hệ thống
- Python 3.12+
- PDM (Python Dependency Manager)

### Các bước cài đặt

1. **Clone repository:**
   ```bash
   git clone <repository-url>
   cd tuvi-mcp
   ```

2. **Cài đặt dependencies:**
   ```bash
   pdm install
   ```

3. **Cài đặt package:**
   ```bash
   pdm build
   pip install dist/tuvi_mcp-0.1.0.tar.gz
   ```

## Sử dụng

### Chạy MCP Server

Sau khi cài đặt, bạn có thể chạy MCP server bằng:

```bash
tuvi-mcp
```

### Sử dụng trong ứng dụng MCP

Server này tuân theo Model Context Protocol và có thể được tích hợp vào các ứng dụng hỗ trợ MCP như Claude Desktop, VS Code, etc.

## Cấu hình FastMCP Server

### Chạy trực tiếp

Sau khi cài đặt package, bạn có thể chạy server trực tiếp:

```bash
tuvi-mcp
```

### Cấu hình với Claude Desktop

Thêm vào file cấu hình Claude Desktop (`claude_desktop_config.json`):

**Trên macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Trên Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "tuvi-mcp": {
      "command": "tuvi-mcp"
    }
  }
}
```

### Cấu hình với VS Code (Cursor)

Thêm vào file settings VS Code/Cursor:

```json
{
  "mcp": {
    "servers": {
      "tuvi-mcp": {
        "command": "tuvi-mcp"
      }
    }
  }
}
```

### Chạy trong Development Mode

Khi phát triển, bạn có thể chạy server trực tiếp từ source:

**Cách 1: Chạy trực tiếp với Python**
```bash
# Từ thư mục gốc của project
python -m src.main
```

**Cách 2: Sử dụng PDM script (khuyến nghị)**
```bash
# Cài đặt dependencies nếu chưa có
pdm install

# Chạy server với script đã định nghĩa
pdm run dev
```

**Cách 3: Cài đặt package ở chế độ editable**
```bash
# Cài đặt package ở chế độ development
pdm install

# Sau đó có thể chạy như đã cài đặt
tuvi-mcp
```

### Kiểm tra server hoạt động

**Test với MCP Inspector (khuyến nghị):**
```bash
# Cài đặt MCP Inspector
pip install mcp-inspector

# Chạy inspector và kết nối với server
mcp-inspector python -m src.main
```

**Hoặc test với MCP CLI:**
```bash
# Cài đặt mcp CLI (nếu chưa có)
pip install mcp

# Test server (cần cài đặt package trước)
pip install -e .
mcp dev tuvi-mcp
```

### Ví dụ sử dụng

```python
from src.main import mcp

# Lấy chi tiết ngày sinh
result = mcp.call_tool("get_date_of_birth_detail", {
    "date_of_birth": "1998-07-19",
    "gender": 1,
    "format": "text"
})

# Dự đoán vận hạn hàng ngày
result = mcp.call_tool("get_daily_fortune", {
    "date_of_birth": "1998-07-19",
    "forecast_day": "2024-12-24",
    "format": "text"
})

# Dự đoán vận hạn chung
result = mcp.call_tool("get_general_fortune", {
    "forecast_day": "2024-12-24",
    "format": "json"
})
```

## API Reference

### get_date_of_birth_detail

**Parameters:**
- `date_of_birth` (string): Ngày sinh theo định dạng YYYY-MM-DD
- `gender` (int, optional): Giới tính (1: nam, 0: nữ), mặc định là 1
- `format` (string, optional): Định dạng trả về ("text" hoặc "json"), mặc định là "text"

**Returns:** Chi tiết ngày sinh dưới dạng text hoặc JSON

### get_daily_fortune

**Parameters:**
- `date_of_birth` (string): Ngày sinh theo định dạng YYYY-MM-DD
- `forecast_day` (string, optional): Ngày cần dự đoán, mặc định là hôm nay
- `format` (string, optional): Định dạng trả về ("text" hoặc "json"), mặc định là "text"

**Returns:** Dự đoán vận hạn hàng ngày

### get_general_fortune

**Parameters:**
- `forecast_day` (string, optional): Ngày cần dự đoán, mặc định là hôm nay
- `format` (string, optional): Định dạng trả về ("text" hoặc "json"), mặc định là "text"

**Returns:** Dự đoán vận hạn chung

## Dependencies

- **fastmcp** (>=2.14.1): Framework cho MCP server
- **lunardate** (>=0.2.2): Xử lý ngày âm lịch
- **lunar-python** (>=1.4.8): Thư viện lịch âm Trung Quốc/Việt Nam

## Kiến trúc dự án

```
src/
├── main.py           # Entry point và định nghĩa MCP tools
├── libs/
│   ├── can_chi.py    # Các hàm liên quan đến Can Chi, Ngũ Hành
│   ├── lunar_date.py # Xử lý ngày âm lịch
│   ├── xung_khac.py  # Tính toán xung khắc
│   └── khuyen.py     # Các bảng khuyên, phán đoán
└── tools/            # Các công cụ bổ sung
```

## Phát triển

### Chạy tests
```bash
python -m pytest tests/
```

### Chạy development server
```bash
python src/main.py
```

## Đóng góp

Mời đóng góp bằng cách tạo Issue hoặc Pull Request trên GitHub.

## Giấy phép

MIT License - Xem file LICENSE để biết thêm chi tiết.

## Lưu ý

Thông tin được cung cấp chỉ mang tính tham khảo và giải trí. Không nên sử dụng để đưa ra quyết định quan trọng trong cuộc sống.
