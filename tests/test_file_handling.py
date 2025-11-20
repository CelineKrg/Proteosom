from pathlib import Path
from proteomics.file_handling import read_fasta

def test_read_fasta():
    tmp_fasta_path = Path("data") / "dummy-proteins.fasta"
    protein_map = read_fasta(tmp_fasta_path)

    assert protein_map["34G7D2"] == "DWRGDSJKLSDFJ"
    assert protein_map["D49J2K"] == "KFPASOKFVVDSKFSL"