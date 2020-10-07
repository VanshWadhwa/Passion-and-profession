        #start as owner function
import re 
import basic_functions as bf
import owner_db as odb
import chat_bot as cb

#,r""

#keyword for all the activities for the owner for ACTIONS only
o_kwd_act =  {r"add",r"stock(s)?" , r"item(s)?"  , r"display" ,r"new",r"history",r"profile(s)?",r"give",r"decrease"
              ,r"increase",r"alter",r"feedback" ,r"show", r"print(s)?",
          r"purcha(s|c)e",}




def display_o_output(text):
    
    """This function displays the user output"""
    #bf.hanprt(text)

def process_o_input(scaned_set , o_input):
    """This functions processes the scanned set and returns the processes output or query"""
    try:
        if (scaned_set == (set([r"add",r"stock(s)?",r"new"]))) or (scaned_set ==(set([r"add",r"stock(s)?"]))) or (scaned_set == (set([r"add",r"item(s)?",r"new"]))) or (scaned_set ==(set([r"add",r"item(s)?"]))):
            
            odb.check_and_add_new_stocks(ask_entire_stock(bf.get_attribute(o_input)))
            
        elif ((scaned_set == (set([r"show",r"stock(s)?"]))) or (scaned_set ==(set([r"display",r"stock(s)?"]))) or (scaned_set ==(set([r"print(s)?",r"stock(s)?"])))) or ((scaned_set == (set([r"show",r"item(s)?"]))) or (scaned_set ==(set([r"display",r"item(s)?"]))) or (scaned_set ==(set([r"print(s)?",r"item(s)?"])))) :
            display_stocks(odb.show_stocks(bf.get_attribute(o_input)))
        elif ((scaned_set == (set([r"show",r"profile(s)?"]))) or (scaned_set ==(set([r"display",r"profile(s)?"]))) or (scaned_set ==(set([r"print(s)?",r"profile(s)?"]))) or (scaned_set ==(set([r"profile(s)?"])))):
            display_profile(odb.get_data_of_profile(which_profile(o_input)))
            
        else:
            cb.chat(o_input)
        
            
        return scaned_set;
    except:
        bf.hanprt("Sorry an error occured in proccessing the input")

def start_as_owner():
    try:
        username = "Infinity"
        bf.handler = "Auto K.B."
        
        bf.easy_center_align("Started as owner")
        
        bf.hanprt("Now you can start.")
        o_input = bf.ask_input()
        while(1):
            if ((o_input == "i am done") or (o_input == "exit") or (o_input == "leave") or (o_input == "quit")):
                bf.hanprt("Thanks for visiting,"+ username)    
                break
            display_o_output(process_o_input(bf.scan_r(o_kwd_act , o_input),o_input))
            
            o_input = bf.ask_input()
    except:
        bf.easy_center_align("Sorry an error occured in starting as owner")
        start_as_owner()
            
    #except:
    #         bf.nnprt("ERROR")


def ask_entire_stock(value_tuple):
    """Asks the entire stocks and stores the values and asks the user for incomplete values if empty values is provided"""
    try:
        
        value_list = list(value_tuple)
        if value_tuple[0] == "":
            
            value_list[0] = bf.ask_item_type()

        
        
        if value_tuple[1] == "":
            value_list[1] = bf.ask_gender()


        if value_tuple[2] == "":
            value_list[2] = bf.ask_size()

        if value_tuple[3] == "":
            
            value_list[3] = bf.ask_prize()

        if value_tuple[4] == "":
            
            value_list[4] = bf.ask_colour()

        if value_tuple[5] == "":
            value_list[5] = bf.ask_brand()

        if value_tuple[6] == "":
            value_list[6] = bf.ask_quantity()

        value_tuple_2 = tuple(value_list)
        
        return value_tuple_2
    
    except:
        bf.easy_center_align("Sorry an error occured in asking the stock")
        ask_entire_stock()
        
