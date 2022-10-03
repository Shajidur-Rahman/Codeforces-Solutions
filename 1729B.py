lenth = int(input())
t = input() + "........"

li = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

string = ""

for i in range(lenth):
	
	if "0" in t:
		ind = t.index("0")
		s = li[int(t[ind-1])-1]
		s2 = li[int(t[ind-2])-1]
		string = string + s + s2

		
	
	else:
		s = li[int(t[i])-1]
		print(s)
		string += s

print(string)