#include <iostream>
#include <set>

using namespace std;


struct edge {
	int ep1, ep2;
	
};

struct graph{
	
	struct edge* edge_list;

	int num_vertices;
	int num_edges;
};





int main(int argc, char *argv[])
{

	int vertices, edges;
	cin >> vertices >> edges;

	printf("vertices %d\n",vertices);
	
	return 0;
}
