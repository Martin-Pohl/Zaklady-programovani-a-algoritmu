#1. Dědictví (11):#
1256983 % 28

#2. Ověření matematických výsledků (16)#
12**52 % 15 < 8 or 3**5 > 100

5*3**3 != 900/75

#3. Balení do závorek nebo množení písmen (21)#
jedna = '[[]]'
dva = 'PYTHON '
jedna [0:2:1] + dva [0:len(dva)-1:1] + jedna [-2::1]

'Python' [4::1]*4

'Perl' [2]*6

#4. Hrátky s řetězci (24)#
name = 'python'
name[0:len(name)//2:1].upper() + name[len(name)//2::1].lower()

name = 'python'
name[0]*len(name)

#5. Vyřešení chyby (27)#
error	důvod: se stringem lze řetězit jen string (nikoli int jako zde)

#6. Hobby proměnná (31)#

hobby = 'hiking'
'My hobby is {0}.'.format(hobby)

date = '2018-11-01'
month = '11'
day = '01'
new_date = '{0}/{1}'.format(month, day)
print(new_date)


#Práce se seznamy (37)#
my_list = []
my_list.append('hiking')
my_list.append('rambling')
my_list.append('running')
print(my_list[0])
print(my_list[-1])

del my_list[-1]

#Řazení měst (38)#
cities = ['Prague', 'Brno', 'Ostrava', 'Plzen', 'Liberec', 'Olomouc', 'Usti nad Labem', 'Hradec Kralove', 'Ceske Budejovice', 'Pardubice']
cities.sort()
"*".join(cities)

#Zen of Python#
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = set(alphabet)
zen = """
... Beautiful is better than ugly.
... Explicit is better than implicit.
... Simple is better than complex.
... Complex is better than complicated.
... Flat is better than nested.
... Sparse is better than dense.
... Readability counts.
... Special cases aren't special enough to break the rules.
... Although practicality beats purity.
... Errors should never pass silently.
... Unless explicitly silenced.
... In the face of ambiguity, refuse the temptation to guess.
... There should be one-- and preferably only one --obvious way to do it.
... Although that way may not be obvious at ﬁrst unless you're Dutch.
... Now is better than never.
... Although never is often better than *right* now.
... If the implementation is hard to explain, it's a bad idea.
... If the implementation is easy to explain, it may be a good idea."""
zen = set(zen)
alphabet.difference(zen)