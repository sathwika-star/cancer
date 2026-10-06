"""Educational cancer-variant analysis with BioPython.

This program is a learning project only. It is not a clinical decision-support
tool and must not be used to diagnose cancer or select treatment.
"""

import argparse
import csv
import json
from pathlib import Path

from Bio.Seq import Seq


BIOMARKER_DATABASE = {
    ("EGFR", "L858R"): {
        "evidence": "Illustrative actionable biomarker example",
        "research_note": "Review approved knowledge bases and molecular-tumour-board guidance.",
    },
    ("BRAF", "V600E"): {
        "evidence": "Illustrative actionable biomarker example",
        "research_note": "Review tumour type, co-mutations, and approved knowledge bases.",
    },
    ("KRAS", "G12D"): {
        "evidence": "Illustrative biomarker example; interpretation depends on tumour context",
        "research_note": "Do not infer treatment eligibility from this demonstration database.",
    },
}


def translate_codon(codon: str) -> str:
    """Translate a three-letter DNA codon to its one-letter amino-acid code."""
    codon = codon.upper().replace("U", "T")
    if len(codon) != 3 or any(base not in "ACGT" for base in codon):
        raise ValueError(f"Invalid DNA codon: {codon!r}")
    return str(Seq(codon).translate())


def protein_change(row: dict) -> str:
    """Create a compact protein-change label such as L858R."""
    reference = translate_codon(row["ref_codon"])
    alternate = translate_codon(row["alt_codon"])
    position = row["protein_position"].strip()
    if not position.isdigit() or int(position) < 1:
        raise ValueError("protein_position must be a positive whole number")
    return f"{reference}{position}{alternate}"


def analyse_variants(input_path: Path) -> list[dict]:
    """Read a CSV file and create an educational research summary for each row."""
    results = []
    with input_path.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        required = {"patient_id", "gene", "ref_codon", "alt_codon", "protein_position"}
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            missing = required - set(reader.fieldnames or [])
            raise ValueError(f"Input CSV is missing columns: {', '.join(sorted(missing))}")

        for row in reader:
            gene = row["gene"].strip().upper()
            change = protein_change(row)
            biomarker = BIOMARKER_DATABASE.get((gene, change))
            results.append(
                {
                    "patient_id": row["patient_id"].strip(),
                    "gene": gene,
                    "protein_change": change,
                    "reference_codon": row["ref_codon"].upper(),
                    "alternate_codon": row["alt_codon"].upper(),
                    "biomarker_match": bool(biomarker),
                    "research_interpretation": biomarker or {
                        "evidence": "No match in this small demonstration database",
                        "research_note": "Search a validated, current clinical knowledge base for expert review.",
                    },
                }
            )
    return results


def main():
    parser = argparse.ArgumentParser(description="Educational BioPython cancer-variant analyser")
    parser.add_argument("input", type=Path, help="CSV file containing tumour variants")
    parser.add_argument("-o", "--output", type=Path, default=Path("patient_report.json"))
    args = parser.parse_args()

    report = {
        "disclaimer": "Educational research output only. Not for diagnosis or treatment decisions.",
        "variants": analyse_variants(args.input),
    }
    args.output.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Report created: {args.output}")
    print("Reminder: this educational output is not clinical advice.")


if __name__ == "__main__":
    main()
