

def decor(func):
    def warp(*args):
        print("================")
        func(*args)
        print("=================")
    return warp
@decor
def print_text(*args):
    print(*args)

print_text('hello world')
