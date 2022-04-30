class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ret = set()
        
        self.recipes, self.supplies = set(recipes), set(supplies)
        self.ingredients = {recipes[i]: ingredients[i] for i in range(len(recipes))}
        
        self.dp = {}
        
        for recipe in recipes:
            if self.canCook(recipe):
                ret.add(recipe)
        return ret
    
    
    def canCook(self, recipe):
        if recipe in self.dp:
            if self.dp[recipe] == 'cooked':
                return True
            # 'cannot be cooked' or 'cooking'
            else:
                return False
            
        # never cooked before
        self.dp[recipe] = 'cooking'
        for ingredient in self.ingredients[recipe]:
            if ingredient in self.supplies:
                continue
            if ingredient in self.recipes:
                if self.canCook(ingredient):
                    continue
                else:
                    self.dp[recipe] = 'cannot be cooked'
                    return False
            else:
                self.dp[recipe] = 'cannot be cooked'
                return False
        self.dp[recipe] = 'cooked'
        return True
        
