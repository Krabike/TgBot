from supabase import create_client, Client
from configs.config import db_url, db_key


supabase: Client = create_client(db_url, db_key)
          
          
class DBConnection:
    async def take_login_db(self, user_id):
        response = (
        supabase.table("TgUsers")
        .select("login")
        .eq("user_id", user_id)
        .execute()
        )

        login = response.data[0]["login"]
        return login

    
    async def take_password_db(self, user_id):
        response = (
        supabase.table("TgUsers")
        .select("password")
        .eq("user_id", user_id)
        .execute()
        )

        password = response.data[0]["password"]
        return password