import os

class AppConfig:
    # Databases
    U_DB = 'db/user.db'
    T_DB = 'db/thread.db'
    K_DB = 'db/thd/kommen.db'
    RPY_DB = 'db/thd/reply.db'
    U_A_DB = 'db/action.db'

    #static
    STATIC = 'static'

    # Secret key
    SECRET_KEY = os.urandom(24)

    # Templates
    DASHBOARD_TEMPLATE = 'dashboard.html'
    LOGIN_TEMPLATE = 'home.html'

    # Images
    DEFAULT_PFP = 'images/default.jpg'
    UNANDEGROUND_BACKGROUND = 'images/underground.png'

    #script
    SCRIPT_JS = 'js/script.js'
    
    #style
    DS_STYLE = 'style-ds.css'
    LG_STYLE = 'style.css'