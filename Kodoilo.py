def base_code():
	from random import sample
	return sample('ABCDEF01234567890', 6)
def encode_txt(txt=base_code()):
	import random
	e=''
	d=ord(txt)
	s=random.randint()
	j=str(d+s)+str(s)
	k=chr(j)
	k=k[::-1]
	return '0K'+k
