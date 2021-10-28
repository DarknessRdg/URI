#include <iostream>
#include <stack>
#include <vector>
#include <algorithm>
using namespace std;

class Node;
class Edge;


class Node {
public:
    char rep;
    int visited;
    vector<Edge*> edges;

    Node(char representation) {
        rep = representation;
        visited = false;
    }

    void add_edge(Edge* e) {
        edges.emplace_back(e);
    }

    bool equal(Node* other) {
        return other->rep == rep;
    }

    void visit() { visited = true; }
};


class Edge {
public:
    Node* a;
    Node* b;
    bool visited;

    Edge(Node* _a, Node* _b) {
        a = _a;
        b = _b;
        visited = false;

        a->add_edge(this);
        b->add_edge(this);
    }

    bool is_available(Node* node) {
        return !visited && (a->equal(node) || b->equal(node));
    }

    Node* get_different_node(Node* node) {
        if (a->equal(node)) {
            return b;
        }
        return a;
    }

    void visit() { visited = true; }
};


vector<char> bfs(Node* current_node) {
    vector<char> components;

    stack<Node*> nodes_stack;

    nodes_stack.push(current_node);

    // filter
    while (!nodes_stack.empty()) {
        current_node = nodes_stack.top();
        nodes_stack.pop();

        if (current_node->visited) { continue; }

        current_node->visit();
        components.emplace_back(current_node->rep);

        for (auto e: current_node->edges) {
            if (e->is_available(current_node)) {
                e->visit();
                nodes_stack.push(e->get_different_node(current_node));
            }
        }
    }

    return components;
}


void test_case() {
    int amount_nodes, amount_edges;
    cin >> amount_nodes;
    cin >>amount_edges;

    int count_connected_components = 0;

    Node* nodes[amount_nodes];
    Edge* edges[amount_edges];

    for (int i = 0; i < amount_nodes; i++) {
        nodes[i] = new Node('a' + i);
    }

    char a, b;
    for (int i = 0; i < amount_edges; i++) {
        cin >> a;
        cin >> b;

        auto node_a = nodes[a - 'a'];
        auto node_b = nodes[b - 'a'];

        edges[i] = new Edge(node_a, node_b);
    }

    for (int i = 0; i < amount_nodes; i++) {
        auto node = nodes[i];

        if (!node->visited) {
            auto components = bfs(node);

            sort(components.begin(), components.end());

            for (auto c: components) {
                cout << c << ',';
            }
            cout << endl;

            count_connected_components++;
        }
    }
    cout << count_connected_components << " connected components" <<endl;

}

int main() {
    int amount_test_case;
    cin >> amount_test_case;

    for (int i = 0; i < amount_test_case; i++) {
        cout << "Case #" << i+1 << ":" << endl;
        test_case();
        cout << endl;
    }

    return 0;
}
