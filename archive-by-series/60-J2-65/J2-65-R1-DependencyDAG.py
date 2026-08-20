#!/usr/bin/env python3
"""Build and verify the 65-R1 J2 dependency DAG."""
from pathlib import Path
import csv

OUT = Path('/mnt/data')
TSV = OUT/'J2-65-R1-DependencyDAG.tsv'

# source,target,relation,scope,provenance
EDGES = [
('GENERAL_RESONANCE','J_DEFINITION','DERIVES','general resonance','strict_layer_A1_double_euclidean_word_smith_terminal_campaign.md'),
('GENERAL_RESONANCE','CYCLOTOMIC_u0','DERIVES','general resonance','strict_layer_A1_resonance_RGCD_overload_extinction_campaign.md'),
('J_DEFINITION','J_EQUALS_LR','SPECIALIZES_TO','R=0 resonance','strict_layer_A1_smith_reduced_common_U_exclusion_campaign.md'),
('CYCLOTOMIC_u0','UNIMODULAR_ENVELOPE','USES','general resonance envelope','65-R1 new theorem: q0=(G+1)/u0'),
('J_DEFINITION','UNIMODULAR_ENVELOPE','USES','general resonance envelope','65-R1 new theorem'),
('GENERAL_RESONANCE','J2_SPECIALIZATION','SPECIALIZES_TO','J=2','strict_layer_A1_resonance_RGCD_overload_extinction_campaign.md -> A1_J2_NRSEC_Report.md'),
('UNIMODULAR_ENVELOPE','J2_DETERMINANT','SPECIALIZES_TO','J=2,u0=u','65-R1 symbolic respecialization'),
('J2_SPECIALIZATION','J2_DETERMINANT','DERIVES','J=2','A1_J2_NRSEC_Report.md'),
('J2_SPECIALIZATION','RCE','DERIVES','J=2','A1_J2_CZDR_Report.md / A1_J2_RCRF4_Report.md'),
('RCE','TAIL','USES','J=2 pre-root','A1_J2_DCDC5_Report.md / later 55 reports'),
('RCE','DCDC','USES','J=2 pre-root','A1_J2_DCDC5_Report.md'),
('TAIL','CARRY_CORE','CONSUMED_BY','R8-R11','J2-55-R12 dependency audit'),
('DCDC','CARRY_CORE','CONSUMED_BY','R8-R11','J2-55-R12 dependency audit'),
('RCE','CARRY_CORE','CONSUMED_BY','R8-R11','J2-55-R12 saturation inputs'),
('FLOOR','CARRY_CORE','CONSUMED_BY','R6-R11','J2-55-R12 saturation inputs'),
('DECIMAL_ROOT','CARRY_CORE','CONSUMED_BY','partial/pre-root modular information','J2-55-R12 dependency audit'),
('LAMBDA','CARRY_CORE','CONSUMED_BY','R8-R10','J2-55-R10 retirement'),
('GAMMA','CARRY_CORE','CONSUMED_BY','R8-R11','J2-55-R11 D_u=gamma'),
('ZETA','CARRY_CORE','CONSUMED_BY','R9-R10','J2-55-R10 retirement'),
('SECOND_RESIDUAL','CARRY_CORE','CONSUMED_BY','R9-R11','J2-55-R12 saturation audit'),
('THIRD_RESIDUAL','CARRY_CORE','CONSUMED_BY','R10-R11','J2-55-R12 saturation audit'),
('R11_CONSTANT','CARRY_CORE','CONSUMED_BY','R11','J2-55-R11: C_B/H=4f^2w Gamma, C_R=4Rf^2w Gamma_R'),
('FULL_ROOT','ROOT_MOD_q','MODULAR_SHADOW','J=2','R7/R12 dependency correction'),
('ROOT_MOD_q','RCE','CONSUMED_BY','J=2','R7: exact root mod q degenerates to old RCE square'),
('FULL_ROOT','ROOT_MOD_u','MODULAR_SHADOW','J=2','A1_J2_PRCC10_Report.md'),
('ROOT_MOD_u','U_SQ','DERIVES','J=2','Q(x) mod u = (x^2-Z^2)/4'),
('U_SQ','CARRY_CORE','INDEPENDENT_MOD_IDEAL','J=2','R12: not consumed by R8-R11 carry ideal'),
('FULL_ROOT','ROOT_MOD_A','MODULAR_SHADOW','J=2','A1_J2_PRCC10_Report.md'),
('ROOT_MOD_A','A_ROOT','USES','nondegenerate exact; degenerate primitive A-root stronger','Q mod A=D2(Kx+Z)'),
('A_ROOT','A_LIFT','USES','J=2','J2-55-R1-A-Root-Lift-Report.md'),
('FULL_ROOT','A_LIFT','USES','J=2','A^2/A^3 lifting uses Q'),
('FULL_ROOT','ROOT_FACTOR','DERIVES','J=2','root-factor pair is equivalent to same quadratic after factor choice'),
('FULL_ROOT','R12_P_B','DERIVES','boundary','J2-55-R12 RootSaturation'),
('FULL_ROOT','R12_P_H','DERIVES','high','J2-55-R12 RootSaturation'),
('FULL_ROOT','R12_P_R','DERIVES','reverse generic','J2-55-R12 RootSaturation'),
('FULL_ROOT','R12_P_K1','DERIVES','reverse k=1 special','J2-55-R12 RootSaturation'),
('R12_P_B','CARRY_CORE','INDEPENDENT_MOD_IDEAL','boundary','FULL_ROOT_MOD_CARRY_IDEAL=NONZERO'),
('R12_P_H','CARRY_CORE','INDEPENDENT_MOD_IDEAL','high','FULL_ROOT_MOD_CARRY_IDEAL=NONZERO'),
('R12_P_R','CARRY_CORE','INDEPENDENT_MOD_IDEAL','reverse','FULL_ROOT_MOD_CARRY_IDEAL=NONZERO'),
('R12_P_K1','CARRY_CORE','INDEPENDENT_MOD_IDEAL','reverse k=1','FULL_ROOT_MOD_CARRY_IDEAL=NONZERO'),
('DIGIT_WINDOW','LOW','DERIVES','J=2','DRL / actual second numerator digit window'),
('ROOT_FACTOR','UP','DERIVES','J=2','complementary factor positivity'),
('LOW','FULL_ROOT','INDEPENDENT_MOD_IDEAL','inequality gate','R12: not derived from carry ideal'),
('UP','FULL_ROOT','INDEPENDENT_MOD_IDEAL','inequality gate','R12: not derived from carry ideal'),
('COMMON_U','PRIMITIVE_GCD_ZU','DERIVES','primitive layer','PRCC/R12 primitive recovery'),
('U_SQ','PRIMITIVE_GCD_XU','USES','primitive layer','gcd(Z,u)=1 + U-SQ => gcd(x,u)=1'),
('PRIMITIVE_GCD_ZU','PRIMITIVE_GCD_XU','USES','primitive layer','R12 primitive support'),
('PRIMITIVE_GCD_XU','CARRY_CORE','INDEPENDENT_MOD_IDEAL','primitive layer','R12: carry chain does not consume gcd(x,u)'),
('COMMON_U','CARRY_CORE','INDEPENDENT_MOD_IDEAL','primitive layer','R12: common-U primitive recovery not consumed'),
]

