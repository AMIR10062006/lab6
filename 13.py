def all_true(tupler):
    return all(tupler)
tupler = (True,1,423,0)
if all_true(tupler):
    print("all elements are true")
else:
    print("there is false element")