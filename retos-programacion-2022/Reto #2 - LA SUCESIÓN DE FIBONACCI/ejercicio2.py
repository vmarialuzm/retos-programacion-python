def fibonacci():

    prev = 0
    next = 1

    for index in range(50):
        print(prev)
        fibo = prev + next
        prev = next
        next = fibo

fibonacci()
    
