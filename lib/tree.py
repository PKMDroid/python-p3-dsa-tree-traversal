# tree.py

class Tree:
    def __init__(self, root):
        """Initialize tree with a root node"""
        self.root = root

    def get_element_by_id(self, target_id):
        """Return the first element with matching id, or None if not found"""
        def dfs(node):
            if node.get('id') == target_id:
                return node
            for child in node.get('children', []):
                result = dfs(child)
                if result is not None:
                    return result
            return None

        return dfs(self.root)
