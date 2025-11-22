"""
status.py - Manages user login status
"""

# Global variable to track current logged-in user
current_user = {
    "username": None,
    "is_logged_in": False
}

def login_user(username):
    """Set the current logged-in user"""
    current_user["username"] = username
    current_user["is_logged_in"] = True

def logout_user():
    """Clear the current logged-in user"""
    current_user["username"] = None
    current_user["is_logged_in"] = False

def get_current_user():
    """Get the current logged-in user info"""
    return current_user.copy()

def is_user_logged_in():
    """Check if a user is currently logged in"""
    return current_user["is_logged_in"]