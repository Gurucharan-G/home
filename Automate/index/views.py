from django.shortcuts import render
from Adafruit_IO import Client        #import client from Adafruit IO

aio=Client('gurucharan9499','9f64ac6b6f7a475a8b124b53fb388c3b')     #copy paste the user_ID and Key from adafruit_io


"""Create 2 variables for each device, 
one keeps the integer value other keeps string value"""

Light_1_State=0
Light_1_Var='off'
Light_2_State=0
Light_2_Var='off'


def home(request):  
    if 'Light_1' in request.POST:       #check which switch is pressed by its name(given in HTML Page/code)

        #declare the 2 variables which you created earlier as global
        global Light_1_State
        global Light_1_Var

        
        Light_1_State=int(not(Light_1_State))       #change the state of Light by doing NOT operation and convert into integer
        aio.send('relay1',Light_1_State)            #send the new data to adafruit_io by specifying its ("feed_name", variable)
        if Light_1_State==0:Light_1_Var='off'       #converting integer data to ON and OFF, to display on webpage
        else: Light_1_Var='on'

        """---------------------------the same is reapeated to multiple switches--------------------------------"""


    elif'Light_2' in request.POST:
        global Light_2_State
        global Light_2_Var
        Light_2_State=int(not(Light_2_State))
        aio.send('relay2',Light_2_State)
        if Light_2_State==0:Light_2_Var='off'
        else: Light_2_Var='on'


        #after finishing with each switches return a webpage with variables
        #the below line returns the same webpage with 2 variables, which contain 
        # either ON or OFF, and its passes using ginjja format

    return render(request,"home.html",{"Light_1_Var":Light_1_Var,"Light_2_Var":Light_2_Var}) 