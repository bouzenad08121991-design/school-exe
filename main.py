import tkinter as tk
import os
import json
import tempfile
from school_mgmt.database import init_db
from school_mgmt.gui import SchoolApp, LoginWindow

def check_session():
    session_path = os.path.join(tempfile.gettempdir(), "genius_academy_session.json")
    if os.path.exists(session_path):
        try:
            with open(session_path, "r") as f:
                data = json.load(f)
                if data.get("logged_in"):
                    return True
        except:
            pass
    return False

def start_app():
    # Clear login window widgets
    for widget in root.winfo_children():
        widget.destroy()
    
    # Initialize the main application
    app = SchoolApp(root)

if __name__ == "__main__":
    # Initialize the database (create tables if they don't exist)
    init_db()
    
    # Create the main window
    root = tk.Tk()
    
    if check_session():
        # Start application directly if session exists
        start_app()
    else:
        # Start with login window
        login = LoginWindow(root, start_app)
    
    # Start the main event loop
    root.mainloop()