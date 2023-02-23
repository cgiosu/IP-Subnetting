from prettytable import PrettyTable
import auxiliary_functions

### The function for. The inputs are number of subnets, 
### a list of number of hosts in each subset, method determining fixed or variable length subnet masks ('F' for fixed , 'V' for variable), 
### choice to use a specific address ('Y' to use a specific address, 'N' to automatically assign), and
### a specific network address to use if entered by the user.

def subnet(num_subnets: int , size_hosts : list , method : str , choice : str , address :str):

    ### We begin with calculating the required block sizes and ordering them from largest to smallest if we are using variable lengths.
    if method == 'V':
        mod_size_hosts = [[2 ** (len(bin(1+size_hosts[i])) - 2) , i] for i in range(num_subnets)]
        mod_size_hosts.sort(reverse = True)
    else:
        mod_size_hosts = [[2 ** (len(bin(1 + max(size_hosts))) - 2) , i] for i in range(num_subnets)]
        
    ### Automatic assignment of the network address depends on the total number of the block sizes. If we were given a specific a network address, then we should 
    ### convert the network portion of the given 32 bits into a decimal for computational purposes.
    sum_blocks = sum(block[0] for block in mod_size_hosts)
    if choice == 'N':
        if sum_blocks <= 2 ** 8:
            ### Class C network address is needed
            net_address = 192 * (2 ** 24) + 168 * (2 ** 16)
        elif sum_blocks <= 2 ** 16:
            ### Class B network address is needed.
            net_address = 172 * (2 ** 24) + 16 * (2 ** 16)
        elif sum_blocks <= 2 ** 24:
            ### Class A network address is needed.
            net_address = 10 * (2 ** 24)
        else:
            ### It is not possible to subnet with given arguments
            print('\n It is not possible to subnet, please try again with smaller number of hosts. \n')
            return
    else:
        ### If the total block size is too large, ask user to try again.
        if sum_blocks > 2 ** (32 - int(address.split('/')[1])):
            print('\n It is not possible to subnet, please try again with smaller number of hosts or smaller number of bits reserved for the network portion.\n')
            return
        else:
            net_address = auxiliary_functions.net_ip_str_to_int(address)

    ### We are finding the S/N Address, S/N Mask, Boradcast Address, and Range of Host Addresses for each subnet and add them to a list.
    pre_answer = []
    for subnet in mod_size_hosts:
        nextrow = []
        ### S/N No
        nextrow.append(subnet[1])
        ### S/N Address
        nextrow.append(auxiliary_functions.ip_int_to_octets(net_address))
        ### S/N Mask
        nextrow.append(auxiliary_functions.ip_int_to_octets(2 ** 32 - subnet[0]))
        ### Broadcast Address
        nextrow.append(auxiliary_functions.ip_int_to_octets(net_address + subnet[0] - 1))
        ### Range of Host Addresses
        nextrow.append(auxiliary_functions.ip_int_to_octets(net_address + 1) + '-' + auxiliary_functions.ip_int_to_octets(net_address + subnet[0] - 2))
        ### We should set net_address to the S/N address of the next subnet and add nextrow to the list pre_answer
        net_address += subnet[0]
        pre_answer.append(nextrow)

    ### We are ordering the rows of pre_answer by S/N No (necessary only if we are using variable length) and print it in the answer table
    if method == 'V':
        pre_answer.sort()
    answer = PrettyTable()
    answer.field_names = ["S/N No", "S/N Address", "S/N Mask", "Broadcast Address", "Range of Host Addresses"]
    for row in pre_answer:
        answer.add_row(row)
    print('\n Please find the IP assignments below: \n')
    print(answer)
    return
