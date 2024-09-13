import datastructures

my_stack = datastructures.Stack()
my_stack.push(1)
my_stack.push(2)
print(my_stack)  # [1, 2]

popped_value = my_stack.pop()  # 2
print(popped_value)
print(my_stack)  # [1]
