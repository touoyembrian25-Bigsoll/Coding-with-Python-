#3-4
guestlist=['Precious','Basil','Christ']
print(guestlist[0], 'You nare invited to the marriange ceremony')
print(guestlist[1], 'You are invited to the marriage ceremony')
print(guestlist[2],'You are invited to the marriage ceremony')
#3-5
guestlist.pop(1)
print(guestlist)
guestlist.insert(1, 'Max')
print(guestlist)
print(guestlist[0],'You are invited to the marriage ceremony')
print(guestlist[1],'You are invited to the marriage ceremony')
print(guestlist[2],'You are invited to the mariage ceremony')

print('Dear guest we have found a biggerr hall for the ceremony and as such we can accomodate more people')

guestlist.insert(0,'Fabiola')
guestlist.insert(1,'Piresse')
guestlist.append('Edla')
print(guestlist)
#3-6
guestlist.insert(0,'Fabiola')
guestlist.insert(1,'Piresse')
guestlist.append('Edla')

print(guestlist[0],'You are invited to the mariage ceremony')
print(guestlist[1],'You are invited to the mariage ceremony')
print(guestlist[2],'You are invited to the mariage ceremony')
print(guestlist[3],'You are invited to the mariage ceremony')
print(guestlist[4],'You are invited to the mariage ceremony')
print(guestlist[5],'You are invited to the mariage ceremony')

#seeing the world 3-8
travellist=['Maldives','Korea','SouthAfrica','New York','Egypt']
print(travellist)
travellist.sort()
print(travellist)
travellist.sort(reverse=True)
print(travellist)
travellist.reverse()
print(travellist)
travellist.sort()
print(travellist)
travellist.sort(reverse=True)
print(travellist)
