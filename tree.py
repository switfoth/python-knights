class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    @property
    def parent(self):
        return self._parent

    def add_child(self, node):
        if node not in self._children:
            self._children.append(node)
            node.parent = self


    def remove_child(self, node):
        node.parent = None
        self._children.remove(node)

    @parent.setter
    def parent(self, parent):
        if (self._parent != None) and (self._parent != parent) and parent != None:
            self._parent.remove_child(self)
        if (parent != None) and (self._parent != parent):
            self._parent = parent
            parent.add_child(self)
        if (parent == None):
            self._parent = parent

    def depth_search(self, value):
        if self._value == value:
            return self
        for child in self._children:
            node = child.depth_search(value)
            if node is not None:
                return node
        return None
