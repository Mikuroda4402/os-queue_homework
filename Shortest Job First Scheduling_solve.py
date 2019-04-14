'''  I use python 2.7  '''
import os

def arrTime ( at, time , length):
    _order = []
    if time <= max(at):
        for i in xrange(length):
            if at[i] <= time:
                _order.append(i)
    else:
        for i in xrange(length):
            _order.append(i)
    
    return _order

def minBruTime ( order, bt ):
    _order = []
    _bt = []
    for i in xrange(len(bt)):
        if bt[i] is not 0:
            _order.append(order[i])
            _bt.append(bt[i])
    if len(_order) is 1:
        return _order
    
    if _bt.count(min(_bt)) is 1:
        _order.append( _order[_bt.index(min(_bt))] )
        return _order[-1]
    else:
        for i in xrange( _bt.count(min(_bt)) ):
            _order.append( _order[_bt.index(min(_bt), i)] )
        return _order[ -(_bt.count(min(_bt))): ]

def jugdepower ( order, jobs ):
    _min = max(jobs)
    for i in order:
        if jobs[i] < _min:
            _min  = jobs[i]
    return order[jobs.index(_min)]

def whodo ( whotodo , second, last_process):
    global bt
    bt[whotodo] -= 1
    if last_process != whotodo and last_process is not '':
        print buffer
    print 'second ' + str(second) + '~' + str(second+1) + ' process P'+ str(whotodo+1)
    return whotodo

if __name__ == '__main__':
    #simple string
    #file_string = '{"P1":{"order":1,"ArrivalTime":2,"BrustTime":4},"P2":{"order":2,"ArrivalTime":0,"BrustTime":6},"P3":{"order":3,"ArrivalTime":0,"BrustTime":6}}'[1:-1].replace('\"','')
    try:
        fo = open('SJF.json','r')
    except:
        print 'file not exist.'
        os._exit(0)

    file_string = fo.read()[1:-1].replace('\"','')
    buffer = '='*20
    second = 0
    Order  = []
    cut_string = file_string.split('P')[1:]
    length = len(cut_string)
    last_process = ''

    ''' string conversion process '''
    for i in cut_string:
        Order.append(i[3:-1].replace('}','').split(','))

    numbers = []
    for i in Order:
        for j in i:
            numbers.append(int(j[j.find(':')+1:]))

    Jobs        = [''] * length
    ArrivalTime = [''] * length
    bt          = [''] * length

    for i in xrange(length):
        Jobs[i]         = numbers[i*3]
        ArrivalTime[i]  = numbers[i*3+1]
        bt[i]    = numbers[i*3+2]

    ''' output procrss '''
    while 1:
        if sum(bt) is 0:
            break
        temp = arrTime( ArrivalTime, second, length )
        quene = []
        
        for i in temp:
            quene.append(bt[i])
        temp = minBruTime( temp, quene )
        
        if type(temp) is int:
            last_process = whodo( temp, second, last_process)
        elif len(temp) is 1:
            last_process = whodo( temp[0], second, last_process)
        else:
            temp = jugdepower(temp, Jobs)
            last_process = whodo( temp, second, last_process)
        
        second += 1
