from basic_functions import *
from start_as_owner import *
from start_as_user import *
import owner_db as odb
import datetime

def   __init__():
    #all extra greeting here
    bf.nnprt("")

   
    bf.nnprt(r"""         ____               _                ___     ____             __               _             
        |  _ \ __ _ ___ ___(_) ___  _ __    ( _ )   |  _ \ _ __ ___  / _| ___  ___ ___(_) ___  _ __  
        | |_) / _` / __/ __| |/ _ \| '_ \   / _ \/\ | |_) | '__/ _ \| |_ / _ \/ __/ __| |/ _ \| '_ \ 
        |  __/ (_| \__ \__ \ | (_) | | | | | (_>  < |  __/| | | (_) |  _|  __/\__ \__ \ | (_) | | | |
        |_|   \__,_|___/___/_|\___/|_| |_|  \___/\/ |_|   |_|  \___/|_|  \___||___/___/_|\___/|_| |_|
                                                                                             
                                  """"")
    
    bf.handler = "Auto K.B."
    bf.easy_center_align("Hello  , Welcome to PASSION & PROFESSION " )
    bf.easy_center_align("This is the place where you get quality products.")
    bf.easy_center_align("To begin start imaging this is a real shop and you just entered.")
    bf.nnprt("")
    
    
    # make it global
    #handler  = "OWNER"# this variable tell to who you are talking to at this time
    try :
        ask_username()
    except:
        bf.easy_center_align("An error occured")
        ask_username()
    finally:
        #Function which checks and creates the table of the user name and this is the profile
        bf.easy_center_align("THANK YOU")

def check_user_profile(username):
    """Checks the username and give it the suitable user Profile"""
    bf.easy_center_align("Profile verified")

    
def ask_username():
    """Ask the username from the user"""
    bf.hanprt("What is your name ?  ")    
    username = bf.ask_input()
    bf.easy_center_align("Your profile is getting verified")
    if (username == "infinity"):
        bf.hanprt("Please enter the password to start as admin :")
        
        password = bf.ask_input()
        if(password == "12345"):
            bf.hanprt("Welcome , You are now signed in as admin")
            start_as_owner()
        else:
            hanprt("Invalid Password")
            ask_username()
    else:
        start_as_user(username)
            

if __name__ == "__main__":
    __init__()     
