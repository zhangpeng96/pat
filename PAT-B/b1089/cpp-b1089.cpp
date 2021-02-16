/*
    @name     : b1089/a1148
    @author   : 丧心病狂工科女
    @source   : https://www.cnblogs.com/zlrrrr/p/10052716.html
*/

#include <bits/stdc++.h>
using namespace std;
 
const int maxn = 1e5 + 10;
int n;
int say[maxn];
 
int main() {
    scanf("%d", &n);
    for(int i = 1; i <= n; i ++) scanf("%d", &say[i]);
 
    for(int i = 1; i <= n; i ++) {
        for(int j = i + 1; j <= n; j ++) {
            vector<int> lie, a(n + 1, 1);
            a[i] = a[j] = -1;
            for(int k = 1; k <= n; k ++)
                if(say[k] * a[abs(say[k])] < 0) lie.push_back(k);
 
            if(lie.size() == 2 && a[lie[0]] + a[lie[1]] == 0) {
                printf("%d %d\n", i, j);
                return 0;
            }
        }
    }
 
    printf("No Solution\n");
    return 0;
}