class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    nodes_to_search = [self.root]

    while len(nodes_to_search) > 0:
      node = nodes_to_search.pop()
      if node['id'] == id:
        return node
      
      if node['children']:
        nodes_to_search = nodes_to_search + node['children']
      
    return None 