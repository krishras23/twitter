from hash import Hashed

answer1 = Hashed("sfhs23")
answer2 = Hashed("sfhs23")
assert answer1 == answer2, "Hashes do not match"

answer3 = Hashed("sfhs231")
assert answer1 != answer3, "Hashes should not match"


