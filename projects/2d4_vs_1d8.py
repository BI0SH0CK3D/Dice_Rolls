import random 

def _2d4():
	damage = random.randint(1,4) + random.randint(1,4)
	#print "2d4:", damage
	return damage

def _1d8():
	damage = random.randint(1,8)
	#print "1d8:", damage
	return damage

def test(size):
	
	wins_2d4 = 0
	wins_1d8 = 0
	ties = 0

	for i in range(int(size)):

		#print '___'
		two_d_four = _2d4()
		one_d_eight = _1d8()

		if two_d_four > one_d_eight:
			#print "2d4 wins"
			wins_2d4 += 1
		if one_d_eight > two_d_four:
			#print "1d8 wins"
			wins_1d8 += 1
		if two_d_four == one_d_eight:
			#print "tie"
			ties += 1

	print '\n*********'	
	print 'total 2d4:', wins_2d4
	print 'total 1d8:', wins_1d8
	print 'total ties:', ties
	
	assert wins_1d8 + wins_2d4 + ties == size		

test(20000)
