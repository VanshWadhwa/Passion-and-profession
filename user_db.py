"""Database compability from the side of user
    all basic functions can be seen here"""
import basic_functions as bf
import mysql.connector as sqltor
import datetime
DB_PASS = "vanshmysql"

try:
    #searching for the old database 
    mycon = sqltor.connect(host = "localhost",user ="root" , port = 3306 , passwd = DB_PASS , database = "autokb")
    
    #bf.easy_center_align("Started with the Auto K.B. Database")
    mycursor = mycon.cursor()
except:

    #there is no databse creating a new one now
   bf.easy_center_align("Could not connect with database please try again ")
    
    
    

"""
if mycon.is_connected():
    bf.easy_center_align("Connection established succesfully")
    
"""
#mycon.close()

         #bf.nnprt(item_type , gender , size  , prize , colour , brand , quantity)

def items_available_to_buy(value_tuple):
    try: 
        filter_3 = ""
        filter_4 = ""
        filter_5 = ""
        filter_6 = ""
        
        if value_tuple[3] != "":
            filter_3 = " and prize = '" + value_tuple[3]+ "'"
        if value_tuple[4] != "":
            filter_4 = " and colour = '" + value_tuple[4] + "'"
        if value_tuple[5] != "":
            
            filter_5 = " and brand = '" + value_tuple[5] + "'"
                   
        
        

        DISPLAYING_FORMULA = "SELECT item_type , gender , size  , prize , colour , brand FROM inventory WHERE item_type = '" + value_tuple[0]  + "'  and   gender  = '" + value_tuple[1]  + "' and size  = '" + value_tuple[2] + "'"+ filter_3 +filter_4 + filter_5
        
        mycursor.execute(DISPLAYING_FORMULA )

        data = mycursor.fetchall()
        return data
    
    except:
        
       bf.easy_center_align("Sorry an error occured in finding the items available to buy")
        

def create_cart(username):
    """This function creates the table as cart"""
    #bf.nnprt("Shopping cart created")
    try:
        if(bool((check_table(str(username+"_cart"))))):
           bf.hanprt("It seem you once visited here so starting with your old cart")
        else:
           
            formula = "CREATE TABLE "+username  +"_cart (item_type VARCHAR(100) , gender CHAR(1) , size CHAR(4)  , prize DECIMAL , colour VARCHAR(20) , brand VARCHAR(100) , quantity INTEGER , amount DECIMAL )"

            
            
            mycursor.execute(formula)
            mycon.commit()
            bf.easy_center_align("New cart created")
    except:
       bf.easy_center_align("Sorry an error occured.Please run the program again as your input is not valid for smooth functioning")
        

def delete_cart(username):
    """This function creates the table as cart"""
    #bf.nnprt("Shopping cart deleted")
    try:
        formula ="DROP TABLE "+username  +"_cart "
        mycursor.execute(formula)
        mycon.commit()
    except:
       bf.easy_center_align("Sorry an error occured as there is no cart to delete")
        

def add_to_cart(value_tuple , username):
    """This function - the items selected by the user to the cart"""

    try:
        if value_tuple == ():
            #bf.hanprt("Sorry you have not asked me of anything to buy")
            #bf.hanprt("Try saying like 'I want to buy'")
            pass
        else:
            
            value_tuple = (get_full_values_of_item(value_tuple))
        
            p = str(value_tuple[3])
            check_quantity_formula = "SELECT quantity FROM inventory WHERE item_type = '" + value_tuple[0]  + "'  and   gender  = '" + value_tuple[1]  + "' and size  = '" + value_tuple[2] + "'and prize = '" + p+ "' and colour = '" + value_tuple[4] + "' and brand = '" + value_tuple[5] + "'"
            mycursor.execute(check_quantity_formula)

            
            
            data = mycursor.fetchall()
            quantity_available = int(data[0][0])
            quantity_needed = int(value_tuple[6])
            if(quantity_needed <= quantity_available):
                
                final_list = []
                final_list.append(value_tuple[0])
                final_list.append(value_tuple[1])
                final_list.append(value_tuple[2])
                final_list.append(p)
                final_list.append(value_tuple[4])
                final_list.append(value_tuple[5])
                final_list.append(quantity_needed)
                amount = int(p) * int(quantity_needed)
                final_list.append(amount)
                final_tuple = tuple(final_list)
                
                
                
                INSERT_TO_cart  = "INSERT INTO "+ username +"_cart (item_type , gender , size  , prize , colour , brand , quantity , amount) VALUES (%s ,%s , %s , %s , %s , %s , %s ,%s)"
                mycursor.execute(INSERT_TO_cart , final_tuple)
                mycon.commit()    
                bf.random_pr_string(("Added to cart","New Item added","Item added to cart","Added","Done"))
            else:
                bf.hanprt("Sorry , we don't have this much quantity available right now the maxinum quantity you can get is " + str(quantity_available))
    except:
       bf.easy_center_align("Sorry an error occured in adding to cart")
                    
