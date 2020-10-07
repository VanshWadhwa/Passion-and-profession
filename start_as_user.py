#Start as user/customer
import basic_functions as bf
import re
import user_db as udb
import datetime
import chat_bot as cb

username  = ""
prev_item_list   = []#item list for previous item
cur_item_list = []#current item list
prev_item_tuple   = ("","","","","","","")#item tuple for previous itmes
cur_item_tuple = ("","","","","","","")#current item tuple
last_viewed_list = []
last_viewed_tuple = ("","","","","","","")
#keyword for all the activities for the user for ACTIONS only
u_kwd_act =  {r"show" , r"item(s)?"  , r"display" ,r"give"
              , r"what(s)?"
              , r"like" , r"buy(ing)?",r"see",r"want",r"add" ,r"cart",r"what(s)?",r"bill(s|ing)?",
          r"purcha(s|c)e",r"big(ger)?" , r"small(er)?" , r"increase(d)? (the )?size(s)?" ,r"decreased(d)? (the )?size(s)?" ,r"delete(s)?",r"remove(s)?"}

def display_u_output(text):
    """This function displays the user output"""
    #bf.hanprt(text)


def process_u_input(scaned_set , u_input):
    """This functions processes the scanned set and returns the processes output or query"""
    try:    
        global cur_item_tuple
        global cur_item_list
        global prev_item_tuple
        global prev_item_list
        global last_viewed_tuple
        global last_viewed_list
        if (scaned_set == (set([r"item(s)?",r"buy(ing)?"]))) or (scaned_set ==(set([r"item(s)?",r"show"]))) or (scaned_set ==(set([r"like",r"see"]))) or (scaned_set ==(set([r"like",r"purcha(s|c)e"]))) or (scaned_set ==(set([r"want",r"see"]))) or (scaned_set ==(set([r"want",r"purcha(s|c)e"]))) or  (scaned_set ==(set([r"buy(ing)?"]))) or  (scaned_set ==(set([r"purcha(s|c)e"]))) or (scaned_set ==(set([r"want",r"buy(ing)?"]))) or (scaned_set ==(set([r"buy(ing)?"]))) or (scaned_set ==(set([r"want",r"purcha(s|c)e"])))  or (scaned_set == (set([r"item(s)?",r"purcha(s|c)e"]))) or (scaned_set ==(set([r"item(s)?",r"show"]))) or (scaned_set ==(set([r"like",r"see"]))) or (scaned_set ==(set([r"item(s)?",r"display"]))):
            
            cur_item_list = list(ask_items_to_buy(buy_what(u_input)))
            cur_item_tuple = tuple(cur_item_list)
            data_list = udb.items_available_to_buy(cur_item_tuple)
            showcase_designs(data_list)
            last_viewed_list = cur_item_list
            last_viewed_tuple = tuple(last_viewed_list)
            
            
        elif(scaned_set == (set([r"add",r"cart"]))):
            #global cur_item_tuple
            udb.add_to_cart(ask_item_to_add_to_cart(bf.merge_tuple_value(cur_item_tuple,buy_what(u_input))),username)
            prev_item_list = prev_item_list
            prev_item_tuple = cur_item_tuple
        elif(scaned_set == (set([r"show",r"cart"]))) or (scaned_set == (set([r"display",r"cart"]))) or (scaned_set == (set([r"what(s)?",r"cart"]))) or (scaned_set == (set([r"see",r"cart"]))) :
            """Print cart"""
            print_cart(udb.data_of_cart(username))
        elif(scaned_set == (set([r"bill(s|ing)?"]))) or (scaned_set == (set([r"bill(s|ing)?" ,r"show" ]))) or (scaned_set == (set([r"bill(s|ing)?" ,r"give" ]))) or (scaned_set == (set([r"bill(s|ing)?" ,r"display" ]))) :
            create_bill(username)
        elif(scaned_set == (set([r"big(ger)?" ,r"show" ]))) or (scaned_set == (set([r"big(ger)?" ,r"give" ]))) or (scaned_set == (set([r"big(ger)?" ,r"display" ]))) or  (scaned_set == (set([r"big(ger)?"])))  or (scaned_set == (set([r"increase(d)? (the )?size(s)?"]))) :
            give_big_size(last_viewed_tuple)
        elif(scaned_set == (set([r"small(er)?" ,r"show" ]))) or (scaned_set == (set([r"small(er)?" ,r"give" ]))) or (scaned_set == (set([r"small(er)?" ,r"display" ]))) or  (scaned_set == (set([r"small(er)?"])))  or (scaned_set == (set([r"decrease(d)? (the )?size(s)?"]))) :
            give_small_size(last_viewed_tuple)
        elif( scaned_set == (set([r"delete(s)?",r"cart"]))) or (scaned_set == (set([r"remove(s)?",r"cart"]))):
            #global cur_item_tuple
            udb.remove_from_cart(ask_item_to_del_to_cart(buy_what(u_input)),username)
            
            
            
            
        else:
            cb.chat(u_input)
            


        return scaned_set;
    except  :
    
        bf.hanprt("Sorry an error occured in processing the output")
      


