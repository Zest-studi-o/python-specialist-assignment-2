
kitty = 500
requests = []
file = open('loan_requests.txt')

for line in file:
    if line.strip().isdecimal():
        requests.append(int(line))
    
file.close()


with open('loan_requests.txt', 'a') as file:

    for request in requests:
    
        if request <= kitty:
            file.write('\nRequest of ' + str(request) + ' paid in full.')
            print(str(request) + ' - Paid!')
            kitty -= request

        elif kitty > 0:
            print(request, 'request cannot be processed in full (Insufficient funds available). Amount paid:', kitty)
            file.write('\nRequest of ' + str(request) + ' could not be paid in full.Partial payment of ' + str(kitty) + ' made.')
            kitty -= kitty
            
        else:
            print('Request of ' + str(request) + ' is UNPAID!')
            file.write('\nOutstanding Request:' + str(request))
