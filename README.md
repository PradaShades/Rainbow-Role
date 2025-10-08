# Guilded Rainbow Role Changer

A Python bot that continuously cycles a Guilded server role through a list of colors, giving your role a rainbow effect.

## Features
- Automatically cycles a role through multiple colors
- Configurable colors
- Adjustable update interval

## Requirements
- Python 3.8 or higher
- aiohttp library  
Install dependencies with: `pip install aiohttp`

## Setup
1. Clone this repository:  
   `git clone https://github.com/Rainbow-Role/Rainbow-Role.git`  
   `cd Rainbow-Role`
2. Open `rainbow.py` and configure your settings:  
   `BOT_TOKEN = ""   # Your Guilded bot token`  
   `ROLE_ID = 49157098  # ID of the role to color`  
   `SERVER_ID = ""   # Your server ID`
3. Optionally, customize the colors:  
   `RAINBOW_COLORS = [0xFF0000, 0xFF9900, 0xFFFF00, 0xA3E8FF, 0x00FF99, 0xA9A3FF, 0xFF99CC]`
4. Run the bot: `python rainbow.bat`  
5. Press `Ctrl+C` to stop the bot.

## Notes
- Default color update interval is 5 seconds. You can adjust `asyncio.sleep(5)` in the script to change it.
