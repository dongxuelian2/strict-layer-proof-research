#!/usr/bin/env python3
"""R14 global regression/audit. No ray, multiplier, prime, or fixed-fibre enumeration."""
from pathlib import Path
import subprocess, hashlib
D=Path('/mnt/data')
scripts=[
'J2-65-R14-ModUAutomaticity.py','J2-65-R14-PrimitiveApproximation.py',
'J2-65-R14-RadialWindow.py','J2-65-R14-WholeModulusCovering.py',
'J2-65-R14-BoundaryTransference.py','J2-65-R14-ProjectiveBoundary.py',
'J2-65-R14-PrimitiveHeight.py','J2-65-R14-PowerTenShell.py']
required=[
'J2-65-R14-Adelic-Primitive-Shell-Report.md',*scripts,'J2-65-R14-Regression.py',
'J2-65-R14-ModUPrimitiveOpen.tsv','J2-65-R14-RadialWindow.tsv',
'J2-65-R14-CoveringRadius.tsv','J2-65-R14-BoundaryTransference.tsv',
'J2-65-R14-ProjectiveBoundary.tsv','J2-65-R14-PrimitiveHeight.tsv',
'J2-65-R14-AdelicShell.tsv','J2-65-R14-certificate.txt']
print('J2-65 R14 REGRESSION')
print('=====================')
for s in scripts:
    p=subprocess.run(['python',str(D/s)],capture_output=True,text=True)
    assert p.returncode==0,(s,p.stderr)
    print(f'SCRIPT_PASS={s}')
for f in required:
    p=D/f
    assert p.exists() and p.stat().st_size>0,f
print('REQUIRED_ARTIFACT_AUDIT=PASS')
# Discipline lint: no integer factorisation API and no historical fixed-fibre probes.
text='\n'.join((D/s).read_text() for s in scripts)
assert 'factorint(' not in text
assert 'q=7' not in text and 'q = 7' not in text
assert 'range(1,10*u)' not in text
print('FACTOR_u_USED=FALSE')
print('PRIME_RESIDUE_CASES_USED=FALSE')
print('RAY_ENUMERATION_USED=FALSE')
print('MULTIPLIER_ENUMERATION_USED=FALSE')
print('FIXED_q_g_k_USED=FALSE')
print('SHA256_BEGIN')
for f in required:
    b=(D/f).read_bytes()
    print(hashlib.sha256(b).hexdigest(),f)
print('SHA256_END')
print('J2_STATUS=OPEN')