def start_as_user(u_name):
    try:
        global username
        username = u_name
        
        """Start as user/customer"""
        #user_name is the name of the user
        
        create_profile(username)
        udb.create_cart(username)
        Username = username[0].upper() + username[1:]
        bf.easy_center_align("Started as " + Username)
        bf.hanprt("Now you can ask me anything")
        bf.handler = "Staff"
        #the handler from basic function
       
        #try:
        
        u_input = bf.ask_input()
        while(1):
            if ((u_input == "i am done") or (u_input == "exit") or (u_input == "leave") or (u_input == "close")):
                bf.hanprt("Thanks for visiting ," + username)
                udb.delete_cart(username)
                break
            display_u_output(process_u_input(bf.scan_r(u_kwd_act , u_input),u_input))
            
            u_input = bf.ask_input()

    except:
        bf.hanprt("Sorry an error occured in starting as user")
        ask.username()
        

def buy_what(u_input):
    try:
        """This function scans the text and searches what you want to buy"""
        value_tuple = bf.get_attribute(u_input)

        return value_tuple
    except:
        bf.hanprt("Sorry an error occured in finding what to buy")

def ask_items_to_buy(value_tuple):
    try:
        """This function ask the user for nessasary items to display"""
        
        value_list = list(value_tuple)
        if value_tuple[0] == "":
            
            value_list[0] = bf.ask_item_type()
            
        if value_tuple[1] == "":
            value_list[1] = bf.ask_gender()
            
        if value_tuple[2] == "":
            value_list[2] = bf.ask_size()

        value_tuple_2 = tuple(value_list)
        return value_tuple_2
    except:
        bf.hanprt("Sorry an error occured in asking items to buy")
def Decimal(text):
    return text

def showcase_designs(item_list):
    try:
        if item_list != []:
            bf.random_pr_string(("Here are some beautiful designs for you" ,
                                  "You may like these designs" ,
                                  "I am sure you will love them" ,
                                  "Please have a look to them",
                                  "These designs are awesome" ,
                                  "Try these" ,))
            
            for i in item_list:
                
                p = str(i[3])
                
                bf.easy_center_align("A " + i[0] + " of brand " + i[5].upper() + " of size " +i[2].upper() + " of colour " + i[4].upper() + " of prize Rs." + p + "/-")
        else:
            bf.hanprt("Sorry sir we don't have this item available at this moment")
    except:
        bf.hanprt("Sorry an error occured in showcasing what to buy")
        
