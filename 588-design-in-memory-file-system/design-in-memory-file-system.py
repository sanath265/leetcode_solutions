class Node:
    def __init__(self):
        self.name = "/"
        self.children = {}
        self.is_file = False
        self.is_folder = False
        self.content = ""
class FileSystem:

    def __init__(self):
        self.folder = Node()
        

    def ls(self, path: str) -> List[str]:
        lis = path.split("/")
        lis = [s for s in lis if s.strip()]
        node = self.folder
        
        for name in lis:
            node = node.children[name]
        
        if node.is_file:
            return [node.name]
        # print(node.name, node.children)
        return sorted(list(node.children.keys()))
        

    def mkdir(self, path: str) -> None:
        lis = path.split("/")
        lis = [s for s in lis if s.strip()]
        node = self.folder

        for name in lis:
            if name in node.children:
                node = node.children[name]
            else:
                node = self.create_directory(name, node)
    
    def create_directory(self, name, node):
        new_node = Node()
        new_node.name = name
        new_node.is_folder = True
        node.children[name] = new_node
        return new_node

    def create_file(self, name, node):
        new_node = Node()
        new_node.name = name
        new_node.is_file = True
        node.children[name] = new_node
        return new_node

    def addContentToFile(self, filePath: str, content: str) -> None:
        lis = filePath.split("/")
        lis = [s for s in lis if s.strip()]
        node = self.folder
        for index in range(len(lis) - 1):
            name = lis[index]
            if name in node.children:
                node = node.children[name]
            else:
                node = self.create_directory(name, node)

        if lis[-1] in node.children and node.children[lis[-1]].is_file:
            # print(node.content)
            node = node.children[lis[-1]]
            node.content += content
        else:
            node = self.create_file(lis[-1], node)
            node.content += content


    def readContentFromFile(self, filePath: str) -> str:
        lis = filePath.split("/")
        lis = [s for s in lis if s.strip()]
        node = self.folder
        for index in range(len(lis)):
            name = lis[index]
            node = node.children[name]
        return node.content
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)