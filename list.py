list = [1.0408683539276191, 0.7303377235504916, 0.8315094115485109, 0.8693446977836481, 0.7083005849912722, 1.155377972002685, 1.032039158904, 0.8354836505716504, 1.0677657444021855, 0.7264320166208978, 1.0710494226163119, 1.0755858334251156, 0.8485402067144756, 1.1291489375776576, 0.7445670281643574, 0.7048417450032917, 0.7764252490505225, 1.0656094366092665, 1.1006444497737105, 1.0854770529306117, 0.7226692143680341, 0.7595336726215556, 0.7656208465199005, 0.7425353414595084, 1.1637472705866674, 0.9771386922812076, 0.8674323345775218, 0.7777102690614507, 0.7410037796010522, 0.980154003028308]

seventies = 0
eighties = 0
nineties = 0
dollar = 0
dollar_teens = 0

other = []

for res in list:
    if res < .80:
        seventies += 1
    elif res >= .8 and res < .9:
        eighties += 1
    elif res >= .9 and res < 1:
        nineties += 1
    elif res >= 1 and res < 1.1:
        dollar += 1
    elif res >= 1.1 and res < 1.2:
        dollar_teens += 1
    else:
        other.append(res)

print(f"There are {seventies} occurances in the 70 cent range,")
print(f"{eighties} occurances in the 80 cent range,")
print(f"{nineties} occurances in the 90 cent range,")
print(f"{dollar} occurances in the dollar range,")
print(f"and {dollar_teens} occurances in the $1.10 range.")
print(f"\n\nOther occurances: {res}")