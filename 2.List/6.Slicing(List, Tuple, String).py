l1 = [10,20,30]

l2 = l1[:]

t1 = (10,20,30)

t2 = t1[:]          # tuple having same element has same id

s1 = "geeks"
s2 = s1[:]          # string of same value have same id

print(l1 is l2)

print(t1 is t2)

print(s1 is s2)









l = [10,20,30,40,50]

print("l[0:5:2]",l[0:5:2])     # start:0, stop:5, step:2

print("l[:4]",l[:4])        # start: 0, stop:4, step:1

print("l[2:]",l[2:])        # start:2,  stop:end of string, step:1

print("l[1:4]",l[1:4])

print("l[4:1:-1]",l[4:1:-1])    #start:4, stop:1,step:-1

print("l[-1:-6:-1]",l[-1:-6:-1])  # start:end,

print("l[::-1]",l[::-1])

print("l[0:5]",l[0:5])

print("l[:]",l[:])
