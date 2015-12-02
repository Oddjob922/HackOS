import random
def ip_rand_gen(number):
    ip_1 = random.randint(0, 255)
    ip_2 = random.randint(0, 255)
    ip_3 = random.randint(0, 255)
    ip_4 = random.randint(0, 255)
    ip = '%r.%r.%r.%r' % (ip_1, ip_2, ip_3, ip_4)
    print ip
