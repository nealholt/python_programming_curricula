'''There is a magic box (variable) that you can put things in and take
things out of. Whenever you take something out, you get a copy (the
original stays in the box). But if you try to put something in when
the box already has contents, the previous thing in the box is
destroyed in a puff of smoke.
'''
little_box = 'dice'
big_box = 'tennis_ball'

print(little_box)
print(big_box)
print(big_box)

little_box = big_box

print(big_box)
print(little_box)
print(little_box)

little_box = 'dice'
print(little_box)
print(little_box)

big_box = little_box

print(big_box)
print(big_box)
print(little_box)
