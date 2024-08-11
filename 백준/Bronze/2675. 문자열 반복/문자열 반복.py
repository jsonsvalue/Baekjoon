import sys
read = sys.stdin.readline

n = int(read().strip())

for i in range(n):
    rpt_list = read().strip().split()
    rpt, rptstr = int(rpt_list[0]), rpt_list[1]
    
    for i in range(len(rptstr)):
        print(rptstr[i] * rpt, end = '')
    print()

      