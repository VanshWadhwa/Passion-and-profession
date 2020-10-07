import basic_functions as bf
import re

def m(t , u_input):
    if re.search(" " + u_input + " "," " + t + " "):
        return 1
    else:
        return 0

def chat(t):
    """This function chats with the user """
    if m(t,r"hi") or m(t,r"hello") or m(t,r"hey") or m(t,r"hello") or m(t,r"hlo") or m(t,r"hello"):
        bf.random_pr_string(("Hey","Hlo","Hey..How are you?","Hi..How are you?" ,"Hello..How can I help you? ","Hi...What can i do for you?" , "Hi..","Nice to see you"))
    elif (m(t,r"how") and m(t,r"you(r)?") ):
        bf.random_pr_string(("I am fine...How are you?","Fine","I am fine...What about you?","As usual...Fine","I am nice","Fine...Thanks for asking"))
    elif (m(t,r"what(')?(s)?") and m(t,r"name")) or (m(t,r"who") and m(t,r"you(r)?")):
        bf.hanprt("Hey I am AutoKB...How can I help you?")
    elif((m(t,r"what") and m(t,r"do")) or (m(t,r"help")) or m(t,r"command(s)?")):
        bf.hanprt("I am here to help you...I can help you in many ways")
        bf.hanprt("Try asking me to display items by saying 'I WANT TO BUY...")
        bf.hanprt("'ADD TO CART' to add to cart")
        bf.hanprt("'BILL' to start you billing")
        bf.hanprt("ADD TO CART' to add to cart")
        bf.hanprt("Ya its that simple'")
    elif(m(t,r"thank(s)?") or m(t,r"thank(-| )you")):
         bf.random_pr_string(("Welcome" , "I am glad to hear that from you"))
    elif(m(t,r"shut up") or (m(t,r"close") and m(t,r"mouth"))):
         bf.hanprt("I am sorry if I offended you")
    elif(m(t,r"awesome") or m(t,r"fine") or m(t,r"good") or m(t,r"nice") or m(t,r"osm") or m(t,r"beauiful(l)?") or m(t,r"liked(d)?" )or m(t,r"wonderful(l)?") or m(t,r"fantastic")or m(t,r"fabulous") or m(t,r"amazing") or m(t,r"lovely") or m(t,r"unique") or m(t,r"suberb") or m(t,r"super")  or m(t,r"great(s| work)?"))  :
         bf.random_pr_string(( "Thanks" , "Good" , "Nice" , "Huh" ,"Hmmm" , "Glad to here"))
    elif(m(t,r"bye(e|ee|eee|eeee)?") or m(t,r"go")):
         bf.random_pr_string(("Bye...See you afterwards" , "Bye...Bye...Bye..." , "See you later"))
    elif(m(t,r"you") and m(t,r"can")):
         bf.random_pr_string(("No.I cannot" , "Let me guess......No." , "What do you think?","May be..." ,"But i will some day"))
    elif(m(t,r"aw(w|ww|www|wwww)?") or m(t,r"hm(m|mm|mmm|mmmm)?")):
         bf.random_pr_string(("I literally hate it." , "Please don't say this again" , "What do you think?","May be..." ,"But i will some day"))
    elif(m(t,r"no") or m(t,r"never") or m(t,r"yes") or m(t,r"may be") ):
        bf.random_pr_string(("Ok...","Hmmm","No Problem"))
    elif(m(t,r"available")):
        bf.hanprt("We have Items - Jeans,Shirts,T-shirts,Tops,Pants")
        bf.hanprt("We have Sizes - S to XXXL")
        bf.hanprt("For both Boys and Girls")
    elif(m(t,r"sorry")):
        bf.random_pr_string(("Its ok..","No problem","Np","I don't have any problem"))
    elif(m(t,r"o(o|oo|ooo|oooo)?k(kk|kkk|kkkk)?") or m(t,r"o(o|oo|ooo|oooo)?k(kk|kkk|kkkk)?a(aa|aaa|aaaa)?y(y|yy|yyy|yyyy)?") or m(t,r"k")) or m(t,r"oh(h|hh|hhh|hhhhh)?"):
        bf.random_pr_string(("Hmmm","Ok","Okay"))
    elif(m(t,r"so") and m(t,r"what(s)?")):
         bf.hanprt("You quess what")
    elif(m(t,r"what(s)?") or m(t,r"when(s)?") or m(t,r"where(s)?") or m(t,r"who(s|se)?")):
         bf.random_pr_string(("Please you tell me....I am just a beta version","Sorry i am new to this world...can't say anything","No answer","No guesses","Sorry i don't know"))
    elif(m(t,r"favourite")):
         bf.hanprt("Sorry but algorithm don't let me choose something....")
    
    elif(m(t,r"who(s)?") and m(t,r"ma(de|ke)")  ):
         bf.hanprt("I master INFINITY made me")
    elif(m(t,r"when(s)?") and m(t,r"b(orn|irth)")):
        bf.hanprt("I was not born...I was an idea which is in front of you")
    elif  m(t,r"foolish(s)?") or m(t,r"looser(s)?") or m(t,r"idiot(s)?") or m(t,r"stupid(s)?") or m(t,r"dumb(s)?"):
        bf.random_pr_string(("No.","No you are.","Same to you."))
    elif((m(t,r"have") or (m(t,r"keep")))) and (((m(t,r"have")))) and (((m(t,r"jean(s)?")) or (m(t,r"pant(s)?")) or (m(t,r"shirt(s)?"))  or (m(t,r"t(-)?shirt(s)?")) or m(t,r"top(s)?"))) and (m(t,r"you(r)?")):
         bf.hanprt("Yes,We have this item available.")
         bf.hanprt("If you want to buy,ask me 'I WANT TO BUY...'")
    elif((m(t,r"have") or (m(t,r"keep")))) and (((m(t,r"have")))) and (m(t,r"you(r)?")):
         bf.hanprt("Sorry , we don't have this item available.")
         bf.hanprt("But we have jeans,pants,t-shirts,shirts and tops for girls.'")
    
    

                   
    else:
         bf.random_pr_string(("Sorry I cannot recorgnised your command","Sorry please try to rephrase your command" ,"Please try to rephrase","Sorry I did not understand","Ask me again in another manner","If you don't know the commands ask me for HELP"))
                             
    
          
        


    

    
