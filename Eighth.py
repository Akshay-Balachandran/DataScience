from typing import List,Tuple, Dict, Union

#List of integers
numbers : List[int] = [1,2,3,4,5]

#Tuple of integer
person: Tuple[str, int] = ("Alice",30)

#Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

#Union type for a variable that can be either int or str
identifier: Union[int, str] = "ID123"
identifier = 12345  # Now it's an int and also valid

