# Cancer Variant Analyser with BioPython

An educational Python project that demonstrates a small personalised-medicine workflow for cancer genomics. It reads simplified tumour-variant data, uses **BioPython** to translate DNA codons into amino acids, derives protein changes, and checks a small demonstration biomarker table.

> **Important:** This is a portfolio and learning project, **not clinical decision-support software**. It does not diagnose disease, establish pathogenicity, or recommend treatment. Do not use it for patient care. Real-world interpretation requires validated data sources, assay validation, current regulatory guidance, clinical context, and review by qualified professionals.

## What it demonstrates

- Parsing patient-specific variant data from CSV
- DNA-to-protein translation with `Bio.Seq.Seq`
- Protein-change notation such as `L858R`
- A simple, transparent rule-based biomarker lookup
- Producing a reproducible JSON research report
- Unit tests with Python's built-in `unittest`

## Project structure

```text
cancer-personalized-medicine-biopython/
├── cancer_variant_analyzer.py
├── sample_variants.csv
├── requirements.txt
├── tests/
│   └── test_analyzer.py
└── README.md
```

## Installation

```bash
git clone https://github.com/YOUR-USERNAME/cancer-personalized-medicine-biopython.git
cd cancer-personalized-medicine-biopython
python -m venv .venv
```

Activate the virtual environment:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate
```

Install BioPython:

```bash
pip install -r requirements.txt
```

## Run the example

```bash
python cancer_variant_analyzer.py sample_variants.csv -o patient_report.json
```

Run the tests:

```bash
python -m unittest discover -s tests
```

## Input format

The CSV requires these columns:

| Column | Description |
|---|---|
| `patient_id` | De-identified educational sample identifier |
| `gene` | Gene symbol, e.g. `EGFR` |
| `ref_codon` | Reference DNA codon |
| `alt_codon` | Alternate DNA codon |
| `protein_position` | One-based amino-acid position |

The included input is fabricated demonstration data only. Do not upload real patient data to a public repository.

## Ideas to extend it

1. Add VCF parsing with `pysam`.
2. Download annotations from a validated, versioned public source.
3. Add tumour type, genome build, transcript ID, and evidence level.
4. Package it as a command-line tool and add GitHub Actions tests.
5. Build a Streamlit interface using only synthetic data.

## Upload to GitHub

```bash
git init
git add .
git commit -m "Add BioPython cancer variant analyser"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/cancer-personalized-medicine-biopython.git
git push -u origin main
```
