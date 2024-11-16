import requests
from fake_useragent import UserAgent

def get_full_headers():
    url = "https://scratch.mit.edu/csrf_token/"
    ua = UserAgent()
    user_agent = ua.chrome
    
    base_headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "cookie": "permissions=%7B%7D",
        "referer": "https://scratch.mit.edu/join",
        "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": user_agent
    }
    
    try:
        response = requests.get(url, headers=base_headers, timeout=10)
        csrf_token = response.cookies.get('scratchcsrftoken')
        
        if not csrf_token:
            return None, None
            
        full_headers = base_headers.copy()
        full_headers.update({
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://scratch.mit.edu",
            "x-csrftoken": csrf_token,
            "x-requested-with": "XMLHttpRequest"
        })
        
        return full_headers, response.cookies
        
    except Exception:
        return None, None