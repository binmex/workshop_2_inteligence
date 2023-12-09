import clips

env = clips.Environment()

# Ordered facts can only be asserted as strings
fact = env.assert_string('(ordered-fact 1 2 3)')

# Ordered facts data can be accessed as list elements
assert fact[0] == 1
assert list(fact) == [1, 2, 3]