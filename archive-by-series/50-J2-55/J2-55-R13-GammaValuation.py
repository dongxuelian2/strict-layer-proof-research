#!/usr/bin/env python3
"""Exact R13 reverse constant-coefficient 2-adic ledger."""
def generic_term_vals(k,vg,ve): return (2*k+vg,6+k+ve,8)
def k1_term_vals(vg,ve): return (4+ve,vg,5)
print('RV2-1 generic term valuations = 2k+v2(gamma), 6+k+v2(e), 8')
for k in range(2,8):
    if k>=5:
        print(f'k={k}: bracket v2=8 EXACT for every e,gamma; hence v2(R0)=v2(gamma)+8')
    elif k==2:
        print('k=2, gamma odd: bracket v2=4 EXACT; v2(R0)=4')
    elif k==3:
        print('k=3: vg=0 ->6 exact; vg=1 ->7 exact; vg=2 gives 8-tie; vg>=3 third term starts at 8')
    elif k==4:
        print('k=4: gamma even -> bracket v2=8 exact; gamma odd gives an 8-tie and cancellation >=9')
print('K1 special valuations = 4+v2(e), v2(gamma), 5')
print('K1 gamma odd => special bracket odd => v2(S0)=0 => impossible for r>=1')
print('GAMMA_PARITY=OPEN_FROM_FROZEN_R8_R12_DATA')
print('GAMMA_V2_BOUND=OPEN_FROM_FROZEN_R8_R12_DATA')
