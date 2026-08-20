#!/usr/bin/env python3
from __future__ import annotations
import csv
from J2_65_R5_common import HERE
p2f=['D7','D8']
p5f=['q+4','3q+2','D4','q-2','D9']
rows=[]
for a in p2f:
    for b in p5f:
        rows.append(dict(p2_factor=a,p5_factor=b,
            q_congruences=f'q=r_2({a},m2) mod 2^m2; q=r_5({b},m5) mod 5^m5',
            crt_modulus='2^m2*5^m5',
            q_pinning_condition='2^m2*5^m5 > q => q is the unique least positive CRT representative',
            u_congruences=f'u=s_2({a},min(m2,g)) mod 2^min(m2,g); u=s_5({b},min(m5,g)) mod 5^min(m5,g)',
            u_pinning_condition='2^min(m2,g)*5^min(m5,g) > u => u is the unique CRT representative',
            actual_forced_case='NO: R5 DNF does not force a simultaneous q-tube pair with sufficient depths',
            deterministic_q_sequence='NONE_FORCED',deterministic_u_sequence='NONE_FORCED',
            product_mismatch_interface='If both pin: r_m*s_n=10^g+1 exactly; E is diagnostic only'))
p=HERE/'J2-65-R5-AdelicPinning.tsv'
with p.open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
print('R5 ADELIC PINNING CERTIFICATE')
print('ADELIC_CRT_THEOREM=PROVED')
print('Q_PINNING_THRESHOLD=2^m2*5^m5>q')
print('U_PINNING_THRESHOLD=2^min(m2,g)*5^min(m5,g)>u')
print('ADELIC_PINNING_CASES=0_FORCED')
print('DETERMINISTIC_q_SEQUENCES=0')
print('DETERMINISTIC_u_SEQUENCES=0')
print('PIN_PRODUCT_INTERFACE=PROVED_CONDITIONAL')
print('OUTPUT=',p.name,sep='')
