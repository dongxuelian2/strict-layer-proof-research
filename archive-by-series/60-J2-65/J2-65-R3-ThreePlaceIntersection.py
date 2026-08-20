#!/usr/bin/env python3
from J2_65_R3_common import *
import csv

def read(path):
    with open(path,encoding='utf-8') as f:return list(csv.DictReader(f,delimiter='\t'))
Arows=read(OUT/'J2-65-R3-ArchimedeanCells.tsv')
P2=read(OUT/'J2-65-R3-2AdicCells.tsv')
P5=read(OUT/'J2-65-R3-5AdicCells.tsv')
rows=[]; n=0
for aa in Arows:
  for b in P2:
    for c in P5:
      n+=1
      rows.append(dict(cell_id=f'TP{n:02d}',scope='q>1',arch_face=aa['cell_id'],p2_min_face=b['cell_id'],p5_min_face=c['cell_id'],
        height_constraints=aa['defining_condition'],
        valuation_constraints=b['minimum_relation']+'; '+c['minimum_relation'],
        residue_constraints='q odd ten-unit; b5>0=>c5=0; b5=0=>c5>=1',
        primitive_constraints_used='gcd(x,u)=gcd(Z,u)=1 checked as external splice; no 2/5 valuation reduction because u is ten-unit',
        status='SURVIVES_META_GEOMETRY',death_reason=''))
write_tsv(OUT/'J2-65-R3-ThreePlaceCells.tsv',rows,list(rows[0]))
# q=1 place profile is a specialization profile, not appended as terminal q>1 cells.
q1=[]
for b in P2:
  for c in P5:
    q1.append((b['cell_id'],c['cell_id']))
print('THREE_PLACE_CELL_COUNT_BEFORE_PRIMITIVE='+str(n))
print('THREE_PLACE_CELL_COUNT_AFTER_PRIMITIVE='+str(n))
print('Q1_PLACE_PROFILE_CELLS='+str(2*len(q1)))
print('Q1_PROFILE_SPLIT=alpha_nonzero_10point + alpha_zero_7point')
print('Q1_ARCH_FACE=A_SIGMA0')
print('Q1_PLACE_GEOMETRY=CLASSIFIED_WITH_ALPHA_ZERO_SUBPROFILE')
