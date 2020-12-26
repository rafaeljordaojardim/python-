
import random
import sys

def subnet_calc():
    try:
        print("\n")

        # check ip address vadility
        while True:
            ip_address = input("Enter an IP address: ")

            #checking octets
            ip_octets = ip_address.split(".")

            if (len(ip_octets) == 4) and (1 <= int(ip_octets[0]) <= 223) and (int(ip_octets[0]) != 127) and (int(ip_octets[0]) != 169 or int(ip_octets[1]) != 254) and (0 <= int(ip_octets[1]) <= 255 and 0 <= int(ip_octets[2]) <= 255 and 0 <= int(ip_octets[3]) <= 255):
                break
            else:
                print("\nThe IP address is INVALID! Please retry!\n")
                continue
        
        masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]

        # checking SUbnet Mask vadility
        while True:
            # checking octets
            subnet_mask = input("Enter a subnet mask: ")

            mask_octets = subnet_mask.split(".")

            if (len(mask_octets) == 4) and (int(mask_octets[0]) == 255) and (int(mask_octets[1]) in masks) and (int(mask_octets[2]) in masks) and (int(mask_octets[3]) in masks) and (int(mask_octets[0]) >= int(mask_octets[1]) >= int(mask_octets[2]) >= int(mask_octets[3])):
                break
            else:
                print("\nThe subnet mask is INVALID! Please retry!\n")
                continue
        # Algorithm for subnet indentification, based on IP and subnet Mask
        #convert mask to binary string
        mask_octers_binary = []

        for octet in mask_octets:
            binary_octet = bin(int(octet)).lstrip('0b')
            print(binary_octet)
            mask_octers_binary.append(binary_octet.zfill(8))
        
        print(mask_octers_binary)
        binary_mask = "".join(mask_octers_binary)
        # Example for 255.255.255.0 => 11111111111111111111111100000000

        #counting host bits in the mask and calculating number of hosts/subnet
        no_of_zeros = binary_mask.count("0")
        no_of_ones = 32 - no_of_zeros
        no_of_hosts = abs(2 ** no_of_zeros - 2) # return positive value for the /32 mask (all 255s)

        print(no_of_zeros)
        print(no_of_ones)
        print(no_of_hosts)

        wildcard_octets = []

        for octet in mask_octets:
            wild_octet = 255 - int(octet)
            wildcard_octets.append(str(wild_octet))
        # print(wildcard_octets)

        wildcard_mask = ".".join(wildcard_octets)

        # converting ip to binary string
        ip_octets_binary = []

        for octet in ip_octets:
            binary_octet = bin(int(octet)).lstrip('0b')
            ip_octets_binary.append(binary_octet.zfill(8))

        binary_ip = "".join(ip_octets_binary)

        #Example: for 192.168.2.100 => 110000001010100000000101000000001

        # Getting the network address and broadcast address from the binary strings abtained above

        network_address_binary = binary_ip[:(no_of_ones)] + "0" * no_of_zeros

        broadcast_address_binary = binary_ip[:(no_of_ones)] + "1" * no_of_zeros

        # converting everything back to decimal (readable format)
        net_ip_octets = []

        # range(0, 32, 8) means 0, 8, 16, 24
        for bit in range(0, 32, 8):
            net_ip_octet = network_address_binary[bit: bit + 8]
            net_ip_octets.append(net_ip_octet)

        # we will end up with 4 slices of the binary IP address: [0:8], [8:16], [16:24] and [24:32]
        # remember that each slice goes up to, but not including the index on the right side of the

        print(net_ip_octets)

        net_ip_address = []

        for each_octet in net_ip_octets:
            net_ip_address.append(str(int(each_octet, 2)))

        network_address = ".".join(net_ip_address)

        bst_ip_octets = []

        # range(0, 32, 8) means 0, 8, 16, 24
        for bit in range(0, 32, 8):
            bst_ip_octet = broadcast_address_binary[bit: bit + 8]
            bst_ip_octets.append(bst_ip_octet)
        
        bst_ip_address = []

        for each_octet in bst_ip_octets:
            bst_ip_address.append(str(int(each_octet, 2)))

        broadcast_address = ".".join(bst_ip_address)

        #Results for selected IP/mask
        print("\n")
        print("Network address is: %s" % network_address)
        print("Broadcast address is: %s" % broadcast_address)
        print("Number of valid hosts per subnet: %s" % no_of_hosts)
        print("Wildcard mask: %s" % wildcard_mask)
        print("Mask bits: %s" % no_of_ones)
        print("\n")

        # generation of ramdom ip addresses in the subnet
        while True:
            generate = input("Generate random IP address from this subnet? (y/n) ")

            if generate == "y":
                generated_ip = []

                # obtain available IP address in range, based on the difference between octets in broadcast address and network address
                for indexb, oct_bst in enumerate(bst_ip_address):
                    for indexn, oct_net in enumerate(net_ip_address):
                        if indexb == indexn:
                            if oct_bst == oct_net:
                                # add identical octets to the generated_ip list
                                generated_ip.append(oct_bst)
                            else:
                                # generate random number(s) from within octet intervals and append to the list
                                generated_ip.append(str(random.randint(int(oct_net), int(oct_bst))))
                # IP address generated from the subnet pool
                y_iaddr = ".".join(generated_ip)

                print("Random IP address is: %s" % y_iaddr)
                print("\n")
                continue
            else:
                print("bye")
                break
    except KeyboardInterrupt:
        print("\n\nProgram aborted by user. Exiting...\n")
        sys.exit()

subnet_calc()