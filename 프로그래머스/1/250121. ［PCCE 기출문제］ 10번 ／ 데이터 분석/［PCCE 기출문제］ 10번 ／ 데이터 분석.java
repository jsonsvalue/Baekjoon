import java.util.*;

class Solution {
    public int[][] solution(int[][] totdata, String ext, int val_ext, String sort_by) {
        int len = totdata.length;
        
        ArrayList<Data> datas = new ArrayList<>();
        
        // 기준에 부합하는 data만 datas에 넣는다.
        int idx = -1;
        if(ext.equals("code"))
        {
            idx=0;
        }
        else if(ext.equals("date"))
        {
            idx=1;
        }
        else if(ext.equals("maximum"))
        {
            idx=2;
        }
        else if(ext.equals("remain"))
        {
            idx=3;
        }
        
        for(int i=0; i<len; i++)
        {
            int[] temp = totdata[i];
            
            int code = temp[0];
            int date = temp[1];
            int maximum = temp[2];
            int remain = temp[3];
            
            int check_data = temp[idx];
            if(check_data < val_ext)
            {
                Data tempData = new Data(code, date, maximum, remain);
                datas.add(tempData);    
            }
        }
        
        // 기준: ext
        // 기준값: val_ext
        // 정보 정렬 기준: sort_by
        PriorityQueue<Data> pq = new PriorityQueue<>(
            (a,b)->{
                if(sort_by.equals("code"))
                {
                    return Integer.compare(a.code, b.code);    
                }
                else if(sort_by.equals("date"))
                {
                    return Integer.compare(a.date, b.date);
                }
                else if(sort_by.equals("maximum"))
                {
                    return Integer.compare(a.maximum, b.maximum);
                }
                else if(sort_by.equals("remain"))
                {
                    return Integer.compare(a.remain, b.remain);
                }
                
                return 0;
            }  
        );
        
        // 기준에 부합하는 datas를 정렬 조건에 맞게 pq에 넣는다.
        for(int i=0; i<datas.size(); i++)
        {
            pq.add(datas.get(i));
        }
        
        // answers에 담아서 정답을 반환한다.
        int ansIdx = 0;
        int totNum = pq.size();
        int[][] answer = new int[totNum][4];
        while(!pq.isEmpty())
        {
            Data temp = pq.poll();
            
            answer[ansIdx][0]=temp.code;
            answer[ansIdx][1]=temp.date;
            answer[ansIdx][2]=temp.maximum;
            answer[ansIdx][3]=temp.remain;
            
            ansIdx++;
        }
        
        return answer;
    }
    
    static class Data
    {
        int code;
        int date;
        int maximum;
        int remain;
        
        public Data(int code, int date, int maximum, int remain)
        {
            this.code = code;
            this.date = date;
            this.maximum = maximum;
            this.remain = remain;
        }
    }
}