import os

# Define the directory structure
structure = {
    "Eventious": {
        "backend": {
            "manage.py": "",
            "eventious": {
                "__init__.py": "",
                "settings.py": "",
                "urls.py": "",
                "wsgi.py": "",
                "asgi.py": ""
            },
            "events": {
                "migrations": {},
                "__init__.py": "",
                "admin.py": "",
                "apps.py": "",
                "models.py": "",
                "tests.py": "",
                "views.py": ""
            }
        },
        "frontend": {
            "node_modules": {},
            "public": {},
            "src": {
                "components": {},
                "App.js": "",
                "index.js": ""
            },
            "package.json": "",
            "package-lock.json": ""
        },
        ".gitignore": "",
        "README.md": ""
    }
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, 'w') as f:
                f.write(content)

# Create the directory structure
create_structure(".", structure)
