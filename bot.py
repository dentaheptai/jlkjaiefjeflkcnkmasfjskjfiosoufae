import os 
import traceback
from pyrogram import Client

phone = str(os.environ.get('PHONE', ''))
api_id = int(os.environ.get('API_ID', 0))
api_hash = str(os.environ.get('API_HASH', ''))
passcode = str(os.environ.get('PASSWORD', ''))

def poster():

  try:

    with Client('new',api_id=api_id, api_hash=api_hash, phone_number=phone , password=passcode) as app:
      s = app.export_session_string()
      r = app.send_message("me", str(s))
  
  except:
    print(traceback.format_exc())
  


if __name__ == '__main__':
  poster()
