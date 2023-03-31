from random import *
from pprint import pprint
import unittest

random_ip = set()
usable_ip = set()
ip_address = ""
numbers_pool = [number for number in range(256)]
for first_octet in range(256):
    ip_address = str(first_octet) + "." + str(choice(numbers_pool)) \
        + "." + str(choice(numbers_pool)) + "." + str(choice(numbers_pool))
    random_ip.add(ip_address)

print("-------------------------- Rnadom Ip Address -------------------------")
pprint(random_ip)

ip_to_cmp = "0" + "." + str(choice(numbers_pool)) \
        + "." + str(choice(numbers_pool)) + "." + str(choice(numbers_pool))
for ip in random_ip:
    if ip is ip_to_cmp:
        print(f"------> can't use this {ip}.")
    else:
        usable_ip.add(ip)


print("-------------------- Usable Ip Address --------------------------------")
pprint(usable_ip)


class RandomIPTest(unittest.TestCase):
    """
        Testing the data randomness and consistency in a set.
    """

    def test_ip_address(self):
        """
            returns: random_ip addresses
        """
        for rand_ip in random_ip:
            self.assertIn(rand_ip, random_ip)


if __name__ == '__main__':
    unittest.main()
