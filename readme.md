# Centroiding mzML Files

This project provides a Python script for centroiding mass spectrometry `.mzML` files using [pyOpenMS](https://pyopenms.readthedocs.io/).

## Function

- Automatically finds all `.mzML` files in the `./Original` directory.
- Centroids each file and saves the result in the `./Centroided` directory.

## Requirements

- Python 3.8+
- [pyOpenMS](https://pypi.org/project/pyopenms/)
- [tqdm](https://pypi.org/project/tqdm/)

Install dependencies with:

```
pip install pyopenms tqdm
```

## Usage

1. Place your `.mzML` files in the `Original` folder.
2. Run the script:

```
python Centroiding.py
```

3. Centroided files will be saved in the `Centroided` folder.

## License

MIT