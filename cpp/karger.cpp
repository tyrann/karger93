#include <stdlib.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <unistd.h>

using namespace std;



struct edge {
	pair<int,int> endpoints;
	
};

struct graph{
	
	vector<struct edge> edge_list;

	int num_vertices;
	int num_edges;
};


pair<int,int> run_karger(struct graph* g){
	int V = g->num_vertices;
	int E = g->num_edges;
	std::vector<struct edge> local_edge_list = g->edge_list;


	//Create a collection of sets
	vector <set<int>> v_set = vector<set<int>>(g->num_vertices) ;

	//Add each vertex in its own set
	for (int i = 0; i < V; ++i) {

		v_set[i].insert(i);
		
	}

	while(V != 2){

		//Pick edge at random
		struct edge e = local_edge_list[rand() % E];

		cout << e.endpoints.first << " <-> " << e.endpoints.second << endl;
		
		//Check where endpoint are
		vector<set<int>*>sets;
		
		for( auto &s : v_set){
			if(s.find(e.endpoints.first) != s.end() || s.find(e.endpoints.second) != s.end()){
				cout << "Found element in set" << endl;
				cout << *(s.begin()) << endl;
				sets.push_back(&s);
			}

		}
		cout << "Size of vector: "  <<sets.size() << endl;
		cout << *(sets[0]->begin()) << " && " << *(sets[1]->begin()) << endl;
		cout << "Showing sets:"<< endl;

		for(auto iter=sets[0]->begin(); iter!=sets[0]->end();++iter) {
			cout << "{"<< (*iter)<<"}" << ", ";
		}
		cout << endl;

		for(auto iter=sets[1]->begin(); iter!=sets[1]->end();++iter) {
			cout << "{"<< (*iter)<<"}" << ", ";
		}
		
		cout << endl;

		sleep(1);
		// Merge subset if different
		// TODO Do it faster
		if(!(*sets[0] == *sets[1])){
			cout << "different sets" << endl;
			//Update set
			sets[0]->insert(sets[1]->begin(),sets[1]->end());
			//Remove one
			v_set.erase(remove(v_set.begin(),v_set.end(), *sets[1]),v_set.end());
			V--;
		}
		

	}
	cout << "Over" << endl;
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
	g->edge_list = vector<edge>(edges);


	for (int i = 0; i < edges; ++i) {
		cin >> g->edge_list[i].endpoints.first >> g->edge_list[i].endpoints.second;
	}

	/*for (auto i = g->edge_list.begin(); i < g->edge_list.end();i++) {
		cout << (*i).endpoints.first << endl;
		
	}*/

	run_karger(g);

	


	
	return 0;
}
