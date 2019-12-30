from setuptools import setup, find_packages

install_requires = [
    "allennlp>=0.9.0",
    "wandb==0.8.15",
]

setup(
    name='allennlp_wandb',
    version='0.0.1',
    description='Utilities to use allennlp with wandb',
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_data={'allennlp_wandb': ['py.typed']},
    install_requires=install_requires,
    zip_safe=False)
