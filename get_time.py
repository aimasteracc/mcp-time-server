from mcp.server.fastmcp import FastMCP
from datetime import datetime
import os
import pytz

# Create FastMCP server instance
mcp = FastMCP("Time Server")

@mcp.tool()
async def get_time() -> str:
    """Get the current time in a given timezone"""
    try:
        timezone = os.getenv("LOCAL_TIMEZONE", "UTC")
        tz = pytz.timezone(timezone)
        current_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S %Z")
        return f"The current time in {timezone} is {current_time}"
    except pytz.UnknownTimeZoneError:
        return f"Unknown timezone: {timezone}"

if __name__ == "__main__":
    mcp.run()

