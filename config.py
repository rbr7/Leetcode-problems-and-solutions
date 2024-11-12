import os

DIFFICULTY_MAP = {"E": "easy", "M": "medium", "H": "hard"}

PY_FILE_DIR = "./src"

EXPLANATIONS_DIR = os.path.join(".", "docs", "explanations")

TEMPLATE = """---
layout: default
parent: {{ difficulty }} Problems
grand_parent: Explanations
has_toc: false
nav_order: {{ number }}
---

# <!-- omit in toc --> Problem {{ number }} - {{ name }}

> Leetcode Link: [{{ name }}]({{ link }}).

- [Statement](#statement)
- [Examples](#examples)
{%- if n_solutions == 1 %}
- [Solution](#solution)
  - [Concept](#concept)
  - [Example](#example)
  - [Time complexity](#time-complexity)
{%- else %}
- [Solution 1](#solution-1)
  - [Concept](#concept)
  - [Example](#example)
  - [Time complexity](#time-complexity)
{%- for i in (2..n_solutions) %}
- [Solution {{ i }}](#solution-{{ i }})
  - [Concept](#concept-{{ i | minus: 1 }})
  - [Example](#example-{{ i | minus: 1 }})
  - [Time complexity](#time-complexity-{{ i | minus: 1 }})
{%- endfor %}
{% endif %}
## Statement

## Examples
{% if n_solutions == 1 %}
## Solution

### Concept

### Example

**Input**

**Procedure**

### Time complexity
{% else %}{% for i in (1..n_solutions) %}
## Solution {{ i }}

### Concept

### Example

**Input**

**Procedure**

### Time complexity
{% endfor %}{% endif %}"""
