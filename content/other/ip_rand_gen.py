import random
def ip_rand_gen2(amount):
    list = open('content/console/ip_list.txt','w')
    while amount >> 0:
        ip_1 = random.randint(0, 255)
        ip_2 = random.randint(0, 255)
        ip_3 = random.randint(0, 255)
        ip_4 = random.randint(0, 255)
        ip = '%r.%r.%r.%r' % (ip_1, ip_2, ip_3, ip_4)
        list.write('%s\n' % ip)
        amount = amount - 1
    list.close()
    print 'Done, returning to terminal...'
def ip_rand_gen():        
    print "This will overwrite any existing IP addresses in the system with new ones. Please type 'confirm' to complete the action"
    choice = raw_input('\n>')
    if choice == 'confirm':
        ip_rand_gen2(10)
    else:
        print "Terminating..."
    
