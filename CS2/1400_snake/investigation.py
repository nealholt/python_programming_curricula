
#This is not ready for prime time yet.

#Shift all forward
snake_body = [1,2,3,4]
for i in range(5,10):
    for j in range(len(snake_body)-1):
        snake_body[j] = snake_body[j+1]
    snake_body[-1] = i
    print(snake_body)

exit()


#use tail index
snake_body = [1,2,3,4]
tail_index = 0
for i in range(5,10):
    snake_body[tail_index] = i
    tail_index = (tail_index + 1)%len(snake_body)
    print(snake_body)


Is there a way to teach the movement update part and make that easier? It's super hard for students.
One model that is easy is this:
#Move each body part to the next body part's location
for i in reversed(range(1, len(body))):
	body[i].moveTo(body[i-1].getLocation())
#Move the head
body[0].move(direction)


