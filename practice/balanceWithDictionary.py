
def sol(text):
  check = {
    ">" : "<",
    "}" : "{",
    ')' : "("
  }
  stack = []
  for i in text:
    if i in check.values():
      stack.append(i)
    elif i in check:
      if len(stack) == 0:
        return False
      if stack.pop() != check[i]:
        return False
  return True
a = sol('(<x)>(())()')
print(a)
