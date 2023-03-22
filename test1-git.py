### Suseción de Fibonacci ###

new_list = (range(33))
def fibonacci():

    vec = list(range(0, 33))
    vec[1] = 0
    vec[2] = 1

    for i in range(3, 33):

        vec[i] = vec[i-1] + vec[i-2]
        new_list = vec[i]
        if new_list == 0:
            print("ME VOY A ESTALLAR FIRME")
        else:
            print("me voy a estallar muy firme")


fibonacci()



