#include <stdlib.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <unistd.h>
#include <assert.h>

using namespace std;



struct edge {
	pair<int,int> endpoints;
	
};

struct graph{
	
	vector<struct edge> edge_list;

	int num_vertices;
	int num_edges;
};


int* run_karger(struct graph* g){

	return NULL;
}




int main(int argc, char *argv[])
{
	struct graph* g = new graph();

	int vertices, edges;
	cin >> vertices >> edges;

	g->num_vertices = vertices;
	g->num_edges = edges;
	g->edge_list = vector<edge>(edges);


	for (int i = 0; i < edges; ++i) {
		cin >> g->edge_list[i].endpoints.first >> g->edge_list[i].endpoints.second;
	}

	for(int i = 0; i < 40000; i++){
	int* res = run_karger(g);
	}


	


	
	return 0;
}
