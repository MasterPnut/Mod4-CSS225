currentTimeStr = input("What is the current time (in hours 0-23)?")
waitTimeStr = input("How many hours do you want to wait? ")
#Added closed parentheses, ' ?'.

currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)
#replaced 'current_time_str' with 'currentTimeStr'
#replaced 'wait_time_str' with 'waitTimeStr'

finalTimeInt = (currentTimeInt + waitTimeInt)
print("Final time is", finalTimeInt)

#replaced 'finalTime_Int' with 'finalTimeInt'
#added "Final time is"
