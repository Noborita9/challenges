pub mod nodeconnections {
    pub struct NodeConnection {
        nodes: Vec<String>,
        value: i32
    }

    
    pub struct NodeMap {
        node_connections: Vec<NodeConnection>,
    }
}
