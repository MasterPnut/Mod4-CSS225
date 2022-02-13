str_time = input("What time is it now (0000 hhmm)?")
str_wait_time = input("What is the number of hours to wait(0000 hhmm)?")
time = int(str_time)
wait_time = int(str_wait_time)

#changed 'wai_time' to 'wait_time'
#added format (0000 hhmm)

time_when_alarm_go_off = time + wait_time
print(time_when_alarm_go_off)

