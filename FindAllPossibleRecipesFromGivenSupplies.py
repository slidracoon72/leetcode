from typing import List


# DFS - Graph Traversal
# Similar to CourseSchedule.py
# Neetcode: https://www.youtube.com/watch?v=AQrsAc3EcyQ&ab_channel=NeetCodeIO
# Time: O(V+E), Space: O(V+E)
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Initialize a dictionary to track whether an ingredient/recipe can be created
        # Key: ingredient/recipe name (str), Value: True if it can be created, False otherwise
        # Start with supplies, which are always available (can be "cooked" by default)
        can_cook = {s: True for s in supplies}

        # Create a dictionary to map each recipe to its index in the recipes list
        # Key: recipe name (str), Value: index in recipes list (int)
        # This allows quick lookup of a recipe's ingredients in the ingredients list
        recipe_index = {r: i for i, r in enumerate(recipes)}

        # Define a DFS function to determine if a recipe can be created
        # Parameter: r (str) - the recipe or ingredient to check
        # Returns: True if the recipe can be created, False otherwise
        def dfs(r):
            # If we've already determined whether this recipe/ingredient can be created, return the result
            if r in can_cook:
                return can_cook[r]

            # If r is not a recipe (not in recipe_index), it must be an ingredient
            # Since it's not in supplies (checked above), it cannot be created
            if r not in recipe_index:
                return False

            # Mark the recipe as being processed (False) to detect cycles
            # If we encounter this recipe again during DFS, it means there's a cycle, and it cannot be created
            can_cook[r] = False

            # Get the ingredients for the current recipe using its index
            # Iterate through each ingredient (nei) required for the recipe
            for nei in ingredients[recipe_index[r]]:
                # Recursively check if the ingredient can be created
                # If any ingredient cannot be created, the recipe cannot be created
                if not dfs(nei):
                    return False

            # If all ingredients can be created, mark the recipe as creatable (True)
            can_cook[r] = True
            return can_cook[r]

        # Use a list comprehension to filter recipes that can be created
        # Call dfs() on each recipe; if dfs returns True, include the recipe in the result
        return [r for r in recipes if dfs(r)]


c = Solution()
recipes = ["bread", "sandwich"]
ingredients = [["yeast", "flour"], ["bread", "meat"]]
supplies = ["yeast", "flour", "meat"]
print(c.findAllRecipes(recipes, ingredients, supplies))
