from setuptools import find_packages, setup

exclude_dirs = ["exmples", "doc", "scripts"]

PACKAGES = find_packages(exclude=exclude_dirs)

setup(
    name="pytorch_integrated_cell",
    version="0.1",
    packages=PACKAGES,
    entry_points={
        "console_scripts": ["ic_train_model=integrated_cell.bin.train_model:main"]
    },
    install_requires=[
        "torch==1.2.0",
        "torchvision==0.2.1",
        "matplotlib==2.2.2",
        "numpy>=1.15.0",
        "pandas>=0.23.4",
        "pip",
        "pillow==5.2.0",
        "scikit-image==0.15.0",
        "scipy==1.1.0",
        "tqdm>=4.28.1",
        "natsort==5.3.3",
        "ipykernel",
        "aicsimageio==3.0.7",
        "msgpack<0.6.0,>=0.5.6",
        "imageio==2.6.0",
        "quilt3==3.1.1",
        "seaborn",
        "brokenaxes",
        "lkaccess",
        "aicsfeature==0.2.1",
    ],
)
