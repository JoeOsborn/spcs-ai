# Assignment 1-1
def check(sm, string):
    for s in string:
        if s not in sm.out_edges():
            return False
        sm.advance(s)
    return sm.is_terminal()

# Assignment 1-2
def test2():
    #(x+@x+\.x+(\.x+)*)
    return StateMachine([("s1", "x", "s2"), ("s2", "x", "s2"), ("s2", "@", "s3"),
                         ("s3", "x", "s4"), ("s4", "x", "s4"), ("s4", ".", "s5"),
                         ("s5", "x", "s6"), ("s6", "x", "s6"), ("s6", ".", "s7"),
                         ("s7", "x", "s6")],
                        "s1",
                        ["s6"])

assert check(test2(), "x@x.x")
assert check(test2(), "x@x.x.x")
assert check(test2(), "x@xx.x")
assert check(test2(), "xx@xx.xx.xx")
assert not check(test2(), "@x.x")
assert not check(test2(), "x@.x")
assert not check(test2(), "x@x.")
assert not check(test2(), "x@x")
assert not check(test2(), "x.x")
assert not check(test2(), "x@")
assert not check(test2(), "x@x..x")

# Assignment 2:
def sample2(sm, length, sofar):
    # Each path of length 0 is either accepting or non-accepting;
    # in the former case we return [sofar] (the path) and in the latter [] (no path)
    if length == 0:
        if sm.is_terminal():
            return [sofar]
        else:
            return []
    state = sm.state
    results = []
    for sym in sm.out_edges():
        # for each edge: advance, sample, backtrack.
        sm.advance(sym)
        results = results + sample2(sm, length-1, sofar + sym)
        sm.state = state
    return results
