from checkUser import checkPassword, checkUsername


t1 = checkUsernamePassword("tiny","password")
t2 = checkUsernamePassword("sfhshshshsh", "s#f")
t4 = checkUsernamePassword("should work", "@ghksfj")
t5 = checkUsernamePassword("toooooooooooooooolong", "#$#$#$#$#$#$j")

assert t1 =