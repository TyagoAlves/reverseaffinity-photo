# reverseaffinity-photo

Photo editor — desmembrado do monorepo `reverseaffinity`.

## Estrutura
```
src/
├── python_ui/        # Interface Python (PyQt5)
│   ├── editor/       # Core editor engine
│   ├── reverseaffinity/  # App-specific modules
│   ├── tests/        # Test suite (pytest)
│   └── main.py       # Entry point
└── cpp_backend/      # C++ engine (performance-critical)
    ├── CMakeLists.txt
    ├── include/
    ├── src/
    └── test/
assets/               # Icons, resources
docs/                 # Documentation
```

## Executar (UI Python)
```bash
pip install -r src/python_ui/requirements.txt
python src/python_ui/main.py
```

## Compilar (C++ Backend)
```bash
cd src/cpp_backend
bash build.sh
```

## Testes
```bash
cd src/python_ui
QT_QPA_PLATFORM=offscreen python -m pytest tests/ -q
```

## Features
- Camadas, blend modes, masks
- Pinceis, gradientes, ferramentas de seleção
- Filtros e ajustes (Brightness/Contrast, HSL, Levels, Curves)
- Suporte a PSD, PNG, JPEG, TIFF, WebP
- 7 idiomas (EN, PT-BR, ES, FR, DE, IT, JP)
