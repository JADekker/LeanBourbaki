"""
This file is copied from the mathlib3 file of the same name.
It reads in the three yaml files, and translates them to simpler json files that are easier to
process in Lean.
"""
from typing import Dict, Optional, Union, Tuple, List
import yaml
import json
import sys

TieredDict = Dict[str, Union[Optional[str], 'TieredDict']]

def tiered_extract(db: TieredDict) -> List[Tuple[List[str], str]]:
  """From a nested dictionary, return a list of (key_path, values)
  of the deepest level."""
  out = []
  for name, entry in db.items():
    if isinstance(entry, dict):
      for subname, value in tiered_extract(entry):
        out.append(([name] + subname, value))
    else:
      if entry and '/' not in entry:
        out.append(([name], entry))
  return out

def flatten_names(data: List[Tuple[List[str], str]]) -> List[Tuple[str, str]]:
  return [(' :: '.join(id), v) for id, v in data]

def print_list(fn: str, pairs: List[Tuple[str, str]]) -> None:
  with open(fn, 'w') as out:
    for (id, val) in pairs:
      out.write(f'{id}\n{val.strip()}\n\n')

chap1_yaml = sys.argv[1]

with open(chap1_yaml, 'r') as hy:
  chap1 = yaml.safe_load(hy)

chap1_decls:List[Tuple[str, str]] = []

for index, entry in chap1.items():
  title = entry['title']
  if 'decl' in entry:
    chap1_decls.append((f'{index} {title}', entry['decl']))
  elif 'decls' in entry:
    chap1_decls = chap1_decls + [(f'{index} {title}', d) for d in entry['decls']]

with open('chap1.json', 'w', encoding='utf8') as f:
  json.dump(chap1_decls, f)
