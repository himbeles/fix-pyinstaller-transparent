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

Works in native and normal mode without respawns, by introducing `freeze_support`

```
uv run pyinstaller --clean --name mytest ./from_docs_freeze.py
```