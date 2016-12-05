import hashlib

door_id = 'abbhdwsy'
#door_id = 'abc'

j = 0
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
	print hex_digest[5:6]
	char_counter += 1
