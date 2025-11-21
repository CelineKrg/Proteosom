from proteomics.protein_digestion import (
    digest_protein_sequence,
    digest_protein_collection,
    compute_sequence_coverage,
)

def test_digest_protein_collection():
    cleave_pat = r"(?<=K)"
    dummy_proteins = {
        "prot1": "ASNKJDEDFRHDFKJDN",
        "prot2": "ASDHBFDSJHKADSFHSDKFBHF",
        "prot3": "ASNKFDKSUKJKNERKFFHKSDF"
    }
    expected_results = {
        "prot1": (["JDEDFRHDFK"], "Nr. of digested peptides: 1"),
        "prot2": (["ASDHBFDSJHK", "ADSFHSDK"], "Nr. of digested peptides: 2"),
        "prot3": ([], "Nr. of digested peptides: 0")
    }

    assert digest_protein_collection(dummy_proteins, cleave_pat) == expected_results

test_digest_protein_collection()

def test_compute_sequence_coverage():
    dummy_prot_seq = "DKDSFJWERNFWERJFOSIRGJFFNVKSVNCJFHS"
    dummy_peps = ["DKDSF", "JWERNF", "OSIRG", "JFFNV", "VNCJF"]

    coverage = compute_sequence_coverage(dummy_prot_seq, dummy_peps)
    assert coverage == 26/35 * 100

test_compute_sequence_coverage()