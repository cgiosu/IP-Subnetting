import inflect , subnetting, auxiliary_functions

### For printing the ordinal numbers
p = inflect.engine()

while True:
    ### Asking whether to use Classful or Classless Subnetting 
    while True:
        method = input('\n Enter F for Fixed Length (Classful) Subnetting and V for Variable Length (Classless) Subnetting: \n').upper()
        if method == 'F':
            print('\n Fixed length subnet masks will be used. \n')
            break
        elif method == 'V':
            print('\n Variable length subnet masks will be used. \n')
            break
        else:
            print('\n The response is invalid, please enter F or V. \n')

    ### Asking if the user would like to use the network portion of a specific IP address
    while True:
        choice = input('\n Would you like to provide a specific network address to use in subnetting? Please enter Y or N. \n').upper()
        if choice == 'N':
            address = ''
            break
        elif choice == 'Y':
            while True:
                address = input('Please enter an IP address in CIDR notation such as 192.168.10.2/24. The network portion of the address will be used in subnetting. \n')
                if not auxiliary_functions.is_ip_valid(address):
                    print('\n The response is invalid, please enter a valid IP address in CIDR notation \n')
                else:
                    break
            break
        else:
            print('\n The response is invalid, please enter Y or N. \n')

    ### The number of subnets is asked
    while True:
        num_subnets_str = input('\n Please enter the number of the subnets? \n')
        try:
            num_subnets = int(num_subnets_str)
            if num_subnets > 0:
                break
            else:
                print('\n Please enter a positive integer. \n')
        except ValueError:
            print('\n The response is invalid, please enter an integer. \n')

    ### The number of the hosts in each subnet are asked from the user and stored in a list
    size_hosts = []
    for i in range(num_subnets):
        while True:
            new_size_str = input('\n Please enter the number of the hosts in the ' + p.ordinal(i) + ' subnet: \n')
            try:
                new_size = int(new_size_str)
                if new_size > 0:
                    size_hosts.append(new_size)
                    break
                else:
                    print('\n Please enter a positive integer. \n')
            except ValueError:
                print('\n The response is invalid, please enter an integer. \n')

    ### Running the subnetting (and asking the user if they want to run it again)
    subnetting.subnet(num_subnets, size_hosts, method, choice, address)
    while True:
        response = input('\n Please enter 1 to exit the program or enter 2 to run the program again: \n')
        if response == '1':
            print('\n Exiting now...... \n')
            break
        elif response == '2':
            print('\n Running the program again. \n')
            break
        else:
            print('\n The response is invalid.\n')
    if response == '1':
        break

