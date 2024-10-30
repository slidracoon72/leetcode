from typing import List


# Neetcode: https://www.youtube.com/watch?v=WDDLp2l9TrM
class Solution:
    # Brute Force - Works well
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Convert the folder list to a set for O(1) average lookup time
        folder_set = set(folder)
        res = []  # List to store the folders that are not subfolders

        # Iterate through each folder path in the input list
        for f in folder:
            # Tentatively add the current folder to the result list
            res.append(f)
            # Check each character in the folder path
            for i in range(len(f)):
                # If a slash is found and the prefix is in folder_set, it's a subfolder
                if f[i] == "/" and f[:i] in folder_set:
                    res.pop()  # Remove the folder from result list
                    break  # Stop further checking and move to the next folder
        return res  # Return the list of folders without subfolders


# Using Trie - Prefix Tree

# Define a Trie (Prefix Tree) structure to represent folder paths
class Trie:
    def __init__(self):
        # Dictionary to hold children nodes
        self.children = {}
        # Boolean flag to mark the end of a complete folder path
        self.end_of_folder = False

    def add(self, path):
        # Add each folder path into the Trie
        cur = self  # Start from the root of the Trie
        # Split the path by "/" to access each folder part individually
        for f in path.split("/"):
            if f not in cur.children:
                # Create a new node if the folder part is not in children
                cur.children[f] = Trie()
            # Move to the next node in the Trie
            cur = cur.children[f]
        # Mark the end of the folder path in the Trie
        cur.end_of_folder = True

    def prefix_search(self, path):
        # Check if a given path has any parent folders in the Trie
        cur = self  # Start from the root of the Trie
        # Split path by "/" to access each folder part
        folders = path.split("/")
        # Traverse up to the second last folder, checking for parent folders
        for i in range(len(folders) - 1):
            cur = cur.children[folders[i]]
            # If a complete folder is found, this path is a subfolder
            if cur.end_of_folder:
                return True  # Found a parent folder; path is a subfolder
        # No parent folder found, so path is not a subfolder
        return False


# Solution class to remove subfolders using the Trie structure
class Solution2:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Initialize a Trie to store all folder paths
        trie = Trie()

        # Add each folder path to the Trie
        for f in folder:
            trie.add(f)

        res = []  # List to store folder paths that are not subfolders
        for f in folder:
            # Check if the folder has a parent folder in Trie
            if not trie.prefix_search(f):
                # If no parent folder is found, add it to the result
                res.append(f)
        return res  # Return the list of non-subfolder paths


c = Solution()
folder = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
print(c.removeSubfolders(folder))

print("/a".split("/"))
