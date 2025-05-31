---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: myst
      format_version: '0.13'
      jupytext_version: 1.14.4
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Scan Session – 2025-05-28

**Participant ID**: S001  
**Session Time**: 10:30 – 11:15  
**Task**: Visual Memory  
**Data File**: `data/S001_2025-05-28_behavior.csv`

```python
import pandas as pd
df = pd.read_csv("data/S001_2025-05-28_behavior.csv")
df.head()