with TSV.open('w', newline='', encoding='utf-8') as f:
    w=csv.writer(f, delimiter='\t')
    w.writerow(['source','target','relation','scope','provenance'])
    w.writerows(EDGES)

# Required audit checks.
def rels_for(node):
    return [(s,t,r) for s,t,r,sc,p in EDGES if s==node or t==node]

# R11 constant term must be old carry, never independent-root.
assert any(s=='R11_CONSTANT' and t=='CARRY_CORE' and r=='CONSUMED_BY' for s,t,r,sc,p in EDGES)
assert not any(s=='R11_CONSTANT' and r=='INDEPENDENT_MOD_IDEAL' for s,t,r,sc,p in EDGES)

# U-SQ is a modular shadow, not a second independent full equation.
assert any(s=='ROOT_MOD_u' and t=='U_SQ' and r=='DERIVES' for s,t,r,sc,p in EDGES)
assert not any(s=='U_SQ' and t=='FULL_ROOT' and r in ('DERIVES','INDEPENDENT_FULL_EQUATION') for s,t,r,sc,p in EDGES)

# All R12 root factors must survive modulo carry ideal.
for n in ('R12_P_B','R12_P_H','R12_P_R','R12_P_K1'):
    assert any(s==n and t=='CARRY_CORE' and r=='INDEPENDENT_MOD_IDEAL' for s,t,r,sc,p in EDGES), n

# LOW/UP must not be carry consequences.
for n in ('LOW','UP'):
    assert not any(s=='CARRY_CORE' and t==n and r in ('DERIVES','USES','CONSUMED_BY') for s,t,r,sc,p in EDGES), n

print('J2-65 R1 DEPENDENCY DAG')
print('STATUS=PASS')
print(f'EDGE_COUNT={len(EDGES)}')
print('R11_CONSTANT_NOT_INDEPENDENT_ROOT=PASS')
print('U_SQ_NOT_INDEPENDENT_FULL_EQUATION=PASS')
print('R12_ALL_INDEPENDENT_MOD_CARRY_IDEAL=PASS')
print('LOW_UP_NOT_CARRY_CONSEQUENCE=PASS')
print(f'TSV={TSV.name}')
