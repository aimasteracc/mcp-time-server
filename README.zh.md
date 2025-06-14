<!-- 语言切换 -->
[English](README.md) | [日本語](README.ja.md) | [中文](README.zh.md)

# 🕐 MCP 时间服务器

一个专业、生产级的支持时区的时间服务，基于 Model Context Protocol (MCP)。支持全球所有时区，提供丰富的时间信息。

## ✨ 特性

- 🌍 **全球时区支持** - 获取任意时区的时间信息
- 📊 **丰富的时间数据** - 格式化时间、ISO格式、时间戳等
- 🔍 **时区发现** - 可按区域筛选时区
- 📝 **全面日志** - 专业日志记录
- ⚡ **异步性能** - 基于 async/await 的高性能
- 🛡️ **错误处理** - 健壮的错误处理
- 🔧 **环境变量配置** - 灵活的配置方式

## 🚀 快速开始

### 安装

```bash
# 克隆仓库
git clone https://github.com/your-username/mcp-time-server.git
cd mcp-time-server

# 推荐使用 uv 安装依赖
uv sync

# 或使用 pip
pip install -e .
```

### 启动服务器

```bash
python get_time.py
# 或
mcp-time-server
```

### 配置

```bash
export LOCAL_TIMEZONE="Asia/Shanghai"
python get_time.py
```

## 🛠️ 可用工具

### `get_current_time`
获取任意时区的详细时间信息（JSON格式）。

**参数：**
- `timezone` (可选): 目标时区标识（如 'UTC', 'Asia/Shanghai'）

**返回示例：**
```json
{
  "timezone": "Asia/Shanghai",
  "formatted_time": "2025-06-14 15:43:37 CST+0800",
  "iso_format": "2025-06-14T15:43:37.123456+08:00",
  "timestamp": 1718349817.123456,
  "weekday": "Friday",
  "month": "June"
}
```

### `list_available_timezones`
获取可用时区列表，可按区域筛选。

**参数：**
- `region` (可选): 区域（如 'Asia', 'America', 'Europe'）

**返回示例：**
```json
["Asia/Shanghai", "Asia/Tokyo", "Asia/Seoul", "..."]
```

### `get_server_info`
获取服务器元数据和功能信息。

**返回示例：**
```json
{
  "name": "Professional Time Server",
  "version": "1.0.0",
  "description": "Professional timezone-aware time service",
  "supported_operations": ["get_current_time", "list_available_timezones", "get_server_info"],
  "default_timezone": "UTC",
  "total_timezones": 594
}
```

## 🏗️ 目录结构

```
./
├── get_time.py          # 主服务器实现
├── pyproject.toml       # 项目配置
├── README.md            # 英文文档
├── README.ja.md         # 日文文档
├── README.zh.md         # 中文文档
├── .gitignore           # Git忽略规则
├── .python-version      # Python版本说明
├── uv.lock              # 依赖锁定文件
```

## 🔧 开发

### 代码质量
- **Ruff** - 快速的 Python 代码格式化和检查工具
- **MyPy** - 静态类型检查
- **Python 3.12+** - 最新 Python 特性

### 运行测试
```bash
ruff format .
ruff check .
mypy get_time.py
```

## 📋 要求
- Python 3.12 或更高
- MCP 框架（mcp[cli] >= 1.9.4）
- pytz（时区处理）

## 🤝 贡献
1. Fork 仓库
2. 创建功能分支
3. 提交更改
4. 推送到远程
5. 创建 Pull Request

## 📄 许可证
MIT 许可证

## 🙏 鸣谢
- Model Context Protocol
- pytz
- 灵感来源于 AI 应用对可靠时间服务的需求

---

<div align="center">
  <strong>为 MCP 生态系统倾注热爱 ❤️</strong>
</div> 