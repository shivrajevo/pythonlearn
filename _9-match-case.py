# normal working of match case flow control statement

var = 30

match int(input("enter the value")):
    case 10:
        print("is 10")
    case 20:
        print("is 20")
    case 30:
        print("is 30")
    case 40:
        print("is 40")
    case 50:
        print("is 50")
    case 60:
        print("is 60")
    case _:
        print("default notmatch")


# using the if else with the match case statment  (in a range)

temprature = 40

match temprature:
    case t if t >= 0 and t < 20:
        print("tempratrue is cold")
    case a if a >= 20 and a < 30:
        print("tempratrue is warm")
    case t if t >= 30 and t < 40:
        print("tempratrue is hot")
    case t if t >= 40 and t <= 50:
        print("tempratrue is extreme")
    case _:
        print("default")

