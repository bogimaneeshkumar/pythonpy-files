#defining the function
def rep(strings):
    init=""
    for letter in strings :
        init=init+(letter*2)
    return init
inputs=input("ENTER THE STRING : ")
out=rep(inputs)
print(out)
