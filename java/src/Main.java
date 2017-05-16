import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Random;
import java.util.Scanner;


public class Main {
	static List<Edge> edges; 
	static int vertices_count;
	static int edges_count;
	static int[] parent_array;
	static int[] rank_array;
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		vertices_count = in.nextInt();
		edges_count = in.nextInt();

		parent_array = new int[vertices_count];
		rank_array = new int[vertices_count];
		
		edges = new ArrayList<Edge>(edges_count);
		
		for (int i = 0; i < edges_count; i++) {
			int v1 = in.nextInt();
			int v2 = in.nextInt();
			
			edges.add(new Edge(v1-1, v2-1));
		}
		
		karger();
		union(1, 2);
		
		
		return;
	}
	
	public static void karger() {
		Collections.shuffle(edges);
		
		for (int i = 0; i < parent_array.length; i++) {
			parent_array[i] = i;
			rank_array[i] = 0;
		}
		
		int v_count = vertices_count;
		int i = 0;
		
		while(v_count > 2) {
			Edge edge = edges.get(i);
			break;
		}
		
		return;
	}
	
	public static int find(int v) {
		if(parent_array[v] != v) {
			parent_array[v] = find(parent_array[v]);
		}
		
		return parent_array[v];
	}
	
	public static void union(int v1, int v2) {
		int root1 = find(v1);
		int root2 = find(v2);
		
		if (root1 != root2) {
			if(rank_array[root1] < rank_array[root2]) {
				parent_array[root1] = root2;
			} else if (rank_array[root1] > rank_array[root2]) {
				parent_array[root2] = root1;
			} else {
	            parent_array[root2] = root1;
	            rank_array[root1] += 1;
			}
		}
	}
}

class Edge {
	int x;
	int y;
	
	public Edge(int x, int y) {
		this.x = x;
		this.y = y;
	}
	
	@Override
	public String toString() {
		return "[" + x + "-" + y + "]";
	}
}