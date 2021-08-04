import pywhatkit as W
  
# using Exception Handling to avoid 
# unprecedented errors

try:

  # sending message to reciever
  # using pywhatkit
  W.sendwhatmsg("+917042244006","Okay Ma I'll do that and you be safe.",12,1)
  print("Successfully Sent!")

except:
    
  # handling exception 
  # and printing error message
  print("An Unexpected Error!")
