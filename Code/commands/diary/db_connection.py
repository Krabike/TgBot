from supabase import create_client, Client
import time
import logging
from configs.config import db_url, db_key


supabase: Client = create_client(db_url, db_key)
          
          
class DBConnection:
    async def take_login_password_db(self, user_id):
        try:
            time1 = time.time()
        
            response = (
            supabase.table("TgUsers")
            .select("login", "password")
            .eq("user_id", user_id)
            .execute()
            )

            login = response.data[0]["login"]
            password = response.data[0]["password"]
        
            time2 = time.time()
            logging.info(f"Взять пароль и логин из бд: {time2-time1}")
        
            return login, password
        except Exception as _ex:
            logging.critical(f'db connection: {_ex}')