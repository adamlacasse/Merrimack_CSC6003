class Creature:
    def __init__(self, name):
        self.name = name
        self.left_child = None
        self.right_child = None

    def add_child(self, child_name):
        if not self.left_child:
            self.left_child = Creature(child_name)
            return True
        elif not self.right_child:
            self.right_child = Creature(child_name)
            return True
        else:
            return False

    def search(self, name, ancestors = None):
        if ancestors is None:
            ancestors = []

        if self.name == name:
            return self, ancestors

        if self.left_child:
            found, ancestors_left = self.left_child.search(name, ancestors + [self.name])
            if found:
                return found, ancestors_left

        if self.right_child:
            found, ancestors_right = self.right_child.search(name, ancestors + [self.name])
            if found:
                return found, ancestors_right

        return None, []

    def print_tree(self, level=0):
        print("  " * level + self.name)
        if self.left_child:
            self.left_child.print_tree(level + 1)
        if self.right_child:
            self.right_child.print_tree(level + 1)
