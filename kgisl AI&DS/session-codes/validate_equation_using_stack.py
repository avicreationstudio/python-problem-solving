from stack_python import Stack
rules = {
	'{':'}',
	'(':')',
	'[':']'
}
value = input() # "([])"
stack = Stack(10)
valid = True
for char in value:
	if char in '{[(':
		stack.push(char)
	elif char in '}])':
		top = stack.peek() # i will have open brakets
		if rules[top] == char:
			stack.pop()
		else:
			print("invalid equation")
			valid = False
			break

if valid:
	print('valid equation')