def Decimal(text):
    return text

def get_full_values_of_item(value_tuple):
    """THIS functions completes the value of the tuple from the unique item and returns the full tuple"""
    try:
        list_1 = list(value_tuple)
        list_2 = list_1
        data = items_available_to_buy(value_tuple)
        if list_1[0] == "":
            list_2[0] =  data[0][0]
        if list_1[1] == "":
            list_2[1] =  data[0][1]
        if list_1[2] == "":
            list_2[2] =  data[0][2]
        if list_1[3] == "":
            list_2[3] =  data[0][3]
        if list_1[4] == "":
            list_2[4] =  data[0][4]
        if list_1[5] == "":
            list_2[5] =  data[0][5]

        #list_2.append(list_1[6])    
        

        final_tuple   = tuple(list_2)
        return  final_tuple
    except:
       bf.easy_center_align("Sorry an error occured in getting the full values.")
        
def data_of_cart(username):
        
    """This functions returns the list of items present in the cart"""
    try:    
        DISPLAYING_FORMULA = "SELECT * FROM " + username + "_cart"
        #Fbf.nnprt(DISPLAYING_FORMULA) #del
        #bf.nnprt(value_tuple)#del
        mycursor.execute(DISPLAYING_FORMULA )
        
        data = mycursor.fetchall()
       # mycursor.commit()
        return data
    except:
       bf.easy_center_align("Sorry an error occured as there is no cart")
        

#delete_cart(username)
def decrease_quantity(value_tuple , quantity):
    
    """THis function decreases the quantity of the function whaen purchased"""
    try:
        
        p = str(value_tuple[3])
        check_quantity_formula = "SELECT quantity FROM inventory WHERE item_type = '" + value_tuple[0]  + "'  and   gender  = '" + value_tuple[1]  + "' and size  = '" + value_tuple[2] + "'and prize = '" + p+ "' and colour = '" + value_tuple[4] + "' and brand = '" + value_tuple[5] + "'"
        mycursor.execute(check_quantity_formula)
        data = mycursor.fetchall()
        quantity_available = int(data[0][0])
        final_quantity = int(quantity_available) - int(quantity)
        f = "UPDATE inventory  SET quantity = '"+ str(final_quantity) + "' WHERE item_type = '" + value_tuple[0]  + "'  and   gender  = '" + value_tuple[1]  + "' and size  = '" + value_tuple[2] + "'and prize = '" + p+ "' and colour = '" + value_tuple[4] + "' and brand = '" + value_tuple[5] + "'"
        mycursor.execute(f)
        mycon.commit()    
        #bf.hanprt("items_quantity fixed")
    except:
        bf.hanprt("Sorry an error occured in decreasing the quantiy")

        
def clear_cart(username):
    try:

        """THis function deletes all the items in the cart"""
        f = "DELETE FROM "+ str(username)  + "_cart"
        mycursor.execute(f)
        mycon.commit()    
        
    except:
        bf.hanprt("Sorry an error occured in clearing the cart")
        

