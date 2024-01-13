import os
import shutil
from setuptools import setup, find_packages

# Supprimez le dossier de distribution existant
shutil.rmtree("dist", ignore_errors=True)

# Exécutez la commande de construction du package
os.system("git add .; git commit -m 'update'; git push;")
os.system("python setup.py sdist bdist_wheel")

# Publiez le package sur PyPI en utilisant twine
os.system("twine upload dist/*")

# Nettoyez le dossier de distribution
shutil.rmtree("dist", ignore_errors=True)
shutil.rmtree("build", ignore_errors=True)

print("Le package a été publié sur PyPI avec succès.")
