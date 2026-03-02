from typing import List, Dict

def make_most_common_keys(d: Dict[int, int]) -> List[int]:
   return sorted(d, key=lambda x: d[x], reverse=True)
   

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)