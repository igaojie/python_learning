#encoding=utf-8
def yield_test(n):
	for i in range(n):
		yield call(i)
		print("i=",i)

	print("do something.")
	print("end.")

def call(i):
	return i*2

for i in yield_test(5):
	print(i,",")



def square():
    for x in range(4):
        yield x ** 2
square_gen = square()
for x in square_gen:
    print(x)