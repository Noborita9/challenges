struct NodeConnection {
    nodes: Vec<String>,
    value: i32,
}

impl NodeConnection {
    fn contains(&self,node: String) -> bool {
        if node == self.nodes[0] || node == self.nodes[1]{
            return true;
        } else {
            return false
        }
    }
}


fn main() {
    let node_connection = NodeConnection{
        nodes: vec!["A".to_string(), "B".to_string()],
        value: 100
    };
    println!("Hello, world!");
}

fn return_node_connection(nodes: Vec<String>) -> NodeConnection {
    NodeConnection{
        value: 1,
        nodes,
    }
}
