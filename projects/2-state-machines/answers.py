# Don't read me until you're totally stuck!
































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


# Extension to Assignment 1-2 (full legal e-mail addresses)
def test2_extension():
    #(x+(\.x+)*)@x+\.x+(\.x+)*)
    return StateMachine([("s1", "x", "s2"), ("s1", ".", "s9"), ("s1", "@", "s9"),
                         ("s2", "x", "s2"), ("s2", ".", "s3"), ("s2", "@", "s4"),
                         ("s3", "x", "s2"), ("s3", ".", "s9"), ("s3", "@", "s9"),
                         ("s4", "x", "s5"), ("s4", ".", "s9"), ("s4", "@", "s9"),
                         ("s5", "x", "s5"), ("s5", ".", "s6"), ("s5", "@", "s9"),
                         ("s6", "x", "s7"), ("s6", ".", "s9"), ("s6", "@", "s9"),
                         ("s7", "x", "s7"), ("s7", ".", "s8"), ("s7", "@", "s9"),
                         ("s8", "x", "s7"), ("s8", ".", "s9"), ("s8", "@", "s9"),
                         ("s9", "x", "s9"), ("s9", ".", "s9"), ("s9", "@", "s9")],
                         "s1",
                         ["s7"]
                        )

    assert check(test2_extension(), "x@x.x")
    assert check(test2_extension(), "x@x.x.x")
    assert check(test2_extension(), "x@xx.x")
    assert check(test2_extension(), "xx@xx.xx.xx")
    assert check(test2_extension(), "x.x@x.x")
    assert check(test2_extension(), "x.x@x.x.x")
    assert check(test2_extension(), "x.x@xx.xx.xx")
    assert check(test2_extension(), "x.x.x@x.x")
    assert check(test2_extension(), "x.x.x@x.x.x")
    assert check(test2_extension(), "x.x.x@xx.xx.xx")
    assert check(test2_extension(), "xx.xx.xx@x.x")
    assert check(test2_extension(), "xx.xx.xx@x.x.x")
    assert check(test2_extension(), "xx.xx.xx@xx.xx.xx")
    assert not check(test2_extension(), "@x.x")
    assert not check(test2_extension(), "x@.x")
    assert not check(test2_extension(), "x@x.")
    assert not check(test2_extension(), "x@x")
    assert not check(test2_extension(), "x.x")
    assert not check(test2_extension(), "x@")
    assert not check(test2_extension(), "x@x..x")
    assert not check(test2_extension(), ".x@x.x")
    assert not check(test2_extension(), "x.@x.x")


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
