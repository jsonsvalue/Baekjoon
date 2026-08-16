import java.util.*;

class Solution {
    static int R, C;
    static String[][] graph;
    static int[] start, end;
    public int solution(String[] board) {
        int answer = 0;
        // R: 처음 위치
        // D: 장애물 위치
        // G: 목표지점 위치
        
        R = board.length;
        C = board[0].length();
        
        graph = new String[R][C];
        
        start = new int[2];
        end = new int[2];
        for(int r=0; r<R; r++)
        {
            String[] temp = board[r].split("");
            for(int c=0; c<C; c++)
            {
                graph[r][c] = temp[c];
                if(graph[r][c].equals("R"))
                {
                    start[0] = r;
                    start[1] = c;
                }
                else if(graph[r][c].equals("G"))
                {
                    end[0] = r;
                    end[1] = c;
                }
            }
        }
        
        // 시작점에서 끝점까지 가는 경로의 최소 횟수를 BFS를 통해서 확인한다.
        int[][] distance = new int[R][C];
        boolean[][] visited = new boolean[R][C];
        
        int result = bfs_ricochet(distance, visited);

        if(result==0) result =-1;
        
        return result;
    }
    
    static String builder(String[][] graph)
    {
        StringBuilder sb = new StringBuilder();
        
        for(int r=0; r<R; r++)
        {
            for(int c=0; c<C;c++)
            {
                sb.append(graph[r][c]).append(" ");
            }
            sb.append("\n");
        }
        
        return String.valueOf(sb);
    }
    
    static int bfs_ricochet(int[][] distance, boolean[][] visited)
    {
        // 벽이나 장애물에 부딪힐 때까지의 횟수를 1로 한다.
        Queue<int[]> q = new LinkedList<>();
        q.add(start);
        visited[start[0]][start[1]] = true;
        
        int count = 0;
        int[] dr = {-1,1,0,0};
        int[] dc = {0,0,-1,1};
        
        while(!q.isEmpty())
        {
            int[] curr = q.poll();
            int currR = curr[0];
            int currC = curr[1];
            
            // 벽이나 장애물에 부딪히기 전까지, 
            // 한방향으로 직진한다.
            for(int i=0; i<4; i++)
            {
                int nr = currR+dr[i];
                int nc = currC+dc[i];
                    
                if(nr<0 || nr>=R || nc<0 || nc>=C) continue;
                
                int dirR = dr[i];
                int dirC = dc[i];
                
                while(true)
                {
                    boolean collision = false;
                    
                    int collisionR = nr-dirR;
                    int collisionC = nc-dirC;
                    
                    // 게임판의 끝에 다다랐을 때
                    if(nr<0||nr>=R|| nc<0 || nc>=C)
                    {
                        if(!visited[collisionR][collisionC])
                        {
                            visited[collisionR][collisionC] = true;
                            q.add(new int[]{collisionR, collisionC});

                            distance[collisionR][collisionC] = distance[currR][currC]+1;
                        }

                        collision = true;
                    }
                    // 장애물에 부딪혔을 때
                    else if(graph[nr][nc].equals("D")) {
                        if (!visited[collisionR][collisionC]) {
                            visited[collisionR][collisionC] = true;
                            q.add(new int[]{collisionR, collisionC});

                            distance[collisionR][collisionC] = distance[currR][currC] + 1;
                        }
                        collision = true;
                    }
                    
                    if(collision) break;
                    
                    // 벽, 게임판 끝에 다다를 때까지 이동.
                    nr+=dirR;
                    nc+=dirC;   
                }       
            }    
        }
        
        return distance[end[0]][end[1]];    
    }
    
}