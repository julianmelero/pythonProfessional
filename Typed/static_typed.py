from typing import Dict, List,Tuple
# Mypy will advertice

num1: int
num2: int
sum: int

def sum(num1: int, num2: int) -> int:
    return num1 + num2

num1 = input("Number 1: ")
num2 = input("Number 2: ")
sum = sum(num1, num2)
print(sum)



positives: List[int] = [1,2,3,4,5]

countries: List[Dict[str, str]] = [
	{
		"name" : "Argentina",
		"people" : "45000",
	},
	{
		"name" : "México",
		"people" : "9000000",
	},
	{
		"name" : "Colombia",
		"people" : "99999999999",
	}
]

numbers: Tuple [int, float, str] = (1, 2.3, "4")