def ask_item_to_add_to_cart(value_tuple):
    """Asks the entire item and stores the values to cart and asks the user for incomplete values if empty values is provided"""
    try:
        value_list = list(value_tuple)
        
        if value_tuple == ():
            return value_tuple
        else:
            
            
             
            value_tuple_2 = tuple(value_list)
                
            data_list = udb.items_available_to_buy(value_tuple_2)  
            
            #if(len(data_list) > 1) or
            if len(data_list) > 1:
                if value_list[0] == "":
                    value_list[0] = bf.ask_item_type()
             
                elif value_list[1] == "":
                    value_list[1] = bf.ask_gender()

                elif value_list[2] == "":
                    value_list[2] = bf.ask_size()

                elif value_list[4] == "":
                    
                    value_list[4] = bf.ask_colour()

                elif value_list[5] == "":
                    value_list[5] = bf.ask_brand()
                    
                elif str(value_list[3]) == "":
                    value_list[3] = str(bf.ask_prize())
                
                
                      
                
                    
                #value_tuple_2 = tuple(value_list)    
                #ask_item_to_add_to_cart(value_tuple_2)
            elif len(data_list) == 0:
                bf.hanprt("No such item available")
                return ()
                
            else:
                if value_list[6] == "":
                    value_list[6] = bf.ask_quantity()
                value_tuple_2 = tuple(value_list)
                    
                
                #value_tuple_2 = tuple(value_list)    
                return value_tuple_2
            
            value_tuple_2 = value_list
            
            
            return ask_item_to_add_to_cart(value_tuple_2)
    except:
        bf.hanprt("Sorry an error occured in asking you what to add to cart")

def print_cart(item_list):
    try:
        """This function prints the cart"""
        if item_list != []:
            bf.random_pr_string(("You have selected " ,
                                  "This is what you have selected" ,
                                  "Your cart contains" ,
                                  "Items you have added" ,))
            for i in item_list:
                
                p = str(i[3])
                q = str(i[6])
                a = str(i[7])
                
                bf.easy_center_align(q +"pcs of " + i[0] + "("+i[1].upper()+") of brand " + i[5].upper() + " of size " +i[2].upper() + " of colour " + i[4].upper() + " of prize Rs." + p + "/-. Amount Rs." + a + "/-")
        else:
            bf.hanprt("Your cart is empty you have not added anything to your cart")
    except:
        bf.hanprt("Sorry an error occured in printing the cart")
            
def ask_payment_mod():
    try:
    
        bf.hanprt("Which payment method will suit you")
        payment_mod = bf.ask_input()
        if( (re.search(r" cash "," " + payment_mod + " ")) or (re.search(r" card "," " + payment_mod + " "))  or (re.search(r" cheque "," " + payment_mod + " ")) or (re.search(r" e(-| )wallet "," " + payment_mod + " "))  ):
            if ( (re.search(r" boy(s)? "," " + payment_mod + " ")) ):
                payment_mod = "cash"
            elif ( (re.search(r" card "," " + payment_mod + " ")) ):
                payment_mod = "card"
            elif ((re.search(r" cheque "," " + payment_mod + " ")) ):
                payment_mod = "cheque"
            elif ((re.search(r" e(-| )wallet "," " + payment_mod + " ")) ):
                payment_mod = "ewallet"
            
            return payment_mod
        else:
            bf.hanprt("Invalid option , Please try again (cash/card/e-wallet/cheque)")
            
        return ask_payment_mod()
    except:
        bf.easy_center_align("Sorry an error occured.Please try again")
        ask_payment_mod()

