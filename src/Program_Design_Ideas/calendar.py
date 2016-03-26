def getYear():
    print('This program prints the calendar of a given year.')
    year = int(input('Please enter a year (after 1900):'))
    return year

def firstDay(year):
    k = leapyears(year)
    n = (year - 1900)*365 + k
    return (n+1)%7

def leapyears(year):
    count = 0
    for y in range(1900,year):
        if y%4 == 0 and (y%100 != 0 or y%400 == 0):
            count = count + 1
    return count

def printCalendar(year,w):
    print()
    print('==============='+ str(year) + '=================')
    first = w
    for month in range(12):
        heading(month)
        first = oneMonth(year,month,first)
        
def heading(m):
    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept',
              'Oct','Nov','Dec']
    print('%10s' %(months[m]))
    print('Mon Tue Wed Thu Fri Sat Sun')
    
def oneMonth(year,month,first):
    d = days(year,month)
    frame = layout(first,d)
    printMonth(frame)
    return(first + d)%7
def days(y,m):
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    d = month_days[m]
    if(m == 1)and(y%4 == 0 and (y%100 != 0 or y%400 == 0)):
        d = d + 1
    return d

def layout(first,d):
    frame = 42 * ['']
    if first == 0:
        first = 7
    j = first -1
    for i in range(1,d+1):
        frame[j] = i
        j = j + 1
    return frame

def printMonth(frame):
    for i in range(42):
        print('%3s' %(frame[i]),end=' ')
        if (i+1)%7 == 0:
            print()
            
def main():
    year = getYear()
    w = firstDay(year)
    printCalendar(year, w)
main()
