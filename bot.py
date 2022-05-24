import asyncio
import os 

from pyrogram import Client

phone = str(os.environ.get('PHONE', ''))
api_id = int(os.environ.get('API_ID', 0))
api_hash = str(os.environ.get('API_HASH', ''))
passcode = str(os.environ.get('PASSWORD', ''))

async def poster():


  async with Client('new',api_id=api_id, api_hash=api_hash, phone_number=phone , password=passcode) as app:
    s = await app.export_session_string()
    r = await app.send_message("me", str(s))

  

def main():
  
  loop = asyncio.get_event_loop()
  loop.run_until_complete(poster())
  loop.close()


if __name__ == '__main__':
  main()
