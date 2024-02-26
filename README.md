This projects seeks to link the results in N. Bourbaki, Topologie Générale to the results in the Mathlib library for Lean4. 

# Background
This project is proof-of-concept for a larger project, in which a selection of textbooks will be linked to results in Mathlib, to facilitate the process of proof formalization, by making important results more findable and by showing users how concepts that are familiar to them have been implemented in Mathlib.

# Details
In particular, each definition and result in the book is described by a YAML file, which contains:
- Its number in the book
- Its name in the book and common alternative names
- The name of the corresponding Lean declaration (or a result that contains the result as a special case)
- Any relevant comments, e.g. on implementation details

Where possible, the Lean declaration links to a declaration in Mathlib. If the result is currently not in Mathlib, a file ChapterXMissing.lean contains the various Lean declarations, with indications whether they should/should not be upstreamed to Mathlib. 

# The source
N. Bourbaki, Topologie Générale, Chapters 1-4. 