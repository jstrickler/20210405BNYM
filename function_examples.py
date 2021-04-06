def spam():
    pass

x = spam()
print(x)

#       positional   named
#       req   opt    req    opt
def ham(req, *opt,   nreq, **nopt):
    print('req:', req)
    print('opt:', opt)
    print('nreq:', nreq)
    print('nopt:', nopt)

ham(1, 2, 3, 4, nreq=5, count=6, size=7, wombat=99)

def f1(a, b):  # 2 args required
    pass

def f2(*a):    # 0 or more args required
    pass

def f3(a, *b):  # 1 arg required, 0 or more additional OK
    pass

f3(1)
f3(1,2,3,4,5,6,7,8,9)
# cannot call f3()

def f4(*, p1, p2):
    print(f"p1 {p1} p2 {p2}")

f4(p1=42, p2='mongoose')

def f5(**values):
    print("values:", values)

f5(count=1, wombats=2, city='Chennai', country='India')

def wacky(p1, p2, *p3, p4, p5, **p6):
    print(p1, p2, p3, p4, p5, p6)

wacky(1, 2, p4='abc', p5='def')
wacky(1, 2, 3, 9, 57, p5='abc', p4='def', p8='ghi',
      p10='jkl', animal='aardvark', city='Goa')

def toast(p1, p2=99):
    print(p1, p2)

toast(5, 10)
toast(100, 256)
toast(5000)

def show_location(*, lat=0, lon=0):
    print("lat, lon:", lat, lon)

show_location()
show_location(lat=5)
show_location(lon=5)
show_location(lat=5, lon=10)

def oatmeal(a, *, b):
    print(a, b)

oatmeal(3, b=6)
oatmeal(3, b=6)

def omelet(*, a, b, c):
    pass

def generic(*a, **b):
    pass

