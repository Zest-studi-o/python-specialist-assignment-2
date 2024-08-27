
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
    #print("Cash in the pot:", kitty - int(values))
    print("Cash in the pot:", kitty)
    print("Loan amount requested:", int(values))

    if (int(values) <= kitty):
      kitty -= int(values)
      print("Loan amount granted!")
      

    elif (int(values) > kitty and kitty > 0):
      print("The exact loan request amount cannot be processed" 
      "in full, however, we will give you what we can ", kitty)
      kitty = 0

    else:
      print("No more money") 
    
  
