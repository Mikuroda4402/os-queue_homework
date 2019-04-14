'''  I use python 2.7  '''
import os
try:
    fo = open('RR.json','r')
except:
    print 'file not exist.'
    os._exit(0)

file_string = fo.read()[1:-1].replace('\"','')

#simple string
#file_string = '{"BurstTime":{"p1":8,"p2":5,"p3":12,"p4":22},"Order":["p3","p1","p4","p2"],"Quantum":4}'[1:-1].replace('\"','')
buffer = '='*20
BurstTime = file_string[:file_string.find("Order")-1]
Order     = file_string[file_string.find("Order"):file_string.find("Quantum")-1]
Quantum   = file_string[file_string.find("Quantum"):]

''' string conversion process '''
#BurstTime Identify
#output is {'p2': 4, 'p3': 1, 'p1': 8}
BurstTime = BurstTime[BurstTime.find('{')+1:-1].split(',')
bt = {}
for i in BurstTime:
    bp = i.find(':')
    bt[i[:bp]] = int(i[bp+1:])

#Order Identify
#output is ['p3', 'p1', 'p2']
Order = Order[Order.find('[')+1:-1].split(',')

#Quantum Identify
#output is 4
Quantum = int(Quantum[Quantum.find(':')+1:])

''' output procrss '''
sec = 0
while 1:
    if not Order:
        break
    queue = Order.pop(0)
    for i in xrange(Quantum):
        if bt[queue] is 0:
            break
        print 'second ' + str(sec) + '~' + str(sec+1) + ' process ' + queue
        bt[queue] -= 1
        sec += 1
    print buffer
    if bt[queue] is 0:
        continue
    Order.append(queue)

''' End Process '''
print 'Process End.'