#!/usr/bin/python


schedules = [
  [['09:00', '11:30'], ['13:30', '16:00'], ['16:00', '17:30'], ['17:45', '19:00']],
  [['09:15', '12:00'], ['14:00', '16:30'], ['17:00', '17:30']],
  [['11:30', '12:15'], ['15:00', '16:30'], ['17:45', '19:00']]
]

def get_start_time(sched, dur):

    bmans=list()
    for i in sched:
        print i
        manX=[0 for k in xrange(600)]
        for j in i:
            (sh,sm)=j[0].split(':')
            (eh,em)=j[1].split(':')
            print sh,sm,eh,em
            sint=(int(sh)-9)*60+int(sm)
            eint=(int(eh)-9)*60+int(em)
            manX[sint:eint]=[1 for k in xrange(sint,eint)]
        bmans.append(manX)
        
    print len(bmans[0]),len(bmans[1]),len(bmans[2])
    merged_sched=map(lambda i: 1 if sum(i) else 0 ,zip(*bmans))
    try:
        res=reduce(lambda i,j: str(i)+str(j), merged_sched).index('0'*dur) 
    except:
        return None
    starth=9+res/60
    startm=res%60
    #return str(starth)+':'+str(startm)
    return '%02d'%starth+':'+'%02d'%startm



print get_start_time(schedules, 60), '== 12:15'
print get_start_time(schedules, 90), '== None'
