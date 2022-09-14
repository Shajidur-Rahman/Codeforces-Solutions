lenth = int(input())
t = input() + "........"

li = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

string = ""

for i in range(lenth):
	
	s = li[int(t[i])-1]
	print(s)
	string += s

print(string)