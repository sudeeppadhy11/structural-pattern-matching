t=(0,0)
match t:
    case (0,0):
        print("origin")
    case (1,y,z):
        print (f"t is at x=1,{y=}")
    case (0,y):
        print (f"t is at x=0,{y=}")
    case _:
        print("t is out of bound")
