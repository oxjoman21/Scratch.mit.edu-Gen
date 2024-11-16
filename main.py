import tls_client
import json
from utils.solver import solve_cap
from utils.logger import Logger
from utils.headers import get_full_headers
import random
import string
import time

log = Logger()

def generate_username():
    letters = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(letters) for i in range(8))
    return username

def register_account():
    url = "https://scratch.mit.edu/accounts/register_new_user/"
    
    headers, cookies = get_full_headers()
    if not headers:
        log.err("Failed to get headers", "Register")
        return False
        
    captcha_response = solve_cap()
    if not captcha_response:
        log.err("Failed to solve captcha", "Register")
        return False

    data = {
        "username": generate_username(),
        "email": f"{generate_username()}@gmail.com",
        "password": "".join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=12)),
        "birth_month": str(random.randint(1,12)),
        "birth_year": str(random.randint(1990,2005)),
        "under_16": "false",
        "g-recaptcha-response": captcha_response,
        "gender": random.choice(["male", "female"]),
        "country": "United States",
        "is_robot": ""
    }

    try:
        session = tls_client.Session(client_identifier="chrome_130")
        
        cookie_dict = {}
        for cookie in cookies:
            if cookie.name != "scratchsessionsid":
                cookie_dict[cookie.name] = cookie.value
                session.cookies.set(cookie.name, cookie.value, domain=".scratch.mit.edu")
        
        response = session.post(url, headers=headers, data=data)
        
        try:
            response_data = response.json()
            if isinstance(response_data, list):
                response_data = response_data[0]  
        except:
            response_data = {"success": False, "errors": {"unknown": ["Failed to parse response"]}}

        if response.status_code == 200 and response_data.get("success") == True:
            username = response_data.get("username", data["username"])
            token = response_data.get("token", "No token found")
            user_id = response_data.get("user_id", "No ID found")
            
            log.suc(f"Genned Acc --> {token}", "Gen")
            
            with open("Scratch/accounts.txt", "a") as f:
                f.write(f"Username: {username} | Token: {token} | ID: {user_id}\n")
                
            return True
        else:
            if isinstance(response_data, dict):
                errors = response_data.get("errors", {})
                for key, msgs in errors.items():
                    log.err(f"{key}: {', '.join(msgs)}", "Gen")
            else:
                log.err(f"Unexpected response: {response.text}", "Register")
            return False
            
    except Exception as e:
        log.err(f"Error during registration: {str(e)}", "Register")
        return False

if __name__ == "__main__":
    while True:
        attempts = 0
        while attempts < 10:
            if register_account():
                break
            attempts += 1
            time.sleep(random.uniform(2, 4))
