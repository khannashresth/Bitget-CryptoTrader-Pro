import os

def create_init_file(path):
    with open(path, 'w', encoding='utf-8') as f:
        f.write('"""\nModule initialization.\n"""\n')

# Create __init__.py files
init_paths = [
    'src/__init__.py',
    'src/trading/__init__.py',
    'src/data/__init__.py',
    'src/models/__init__.py',
    'src/risk/__init__.py'
]

for path in init_paths:
    create_init_file(path)
    print(f"Created {path}") 