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

def highPri ( order, pri ):
    if len(order) is 1:
        return order
    _order = []
    _min = min(pri)
    if pri.count(_min) is 1:
        _order.append( order[ pri.index(_min) ] )
    else:
        for i in xrange(pri.count(_min)):
            _order.append( order[ pri.index(_min, i) ] )
    return _order

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
    #file_string = '{"P1":{"Order":1,"ArrivalTime":3,"BurstTime":5,"Priority":1},"P2":{"Order":2,"ArrivalTime":0,"BurstTime":5,"Priority":6},"P3":{"Order":3,"ArrivalTime":8,"BurstTime":3,"Priority":8},"P4":{"Order":4,"ArrivalTime":3,"BurstTime":5,"Priority":6}}'[1:-1].replace('\"','')
    
    try:
        fo = open('PriorityScheduling_test.json','r')
    except:
        print 'file not exist.'
        os._exit(0)

    file_string = fo.read()[1:-1].replace('\"','')
    
    buffer = '='*20
    second = 0
    Order  = []
    cut_string = file_string.split('P')[1:]
    length = len(cut_string) /2
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
    priority    = [''] * length

    for i in xrange(length):
        Jobs[i]         = numbers[i*4]
        ArrivalTime[i]  = numbers[i*4+1]
        bt[i]           = numbers[i*4+2]
        priority[i]     = numbers[i*4+3]

    ''' output procrss '''
    while 1:
        if sum(bt) is 0:
            break
        temp = arrTime( ArrivalTime, second, length )
        quene = []
        _ntemp = []
        for i in temp:
            if bt[i] is not 0:
                quene.append(priority[i])
                _ntemp.append(i)
        temp = highPri( _ntemp, quene )
        
        if type(temp) is int:
            last_process = whodo( temp, second, last_process)
        elif len(temp) is 1:
            last_process = whodo( temp[0], second, last_process)
        else:
            temp = jugdepower(temp, Jobs)
            last_process = whodo( temp, second, last_process)
        second += 1
    
