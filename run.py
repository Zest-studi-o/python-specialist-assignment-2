
requests = []

#Available cash
kitty = 500

#Open request file read mode
requests = open('loan_requests.txt', "r+")
#Read request - readlines entire list to work with
data = requests.readlines()

"""
Split into lines
Stackoverflow suggestion for converting contents of a file to int from string
https://stackoverflow.com/questions/32478533/python-converting-contents-of-a-file-to-int-from-string
"""

for line in data:
  splitted_line = line.split()
  for values in splitted_line: #value can be converted to int
    # ... do something with value now
    print("Cash in the pot:", kitty)
    
    if (int(values) <= kitty):
      kitty -= int(values)
      print(int(values), "- Paid!\n")
      # Can only pass one argument, concatenate strings instead of using int conversion"
      requests.write("Loan amount requested "+str(values)+ " paid in full.\n" )

    elif (int(values) > kitty and kitty > 0):
      print(int(values),"requested cannot be processed in full.(Insufficient funds available)\n")
      requests.write("Request of "+str(values)+" could not be made in full. "
      "Partial payment of "+str(kitty)+" made.\n")
      kitty = 0

    else:
      print("Request of",values,"is UNPAID.\n")
      requests.write("Outstanding request: "+str(values)+"\n")
  
    
  