def create_bill(username):

    try:
        """This function creates the billl"""

        item_list = udb.data_of_cart(username)

        if item_list == []:
            bf.hanprt("I can't create you bill as your cart is empty.")
            bf.hanprt("Add something to your cart buy asking to 'add to cart'")
            
        else:
            
            file = username+"_bill"
            file = open(file +".txt", "w")
            
            payment_mod = ask_payment_mod()
            total_amount = 0

            bf.hanprt(bf.append_file("Bill of " + username ,file ))
            bf.hanprt(bf.append_file("Bill created" ,file ))
            bf.line("_",106)
            bf.nnprt(bf.append_file(("|"+bf.center_align("___" ,104)+"|"),file))
            
            bf.nnprt(bf.append_file(("|"+bf.center_align("PASSION AND PROFESSION" ,104)+"|"),file))
            bf.nnprt(bf.append_file(("|"+bf.center_align("___" ,104)+"|"),file))
            bf.nnprt(bf.append_file(("|"+bf.center_align("ESTIMATE" ,104)+"|"),file))
            bf.nnprt(bf.append_file(("|"+bf.center_align("___" ,104)+"|"),file))
            
            
            bf.nnprt(bf.append_file("|"+bf.center_align(str("DATE_AND_TIME__"+str(datetime.datetime.now())),104) +"|",file))
            bf.nnprt(bf.append_file("|__"+ bf.left_align("ITEM" , 10).upper() + "|__"+bf.left_align("gender" , 7).upper() + "|__"+bf.left_align("SIZE" , 7).upper()+"|__"+bf.left_align("PRIZE" , 10).upper()+"|__"+bf.left_align("COLOUR", 10).upper()+"|__"+bf.left_align("BRAND" , 15).upper()+"|__"+bf.left_align("QUANTITY" , 10).upper()+"|__"+bf.left_align("AMOUNT" , 12).upper()+"|",file))
            bf.nnprt(bf.append_file(("|"+bf.center_align("__" ,104)+"|"),file))
            now = datetime.datetime.now()
            date = now.strftime("%Y-%m-%d")
            
            
            
            for i in item_list:
                
                p = str(i[3])
                q = str(i[6])
                a = str(i[7])
                #bf.easy_center_align( q + "pcs. of " +  i[0] + " of brand " + i[5].upper() + " of size " +i[2].upper() + " of colour " + i[4].upper() + " of prize Rs." + p + "/-")
            
                bf.nnprt(bf.append_file("|__" + bf.left_align(i[0] , 10).upper() +"|__"+  bf.left_align(i[1]  , 7).upper() + "|__"+ bf.left_align(i[2] , 7).upper() + "|__Rs."+  bf.left_align(p , 7).upper() + "|__"+bf.left_align(i[4] , 10).upper()+ "|__" + bf.left_align(i[5] , 15).upper() +"|__"+ bf.left_align(q , 10).upper() + "|__Rs." + bf.left_align(a , 9).upper() + "|",file))
                total_amount += i[7]
                udb.decrease_quantity(i , q)
                
                udb.add_to_profile(i ,username,payment_mod)
                udb.delete_empty_stock(i)

            bf.nnprt(bf.append_file(("|"+bf.center_align("_" ,104)+"|"),file))
            bf.nnprt(bf.append_file(("|"+bf.center_align("_" ,10))+bf.left_align(payment_mod , 10).upper() +bf.center_align("_" ,61)+"Rs."+ bf.left_align(a , 10).upper()+(bf.center_align("_" ,10)+"|"),file))
            bf.nnprt(bf.append_file(("|"+bf.center_align("_" ,104)+"|"),file))
            bf.nnprt(bf.append_file(("|"+bf.center_align("THANK YOU" ,104)+"|"),file))
            bf.nnprt(bf.append_file(("|"+bf.center_align("HAVE A NICE DAY" ,104)+"|"),file))
            bf.nnprt(bf.append_file(("|"+bf.center_align("_" ,104)+"|"),file))
            file.close()
            udb.clear_cart(username)
            

    
    #create_bill(username)
    except:
        bf.hanprt("Sorry an error occured in creating the bill")
        

#create_bill("user_41")
def create_profile(username):
    try:
        """CREATING the user profile"""
        
        if(bool(udb.check_table(str(username)+"_profile"))):
            bf.random_pr_string(("Welcome again." , "We love to see your face... Welcome again"))
        else:

            udb.create_profile_table(username)
            pass#del
    except:
        bf.hanprt("Sorry an error occured in creating new profie")
        
def give_big_size(value_tuple):
    try:
        global last_viewed_tuple
        global cur_item_tuple
        value_list = list(value_tuple)
        if value_list[2] == "xxxl":
            bf.hanprt("Sorry we only have upto size XXXL")
        else:    
            if value_tuple[2] == "s":
                value_list[2] = "m"
            if value_tuple[2] == "m":
                value_list[2] = "l"
            if value_tuple[2] == "l":
                value_list[2] = "xl"
            if value_tuple[2] == "xl":
                value_list[2] = "xxl"
            if value_tuple[2] == "xxl":
                value_list[2] = "xxxl"

            bf.random_pr_string(("No problem I will give you a bigger size"
                                ,"No problem"
                                ,"Sure"
                                ,"This is bigger"
                                ,"I hope this will fit you"
                                ,"Try this size"))
           
            value_tuple_2 = tuple(value_list)
            last_viewed_tuple =  value_tuple_2
            cur_item_tuple =  value_tuple_2
            data_list = udb.items_available_to_buy(value_tuple_2)
            showcase_designs(data_list)
    except:
        bf.hanprt("Sorry an error occured in getting you the big size")
            

