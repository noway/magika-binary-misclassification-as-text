# Magika binary misclassification as text

## Install

```bash
git clone git@github.com:noway/magika-binary-misclassification-as-text.git
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
cd result/
magika -r *
```

## Expected

Files should be classified as data

## Observed

Files are classified as text and code