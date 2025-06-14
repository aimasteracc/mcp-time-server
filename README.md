<!-- Language Switcher -->
[English](README.md) | [日本語](README.ja.md) | [中文](README.zh.md)

# 🕐 MCP Time Server

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-green.svg)](https://modelcontextprotocol.io/)

A professional, production-ready timezone-aware time service built for the Model Context Protocol (MCP). Provides comprehensive time information with support for all global timezones.

## ✨ Features

- 🌍 **Global Timezone Support** - Access time information for any timezone worldwide
- 📊 **Rich Time Data** - Get formatted time, ISO format, timestamps, and more
- 🔍 **Timezone Discovery** - List and filter available timezones by region
- 📝 **Comprehensive Logging** - Professional logging for monitoring and debugging
- ⚡ **Async Performance** - Built with async/await for optimal performance
- 🛡️ **Error Handling** - Robust error handling with detailed error messages
- 🔧 **Environment Configuration** - Flexible configuration via environment variables

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/mcp-time-server.git
cd mcp-time-server

# Install dependencies using uv (recommended)
uv sync

# Or using pip
pip install -e .
```

### Running the Server

```bash
# Start the MCP server
python get_time.py

# Or use the installed script
mcp-time-server
```

### Configuration

Set your preferred timezone using environment variables:

```bash
export LOCAL_TIMEZONE="Asia/Shanghai"
python get_time.py
```

## 🛠️ Available Tools

### `get_current_time`

Get comprehensive time information for any timezone.

**Parameters:**
- `timezone` (optional): Target timezone identifier (e.g., 'UTC', 'Asia/Shanghai')

**Returns:**
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

Discover available timezones with optional region filtering.

**Parameters:**
- `region` (optional): Filter by region (e.g., 'Asia', 'America', 'Europe')

**Returns:**
```json
["Asia/Shanghai", "Asia/Tokyo", "Asia/Seoul", "..."]
```

### `get_server_info`

Get server metadata and capabilities.

**Returns:**
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

## 🏗️ Architecture

```
./
├── get_time.py          # Main server implementation
├── pyproject.toml       # Project configuration
├── README.md            # Documentation
├── .gitignore           # Git ignore rules
├── .python-version      # Python version specification
├── uv.lock              # Dependency lock file
```

## 🔧 Development

### Code Quality

This project uses modern Python development tools:

- **Ruff** - Fast Python linter and formatter
- **MyPy** - Static type checking
- **Python 3.12+** - Latest Python features

### Running Tests

```bash
# Format code
ruff format .

# Lint code
ruff check .

# Type checking
mypy get_time.py
```

## 📋 Requirements

- Python 3.12 or higher
- MCP framework (mcp[cli] >= 1.9.4)
- pytz for timezone handling

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Model Context Protocol](https://modelcontextprotocol.io/)
- Timezone data provided by [pytz](https://pythonhosted.org/pytz/)
- Inspired by the need for reliable time services in AI applications

---

<div align="center">
  <strong>Made with ❤️ for the MCP ecosystem</strong>
</div>