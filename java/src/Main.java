import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;


public class Main {
	static List<Edge> edges;
	static int vertices_count;
	static int edges_count;
	static int[] parent_array;
	static int[] rank_array;
	static int min_cut_size;
	static Set<Set<Edge>> cut_collection;
	static int current_collection_rank;

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);

		vertices_count = in.nextInt();
		edges_count = in.nextInt();

		parent_array = new int[vertices_count];
		rank_array = new int[vertices_count];

		edges = new ArrayList<Edge>(edges_count);
		cut_collection = new HashSet<Set<Edge>>();
		current_collection_rank = edges_count;

		for (int i = 0; i < edges_count; i++) {
			int v1 = in.nextInt();
			int v2 = in.nextInt();

			edges.add(new Edge(v1 - 1, v2 - 1));
		}
		int iter = vertices_count*vertices_count*6;
		min_cut_size = edges_count;
		for (int i = 0; i < iter; i++) {
			Set<Edge> cut = karger();
			if (cut != null) {
				if (!cut.isEmpty()) {
					cut_collection.add(cut);
				}

			}

		}

		System.out.println(min_cut_size + " " + cut_collection.size());

		in.close();
		return;
	}

	public static Set<Edge> karger() {
		Collections.shuffle(edges);

		for (int i = 0; i < parent_array.length; i++) {
			parent_array[i] = i;
			rank_array[i] = 0;
		}

		int v_count = vertices_count;
		int i = 0;

		while (v_count > 2) {

			Edge random_edge = edges.get(i);

			int root1 = find(random_edge.x);
			int root2 = find(random_edge.y);

			if (root1 != root2) {
				union(root1, root2);
				v_count--;

			}
			i++;

		}
		Set<Edge> cut_edges = new HashSet<Edge>();
		int cut_size = 0;
		for (int j = 0; j < edges_count; j++) {
			Edge current = edges.get(j);

			int r1 = find(current.x);
			int r2 = find(current.y);

			if (r1 != r2) {
				cut_size++;

				if (cut_size > min_cut_size) {
					return null;
				}
				cut_edges.add(current);
			}

		}
		if (cut_size < min_cut_size) {
			min_cut_size = cut_size;
		}
		if(cut_size < current_collection_rank){
			current_collection_rank = cut_size;
			cut_collection.clear();
		}
		return cut_edges;

	}

	public static int find(int v) {
		if (parent_array[v] != v) {
			parent_array[v] = find(parent_array[v]);
		}

		return parent_array[v];
	}

	public static void union(int v1, int v2) {
		int root1 = find(v1);
		int root2 = find(v2);

		if (root1 != root2) {
			if (rank_array[root1] < rank_array[root2]) {
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
	private final Set<Integer> set;
	
	public Edge(int x, int y) {
		this.x = x;
		this.y = y;
        set = new HashSet<Integer>();
        set.add(x);
        set.add(y);
	}

	@Override
	public String toString() {
		return "[" + x + "-" + y + "]";
	}

	@Override
	public int hashCode() {
		return set.hashCode();

	}
}
