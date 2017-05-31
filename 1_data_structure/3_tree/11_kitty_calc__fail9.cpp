#include <algorithm>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

const int MAX_NODE = (2 * int(pow(10, 5))) + 1; // 200000 + 1
const int MAX_PARENT_HEIGH = int(log2(MAX_NODE)); // ..18

int n, q;
int parent[200001][18];
int depth[200001];
vector<int> adj[200001];

void makeDFSTree(int curr) {
	for (int next: adj[curr]) {
		if (depth[next] == -1) {
			parent[0][next] = curr;
			depth[next] = depth[curr] + 1;
			makeDFSTree(next);
		}
	}
}

int getLCA(int u, int v) {
	if (depth[u] < depth[v]) swap(u, v);
	int diff = depth[u] - depth[v];

	for (int i=0; diff; i++) {
		if (diff % 2)
			u = parent[i][u];
		diff /= 2;
	}

	if (u != v) {
		for (int j=MAX_PARENT_HEIGH-1; j>=0; j--) {
			if(parent[j][u] != -1 && parent[j][u] != parent[j][v]) {
                u = parent[j][u];
                v = parent[j][v];
            }
		}
		u = parent[0][u];
	}

	return u;
}

int getDistance(int u, int v) {
	int lca = getLCA(u, v);
	return depth[u] + depth[v] + (depth[lca] * 2);
}

int main() {
	cin>>n>>q;

	for(int i=0; i<n-1; i++) {
		int u, v;
		cin>>u>>v;
		adj[u].push_back(v);
		adj[v].push_back(u);
	}

	memset(parent, -1, sizeof(parent));
	fill(depth, depth+n, -1);
	depth[1] = 0;

	makeDFSTree(1);

	for (int i=0; i<MAX_PARENT_HEIGH; i++) {
		for (int j=1; j<n+1; j++) {
			if (parent[i][j] != -1)
				parent[i+1][j] = parent[i][parent[i][j]];
		}
	}

	for (int i=0; i<q; i++) {
		int k, node;
		vector <int> nodes;
		cin>>k;
		for (int j=0; j<k; j++) {
			cin>>node;
			nodes.push_back(node);
		}

		int s = 0;
		for (int x=0; x < nodes.size()-1; x++) {
			for (int y=x+1; y < nodes.size(); y++) {
				s += nodes[x] * nodes[y] * getDistance(nodes[x], nodes[y]);
			}
		}
		int kitty_cal = s % (int(pow(9, 10)) + 7);
		printf("%d\n", kitty_cal);
	}

	return 0;
}