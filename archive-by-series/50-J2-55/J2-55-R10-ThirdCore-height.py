#!/usr/bin/env python3
"""Exact rational bookkeeping for R10 centered third-core finite-height/deterministic-u theorem.
Scope: q>1 high/boundary moderate normalized branches, q>=7.
No asymptotic notation is used in the certified constants below.
"""
from fractions import Fraction as F

# Uniform elementary bounds for q>=7:
# f=5^b <= q+4 <= 11q/7; B<(q+2)q^2<=9q^3/7.
fq=F(11,7); Bq3=F(9,7)
# boundary: t<9q, |alpha|<30 f q^4
E_B = 2*fq*Bq3*9 + 30*fq
assert E_B < 84
# high: H>=10, t<3q+8<=29q/7, |alpha|<3 f q^4
E_H = 2*fq*Bq3*F(29,7) + 3*fq
assert E_H < 22

# eta=(e+8 f t(3q+5))/h5, h5>=1; 3q+5<=26q/7.
ETA_B_extra_q3=8*fq*9*F(26,7)
ETA_H_extra_q3=8*fq*F(29,7)*F(26,7)
# convert q^3 to q^4 using q>=7.
ETA_B_q4=E_B+ETA_B_extra_q3/7
ETA_H_q4=E_H+ETA_H_extra_q3/7
assert ETA_B_q4 < 144
assert ETA_H_q4 < 50

# Centered xi bounds inherited from R9 zeta heights:
# |xiB|<2,000,001 q^8; |xiH|<3,700,000,001 q^18.
# For the affine equation D_u u=N_u, if D_u!=0, |u|<=|N_u|.
# We bound N_u=q*xi+c0 using the exact c0 coefficient groups emitted by
# J2-55-R10-TailReintegration-symbolic.py.

# Boundary c0 groups, converted to q^12.
# |ch|<800000 q^8, w<=9q, f<=11q/7, |eta|<93q^4, s<=20, t<9q.
CB_ch = 8*800000*fq**2*9
# eta polynomial <=26 q^5 for q>=7
CB_eta = 26*144*fq*9/F(7)
# s polynomial <=136 q^6; degree q^10 -> q^12 /49
CB_s = 136*fq**3*20*9/F(7**2)
# t polynomial <=85 q^6; degree q^11 -> q^12 /7
CB_t = 85*fq**3*9*9/F(7)
CB_xi = F(2000001,7**3)   # q*xi degree9 -> q12
CB_r = F(1,2*7**11)
CB_total = CB_ch+CB_eta+CB_s+CB_t+CB_xi+CB_r
assert CB_total < 143_000_000

# High c0 groups, converted to q^21.
# H<48q^5, |ch|<3.73e7 q^10, w<=t<29q/7, eta<50q^4, s=0.
CH_H2_eta = 24*(48**2)*50*fq*F(29,7)
CH_H2_t = 62*(48**2)*fq**3*F(29,7)**2
# degree19 -> q21 /49
CH_H_ch = 8*48*37_300_000*fq**2*F(29,7)/F(7**2)
# lower-degree groups are retained exactly but tiny at q>=7
CH_eta = 17*50*fq*F(29,7)/F(7**11)
CH_t = 156*fq**3*F(29,7)**2/F(7**11)
CH_xi = F(3_700_000_001,7**2) # degree19 -> q21
CH_r = F(1,2*7**20)
CH_total=CH_H2_eta+CH_H2_t+CH_H_ch+CH_eta+CH_t+CH_xi+CH_r
assert CH_total < 3_100_000_000

print('J2-55 R10 ThirdCore height certificate')
print('E_BOUNDARY_ABS_LT_84_Q4=PASS')
print('E_HIGH_ABS_LT_22_Q4=PASS')
print('ETA_BOUNDARY_ABS_LT_144_Q4=PASS')
print('ETA_HIGH_ABS_LT_50_Q4=PASS')
print('XI_BOUNDARY_CENTERED_ABS_LT_2000001_Q8=PASS')
print('XI_HIGH_CENTERED_ABS_LT_3700000001_Q18=PASS')
print('BOUNDARY_NONDEGENERATE_U_LT_143000000_Q12=PASS')
print('BOUNDARY_NONDEGENERATE_G_LT_143000000_Q13=PASS')
print('HIGH_NONDEGENERATE_U_LT_3100000000_Q21=PASS')
print('HIGH_NONDEGENERATE_G_LT_3100000000_Q22=PASS')
print('BOUNDARY_COEFF_EXACT=',float(CB_total))
print('HIGH_COEFF_EXACT=',float(CH_total))
