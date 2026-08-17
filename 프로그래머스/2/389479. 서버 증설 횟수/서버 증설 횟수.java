class Solution {
    static int HOURS=24;
    public int solution(int[] players, int m, int k) { 
        // m*n ~ m*(n+1)
        // 서버당 감당 가능 인원:m
        // 증설 시 지속 시간: k

        // totsvrNeeded = hotSvr + svrAdded
        // 서버 꺼지는 시간 반영하는 배열
        int[] svrOffTime = new int[HOURS];
        int hotSvr = 0;
        int svrAdded = 0;
        for(int h=0; h<HOURS; h++)
        {
            int player = players[h];

            if(svrOffTime[h]!=0) hotSvr = Math.max(hotSvr - svrOffTime[h],0);

            int totSvrNeeded = player/m;

            // totSvrNeeded-hotSvr가 양수일 때만 더해준다.
            // 즉 해당 서버 사용자 수 보다 띄워져 있는 서버가 더 많다고 서버를 줄이지 않는다.
            int givHourAdded = Math.max(totSvrNeeded-hotSvr , 0);
            svrAdded += givHourAdded;

            // 띄워져 있는 서버, 필요한 서버 중 더 큰 수를, 띄워져 있는 서버 수로 지정한다.
            hotSvr=Math.max(hotSvr, totSvrNeeded);

            if(h + k < HOURS) svrOffTime[h+k] = givHourAdded;
        }
        
        return svrAdded;
    }
}