def delete_empty_stock(value_tuple):
    """THis function deletes the empty stock when quantity becomes zero"""
    try:
     
        p = str(value_tuple[3])
        check_quantity_formula = "SELECT quantity FROM inventory WHERE item_type = '" + value_tuple[0]  + "'  and   gender  = '" + value_tuple[1]  + "' and size  = '" + value_tuple[2] + "'and prize = '" + p+ "' and colour = '" + value_tuple[4] + "' and brand = '" + value_tuple[5] + "'"
        mycursor.execute(check_quantity_formula)
        data = mycursor.fetchall()
        quantity_available = int(data[0][0])
        #final_quantity = int(quantity_available) - int(quantity)
        if quantity_available == 0:
            #f = "UPDATE inventory  SET quantity = '"+ str(final_quantity) + "' WHERE item_type = '" + value_tuple[0]  + "'  and   gender  = '" + value_tuple[1]  + "' and size  = '" + value_tuple[2] + "'and prize = '" + p+ "' and colour = '" + value_tuple[4] + "' and brand = '" + value_tuple[5] + "'"
            f = "DELETE FROM inventory  WHERE item_type = '" + value_tuple[0]  + "'  and   gender  = '" + value_tuple[1]  + "' and size  = '" + value_tuple[2] + "'and prize = '" + p+ "' and colour = '" + value_tuple[4] + "' and brand = '" + value_tuple[5] + "'"
            mycursor.execute(f)
            mycon.commit()
    except:
        bf.hanprt("Sorry an error occured in deleting the empty stocks")

def check_table(table_name):
    """This function gets the name of all the tables available in the database"""
    #mycursor.execute("SELECT Distinct TABLE_NAME FROM information_schema.TABLES where table_schema = 'tableowner'")
    try:
        mycursor.execute("SELECT * FROM information_schema.tables WHERE table_name = '"+ table_name +"'")
        data = mycursor.fetchall()
        if data == []:
            b = 0
        else:
            b = 1
        return b
    except:
        bf.hanprt("Sorry an error occured in checking the table")


def create_profile_table(username):
    """Creating user profile"""
    try:
        formula = "CREATE TABLE "+username  +"_profile (item_type VARCHAR(100) , gender CHAR(1) , size CHAR(4)  , prize DECIMAL , colour VARCHAR(20) , brand VARCHAR(100) , quantity INTEGER , amount DECIMAL , payment_mod VARCHAR(20) , date DATETIME )"
        
        mycursor.execute(formula)
        mycon.commit()
        
        bf.easy_center_align("New profile created.")
    except:
        #bf.hanprt("Sorry an error occured in creating the profile table")
        pass

        

def add_to_profile(value_tuple,username , payment_mod  ):
    """
    bf.nnprt(value_tuple)
    bf.nnprt(username)
    bf.nnprt(payment_mod)"""
    try:
        #bf.nnprt(date)
        """Add the items to the profile"""
        #INSERTION_FORMULA  = "INSERT INTO "+username  +"_profile (item_type , gender , size  , prize , colour , brand , quantity ,amount ,  payment_mod , date ) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}').format('"+str(value_tuple[0][0])+"','"+str(value_tuple[0][1])+"','"+str(value_tuple[0][2])+"','"+str(value_tuple[0][3])+"','"+str(value_tuple[0][4])+"','"+str(value_tuple[0][5])+"','"+str(value_tuple[0][6])+"','"+str(value_tuple[0][7])+"','"+str(payment_mod)+"','" + date+"')"
        INSERTION_FORMULA  = "INSERT INTO "+username  +"_profile (item_type , gender , size  , prize , colour , brand , quantity ,amount ,  payment_mod , date ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        value_list = list(value_tuple)
        value_list.append(payment_mod)
        value_list.append(datetime.datetime.now())
        value_tuple_2 = tuple(value_list)
        
        
        mycursor.execute(INSERTION_FORMULA,value_tuple_2)
        mycon.commit()

    except:
        bf.hanprt("Sorry an error occured in adding to profile")

