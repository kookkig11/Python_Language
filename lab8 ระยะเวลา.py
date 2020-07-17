def read_hour() :
    h = int(input("Enter hour: "))
    if h>=0 and h<=23:
        return h    
def read_minute() :
    m = int(input("Enter minute: "))
    if m>=0 and m<=59:
        return m
def read_second() :
    s = int(input("Enter second: "))
    if s>=0 and s<=59:
        return s
def to_seconds(h,m,s) :
    time = (h*3600) + (m*60) + s
    return time
def time_elapsed(start,finish) :
    usetime = finish - start
    hour = usetime//3600
    minute = (usetime-(hour*3600))//60
    second = usetime-(hour*3600)-(minute*60)
    printstr = "%d hours %d minutes %d seconds." %(hour,minute,second)
    return printstr

def read_time():
    print('>> ', end='')
    hour = read_hour()
    print('>> ', end='')
    minute = read_minute()
    print('>> ', end='')
    second = read_second()
    return to_seconds(hour, minute, second)

print('Start time:')
start_time = read_time()
print('Finish time:')
finish_time = read_time()
print('Elapsed time is', time_elapsed(start_time, finish_time))