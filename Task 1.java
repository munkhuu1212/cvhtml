class Solution {
    private Set<Pair<Integer, Integer>> visit = new HashSet<>();
    
    public int islandPerimeter(int[][] grid) {
        for(int i = 0; i < grid.length; i++) {
            for(int j = 0; j < grid[0].length; j++) {
                if(grid[i][j] == 1) {
                    return dfs(i, j, grid);
                }
            }
        }
        return 0;
    }
    
    private int dfs(int i, int j, int[][] grid) {
        if(i >= grid.length || j >= grid[0].length || i < 0 || j < 0 || grid[i][j] == 0) {
            return 1;
        }
        
        Pair<Integer, Integer> pair = new Pair<>(i, j);
        if(visit.contains(pair)) {
            return 0;
        }
        
        visit.add(pair);
        
        int perim = dfs(i, j + 1, grid);
        perim += dfs(i + 1, j, grid);
        perim += dfs(i - 1, j, grid);
        perim += dfs(i, j - 1, grid);
        
        return perim;
    }
}