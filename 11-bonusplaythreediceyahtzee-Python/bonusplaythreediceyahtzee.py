# bonusPlayThreeDiceYahtzee(dice) [5pts]
# In this exercise, we will write a simplified form of the dice game Yahtzee. In this version, the 
# goal is to get 3 matching dice, and if you can't do that, then you hope to at least get 2 
# matching dice. The game is played like so:
# Roll 3 dice.
# If you do not have 3 matching dice:
# If you have 2 matching dice (a pair), keep the pair and roll one die to replace the third die.
# Otherwise, if you have no matching dice, keep the highest die and roll two dice to replace the 
# other two dice.
# Repeat step 2 one more time.
# Finally, compute your score like so:
# If you have 3 matching dice, your score is 20 + the sum of the matching dice.
# So if you have 4-4-4, your score is 20+4+4+4, or 32.
# If you only have 2 matching dice, your score is 10 + the sum of the matching dice.
# So if you have 4-4-3, your score is 10+4+4, or 18.
# If you have no matching dice, your score is the highest die.
# So if you have 4-3-2, your score is just 4.
# Our goal is to write some Python code that plays this game. It's a large task, so we will use 
# top-down design and break it up into smaller, more manageable pieces. So we'll first write some 
# helper functions that do part of the work, and then those helper functions will make our final 
# function much easier to write. 

# Also note: we will represent a hand of 3 dice as a single 3-digit integer. So the hand 4-3-2 will 
# be represented by the integer 432. With that, let's start writing some code. Be sure to write 
# your functions in the same order as given here, since later functions will make use of earlier 
# ones!

# we've made it to the last function: bonusPlayThreeDiceYahtzee(dice), the function that actually earns 
# the 2.5 bonus points! This function takes one value, the dice with all the rolls for a game of 3-Dice 
# Yahtzee. The function plays the game -- it does step1 and gets the first 3 dice (from the right), then it 
# does step2 twice (by calling playStep2, which you already wrote), and then it computes the score (by 
# calling score, which you already wrote). The function should return two values -- the resulting hand 
# and the score for that hand. For example:

def handlist(dice):
	alist = [int(i) for i in str(dice)]
	handlist_ = alist[-3:]
	return handlist_

def dicelist(dice):
	alist = [int(i) for i in str(dice)]
	dicelist_ = alist[:4]
	return dicelist_

def score(roll):
	rolllist = [int(i) for i in str(roll)]
	if rolllist.count(rolllist[0]) ==3:
		score = 20 + (3*int(rolllist[0]))
	elif rolllist.count(rolllist[0]) ==2:
		score = 10 + (2*int(rolllist[0]))
	elif rolllist.count(rolllist[1]) ==2:
		score = 10 + (2*int(rolllist[1]))
	elif rolllist.count(rolllist[2]) ==2:
		score = 10 + (2*int(rolllist[2]))
	else:
		score = max(rolllist)
	return score

def checkMatching(roll):
	rolllist = [int(i) for i in str(roll)]
	if rolllist.count(rolllist[0]) ==3:
		return '3'
	elif rolllist.count(rolllist[0]) ==2:
		return '2'
	elif rolllist.count(rolllist[1]) ==2:
		return '2'
	elif rolllist.count(rolllist[2]) ==2:
		return '2'
	else:
		return '1'

def twoMatching(roll, dice):
	rolllist = [int(i) for i in str(roll)] #[4,4,3]
	dicelist_ = dicelist(dice) #[2,3,4,5]
	res = []
	for i in rolllist:
		if rolllist.count(i) ==2:
			res.append(i)
			res.append(i)
	res.append(dicelist_[-1])
	dicelist_.pop()
	roll = int(''.join(str(i) for i in res))
	if checkMatching(roll) == '3':
		return int(roll), score(roll)
	if checkMatching(roll) == '2':
		rolllist = [int(i) for i in str(roll)] 
		# dicelist_ = dicelist(dice) 
		res2 = []
		for i in rolllist:
			if rolllist.count(i) ==2:
				res2.append(i)
				res2.append(i)
		res2.append(dicelist_[-1])
		dicelist_.pop()
		res2.sort(reverse = True)
		roll = int(''.join(str(i) for i in res2))
		return roll
	if checkMatching(roll) == '1':
		res2 = []
		res2.append(max(res))	#[5]
		res2.append(dicelist_[-1])	#[5,3]
		res2.append(dicelist_[-2])	#[5,3,2]
		dicelist_.pop()				#[2,]
		dicelist_.pop()				#[]
		res2.sort(reverse = True)
		roll = int(''.join(str(i) for i in res2)) #532
		return roll

def noMatching(roll, dice):
	rolllist = [int(i) for i in str(roll)] #[4,1,3]
	dicelist_ = dicelist(dice) #[2,6,3,3]
	res = []
	res.append(max(rolllist))	#[4]
	res.append(dicelist_[-1])	#[4,3]
	res.append(dicelist_[-2])	#[4,3,3]
	dicelist_.pop()				#[2,6,3]
	dicelist_.pop()				#[2,6]
	roll = int(''.join(str(i) for i in res)) #433
	if checkMatching(roll) == '3':
		return int(roll), score(roll)
	if checkMatching(roll) == '2':
		rolllist = [int(i) for i in str(roll)] #[4,3,3]
		# dicelist_ = dicelist(dice) 
		res2 = []
		for i in rolllist:
			if rolllist.count(i) ==2:
				res2.append(i)					#[3,3]
		res2.append(dicelist_[-1])
		dicelist_.pop()
		res2.sort(reverse = True)
		roll = int(''.join(str(i) for i in res2))
		return roll
	if checkMatching(roll) == '1':
		res2 = []
		res2.append(max(res))	#[5]
		res2.append(dicelist_[-1])	#[5,3]
		res2.append(dicelist_[-2])	#[5,3,2]
		dicelist_.pop()				#[2,]
		dicelist_.pop()				#[]
		res2.sort(reverse = True)
		roll = int(''.join(str(i) for i in res2)) #532
		return roll

def bonusplaythreediceyahtzee(dice):
	handlist_ = handlist(dice)
	dicelist_ = dicelist(dice)
	roll = dice%1000
	if checkMatching(roll) == '3':
		return int(roll), score(roll)
	if checkMatching(roll) == '2':
		roll = twoMatching(roll, dice)
		return roll, score(roll)
	if checkMatching(roll) == '1':
		roll = noMatching(roll,dice)
		return roll, score(roll)

	# return score(432), score(443), score(444), checkMatching(432), checkMatching(443), checkMatching(444),


print(bonusplaythreediceyahtzee(2633413))

# assert(bonusPlayThreeDiceYahtzee(2312413) == (432, 4))
# assert(bonusPlayThreeDiceYahtzee(2315413) == (532, 5))
# assert(bonusPlayThreeDiceYahtzee(2345413) == (443, 18))--
# assert(bonusPlayThreeDiceYahtzee(2633413) == (633, 16))--
# assert(bonusPlayThreeDiceYahtzee(2333413) == (333, 29))
# assert(bonusPlayThreeDiceYahtzee(2333555) == (555, 35))
# print(noMatching(413, 2345413))
