from COW import COW

with open('./examples/fib.cow') as f:
    code = f.read()
    moo = COW(code)
    moo.read_code()
