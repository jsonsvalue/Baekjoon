import java.util.*;

class Solution {
    public int solution(String[][] book_time) {
        int len = book_time.length;

        int[][] bookings = new int[len][2];

        // 숫자로 바꿔서 bookings에 넣는다.
        // String이 아니라 숫자 범위로 확인하는 방식으로 바꾸는 것이다.
        for(int i=0; i<len; i++)
        {
            String start = book_time[i][0];
            String end = book_time[i][1];

            String[] startStr = start.split(":");
            String[] endStr = end.split(":");

            int startInt = Integer.parseInt(startStr[0]) * 60 +Integer.parseInt(startStr[1]);
            int endInt = Integer.parseInt(endStr[0]) * 60 + Integer.parseInt(endStr[1]);

            bookings[i][0] = startInt;
            bookings[i][1] = endInt;
        }
        Arrays.sort(bookings, (a,b)->Integer.compare(a[0], b[0]));

        // 각 방별로 사용 시간대를 넣음.
        Map<Integer, ArrayList<int[]>> totalRooms = new HashMap<>();
        ArrayList<int[]> rooms = new ArrayList<>();
        int roomNum =1;

        for(int i=0; i<len; i++)
        {
            int startBook = bookings[i][0];
            int endBook = bookings[i][1] + 10;

            // 방이 비어 있으면 첫 방에 배정해준다.
            if(totalRooms.size()==0)
            {
                rooms.add(new int[]{startBook, endBook});
                totalRooms.put(roomNum, rooms);
                continue;
            }

            // 방을 탐색하면서 방 내 사용 시간과 겹친다면 새로운 방을 만들어주고,
            // 겹치지 않으면 해당 방에 넣어준다.
            boolean makeRoom = true;

            outer:for(int key: totalRooms.keySet())
            {
                boolean useRoom = true;
                ArrayList<int[]> tempRoom = totalRooms.get(key);
                int hourSize = tempRoom.size();
                // 주어진 방에 대해서,
                // 한번이라도 시간이 겹치는 시간대가 있는지 확인한다.
                for(int k=0; k<hourSize; k++)
                {
                    int[] roomUse = tempRoom.get(k);
                    int startRoomUse = roomUse[0];
                    int endRoomUse = roomUse[1];

                    if( startRoomUse < endBook && startBook< endRoomUse )
                    {
                        useRoom = false;
                        break;
                    }
                }

                // 주어진 방에 대해서 사용 시간이 한번이라도 겹치지 않는다면,
                // 해당 방에a만 사용 시간을 넣어준다.
                if(useRoom)
                {
                    tempRoom.add(new int[]{startBook, endBook});
                    makeRoom = false;
                    break outer;
                }
            }

            // 주어진 방에 대해서 시간이,
            // 겹친다면 새로운 방을 만들어준다.
            if(makeRoom)
            {
                ArrayList<int[]> newRoom = new ArrayList<>();
                newRoom.add(new int[]{startBook, endBook });

                roomNum++;
                totalRooms.put(roomNum, newRoom);
            }
        }
        
        return totalRooms.size();
    }
}