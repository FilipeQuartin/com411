def likelihood() :
    likelihoods = (50, 38, 27, 99, 4)
    return (min(likelihoods))

run ():
value = likelihood()
print(f"Minimum likelihood of falling: {value}%")