def display_stocks(item_list):
    try:
        if item_list != []:
            bf.random_pr_string(("This is what we have" ,
                                  "We have these" ,
                                  "This is the stock" ,
                                  "Stock available with us",
                                  "Items we have" ,
                                  "Available stock" ,))
            
            bf.line("_",90)
            bf.center_align("_",20)
            #bf.nnprt("|___ITEM____|__GENDER__|__SIZE___|____PRIZE__|_COLOUR_|__BRAND_|__QUANTY_|")
            bf.nnprt(("|__"+ bf.left_align("ITEM" , 10).upper() + "|__"+bf.left_align("gender" , 7).upper() + "|__"+bf.left_align("SIZE" , 7).upper()+"|__"+bf.left_align("PRIZE" , 10).upper()+"|__"+bf.left_align("COLOUR", 10).upper()+"|__"+bf.left_align("BRAND" , 15).upper()+"|__"+bf.left_align("QUANTITY" , 10)+"|"))
            
            for i in item_list:
                
                p = str(i[3])
                q = str(i[6])
                #bf.easy_center_align( q + "pcs. of " +  i[0] + " of brand " + i[5].upper() + " of size " +i[2].upper() + " of colour " + i[4].upper() + " of prize Rs." + p + "/-")
                
                bf.nnprt("|__" + bf.left_align(i[0] , 10).upper() +"|__"+  bf.left_align(i[1] , 7).upper() + "|__"+ bf.left_align(i[2] , 7).upper() + "|__Rs."+  bf.left_align(p , 7).upper() + "|__"+bf.left_align(i[4] , 10).upper()+ "|__" + bf.left_align(i[5] , 15).upper() +"|__"+ bf.left_align(q , 10).upper() + "|") 
            bf.line("_",90)
            bf.nnprt("")
        else:
            bf.hanprt("No Item available in the stocks")    
    
    except:
        bf.easy_center_align("Sorry an error occured in finding whats in the stock")
        

def display_profile(item_list):
    """THis function displays the user profile"""
    try:
        if item_list != []:
            bf.random_pr_string(("Your customer loves these" ,
                                  "History of the user" ,
                                  "Profile " ,
                                  "Showing the profile" ))
            bf.nnprt("")
            #bf.line("_",130)
            bf.nnprt(bf.center_align("_",149))
            #bf.nnprt("|___ITEM____|__GENDER__|__SIZE___|____PRIZE__|_COLOUR_|__BRAND_|__QUANTY_|___AMOUNT___|__PAYMENT_MOD__|__DATE_AND_TIME____|")
            bf.nnprt("|__"+ bf.left_align("ITEM" , 10).upper() + "|__"+bf.left_align("gender" , 7).upper() + "|__"+bf.left_align("SIZE" , 7).upper()+"|__"+bf.left_align("PRIZE" , 13).upper()+"|__"+bf.left_align("COLOUR", 10).upper()+"|__"+bf.left_align("BRAND" , 15).upper()+"|__"+bf.left_align("QUANTITY" , 10).upper()+"|__"+bf.left_align("AMOUNT" , 13).upper() +"|__"+bf.left_align("PAYMENT_MOD" , 12).upper() + "|__"+bf.left_align("DATE AND TIME" , 20).upper() + "|")
            
            for i in item_list:
                
                p = str(i[3])
                q = str(i[6])
                a = str(i[7])
                d = str(i[9])
                #print(d)
                #bf.easy_center_align( q + "pcs. of " +  i[0] + " of brand " + i[5].upper() + " of size " +i[2].upper() + " of colour " + i[4].upper() + " of prize Rs." + p + "/-")
                
                bf.nnprt("|__" + bf.left_align(i[0] , 10).upper() +"|__"+  bf.left_align(i[1] , 7).upper() + "|__"+ bf.left_align(i[2] , 7).upper() + "|__Rs."+  bf.left_align(p , 10).upper() + "|__"+bf.left_align(i[4] , 10).upper()+ "|__" + bf.left_align(i[5] , 15).upper() +"|__"+ bf.left_align(q , 10).upper() + "|__Rs."+ bf.left_align(a , 10).upper() + "|__"+ bf.left_align(i[8] , 12).upper() + "|__"+ bf.left_align(d , 20).upper() + "|") 
            #bf.line("_",130)
            bf.nnprt(bf.center_align("_",149))
            bf.nnprt("")
        else:
            bf.hanprt("No History available")    

    except:
        bf.easy_center_align("Sorry an error occured displaying the profile")
        
        
            
def ask_customer_name():
    """This function asks the customers name"""
    try:
        bf.hanprt("Whats the username?")
        c_name = bf.ask_input()
        return c_name
    except:
        bf.hanprt("Sorry an error occured in asking the customer name")
    
#display_profile(odb.get_data_of_profile("user_54"))    
    
attribute_of_username_r = {r"user (\w+)" , r"username (\w+)" , r"customer (\w+)"}

def which_profile(o_input):
    try:
        """This function scans th o_input for username"""
        s = (bf.scan_n(attribute_of_username_r , o_input))
        try:
            t = str(s.pop())
        except:
             t = ""
        if (re.match(r" user (\w+)",t)):
            username = t[6:-1]
        elif (re.match(r" username (\w+)",t)):
            username = t[10:-1]
        elif (re.match(r" customer (\w+)",t)):
            username = t[10:-1]
        else:
            username = ask_customer_name()
        return username
    except:
        bf.hanprt("Sorry an error occured in asking you which profile")
        
#display_profile(odb.get_data_of_profile(which_profile("show profile of username user_54")))

