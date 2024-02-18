# How misclassifications were created

The misclassifications are created by fuzzing the `output.png` file and filtering for results that are code or text.

## Steps to generate results

### 1. Generate fuzzed files
```bash
./generate_all.sh
```

### 2. Execute magika on fuzzed files
```bash
./generate_magika_output.sh
```

### 3. Find misclassifications
```bash
./find_misclassifications.sh
```

### 4. Find the text and code misclassifications
```bash
python interpret_data.py
```

## Pre-installed software
- zzuf 0.15