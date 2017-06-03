from itertools import izip
import hashlib

passwords_file = '/root/Desktop/SecLists/Passwords/10k_most_common.txt'
salts_file = '/root/Desktop/Bsides2017/salts_list.txt'
user_hashes_file = '/root/Desktop/Bsides2017/user_hashes.txt' 

with open(passwords_file , 'r') as f1:
	passwords = f1.read().split()

with open(salts_file , 'r') as f2:
	salts = f2.read().split()

with open(user_hashes_file , 'r') as f3:
	user_hashes = f3.read().split()

for p in passwords:
	for s in salts:
		hash_raw = hashlib.md5(p+s)
		hash = hash_raw.hexdigest()
		for h in user_hashes:
			if (h in hash):
				print "FOUND MATCH !"
				print "password:{0} \t salt:{1} \t hash:{2}".format(p,s,hash)




