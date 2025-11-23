## Pyinstaller tests

### Failing 

Infinite with infinite respawns

```
uv run pyinstaller --clean --name mytest ./from_docs.py
```

### Working

Works in native mode without respawns

```
uv run pyinstaller --clean --name mytest ./from_docs_native.py
```