def give_small_size(value_tuple):
    try:
        global last_viewed_tuple
        global cur_item_tuple
        value_list = list(value_tuple)
        if value_list[2] == "s":
            bf.hanprt("Sorry we don't have any size smaller than S")
        else:    
            if value_tuple[2] == "xxxl":
                value_list[2] = "xxl"
            if value_tuple[2] == "xxl":
                value_list[2] = "xl"
            if value_tuple[2] == "xl":
                value_list[2] = "l"
            if value_tuple[2] == "l":
                value_list[2] = "m"
            if value_tuple[2] == "m":
                value_list[2] = "s"

            bf.random_pr_string(("No problem I will  give you a small size"
                                ,"No problem"
                                ,"Sure"
                                ,"This is smalller"
                                ,"I hope this will fit you"
                                ,"Try this size"))
           
            value_tuple_2 = tuple(value_list)
            last_viewed_tuple =  value_tuple_2
            cur_item_tuple =  value_tuple_2
            data_list = udb.items_available_to_buy(value_tuple_2)
            showcase_designs(data_list)
            #prev_item_tuple =  value_tuple_2
    except:
        bf.hanprt("Sorry an error occured in getting you the small size")

def ask_items_to_remove_from_cart(value_tuple):
    try:
        """This function ask the user for removing from cart"""
        
        value_list = list(value_tuple)
        if value_tuple[0] == "":
            
            value_list[0] = bf.ask_item_type()
            
        if value_tuple[1] == "":
            value_list[1] = bf.ask_gender()
            
        if value_tuple[2] == "":
            value_list[2] = bf.ask_size()

        value_tuple_2 = tuple(value_list)
        return value_tuple_2
    except:
        bf.hanprt("Sorry an error occured in asking items to buy")

def ask_item_to_del_to_cart(value_tuple):
    
    """Asks the entire item and stores the values to cart and asks the user for incomplete values if empty values is provided"""
    try:
        value_list = list(value_tuple)
        
    #"""if value_tuple == (): return value_tuple else:"""
            
        #if value_tuple == ("", "", "", "", "", "", ""):
            
           
             
        value_tuple_2 = tuple(value_list)
                
        data_list = udb.items_available_to_remove(value_tuple_2,username)  
        
            #if(len(data_list) > 1) or
        if len(data_list) > 1:
            if value_list[0] == "":
                value_list[0] = bf.ask_item_type()
         
            elif value_list[1] == "":
                value_list[1] = bf.ask_gender()

            elif value_list[2] == "":
                value_list[2] = bf.ask_size()

            elif value_list[4] == "":
                
                value_list[4] = bf.ask_colour()

            elif value_list[5] == "":
                value_list[5] = bf.ask_brand()
                
            elif value_list[3] == "":
                value_list[3] = str(bf.ask_prize())
            
            
                  
            
                
            #value_tuple_2 = tuple(value_list)    
            #ask_item_to_add_to_cart(value_tuple_2)
        elif len(data_list) == 0:
            bf.hanprt("No such item available")
            
            """elif len(data_list) == 1:
            bf.hanprt("clear_cart")
            udb.clear_cart(username)
            return ()"""
            return ()
            
        elif len(data_list) == 1:
            """if value_list[6] == "":
                value_list[6] = bf.ask_quantity()"""
            value_tuple_2 = tuple(value_list)
            return value_tuple_2
        else:
            pass
                
            
            #value_tuple_2 = tuple(value_list)    
            return value_tuple_2
        
        value_tuple_2 = value_list
        
        
        return ask_item_to_del_to_cart(value_tuple_2)
    except :
        
        bf.hanprt("Sorry an error occured in asking you what to add to cart")


    
            