def remove_from_cart(value_tuple , username):
    """This function removes item from cart
    f = "DELETE FROM "+ str(username)  + "_cart"
        mycursor.execute(f)
        mycon.commit()    """
    """
    #del_to_cart  = "DELETE FROM "+ username +"_cart (item_type , gender , size  , prize , colour , brand , quantity , amount) VALUES (%s ,%s , %s , %s , %s , %s , %s ,%s)"
    del_to_cart  = "DELETE FROM "+ username +"_cart (item_type , gender , size  , prize , colour , brand ) VALUES (%s ,%s , %s , %s , %s , %s """
    try:
        filter_0 = ""
        filter_1 = ""
        filter_2 = ""
        filter_3 = ""
        filter_4 = ""
        filter_5 = ""
        filter_6 = ""
        additional_statement = ""#where clause
        if value_tuple[0] != "":
            filter_0 = "item_type = '" + value_tuple[0]+ "' and "
        if value_tuple[1] != "":
            filter_1 = "gender = '" + value_tuple[1]+ "' and "
        if value_tuple[2] != "":
            filter_2 = "size = '" + value_tuple[2]+ "'  and "
        if value_tuple[3] != "":
            filter_3 = "prize = '" + value_tuple[3]+ "'  and "
        if value_tuple[4] != "":
            filter_4 = "colour = '" + value_tuple[4] + "'  and "
        if value_tuple[5] != "":
            filter_5 = "brand = '" + value_tuple[5] + "'  and "
        if value_tuple[6] != "":
            filter_6 = "quantity = '" + value_tuple[6]+ "'  and "

        if((value_tuple[0] != "") or (value_tuple[1] != "") or (value_tuple[2] != "") or (value_tuple[3] != "") or (value_tuple[4] != "") or (value_tuple[5] != "") or (value_tuple[6] != "")):
            additional_statement = "WHERE "

       
        
        DISPLAYING_FORMULA = "DELETE FROM "+ username +"_cart     " + additional_statement +filter_0 +filter_1 +filter_2 +filter_3 +filter_4 + filter_5 + filter_6
        d = DISPLAYING_FORMULA[0:-4]
        mycursor.execute(d)

        #mycursor.execute(del_to_cart , value_tuple)
        mycon.commit()    
        bf.random_pr_string(("Removed from cart","Item deleted from cart","Item removed to cart","Removed","Done","Deleted"))

    except:
        bf.hanprt("Sorry an error occured in removing from cart from database")

def items_available_to_remove(value_tuple , username):
    try:
        
        """filter_3 = ""
        filter_4 = ""
        filter_5 = ""
        filter_6 = ""
        if value_tuple[3] != "":
            filter_3 = " and prize = '" + value_tuple[3]+ "'"
        elif value_tuple[4] != "":
            filter_4 = " and colour = '" + value_tuple[4] + "'"
        elif value_tuple[5] != "":
            filter_5 = " and brand = '" + value_tuple[5] + "
            
                   


        #DISPLAYING_FORMULA = "SELECT item_type , gender , size  , prize , colour , brand FROM "+username+"_cart WHERE item_type = '" + value_tuple[0]  + "'  and   gender  = '" + value_tuple[1]  + "' and size  = '" + value_tuple[2] + "'"+ filter_3 +filter_4 + filter_5
        DISPLAYING_FORMULA = "SELECT * FROM "+username+"_cart" 
        mycursor.execute(DISPLAYING_FORMULA )
        
        data = mycursor.fetchall()
        print(data)
        return data"""
        filter_0 = ""
        filter_1 = ""
        filter_2 = ""
        filter_3 = ""
        filter_4 = ""
        filter_5 = ""
        filter_6 = ""
        additional_statement = ""#where clause
        if value_tuple[0] != "":
            filter_0 = "item_type = '" + value_tuple[0]+ "' and "
        if value_tuple[1] != "":
            filter_1 = "gender = '" + value_tuple[1]+ "' and "
        if value_tuple[2] != "":
            filter_2 = "size = '" + value_tuple[2]+ "'  and "
        if value_tuple[3] != "":
            filter_3 = "prize = '" + value_tuple[3]+ "'  and "
        if value_tuple[4] != "":
            filter_4 = "colour = '" + value_tuple[4] + "'  and "
        if value_tuple[5] != "":
            filter_5 = "brand = '" + value_tuple[5] + "'  and "
        if value_tuple[6] != "":
            filter_6 = "quantity = '" + value_tuple[6]+ "'  and "

        if((value_tuple[0] != "") or (value_tuple[1] != "") or (value_tuple[2] != "") or (value_tuple[3] != "") or (value_tuple[4] != "") or (value_tuple[5] != "") or (value_tuple[6] != "")):
            additional_statement = "WHERE "

       
        
        DISPLAYING_FORMULA = "SELECT * FROM "+username+"_cart     "   + additional_statement +filter_0 +filter_1 +filter_2 +filter_3 +filter_4 + filter_5 + filter_6
        d = DISPLAYING_FORMULA[0:-4]
        mycursor.execute(d)
        
        data = mycursor.fetchall()
        return data
    
    except :
        
        bf.easy_center_align("Sorry an error occured in finding the items available to buy")
        


            
