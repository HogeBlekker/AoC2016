import hashlib
import re

door_id = 'abbhdwsy'
#door_id = 'abc'

j = 0
the_posish = ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g']
char_counter = 0
while char_counter < 8:
	hex_digest = ''
	m = hashlib.md5()
	m.update(door_id)
	while hex_digest[0:5] != '00000':
		m_clone = m.copy()
		m_clone.update(str(j))
		hex_digest = m_clone.hexdigest()
		j += 1
	if re.match("0|1|2|3|4|5|6|7", hex_digest[5:6]) and the_posish[int(hex_digest[5:6])] == 'g':
		the_posish[int(hex_digest[5:6])] = hex_digest[6:7]
		char_counter += 1

print the_posish
