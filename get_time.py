#!/usr/bin/env python3
"""
MCP Time Server - A professional time service provider

This server provides timezone-aware time information through the Model Context Protocol.
Supports multiple timezone formats and provides detailed time information.

Author: AI Assistant
Version: 1.0.0
License: MIT
"""

import os
import logging
from datetime import datetime
from typing import Optional
import pytz
from mcp.server.fastmcp import FastMCP

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Server configuration
SERVER_NAME = "Professional Time Server"
SERVER_VERSION = "1.0.0"
DEFAULT_TIMEZONE = "UTC"

# Initialize FastMCP server
server = FastMCP(SERVER_NAME)

@server.tool()
async def get_current_time(timezone: Optional[str] = None) -> str:
    """
    Get the current time in the specified timezone.
    
    Args:
        timezone: Target timezone (e.g., 'UTC', 'Asia/Shanghai', 'America/New_York').
                 If not provided, uses LOCAL_TIMEZONE environment variable or UTC.
    
    Returns:
        Formatted time string with timezone information.
        
    Raises:
        ValueError: If the specified timezone is invalid.
    """
    try:
        # Determine target timezone
        target_tz = timezone or os.getenv("LOCAL_TIMEZONE", DEFAULT_TIMEZONE)
        
        # Validate and get timezone object
        tz = pytz.timezone(target_tz)
        
        # Get current time in the specified timezone
        current_time = datetime.now(tz)
        
        # Format the time string
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S %Z%z")
        
        logger.info(f"Time requested for timezone: {target_tz}")
        
        return {
            "timezone": target_tz,
            "formatted_time": formatted_time,
            "iso_format": current_time.isoformat(),
            "timestamp": current_time.timestamp(),
            "weekday": current_time.strftime("%A"),
            "month": current_time.strftime("%B")
        }
        
    except pytz.UnknownTimeZoneError as e:
        error_msg = f"Invalid timezone '{target_tz}'. Please use a valid timezone identifier."
        logger.error(error_msg)
        raise ValueError(error_msg) from e
    except Exception as e:
        error_msg = f"Failed to get time: {str(e)}"
        logger.error(error_msg)
        raise RuntimeError(error_msg) from e

@server.tool()
async def list_available_timezones(region: Optional[str] = None) -> list:
    """
    List available timezones, optionally filtered by region.
    
    Args:
        region: Optional region filter (e.g., 'Asia', 'America', 'Europe').
    
    Returns:
        List of available timezone identifiers.
    """
    try:
        all_timezones = list(pytz.all_timezones)
        
        if region:
            filtered_timezones = [tz for tz in all_timezones if tz.startswith(region)]
            logger.info(f"Listed {len(filtered_timezones)} timezones for region: {region}")
            return sorted(filtered_timezones)
        
        logger.info(f"Listed all {len(all_timezones)} available timezones")
        return sorted(all_timezones)
        
    except Exception as e:
        error_msg = f"Failed to list timezones: {str(e)}"
        logger.error(error_msg)
        raise RuntimeError(error_msg) from e

@server.tool()
async def get_server_info() -> dict:
    """
    Get server information and capabilities.
    
    Returns:
        Dictionary containing server metadata.
    """
    return {
        "name": SERVER_NAME,
        "version": SERVER_VERSION,
        "description": "Professional timezone-aware time service",
        "supported_operations": [
            "get_current_time",
            "list_available_timezones",
            "get_server_info"
        ],
        "default_timezone": DEFAULT_TIMEZONE,
        "total_timezones": len(pytz.all_timezones)
    }

def main():
    """Main entry point for the MCP server."""
    try:
        logger.info(f"Starting {SERVER_NAME} v{SERVER_VERSION}")
        logger.info(f"Default timezone: {DEFAULT_TIMEZONE}")
        logger.info(f"Environment timezone: {os.getenv('LOCAL_TIMEZONE', 'Not set')}")
        
        server.run()
        
    except KeyboardInterrupt:
        logger.info("Server shutdown requested by user")
    except Exception as e:
        logger.error(f"Server error: {str(e)}")
        raise

if __name__ == "__main__":
    main()

