test_cases = [
	[1,1,1],
	[1,1,2],
	[1,1,3],
	[1,2,1],
	[1,2,2],
	[1,2,3],
	[1,3,1],
	[1,3,2],
	[1,3,3],
	[2,1,1],
	[2,1,2],
	[2,1,3],
	[2,2,1],
	[2,2,2],
	[2,2,3],
	[2,3,1],
	[2,3,2],
	[2,3,3],
	[3,1,1],
	[3,1,2],
	[3,1,3],
	[3,2,1],
	[3,2,2],
	[3,2,3],
	[3,3,1],
	[3,3,2],
	[3,3,3],
]

def max_of_3(a,b,c):
    correct_ans = max(a,b,c)
    test_ans =  a if a>=b and a>=c else b if b>=a and b>=c else c 
    return correct_ans==test_ans

final_res_list = []
for itr,test_case in enumerate(test_cases):
    li = test_case
    final_res = max_of_3(*li)
    if not final_res:
        final_res_list.append(final_res)

print("total false case count: ", len(final_res_list))