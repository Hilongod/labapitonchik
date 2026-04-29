import io, sys, functools

def printi(f=None, *, verbose=False):
    def decorator(func):
        depth = [0]
        buf = [None]
        @functools.wraps(func)
        def wrap(*args, **kwargs):
            depth[0] += 1
            if depth[0] == 1:
                buf[0] = io.StringIO()
                sys.stdout = buf[0]
            try:
                result = func(*args, **kwargs)
            finally:
                depth[0] -= 1
                if depth[0] == 0:
                    sys.stdout = sys.__stdout__
                    if verbose:
                        print(buf[0].getvalue(), end="")
            return result
        return wrap
    return decorator(f) if f is not None else decorator

@printi
def hero():
    hp = 100
    def heal(n):
        nonlocal hp 
        hp = min(100, hp + n)
    def damage(n):
        nonlocal hp
        hp = max(0, hp - n)
    def get_hp():
        return hp
    print(hp)
    return get_hp, heal, damage

get_hp, heal, damage = hero()
damage(30)  
heal(20)     
damage(80)  
print(get_hp())
