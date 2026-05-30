notes=["""python基础数据结构
符号	数据结构	英文名	特点	示例
{k: v}	字典	dict	键值对映射，键唯一，查找极快	{"id": 101}
{x}	集合	set	无序，去重，支持交集/并集运算	{1, 2, 3}
[ ]	列表	list	有序，可变，随意增删改	[1, 2, 3]
( )	元组	tuple	有序，不可变，历史数据或配置	(1, 2, 3)""",
"""推
杠铃卧推/4*5
记录
5.24/60
5.28/60，7
tips
整个脚掌踩实地面，向下蹬，使臀大肌受紧（利于下肢稳定）
肩胛骨向后缩

上斜卧推/3*8
记录
5.28/15器械
tips
凳子余角为30度
稍微挺胸
手臂稍微内旋
保正哑铃稳定性，不要发生旋转
坐姿下胸/3*8
记录
tips
肩胛骨顶住靠板，下背略微反弓
挺胸，肩胛骨哦内收
推的时候靠虎口位置发力
哑铃侧平举/3*12
三头/3*12""",
"""腿
罗马尼亚硬拉
tips
小腿始终保持垂直地面，腰背不可弯
杆始终不超过脚尖
髋关节向后
不要过度挺胸，保持身体直立即可
记录
5.26/60kg，10
深蹲 or哈克深蹲
保加利亚分腿蹲/3*8
记录
5.22/5，12
5.26/12.5，
tips
身体先前倾斜15到30度
下放：髋部向后下方推，膝盖跟随但不过度前移，前小腿保持接近垂直
最低点：前大腿与地面平行，感觉臀和腘绳被拉伸
发力：前脚跟踩地，臀部带动髋伸，回到起始位

臀推 /3*8
记录
5.22/20，12
5.26/60，8
tips
杠铃放在大腿根部
推起时小腿垂直地面
颈椎保持稳定
上背1/3 或者肩胛低端在靠背上

单腿RLD or 北欧腿弯举/3*8
哑铃推肩  /3*8
记录
5.22/15，8
侧平举/3*12
记录
5.22/5，12
二头弯举/3*10
记录
5.25/15kg
5.26/20kg，8""",
"""拉
引体向上/4*力竭/不做
T杆划船/4*8
坐姿划船/4*6
记录
5.25/45kg
tips
肘关节内收，下压
拉向腹部
身体不要反弓
高位下拉/3*10
记录
5.25/宽50kg，窄45kg
反向飞鸟/3*12
面拉/3*15""",
"""增肌
|食物    |数量 |热量     |蛋白质      |碳水       |脂肪       |
|------|---|-------|---------|---------|---------|
|燕麦    |80g|316    |8.8g     |48g      |7.8g     |
|蛋白粉   |15g|55     |11g      |1.5g     |0.5g     |
|鸡蛋    |2个 |140    |12g      |0g       |10g      |
|**小计**|   |**511**|**31.8g**|**49.5g**|**18.3g**|

午餐



|食物    |数量  |热量     |蛋白质    |碳水     |脂肪       |
|------|----|-------|-------|-------|---------|
|荞麦面   |120g|410    |14g    |77g    |0g       |
|鸡胸肉丸  |150g|110    |29g    |5g     |2.4g     |
|蔬菜    |200g|40     |2g     |6g     |0g       |
|花椒油   |10g |90     |0g     |0g     |10g      |
|**小计**|    |**650**|**45g**|**88g**|**12.4g**|

晚餐
| 同午餐 | | 650 | 45g | 88g | 12.4g |
练后加餐



|食物    |数量 |热量     |蛋白质       |碳水       |脂肪    |
|------|---|-------|----------|---------|------|
|蛋白粉   |15g|55     |11g       |1.5g     |0.5g  |
|提子饼   |50g|165    |1.75g     |29g      |4.5g  |
|**小计**|   |**220**|**12.75g**|**30.5g**|**5g**|

睡前



|食物    |数量 |热量     |蛋白质    |碳水    |脂肪     |
|------|---|-------|-------|------|-------|
|鸡蛋    |2个 |140    |12g    |0g    |10g    |
|坚果    |30g|180    |4g     |6g    |16g    |
|**小计**|   |**320**|**16g**|**6g**|**26g**|

每日总计



|指标 |数值          |
|---|------------|
|总热量|**2351kcal**|
|蛋白质|**151g**    |
|碳水 |**262g**    |
|脂肪 |**74g**     |""",
"""主机配置
i5 12400f  微星proH610M-S WiFi  1259
微星RTX4060万图师  2250
长城6000DS500w  219
咸鱼海盗船DDR4 2*8g 3200hz  450
咸鱼三星PM981 256G固态 200
咸鱼机箱+5风扇  112
三星t7 1t
总  4490""",
"""图论：去问自己这一步到底在防什么
DFS
List<List<Integer>> result = new ArrayList<>();
List<Integer> path = new ArrayList<>();

void dfs(图, 目前搜索的节点) {
    if(终止条件) {
        result.add(new ArrayList<>(path));  // 存放结果
        return;
    }
    
    for(选择: 本节点连接的节点) {
        path.add(节点);          // 处理节点
        dfs(图, 选择的节点);     // 递归
        path.remove(path.size()-1);  // 回溯，撤销处理结果
    }
}

组合枚举型（选数、拼数）
数字是基本类型，java是值传递，自己会回溯
static void dfs(int start, int count, long sum) {
    if(count == k) {
        // 处理结果
        return;
    }
    for(int i = start; i < n; i++) {
        dfs(i+1, count+1, sum+ele[i]);
    }
}

图/迷宫型（需要回溯vis）
static void dfs(int x, int y) {
    if(到达终点) {
        // 处理结果
        return;
    }
    for(四个方向) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if(越界 || vis[nx][ny] || 障碍) continue;
        vis[nx][ny] = true;
        dfs(nx, ny);
        vis[nx][ny] = false;  // 回溯
    }
}

BFS:vis[]是入口的守卫，防止重复入队，所以元素只要加入队列，立刻标记为访问过的节点
static void bfs(int x, int y) {
    Queue<int[]> queue = new LinkedList<>();
    queue.add(new int[]{x, y});
    vis[x][y] = true;
    dist[x][y] = 0;
    
    while(!queue.isEmpty()) {
        int[] p = queue.poll();
        for(int i = 0; i < 4; i++) {
            int nx = p[0] + dx[i];
            int ny = p[1] + dy[i];
            if(越界 || vis[nx][ny] || 障碍) continue;
            vis[nx][ny] = true;
            dist[nx][ny] = dist[p[0]][p[1]] + 1;
            queue.add(new int[]{nx, ny});
        }
    }
}
最小生成树prim：稠密图，对点操作
可以用堆优化和dijkstra基本一致
1. 第一步，选距离生成树最近节点
2. 第二步，最近节点加入生成树
3. 第三步，更新非生成树节点到生成树的距离（即更新minDist数组）
	minDist数组用来记录每一个节点距离最小生成树的最近距离

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int v = scanner.nextInt();
        int e = scanner.nextInt();

        int INF = 10001;
        int[][] grid = new int[v + 1][v + 1];
        for (int i = 0; i <= v; i++) {
            Arrays.fill(grid[i], INF);
        }

        for (int i = 0; i < e; i++) {
            int x = scanner.nextInt();
            int y = scanner.nextInt();
            int k = scanner.nextInt();
            grid[x][y] = k;
            grid[y][x] = k;
        }

        int[] minDist = new int[v + 1];
        Arrays.fill(minDist, INF);
        boolean[] inTree = new boolean[v + 1];

        minDist[1] = 0; // 显式指定起点

        for (int i = 1; i <= v; i++) {
            // 第一步：找未入树的最小距离节点
            int cur = -1;
            for (int j = 1; j <= v; j++) {
                if (!inTree[j] && (cur == -1 || minDist[j] < minDist[cur]))
                    cur = j;
            }

            // 判断不连通
            if (minDist[cur] == INF) {
                System.out.println(-1);
                return;
            }

            // 第二步：入树
            inTree[cur] = true;

            // 第三步：用 cur 更新邻居
            for (int j = 1; j <= v; j++) {
                if (!inTree[j] && grid[cur][j] < minDist[j])
                    minDist[j] = grid[cur][j];
            }
        }

        int result = 0;
        for (int i = 2; i <= v; i++) {
            result += minDist[i];
        }
        System.out.println(result);
    }
}
最小生成树Kruskal：稀疏图，对边操作
使用并查集优化
* 边的权值排序，因为要优先选最小的边加入到生成树里
* 遍历排序后的边
    * 如果边首尾的两个节点在同一个集合，说明如果连上这条边图中会出现环
    * 如果边首尾的两个节点不在同一个集合，加入到最小生成树，并把两个节点加入同一个集合
import java.util.*;

class Edge {
    int l, r, val;

    Edge(int l, int r, int val) {
        this.l = l;
        this.r = r;
        this.val = val;
    }
}

public class Main {
    private static int n = 10001;
    private static int[] father = new int[n];

    // 并查集初始化
    public static void init() {
        for (int i = 0; i < n; i++) {
            father[i] = i;
        }
    }

    // 并查集的查找操作
    public static int find(int u) {
        if (u == father[u]) return u;
        return father[u] = find(father[u]);
    }

    // 并查集的加入集合
    public static void join(int u, int v) {
        u = find(u);
        v = find(v);
        if (u == v) return;
        father[v] = u;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int v = scanner.nextInt();
        int e = scanner.nextInt();
        List<Edge> edges = new ArrayList<>();
        int result_val = 0;

        for (int i = 0; i < e; i++) {
            int v1 = scanner.nextInt();
            int v2 = scanner.nextInt();
            int val = scanner.nextInt();
            edges.add(new Edge(v1, v2, val));
        }

        // 执行Kruskal算法
        edges.sort(Comparator.comparingInt(edge -> edge.val));
	//edges.sort(edges,(a,b)->Integer.compare(a.val,b.val);

        // 并查集初始化
        init();

        // 从头开始遍历边
        for (Edge edge : edges) {
            int x = find(edge.l);
            int y = find(edge.r);

            if (x != y) {
                result_val += edge.val;
                join(x, y);
            }
        }
        System.out.println(result_val);
        scanner.close();
    }
}
Dijkstra
1. 第一步，选源点到哪个节点近且该节点未被访问过
2. 第二步，该最近节点被标记访问过
3. 第三步，更新非访问节点到源点的距离（即更新minDist数组）
	minDist数组 用来记录 每一个节点距离源点的最小距离
import java.util.*;

class Edge {
    int to;  // 邻接顶点
    int val; // 边的权重

    Edge(int to, int val) {
        this.to = to;
        this.val = val;
    }
}

class MyComparison implements Comparator<Pair<Integer, Integer>> {
    @Override
    public int compare(Pair<Integer, Integer> lhs, Pair<Integer, Integer> rhs) {
        return Integer.compare(lhs.second, rhs.second);
    }
}

class Pair<U, V> {
    public final U first;
    public final V second;

    public Pair(U first, V second) {
        this.first = first;
        this.second = second;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();

        List<List<Edge>> grid = new ArrayList<>(n + 1);
        for (int i = 0; i <= n; i++) {
            grid.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            int p1 = scanner.nextInt();
            int p2 = scanner.nextInt();
            int val = scanner.nextInt();
            grid.get(p1).add(new Edge(p2, val));
        }

        int start = 1;  // 起点
        int end = n;    // 终点

        // 存储从源点到每个节点的最短距离
        int[] minDist = new int[n + 1];
        Arrays.fill(minDist, Integer.MAX_VALUE);

        // 记录顶点是否被访问过
        boolean[] visited = new boolean[n + 1];

        // 优先队列中存放 Pair<节点，源点到该节点的权值>
        PriorityQueue<Pair<Integer, Integer>> pq = new PriorityQueue<>(new MyComparison());

        // 初始化队列，源点到源点的距离为0，所以初始为0
        pq.add(new Pair<>(start, 0));

        minDist[start] = 0;  // 起始点到自身的距离为0

        while (!pq.isEmpty()) {
            // 1. 第一步，选源点到哪个节点近且该节点未被访问过（通过优先级队列来实现）
            // <节点， 源点到该节点的距离>
            Pair<Integer, Integer> cur = pq.poll();

            if (visited[cur.first]) continue;

            // 2. 第二步，该最近节点被标记访问过
            visited[cur.first] = true;

            // 3. 第三步，更新非访问节点到源点的距离（即更新minDist数组）
            for (Edge edge : grid.get(cur.first)) { // 遍历 cur指向的节点，cur指向的节点为 edge
                // cur指向的节点edge.to，这条边的权值为 edge.val
                if (!visited[edge.to] && minDist[cur.first] + edge.val < minDist[edge.to]) { // 更新minDist
                    minDist[edge.to] = minDist[cur.first] + edge.val;
                    pq.add(new Pair<>(edge.to, minDist[edge.to]));
                }
            }
        }

        if (minDist[end] == Integer.MAX_VALUE) {
            System.out.println(-1); // 不能到达终点
        } else {
            System.out.println(minDist[end]); // 到达终点最短路径
        }
    }
}
Floyd
传递闭包（判断可达性）把"间接能到"变成"直接能到"
全源最短路（求任意两点最短距离）

三重循环，最外层枚举中间点，内层枚举起点终点，能拼起来就更新。
for (int mid = 0; mid < 10; mid++)
    for (int i = 0; i < 10; i++)
        for (int j = 0; j < 10; j++)
            if (reach[i][mid] && reach[mid][j])
                reach[i][j] = true;

memset(dis,0x3f,sizeof(dis));      //初始化为极大值
for(int i=1;i<=n;i++) dis[i][i]=0; //自己到自己不必花费
for(int k=1;k<=n;k++)
{
	for(int i=1;i<=n;i++)
	{
		for(int j=1;j<=n;j++)
		{
			if(dis[i][j]<dis[i][k]+dis[k][j]) dis[i][j]=dis[i][k]+dis[k][j];
		}
	}
}

DP
1. 确定dp数组（dp table）以及下标的含义
2. 确定递推公式
3. dp数组如何初始化
4. 确定遍历顺序
5. 举例推导dp数组
01背包：滚动数组
int[] dp = new int[V + 1]; // V 是背包总容量
w[]为物品重量
v[]为物品价值
for (int i = 0; i < n; i++) { // 遍历物品
    // 注意：必须逆序遍历容量！
    for (int j = V; j >= w[i]; j--) { 
        dp[j] = Math.max(dp[j], dp[j - w[i]] + v[i]);
    }
}
System.out.println(dp[V]);
完全背包：遍历背包的时候正序
一维的时候注意：（二维无所谓）
如果求组合数就是外层for循环遍历物品，内层for遍历背包。//不要求顺序
如果求排列数就是外层for遍历背包，内层for循环遍历物品。//要求顺序

线性dp：求最长序列
求最长增序列
public int lengthOfLIS(int[] nums) {
        int n=nums.length;
        int[] dp=new int[n];
        Arrays.fill(dp,1);
        for(int i=0;i<n;i++){
            for(int j=0;j<i;j++){
                if(nums[j]<nums[i]){
                    dp[i]=Math.max(dp[i],dp[j]+1);
                }
            }
        }
        int max=0;
        for(int i=0;i<n;i++){
            if(max<dp[i]) max=dp[i];
        }
        return max;
    }


埃氏筛
    boolean [] isprims=new boolean[n+1];
    Arrays.fill(isprims, true);
    isprims[0]=false;
    isprims[1]=false;
    for(int i=2;i*i<=n;i++) {
      if(isprims[i]) {
        for(int j=i*i;j<=n;j+=i) {
          isprims[j]=false;
        }
      }
    }
  
并查集 O( logN)—O(1)
int n = 1005; // n根据题目中节点数量而定，一般比节点数量大一点就好
vector<int> father = vector<int> (n, 0); // C++里的一种数组结构

// 并查集初始化
void init() {
    for (int i = 0; i < n; ++i) {
        father[i] = i;
    }
}
// 并查集里寻根的过程
int find(int u) {
    if (u == father[u]) return u;
    else return father[u] = find(father[u]); // 路径压缩
}

// 判断 u 和 v是否找到同一个根
bool isSame(int u, int v) {
    u = find(u);
    v = find(v);
    return u == v;
}

// 将v->u 这条边加入并查集
void join(int u, int v) {
    u = find(u); // 寻找u的根
    v = find(v); // 寻找v的根
    if (u == v) return ; // 如果发现根相同，则说明在一个集合，不用两个节点相连直接返回
    father[v] = u;
}
队列
单调队列
单调增队列，last到farst递增，farst为该窗口内的最大值
Deque<Integer> dq=new ArrayDeque<>();//dq存的是index
for (int i = 0; i < n; i++) {
    // 1. 队尾比新值小，弹（维护单调递减）
    while (!dq.isEmpty() && a[dq.peekLast()] <= a[i]) dq.pollLast();//单调减把<=换成>=即可
    // 2. 入队
    dq.addLast(i);
    // 3. 队首过期，弹
    if (dq.peekFirst() < i - k + 1) dq.pollFirst();
    // 4. 窗口满了，取结果
    if (i >= k - 1) result += a[dq.peekFirst()];
}
快速幂
static long power(int x,int n){
    long result=1;
    while (n!=0){
        if(n%2==1) result=result*x;
        x=x*x;
        n=n/2;
    }
    return result;
}
快速幂取模：每次乘法后面都跟 % MOD，无一例外
static long power(int x,int n，long mod){
    long result=1;
    x=x%mod;
    while (n!=0){
        if(n%2==1) result=result*x%mod;
        x=x*x%mod;
        n=n/2;
    }
    return result;
}
回溯
回溯法抽象为树形结构后，其遍历过程就是：for循环横向遍历，递归纵向遍历，回溯不断调整结果集。
void backtracking(参数) {
    if (终止条件) {
        存放结果;
        return;
    }


    for (选择：本层集合中元素（树中节点孩子的数量就是集合的大小）) {
        处理节点;
        backtracking(路径，选择列表); // 递归
        回溯，撤销处理结果
    }
}
辗转相除法：求最大公约数"""]