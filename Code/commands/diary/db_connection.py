from supabase import create_client, Client
from configs.config import db_url, db_key
#db_url = 'https://eraychronvbgezcirhos.supabase.co'
#db_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVyYXljaHJvbnZiZ2V6Y2lyaG9zIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mjk5MzgzOTIsImV4cCI6MjA0NTUxNDM5Mn0.18z-sKQMX7c4O-KnR6t2uTo3oARcIdnOfly_baS-_Kc'
  

supabase: Client = create_client(db_url, db_key)
          
class DBConnection:
    def take_login_db(self, user_id):
        response = (
        supabase.table("TgUsers")
        .select("login")
        .eq("user_id", user_id)
        .execute()
        )

        login = response.data[0]["login"]
        return login

    
    def take_password_db(self, user_id):
        response = (
        supabase.table("TgUsers")
        .select("password")
        .eq("user_id", user_id)
        .execute()
        )

        password = response.data[0]["password"]
        return password
    