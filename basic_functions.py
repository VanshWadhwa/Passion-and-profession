import os
import time as t
import re
from random import randint
handler  = "OWNER"# this variable tell to who you are talking to at this time
MAX_WIDTH = 130    

def nprt(text):
    for i in text:
        print(i,end="")
        t.sleep(0.04)
    print()

attribute_of_item_type_r = {r"jean(s)?" ,r"pant(s)?" , r"shirt(s)?"  , r"t(-)?shirt(s)?" , r"top(s)?"}
attribute_of_gender_r = {  r"boy(s)?" , r"girl(s)?",
                        r"male(s)?" , r"female(s)?" ,  r"m(a|e)n" ,  r"w(o|e)men?",
                         r"gent(s)?", r"lad(y|ies)?" }
attribute_of_size_r = { r"size (s|m|l|xl|xxl|xxxl|)" }

attribute_of_prize_r = {r"prize (\d+)"}

attribute_of_colour_r = {r"colour (\w+)"}

attribute_of_quantity_r = {r"quantity (\d+)"}

attribute_of_brand_r = {r"brand (\w+)"}



def retrieve_attribute_value(reg_n_set):
    try:
        if(reg_n_set == set()):
            attribute_value = ""
            
        else:
            
            t = reg_n_set.pop()
            
            
            """This functions takes the grouped regex and gets the value stored in the suitale value"""
            
            if(re.match(r" boy(s)?",t) or re.match(r" male(s)?",t) or re.match(r" m(a|e)n",t) or re.match(r" gent(s)?",t)):
                attribute_value = "m"
                
            elif(re.match(r" girl(s)?",t) or re.match(r" female(s)?",t) or re.match(r" w(o|e)men",t) or re.match(r" lad(y|ies)",t)):
                attribute_value = "f"
                    
            elif(re.match(r" jean(s)?",t)):
                attribute_value = "jean"
                
            elif(re.match(r" pant(s)?",t)):
                attribute_value = "pant"
            elif(re.match(r" shirt(s)?",t)):
                attribute_value = "shirt"
            elif(re.match(r" t(-)?shirt(s)?",t)):
                attribute_value = "tshirt"
            elif(re.match(r" top(s)?",t)):
                attribute_value = "top"
            elif(re.match(r" colour (\w+)",t)):
                s = t[8:-1]
                attribute_value = s
            elif(re.match(r" prize (\d+)",t)):
                s = t[7:-1]
                attribute_value = s
            elif(re.match(r" brand (\w+)",t)):
                s = t[7:-1]
                attribute_value = s
            elif(re.match(r" quantity (\d+)",t)):
                s = t[10:-1]
                attribute_value = s    
            elif(re.match(r" size (s|m|l|xl|xxl|xxxl|)",t)):
                s = t[6:-1]
                attribute_value = s

        return attribute_value
    except:
        hanprt("Sorry an error occured in retrieving attributes")

def random_pr_string(value_tuple):
    try:
        hanprt(value_tuple[randint(0,(len(value_tuple)-1))])
    except:
        hanprt("Sorry an error occured in random print string")



        
def get_attribute(text):
    """This function scans the  text and if attributes are found get the attribute and retrieve its value from another function"""
    try:
        item_type = retrieve_attribute_value(scan_n(attribute_of_item_type_r , text))
        gender = retrieve_attribute_value(scan_n(attribute_of_gender_r , text))
        size = retrieve_attribute_value(scan_n(attribute_of_size_r , text))
        prize = retrieve_attribute_value(scan_n(attribute_of_prize_r , text))
        colour = retrieve_attribute_value(scan_n(attribute_of_colour_r , text))
        brand = retrieve_attribute_value(scan_n(attribute_of_brand_r , text))
        quantity = retrieve_attribute_value(scan_n(attribute_of_quantity_r , text))
         
        return item_type , gender , size  , prize , colour , brand , quantity
    except:
        hanprt("Sorry an error occured in getting attributes")
        

def ask_input():
    """Ask the input and returns it in the special manner"""
    try:
        u_input  = input(" You : ").lower()
        return u_input
    except:
        easy_center_align("Sorry an error occured.Please try againt")
        ask_input()

    
