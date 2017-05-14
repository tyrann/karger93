#include <iostream>
#include <vector>
#include <set>

using namespace std;


struct edge {
	pair<int,int> endpoints;
	
};

struct graph{
	
	struct edge* edge_list;

	int num_vertices;
	int num_edges;
};


pair<int,int> run_karger(struct graph* g){
	int V = g->num_vertices;
	//Create a collection of sets
	set<int> *c_set = new set<int>[g->num_vertices] ;

	//Add each vertex in its own set
	for (int i = 0; i < V; ++i) {

		c_set[i].insert(i);
		
	}

	for (int i =0;i < V;i++)
    {
        cout << "size of set # " << i << ' ' << c_set[i].size() << endl;
    }

	while(V != 2){
		//Pick edge at random
		
		//Check where endpoint are
		
		// Merge subset if different
		

	}
	//Retreive size of cut and edges
	//Rerun until obtaining all min cut

}




int main(int argc, char *argv[])
{
	struct graph* g = new graph();

	int vertices, edges;
	cin >> vertices >> edges;

	g->num_vertices = vertices;
	g->num_edges = edges;
	g->edge_list = new edge[edges];

	for (int i = 0; i < edges; ++i) {
		cin >> g->edge_list[i].endpoints.first >> g->edge_list[i].endpoints.second;

		//printf("Adding edge %d: %d <-> %d\n",i,g->edge_list[i].endpoints.first,g->edge_list[i].endpoints.second);
		
	}

	run_karger(g);

	


	
	return 0;
}
