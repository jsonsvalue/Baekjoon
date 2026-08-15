import java.util.*;

class Solution {
    static int R, C;
    static boolean[][] visited;
    
    public int solution(int[][] land) {
        int answer = 0;
        
        R = land.length;
        C = land[0].length;
        
        visited = new boolean[R][C];
        
        int[] dp = new int[C];
        // dp 배열에는 각 열마다 탐색 시 시추할 수 있는 석유량을 저장.
        // 매번 bfs로 탐색하지 않고 주어진 dp 배열에서 계산.
        for(int r=0; r<R; r++)
        {
            for(int c=0; c<C; c++)
            {
                if(!visited[r][c] && land[r][c]==1) bfs(dp, r, c, land);
            }
        }
        
        // dp배열에서 각 열에서의 시추량 중 최대값을 반환.
        return findMax(dp);
        
        // 프로그래머스, C코드 마무리, instant runoff 객체지향코드 (토,일,월)
        // SQL
        
    }
    
    // 각 열에서 석유를 시추했을 때 최대양을 찾는다.
    static int findMax(int[] dp)
    {
        int max = Integer.MIN_VALUE;
        for(int c=0; c<C; c++)
        {
            max = Math.max(dp[c], max);
        }
        
        return max;
    }
    
    // 각 지점에서 bfs를 실행하고, 각 열마다 시추량을 dp배열에 저장
    // 각 석유 시추 지점마다 열별로 시추량을 저정하기 때문에
    // bfs 내부에서 set을 만드는 것이 적절하다.
    static void bfs(int[] dp, int r, int c, int[][] land)
    {        
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{r,c});
        visited[r][c] = true;
        
        Set<Integer> columnSet = new HashSet<>();
        columnSet.add(c);
        
        int amount = 1;
        int[] dr = {-1,1,0,0};
        int[] dc = {0,0,-1,1};
        
        while(!q.isEmpty())
        {
            int[] curr = q.poll();
            int currR = curr[0];
            int currC = curr[1];
            
            // 어차피 한번 탐색할 때 큐에 여러 번 넣는게 낫지 않나.
            for(int i=0; i<4; i++)
            {
                int nr = currR + dr[i]; 
                int nc = currC + dc[i];
            
                if(nr<0 || nr>=R || nc<0 || nc>=C) continue;

                if(land[nr][nc]==0) continue;

                // 조건 다 통과했을 시 방문 안한 곳이라면, 
                // bfs 수행.
                // 방문한 곳마다 석유 시추량을 amount 변수에 저장.
                if(!visited[nr][nc])
                {
                    visited[nr][nc] = true;
                    q.add(new int[]{nr, nc});
                    amount++;

                    columnSet.add(nc);
                }
            }
        }
        
        // dp 배열에 각 열마다 석유 시추량을 저장한다.
        for(int cs:columnSet)
        {
            dp[cs] += amount;
        }
        
    }
    
}