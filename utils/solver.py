import requests
import time
from .logger import Logger

# Initialize logger
logger = Logger()

API_KEY = "ur key"

website_url = "https://scratch.mit.edu/join"
website_key = "6LeRbUwUAAAAAFYhKgk3G9OKWqE_OJ7Z-7VTUCbl"

def create_recaptcha_task(api_key, website_url, website_key):
    url = "https://api.capmonster.cloud/createTask"
    payload = {
        "clientKey": api_key,
        "task": {
            "type": "RecaptchaV2TaskProxyless",  
            "websiteURL": website_url,
            "websiteKey": website_key
        }
    }
    response = requests.post(url, json=payload)
    result = response.json()
    
    if result.get("errorId") == 0:
        task_id = result.get("taskId")
        return task_id
    else:
        logger.err(f"Error creating task: {result.get('errorDescription')}", "Captcha")
        return None

def get_recaptcha_solution(api_key, task_id):
    url = "https://api.capmonster.cloud/getTaskResult"
    payload = {
        "clientKey": api_key,
        "taskId": task_id
    }
    
    attempts = 0
    max_attempts = 60  
    
    while attempts < max_attempts:
        try:
            response = requests.post(url, json=payload, timeout=10)
            result = response.json()
            
            if result.get("errorId") == 0:
                status = result.get("status")
                if status == "ready":
                    solution = result.get("solution", {}).get("gRecaptchaResponse")
                    if solution:
                        logger.suc(f"Solved Cap", "Solver")
                        return solution
                    logger.err("No solution in response", "Solver")
                    return None
            else:
                continue
                
        except Exception as e:
            logger.err(f"Request error: {str(e)}", "Solver")
            return None
            
        attempts += 1
        time.sleep(1)
    
    logger.err("Captcha timeout", "Solver")
    return None

def solve_cap():
    
    max_attempts = 5
    for attempt in range(max_attempts):
        try:
            task_id = create_recaptcha_task(API_KEY, website_url, website_key)
            if task_id:
                solution = get_recaptcha_solution(API_KEY, task_id)
                if solution:
                    return solution
            logger.err(f"Retrying captcha ({attempt + 1}/{max_attempts})", "Solver")
            time.sleep(2)
        except Exception as e:
            logger.err(f"Captcha error: {str(e)}", "Solver")
            time.sleep(1)
    return None