def hanprt(text):
    #this is the function to print with the name of the handler
    print(" "  + handler + " : " , end ="")
    nprt(text)

    
def line(char , width_limit):
    #a basic function to create lines
    for i in range(width_limit):
        print(char , end="")
    print()
    
def center_line(text):
    #this is the function to enter string in the middle in the bill
    print("|" , end = "")
    for i in range(((MAX_WIDTH)-len(text))//2):
        print("." , end = "")
    print(text , end= "")
    for i in range(((MAX_WIDTH)-len(text))//2):
         print("." , end = "")
    print("|")


def  easy_center_align(text):
    #thsi function aligns the text in middle in this format
        #*Your profile is getting verified*
    for i in range(((MAX_WIDTH)-len(text))//2):
        print(" " , end = "")
    print("*"  , text ,"*"  , end= "")
    for i in range(((MAX_WIDTH)-len(text))//2):
         print(" " , end = "")
    print()
    

def display_output(text):
    """Displays the text in with a space in front"""
    new_text = text.split("\n")
    for i in new_text:
        print(" " , i)
    
def scan_r(kwd_set , text):
    """SCANs the user input and returns the matched set in the regex set form"""

    matched_set = set()#declaration of the empty set of main keywords from the text/input from the user
    
    for kw in kwd_set:
        if re.search(" " + kw + " "," " + text + " "):
            matched_set.add(kw)
    return matched_set

def scan_n(kwd_set , text):
    """SCANs the user input and returns the matched set in the normal set of normal text form"""

    matched_set = set()#declaration of the empty set of main keywords from the text/input from the user

    for kw in kwd_set:
        if re.search(" " + kw + " "," " + text + " "):
            m = re.search(" " + kw + " "," " + text + " ")
            matched_set.add(m.group())
        
                 
    return matched_set


def ask_gender():
    try:
        random_pr_string(("For which gender you want to specify your item?","Gender?","For which gender"))
        gender = ask_input()
        if(gender == "m") or (gender == "f") or (re.search(r" boy(s)? "," " + gender + " ")) or (re.search(r" girl(s)? "," " + gender + " ")) or (re.search(r" male(s)? "," " + gender + " ")) or (re.search(r" female(s)? "," " + gender + " ")) or (re.search(r" m(a|e)n(s)? "," " + gender + " ")) or (re.search(r" w(o|e)men(s)? "," " + gender + " ")) or (re.search(r" gent(s)? "," " + gender + " ")) or (re.search(r" lad(y|ies) "," " + gender + " ")):
            if  (gender == "m") or   (re.search(r" boy(s)? "," " + gender + " "))  or (re.search(r" male(s)? "," " + gender + " ")) or (re.search(r" m(a|e)n(s)? "," " + gender + " ")) or  (re.search(r" gent(s)? "," " + gender + " "))  :
                gender = "m"
            elif  (gender == "f")  or (re.search(r" girl(s)? "," " + gender + " "))  or (re.search(r" female(s)? "," " + gender + " ")) or (re.search(r" w(o|e)men(s)? "," " + gender + " ")) or (re.search(r" lad(y|ies) "," " + gender + " ")):
                gender = "f"
            return gender
        else:
            hanprt("Invalid option , Please try again (Male/Female)(m/f)")
            
        return ask_gender()
    except:
        easy_center_align("Sorry an error occured.Please try again")
        ask_gender()
        
def ask_size():
    try :
        random_pr_string(("Of what size ?","Size?","For which size"))
        size = ask_input()
        if (size =="s") or (size =="m") or (size =="l") or (size =="xl") or (size =="xxl") or (size =="xxxl") :
            return size
        else:
            hanprt("Invalid option , Please try again (S/M/L/XL/XXL/XXXL)")
            
        return ask_size()
    except:
        easy_center_align("Sorry an error occured.Please try again")
        ask_size()

def ask_colour():
    try:
        random_pr_string(("Whats the colour of the item ?","Colour?","Of which colour?"))
        colour = ask_input()
        return colour
    except:
        easy_center_align("Sorry an error occured.Please try again")
        ask_colour()

def ask_brand():
    try:
        random_pr_string(("Of which brand it belongs to ?","Brand?","Of which brand?"))
        brand = ask_input()
        return brand
    except:
        easy_center_align("Sorry an error occured.Please try again")
        ask_brand()

def ask_item_type():
    try:
        random_pr_string(("Type of item?","Item type?","Which type the item belongs"))
        item_type = ask_input()
        

        if((re.match(r"jean(s)?",item_type)) or (re.match(r"pant(s)?",item_type)) or (re.match(r"shirt(s)?",item_type)) or (re.match(r"t(-)?shirt(s)?",item_type)) or (re.match(r"top(s)?",item_type))):
            
            
            if(re.match(r"jean(s)?",item_type)):
                item_type = "jean"
                    
            elif(re.match(r"pant(s)?",item_type)):
                item_type = "pant"
            elif(re.match(r"shirt(s)?",item_type)):
                item_type = "shirt"
            elif(re.match(r"t(-)?shirt(s)?",item_type)):
                item_type = "tshirt"
            elif(re.match(r"top(s)?",item_type)):
                item_type = "top"
            return item_type
        else:
            """nothing"""

        return ask_item_type()
    except:
        easy_center_align("Sorry an error occured.Please try again")
        ask_item_type()
            
            
        


def ask_prize():
    try:
        random_pr_string(("Please tell me the prize?","Prize?","Whats the prize?"))
        prize = int(ask_input())
        if (prize == 0) :
            hanprt("Wow , You want your item to cost free")
             
        elif (prize < 0 ):
            hanprt("Prize cannot be in negative")
            
        else:
            return prize
        return ask_prize()
    except:
        easy_center_align("Sorry an error occured.Please try again with direct input")
        ask_prize()
        
def ask_quantity():
    try:
        random_pr_string(("What's the  quantity ?","Quantity?","Please tell me the quantity?"))
        quantity = int(ask_input())
        if (quantity == 0) :
            hanprt("Quantity cannot be equal to zero.")
             
        elif (quantity < 0 ):
            hanprt("Quantity cannot be in negative")
        else:
            return quantity
        return ask_quantity()
    except:
        easy_center_align("Sorry an error occured.Please try again with direct input")
        ask_quantity()
 
    



def left_align(text,limit):
    """This function aligns the text in left in a column"""
    string = text
    if(len(str(text)) < limit):
        string = text
        

    else:
        string = string[0:-(limit-2)]+"."

    for i in range((limit-(len(text)))):
            string += "_"

    return string


def merge_tuple_value(merge_to,merge_from):
    """THis function merges two tuples with empty values"""
    list_to = list(merge_to)
    list_from = list(merge_from)

    if list_to[0] == "":
        list_to[0] = list_from[0]
    if list_to[1] == "":
        list_to[1] = list_from[1]
    if list_to[2] == "":
        list_to[2] = list_from[2]
    if list_to[3] == "":
        list_to[3] = list_from[3]
    if list_to[4] == "":
        list_to[4] = list_from[4]
    if list_to[5] == "":
        list_to[5] = list_from[5]
    if list_to[6] == "":
        list_to[6] = list_from[6]

    new_tuple = tuple(list_to)
    return new_tuple           

    
        
    
def append_file(text , file):
    """This function appends the text to the file"""
    try:
    
        file.write(text + "\n")
        return text
    except:
        easy_center_align("Sorry an error occured.File may be deleted")

def nnprt(text):
    """Normal print used for cross platform"""
    print(text)

def  center_align(text , w):
    #thsi function aligns the text in middle in this format
        #*Your profile is getting verified*
    """
    for i in range(((MAX_WIDTH)-len(text))//2):
        print(" " , end = "")
    print("*"  , text ,"*"  , end= "")
    for i in range(((MAX_WIDTH)-len(text))//2):
         print(" " , end = "")
    print()"""
    
    text = str(text)
    s = ""
    if (len(text) %2)== 0 :
        #even
        for i in range(((w)-len(text))//2):
            #print(" " , end = "")
            s +="_"
        #print(text  , end= "")
        s += text
        for i in range(((w)-len(text))//2):
             #print(" " , end = "")
            s+="_"
    else:
        for i in range((((w)-len(text))//2)-1):
            s+="_"
            #print(" " , end = "")
        #print(text  , end= "")
        s+=text
        for i in range((((w)-len(text))//2)+1):
             #print(" " , end = "")
            s+="_"

    return s
    
    
        

