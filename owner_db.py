"""Database compability from the side of owner
    all basic functions can be seen here"""
import basic_functions as bf
import mysql.connector as sqltor
DB_PASS = "vanshmysql"
INSERTION_FORMULA  = "INSERT INTO inventory (item_type , gender , size  , prize , colour , brand , quantity) VALUES (%s ,%s , %s , %s , %s , %s , %s)"
try:
    #searching for the old database 
    mycon = sqltor.connect(host = "localhost",user ="root" , port = 3306 , passwd = DB_PASS , database = "autokb")
    
    #bf.easy_center_align("Started with the old database")
    mycursor = mycon.cursor()
except:

    #there is no databse creating a new one now
    mycon = sqltor.connect(host = "localhost",user ="root" , passwd = DB_PASS)
    
    bf.easy_center_align("Old database was not found creating a new one")
    mycursor = mycon.cursor()
    
    mycursor.execute("CREATE DATABASE  autokb")
    
    bf.easy_center_align("Database autokb created successfully")
    #mycursor.execute("USE DATABASE  autokb4")
    mycon.close()
    mycon = sqltor.connect(host = "localhost",user ="root" , port = 3306 , passwd = DB_PASS , database = "autokb")
    
    mycursor = mycon.cursor()
        
    mycursor.execute("CREATE TABLE inventory (item_type VARCHAR(100) , gender CHAR(1) , size CHAR(4)  , prize DECIMAL , colour VARCHAR(20) , brand VARCHAR(100) , quantity INTEGER)")
    bf.easy_center_align("Inventory created successfully")
    
    
    
"""
    
if mycon.is_connected():
    bf.easy_center_align("Connection established succesfully")
    
"""
#mycon.close()

def add_entire_stock(value_tuple):
    """Add entire stocks completely whole row
    bf.nnprt(value_tuple)
    bf.nnprt(type(value_tuple[0]))
    bf.nnprt(type(value_tuple[1]))
    bf.nnprt(type(value_tuple[2]))
    bf.nnprt(type(value_tuple[3]))
    bf.nnprt(type(value_tuple[4]))
    bf.nnprt(type(value_tuple[5]))
    bf.nnprt(type(value_tuple[6]))
    bf.nnprt(type(value_tuple))
    """
    try:
        mycursor.execute(INSERTION_FORMULA , value_tuple)
        #mycursor.commit()
        bf.random_pr_string(("New stock added successfully","New stock added","Stock added","Done"))
       # mycursor.execute("INSERT INTO inventory (item_type , gender , size  , prize , colour , brand , quantity) VALUES ((jean, m, 'm , 800 , blue , gucci , 4 ))")
        mycon.commit()
        
        #bf.nnprt(item_type , gender , size  , prize , colour , brand , quantity)
    except:
        bf.easy_center_align("Sorry an error occured in adding entire stock")
def show_stocks(value_tuple):
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

       
        
        DISPLAYING_FORMULA = "SELECT * FROM inventory     "  + additional_statement +filter_0 +filter_1 +filter_2 +filter_3 +filter_4 + filter_5 + filter_6
        d = DISPLAYING_FORMULA[0:-4]
        mycursor.execute(d)
        
        data = mycursor.fetchall()
       # mycursor.commit()
        return data
    except:
        bf.easy_center_align("Sorry an error occured in displaying stocks")

def check_and_add_new_stocks(value_tuple):
    try:
        """This function checks the table for a item and update its quantity if found else create a new one"""
        p = str(value_tuple[3])
        check_quantity_formula = "SELECT * FROM inventory WHERE item_type = '" + value_tuple[0]  + "'  and   gender  = '" + value_tuple[1]  + "' and size  = '" + value_tuple[2] + "'and prize = '" + p+ "' and colour = '" + value_tuple[4] + "' and brand = '" + value_tuple[5] + "'"
        mycursor.execute(check_quantity_formula)
        data = mycursor.fetchall()
        if data == []:
            """Creating a new item"""
            add_entire_stock(value_tuple)
        else:
            
            
            bf.hanprt("There is a same item already exisiting in the stocks so increasing its quantiy")
            increase_quantity(value_tuple , value_tuple[6])
    except:
        bf.hanprt("Sorry an error occured in adding new stocks")
        




def increase_quantity(value_tuple , quantity):
    
    """THis function decreases the quantity of the function whaen purchased"""
    try:
        
        p = str(value_tuple[3])
        check_quantity_formula = "SELECT quantity FROM inventory WHERE item_type = '" + value_tuple[0]  + "'  and   gender  = '" + value_tuple[1]  + "' and size  = '" + value_tuple[2] + "'and prize = '" + p+ "' and colour = '" + value_tuple[4] + "' and brand = '" + value_tuple[5] + "'"
        mycursor.execute(check_quantity_formula)
        data = mycursor.fetchall()
        quantity_available = int(data[0][0])
        final_quantity = int(quantity_available) + int(quantity)
        f = "UPDATE inventory  SET quantity = '"+ str(final_quantity) + "' WHERE item_type = '" + value_tuple[0]  + "'  and   gender  = '" + value_tuple[1]  + "' and size  = '" + value_tuple[2] + "'and prize = '" + p+ "' and colour = '" + value_tuple[4] + "' and brand = '" + value_tuple[5] + "'"
        mycursor.execute(f)
        mycon.commit()    
        bf.hanprt("Quantity increased.")
    except:
        bf.hanprt("Sorry an error occured in decreasing the quantiy")

        
        
def check_table(table_name):
    try:
        """This function gets the name of all the tables available in the database"""
        #mycursor.execute("SELECT Distinct TABLE_NAME FROM information_schema.TABLES where table_schema = 'tableowner'")
        mycursor.execute("SELECT * FROM information_schema.tables WHERE table_name = '"+ table_name +"'")
        data = mycursor.fetchall()
        if data == []:
            b = 0
        else:
            b = 1
        return b
    except:
        bf.hanprt("Sorry an error occured in checking the table")
        
def get_data_of_profile(username):
    """THis function gets the data from profile of the user"""
    try:
        if check_table(username+"_profile"):
        
            DISPLAYING_FORMULA = "SELECT * FROM "+username+    "_profile"
            
            mycursor.execute(DISPLAYING_FORMULA)
            
            data = mycursor.fetchall()
           # mycursor.commit()
            return data
        else:
            bf.hanprt("No such rercord of customer exists in the database")
            data = []
            return data

    except:
        bf.hanprt("Sorry an error occured in getting data of profile")

        
