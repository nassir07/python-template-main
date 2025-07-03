# python-template

**A template for Python projects with built-in support for:**

* Code quality (linting, formatting, typing)
* CI/CD with GitLab CI and Docker
* Auto-generated documentation with Sphinx
* Dependency and environment management using Pipenv

---

## 🚀 Installation

### Prerequisites

* [Git](https://git-scm.com/)
* [Python](https://www.python.org/) (with pipenv)

### Initiation

1. **Use the template for a new repo:**

   ```bash
   git clone git@git.technica-engineering.net:data/templates/python-template.git
   ```

   * Remove the `.git` folder
   * Run `./scripts/change-name.sh` (or `change-name.bat` on Windows) to replace `python-template` with the new repo name
   * Run `./scripts/change-name.sh` again to replace `python_template` with the new main package name
   * Rename the repo folder
   * Initiate a new git repo

     ```bash
     git init .
     git add .
     git commit -m "First commit"
     ```

2. **Install Development Dependencies:**

   ```bash
   pipenv install --dev
   ```

3. **Configure Pre-Commit Hooks:**

   ```bash
   pipenv run pre-commit install
   ```

---

## 📁 Structure

```
│   .env                                   
│   .gitignore  
│   .gitlab-ci.yml                          
│   .pre-commit-config.yaml                 
│   CHANGELOG.md  
│   log.conf                                
│   Pipfile                                 
│   Pipfile.lock                            
│   README.md  
│   tox.ini                                 
│
├───docs                                   
│   │   conf.py  
│   │   index.rst  
│   │   make.bat  
│   │   Makefile  
│   │   requirements.in  
│   │   requirements.txt  
│   └───_templates  
│           custom-class-template.rst  
│           custom-module-template.rst  
│
├───logs                                   
├───notebooks                              
│       example.ipynb  
├───scripts                                
│       change-name.bat  
│       change-name.sh  
├───template_python                        
│   │   config.py  
│   │   main.py  
│   │   __init__.py  
│   ├───application  
│   │   │   my_module.py  
│   │   └───  __init__.py  
│   ├───data_access  
│   │   └───__init__.py  
│   └───infra  
│       │   jiraconnection.py  
│       │   mailing.py  
│       └───   __init__.py  
└───tests  
    │   test_my_module.py  
    └───__init__.py  
```

---

## 🛠️ Tools

### 1. Virtual environment (pipenv)

[Pipenv](https://pipenv.pypa.io/en/latest/) is used for package and virtual environment management.

### 2. Logging

This template uses the built-in Python [logging](https://docs.python.org/3/library/logging.html) module.

* **Logging configuration is defined in `log.conf`** and applied in the entry script:

```python
import logging.config
logging.config.fileConfig("../log.conf")
```

* **Each module can retrieve a logger using**:

```python
import logging
logger = logging.getLogger(__name__)
```

* This ensures consistent logging across the codebase.
* Logs are written to files under the `logs/` directory.

### 3. Documentation (Sphinx)

[Sphinx](https://www.sphinx-doc.org/en/master/) is configured to auto-generate documentation:

* Recursively extracts from all modules
* Adds paths in `docs/conf.py` to ensure modules are importable
* Templates: `custom-class-template.rst`, `custom-module-template.rst`
* To generate docs:

```bash
tox -e docs
```

### 4. Linting

Uses [flake8](https://flake8.pycqa.org/) with these plugins:

* `flake8-bugbear`: finds bugs and design issues
* `flake8-docstrings`: validates docstrings via `pydocstyle`
* `flake8-typing-imports`: ensures typing imports are guarded
* `pep8-naming`: checks naming conventions

Run via:

```bash
tox -e lint
```

Linting is integrated into both pre-commit and CI (GitLab pipeline).

### 5. Formatting

Uses [black](https://black.readthedocs.io/) and [isort](https://pycqa.github.io/isort/):

```bash
tox -e format
```

### 6. Typing

[Mypy](http://mypy-lang.org/) performs static type checks based on type hints:

```bash
tox -e typing
```

### 7. Gitlab CI/CD

Defined in `.gitlab-ci.yml`, includes:

* **Test stage**: runs linting, unit tests, and typing

```bash
tox -e lint,unitest,type
```

* **Build stage**: builds Docker image via `Dockerfile`

### 8. Global Structure

The overall structure is as follows:

* `template_python/`: main package containing all source code.

  * `application/`: business logic modules
  * `infra/`: infrastructure utilities like `jiraconnection.py`, `mailing.py`
  * `data_access/`: data access layer
  * `config.py`: handles configuration via `.env` using `python-dotenv`
* `tests/`: contains unit and other tests (expandable)
* `notebooks/`: holds Jupyter notebooks for examples and experimentation
* `scripts/`: any necessary shell/batch scripts (e.g., project renaming)
* `logs/`: for log outputs, used by the `logging` system
* `data/`: placeholder for external or intermediate data

> If you introduce new test types or folders, make sure to update `tox.ini` accordingly.

### 9. Merge Request Template

`.gitlab/default.md` includes a default GitLab MR template. More info: [https://docs.gitlab.com/user/project/description\_templates/](https://docs.gitlab.com/user/project/description_templates/)

### 10. Pre-commit Hooks

Managed by [pre-commit](https://pre-commit.com/):

* Configuration: `.pre-commit-config.yaml`
* Installed with:

```bash
pipenv run pre-commit install
```

* Hooks used:

  * `black` (black-pre-commit-mirror)
  * `isort` (mirrors-isort)
  * `flake8`

### 11. Unit Testing

Uses [pytest](https://docs.pytest.org/):

* Tests in `tests/`
* Run unit tests:

```bash
tox -e unitest
```

* Generate coverage:

```bash
tox -e coverage
```

### 12. tox

[tox](https://tox.readthedocs.io/) is used to orchestrate all environments:

Configured in `tox.ini` for:

* `unitest`: unit testing
* `coverage`: test coverage
* `type`: mypy typing
* `lint`: flake8
* `format`: black & isort
* `docs`: sphinx documentation

### 13. README Template

Use this README structure as a starting point for project documentation.

---

## 🤝 Contributing

Pull requests are welcome. Please make sure to update and test any code changes.

---

## 📄 License

Specify the project's license.
