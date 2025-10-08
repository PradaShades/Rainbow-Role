import requests
import time
import asyncio
import aiohttp
from datetime import datetime


BOT_TOKEN = "" # Your bot token 
ROLE_ID = 49157098  # the role ID for the rainbow effect 
SERVER_ID = ""  # Your server ID


RAINBOW_COLORS = [
    0xFF0000,  # Red
    0xFF9900,  # Yellow-Orange
    0xFFFF00,  # Yellow
    0xA3E8FF,  # Cyan
    0x00FF99,  # Mint Green
    0xA9A3FF,  # PURP
    0xFF99CC,  # Pale Pink
]


BASE_URL = "https://www.guilded.gg/api/v1"
ROLE_UPDATE_URL = f"{BASE_URL}/servers/{SERVER_ID}/roles/{ROLE_ID}"

async def update_role_color(session, color):
    headers = {
        "Authorization": f"Bearer {BOT_TOKEN}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    
    payload = {
        "colors": [color]
    }
    
    try:
        async with session.patch(ROLE_UPDATE_URL, json=payload, headers=headers) as response:
            if response.status == 200:
                print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} -  role color changed to #{color:06X}")
            else:
                error_text = await response.text()
                print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Failed to change role color: {response.status} - {error_text}")
    except Exception as e:
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Error changing role color: {str(e)}")

async def rainbow_role_changer():
    color_index = 0
    async with aiohttp.ClientSession() as session:
        while True:
            
            current_color = RAINBOW_COLORS[color_index]
            
          
            await update_role_color(session, current_color)
            
            color_index = (color_index + 1) % len(RAINBOW_COLORS)
            
           
            await asyncio.sleep(5)

if __name__ == "__main__":
    print("Starting... (Press Ctrl+C to stop)")
    
    try:
        asyncio.run(rainbow_role_changer())
    except KeyboardInterrupt:
        print("\nProcess Interrupted")