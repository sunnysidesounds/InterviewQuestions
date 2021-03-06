# Google Question
# Given an array = [2,5,1,2,3,5,1,2,4]:
# It should return 2

# Given an array = [2,1,1,2,3,5,1,2,4]:
# It should return 1

# Given an array = [2,3,4,5]:
# It should return undefined


#function firstRecurringCharacter(input) 
#}

# Bonus... What if we had this:
# [2,5,5,2,3,5,1,2,4]
# return 5 because the pairs are before 2,2

def first_recurring_character(arr):
  character_map = {}
# create a dict / map checking if it's already in the map. If it is, it's the first recurring
  for item in arr: 
    if item in character_map:
      return item     
    else:
      character_map[item] = 1    
      
  return  None
