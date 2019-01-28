st1 = """bottles of beer on the wall, """
st2 = """ bottles on the wall\n"""
st3 = """Take one down and pass it around, and you have """
st4 = """bottles of beer...\n"""
st5 = """go to the shop and buy some more, 99 bottles of beer"""

for i in range(99, -1, -1):
	if i > 1:
		if i!=2:
			print(i, st1, i, st2,st3, i-1, st4)
		else:
			print(i, st1, i, st2, st3, i - 1, st4.replace("bottles", "bottle"))
	elif i == 1:
		print("One ",st1.replace("bottles","bottle"),"One", st2.replace("bottles", "bottle"), st3, "no ", end="" )
		print(st4.replace("bottles", "bottle"))
	else:
		print("No ", st1, "no ", st2, st5)
