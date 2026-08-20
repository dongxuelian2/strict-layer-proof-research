#!/usr/bin/env python3
from __future__ import annotations
import csv, json, math
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def ceildiv(a,b): return (a+b-1)//b

def divisors(n):
    out=[]
    r=isqrt(n)
    for d in range(1,r+1):
        if n%d==0:
            out.append(d)
            if d*d!=n: out.append(n//d)
    return sorted(out)

def vp(n,p):
    if n==0: return 10**9
    e=0
    while n%p==0:
        n//=p; e+=1
    return e

def nu10(n): return min(vp(n,2),vp(n,5))

def delta_set(M,N):
    L=max(len(str(M)),len(str(N)))+3
    out=[]
    for d in range(-L,L+1):
        if d-1>=0: low = M > N*10**(d-1)
        else: low = M*10**(1-d) > N
        if d+1>=0: high = M < N*10**(d+1)
        else: high = M*10**(-d-1) < N
        if low and high: out.append(d)
    return out

def tc1_hits(pi):
    P1,P2,P3,Q=pi; T=Q-P3
    hits=[]
    for A in divisors(P3):
      for W in divisors(P2):
        common=gcd(P2//W,P3//A)
        for u0 in divisors(common):
          M=P2//W; N=P3//A
          for g1 in divisors(P1):
            num=W*g1*T
            if num%A: continue
            NE=num//A
            for n in range(1,nu10(NE)+1):
              E=NE//10**n
              for delta in delta_set(M,N):
                ssum=n+delta
                if ssum<2: continue
                for rho in range(2,ssum+1):
                  g=ssum-rho
                  for m in range(1,rho):
                    R=E-g1*P2
                    S=W*u0*P1*10**rho-Q*(W*u0*10**m+g1)
                    if R==10**g*S:
                        hits.append((A,W,u0,g1,n,delta,rho,m,g))
    return hits

def row_from_hit(pi,h):
    P1,P2,P3,Q=pi
    A,W,u0,g1,n,delta,rho,m,g=h
    k=rho-m; n2=n+delta; n3=n; m2=m; m3=n+g
    assert P2%(u0*W)==0 and P3%(u0*A)==0
    C2=P2//(u0*W); C3=P3//(u0*A)
    g0=gcd(u0*A*W,P1)
    if g1%g0: return None
    mu=g1//g0
    T=Q-P3
    lz=10**n3//gcd(10**n3,W*T)
    Lam=math.lcm(mu,lz)
    tau=lz//gcd(lz,mu)
    Zminus=max(ceildiv(10**(m2-1),A),ceildiv(10**(m3-1),W))
    Zplus=min((10**m2-1)//A,(10**m3-1)//W)
    q1=(Zminus<=Lam<=Zplus)
    Ulo=max(ceildiv(10**(n2-1),C2),ceildiv(10**(n3-1),C3))
    Uhi=min((10**n2-1)//C2,(10**n3-1)//C3)
    return dict(
        P1=P1,P2=P2,P3=P3,Q0=Q,A=A,W=W,u0=u0,g1star=g1,
        n=n,delta=delta,rho=rho,m=m,g=g,k=k,n2=n2,n3=n3,m2=m2,m3=m3,
        C2=C2,C3=C3,g0=g0,mu=mu,lambda_z=lz,Lambda=Lam,tau=tau,
        Zminus=Zminus,Zplus=Zplus,q1=int(q1),Ulo=Ulo,Uhi=Uhi,
        face2_room_kill=int(C2>=10**n2),face3_room_kill=int(C3>=10**n3),
        C2_over_10n2=f"{C2}/{10**n2}", C3_over_10n3=f"{C3}/{10**n3}",
        P2_over_u0W10n2=f"{P2}/{u0*W*10**n2}",
        P3_over_u0A10n3=f"{P3}/{u0*A*10**n3}",
        exponent_difference=(m3-m2)-(n3-n2),
        two_g_plus_k=2*g+k,
        first_failure="POSITIVE_RADIAL_BOX" if Ulo>Uhi else "ROOM_SURVIVE"
    )

SEVEN = [
    (20,120,123,173),
    (48,436,75,445),
    (120,900,691,1141),
    (140,1240,491,1341),
    (230,330,1593,1643),
    (288,2584,585,2665),
    (298,2514,1485,2935),
]

seven_rows=[]
for packet in SEVEN:
    q1rows=[]
    for h in tc1_hits(packet):
        r=row_from_hit(packet,h)
        if r and r["q1"]:
            q1rows.append(r)
    assert len(q1rows)==1, (packet,q1rows)
    seven_rows.extend(q1rows)

assert len(seven_rows)==7
assert all(r["Ulo"]==1 and r["Uhi"]==0 for r in seven_rows)
assert all(r["face3_room_kill"]==1 for r in seven_rows)
assert sum(r["face2_room_kill"] for r in seven_rows)==5
assert all(r["exponent_difference"]==r["two_g_plus_k"] for r in seven_rows)
assert all(r["g"]==0 and r["k"]==1 and r["lambda_z"]==1 and r["tau"]==1 for r in seven_rows)

autopsy_fields=[
    "packet","A","W","u0","g1star","C2","C3","Lambda","m2","m3","n2","n3",
    "Zminus","Zplus","Ulo","Uhi","C2_over_10n2","C3_over_10n3",
    "P2_over_u0W10n2","P3_over_u0A10n3","face2_room_kill","face3_room_kill",
    "g","k","lambda_z","tau","exponent_difference","first_failure"
]
with (ROOT/"105-R32-q1-seven-hit-autopsy.csv").open("w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=autopsy_fields)
    w.writeheader()
    for r in seven_rows:
        rr={k:r.get(k,"") for k in autopsy_fields}
        rr["packet"]=f"({r['P1']},{r['P2']},{r['P3']},{r['Q0']})"
        w.writerow(rr)

near_fields=["packet","Ulo","Uhi","Delta_U","face2_room_kill","face3_room_kill","C2","C3","n2","n3","status"]
with (ROOT/"105-R32-unit-near-hit-registry.csv").open("w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=near_fields); w.writeheader()
    for r in seven_rows:
        w.writerow({
            "packet":f"({r['P1']},{r['P2']},{r['P3']},{r['Q0']})",
            "Ulo":r["Ulo"],"Uhi":r["Uhi"],"Delta_U":r["Ulo"]-r["Uhi"],
            "face2_room_kill":r["face2_room_kill"],"face3_room_kill":r["face3_room_kill"],
            "C2":r["C2"],"C3":r["C3"],"n2":r["n2"],"n3":r["n3"],
            "status":"BOUNDED_Q1_TC1_HIT__ROOM_EMPTY"
        })

# Structural digit-only countermodel: all requested digit/support gates but NOT TC1/master.
P1,P2,P3,Q=50,10,1,51
A=W=u0=g1=1; n=1; delta=1; rho=2; m=1; g=0; k=1
n2=n+delta; n3=n; m2=m; m3=n+g
C2=P2//(u0*W); C3=P3//(u0*A)
T=Q-P3; H=10**g*Q-P2; D=10**k*P1-Q
g0=gcd(u0*A*W,P1); mu=g1//g0
lambda_z=10**n3//gcd(10**n3,W*T)
Lam=math.lcm(mu,lambda_z); tau=lambda_z//gcd(lambda_z,mu); R1=P1//g1
Ulo=max(ceildiv(10**(n2-1),C2),ceildiv(10**(n3-1),C3))
Uhi=min((10**n2-1)//C2,(10**n3-1)//C3)
lhs=Fraction(W*g1*T,A*10**n)-g1*P2
rhs=10**g*(W*u0*P1*10**rho-Q*(W*u0*10**m+g1))
assert P1*P1+P2*P2+P3*P3==Q*Q
assert gcd(gcd(gcd(P1,P2),P3),Q)==1
assert delta in delta_set(P2//W,P3//A)
assert (Ulo,Uhi)==(1,9)
assert Lam==1 and 10**(m2-1)<=A*Lam<=10**m2-1 and 10**(m3-1)<=W*Lam<=10**m3-1
assert gcd(A,C2)==gcd(W,C3)==gcd(A,W)==1
assert gcd(mu,C2*C3)==gcd(tau,R1)==gcd(tau,C2*C3)==1
assert (T,H,D)==(50,41,449)
assert lhs-rhs==-4444

countermodel = {
    "packet":"(50,10,1,51)","A":1,"W":1,"u0":1,"g1star":1,
    "n2":2,"n3":1,"m2":1,"m3":1,"g":0,"k":1,"C2":10,"C3":1,
    "Lambda":1,"Ulo":1,"Uhi":9,"chosen_U":1,
    "sphere":"PASS","primitive":"PASS","q1_digits":"PASS","source_room":"PASS",
    "shape":"PASS","mu_smith":"PASS","tail":"PASS","DHT_positive":"PASS",
    "TC1_master":"FAIL","TC1_residual":str(lhs-rhs),
    "status":"DIGIT_ONLY_COUNTERMODEL__NOT_GENUINE_Q1_ARCHITECTURE"
}

# Determinization verifier on all seven.
for r in seven_rows:
    assert len(str(r["A"]*r["Lambda"]))==r["m2"]
    assert len(str(r["W"]*r["Lambda"]))==r["m3"]
    assert r["g"]==r["m3"]-r["n3"]
    assert r["k"]==r["n2"]-r["m2"]-r["g"]

# Restricted architecture-first q=1/master falsification lane:
# A=W=u0=g1=Lambda=1, n3=m2=m3=1, g=0, U=1, k=1..4,
# C3 one digit and C2 exactly (k+1)-digit. TC1 reduces to
# 10^(k+2) P1 + 10 C2 + C3 = 111 Q0.
restricted=[]
restricted_hits=[]
for kk in range(1,5):
    checked=square_disc=int_roots=finals=0
    aa=10**(kk+2)
    Acoef=111**2-aa*aa
    for c2 in range(10**kk,10**(kk+1)):
      for c3 in range(1,10):
        checked+=1
        bb=10*c2+c3
        Bcoef=-2*aa*bb
        Ccoef=111**2*(c2*c2+c3*c3)-bb*bb
        disc=Bcoef*Bcoef-4*Acoef*Ccoef
        if disc<0: continue
        ss=isqrt(disc)
        if ss*ss!=disc: continue
        square_disc+=1
        den=2*Acoef
        for num in (-Bcoef+ss,-Bcoef-ss):
            if num%den: continue
            p1=num//den
            if p1<=0: continue
            int_roots+=1
            nq=aa*p1+bb
            if nq%111: continue
            q0=nq//111
            if p1*p1+c2*c2+c3*c3!=q0*q0: continue
            if gcd(gcd(gcd(p1,c2),c3),q0)!=1: continue
            if min(q0-c3,q0-c2,10**kk*p1-q0)<=0: continue
            if (q0-c3)%10: continue # lambda_z=1
            finals+=1
            restricted_hits.append((kk,c2,c3,p1,q0))
    restricted.append({"k":kk,"exact_configurations":checked,"square_discriminants":square_disc,
                       "positive_integer_roots":int_roots,"final_hits":finals})
assert sum(x["exact_configurations"] for x in restricted)==899910
assert not restricted_hits
assert sum(x["square_discriminants"] for x in restricted)==0

# Main q1 registry.
q1_fields=["kind","packet","A","W","u0","g1star","Lambda","n2","n3","m2","m3","g","k",
           "C2","C3","Ulo","Uhi","q1_denominator","source_room","TC1_master","first_failure","scope"]
with (ROOT/"105-R32-q1-registry.csv").open("w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=q1_fields); w.writeheader()
    for r in seven_rows:
        w.writerow({
            "kind":"R28_B3000_RAW_TC1_Q1_HIT","packet":f"({r['P1']},{r['P2']},{r['P3']},{r['Q0']})",
            "A":r["A"],"W":r["W"],"u0":r["u0"],"g1star":r["g1star"],"Lambda":r["Lambda"],
            "n2":r["n2"],"n3":r["n3"],"m2":r["m2"],"m3":r["m3"],"g":r["g"],"k":r["k"],
            "C2":r["C2"],"C3":r["C3"],"Ulo":r["Ulo"],"Uhi":r["Uhi"],
            "q1_denominator":"PASS","source_room":"FAIL","TC1_master":"PASS",
            "first_failure":"POSITIVE_RADIAL_BOX","scope":"COMPLETE_R28_E27_CORPUS_Q0_LE_3000"
        })
    w.writerow({
        "kind":"DIGIT_ONLY_COUNTERMODEL","packet":countermodel["packet"],"A":1,"W":1,"u0":1,"g1star":1,
        "Lambda":1,"n2":2,"n3":1,"m2":1,"m3":1,"g":0,"k":1,"C2":10,"C3":1,
        "Ulo":1,"Uhi":9,"q1_denominator":"PASS","source_room":"PASS","TC1_master":"FAIL",
        "first_failure":"TC1_MASTER_RESIDUAL_-4444","scope":"STRUCTURAL_COUNTERMODEL_NOT_FULL_ARCHITECTURE"
    })
    w.writerow({
        "kind":"R28_INFINITE_F1_ARCHITECTURE","packet":"1000P1+50P2+P3=151Q0",
        "A":1,"W":2,"u0":1,"g1star":10,"n2":2,"n3":2,"m2":1,"m3":2,"g":0,"k":1,
        "q1_denominator":"INHERITED_FIXED_ARCH_Q1_SCALE","source_room":"GLOBAL_EMPTY_ON_F1",
        "TC1_master":"PASS_BY_FAMILY_DEFINITION","first_failure":"POSITIVE_RADIAL_BOX",
        "scope":"R28_GLOBAL_FOR_FIXED_ARCHITECTURE_F1"
    })

# Exponent identity table.
exp_fields=["source","packet","m2","m3","n2","n3","g","k",
            "m3_minus_m2","n3_minus_n2","difference","two_g_plus_k","status"]
with (ROOT/"105-R32-exponent-identity-table.csv").open("w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=exp_fields); w.writeheader()
    w.writerow({"source":"SYMBOLIC_R26","packet":"ALL_LEGAL_EXPONENT_TUPLES",
                "m2":"m","m3":"n+g","n2":"m+g+k","n3":"n","g":"g","k":"k",
                "m3_minus_m2":"n+g-m","n3_minus_n2":"n-(m+g+k)",
                "difference":"2g+k","two_g_plus_k":"2g+k","status":"PROVED_BY_SUBSTITUTION"})
    for r in seven_rows:
        w.writerow({"source":"SEVEN_HIT_REPLAY","packet":f"({r['P1']},{r['P2']},{r['P3']},{r['Q0']})",
                    "m2":r["m2"],"m3":r["m3"],"n2":r["n2"],"n3":r["n3"],"g":r["g"],"k":r["k"],
                    "m3_minus_m2":r["m3"]-r["m2"],"n3_minus_n2":r["n3"]-r["n2"],
                    "difference":r["exponent_difference"],"two_g_plus_k":2*r["g"]+r["k"],"status":"PASS"})

# Restricted exact search certificate.
with (ROOT/"105-R32-restricted-q1-master-search.csv").open("w",newline="",encoding="utf-8") as f:
    fields=["k","exact_configurations","square_discriminants","positive_integer_roots","final_hits"]
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(restricted)

# Prime branch registry. Since q1 was not globally killed, only symbolic reduction + bounded inherited/restricted lanes are recorded.
prime_fields=["kind","prime_q","scope","m2_recovery","m3_recovery","g_recovery","k_recovery",
              "coprime_gate","candidate_count","survivor_count","status"]
with (ROOT/"105-R32-prime-q-registry.csv").open("w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=prime_fields); w.writeheader()
    for p in (2,3,5,7):
        w.writerow({
            "kind":"RESTRICTED_ONE_DIGIT_PRIME_LANE","prime_q":p,
            "scope":"A=W=u0=g1=Lambda=1;U=1;n3=m2=m3=1;g=0;k=1..4",
            "m2_recovery":"digits(A*Lambda*p)=1","m3_recovery":"digits(W*Lambda*p)=1",
            "g_recovery":"m3-n3=0","k_recovery":"n2-m2-g",
            "coprime_gate":"p does not divide F*U (not reached because TC1-conic count=0)",
            "candidate_count":899910,"survivor_count":0,
            "status":"BOUNDED_EXACT_NO_TC1_CONIC__NOT_GLOBAL_PRIME_EXTINCTION"
        })
    w.writerow({
        "kind":"SYMBOLIC_PRIME_BRANCH","prime_q":"p","scope":"ALL_FIXED_POST_SUPPORT_ARCHITECTURES",
        "m2_recovery":"digits(A*Lambda*p)","m3_recovery":"digits(W*Lambda*p)",
        "g_recovery":"m3-n3","k_recovery":"n2-m2-g","coprime_gate":"p∤F*U",
        "candidate_count":"","survivor_count":"","status":"EXACT_REDUCTION_ONLY__GLOBAL_EXISTENCE_UNDECIDED"
    })

# Exceptional/reconstruction registries.
exc_fields=["object","type","status","exact_data","implication"]
with (ROOT/"105-R32-exceptional-branch-registry.csv").open("w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=exc_fields); w.writeheader()
    w.writerow({"object":"DIGIT_ONLY_COUNTERMODEL","type":"COUNTERMODEL_TO_DIGIT_ONLY_KILL",
                "status":"VERIFIED","exact_data":json.dumps(countermodel,ensure_ascii=False),
                "implication":"Master/TC1 is essential; interval intersection alone cannot prove q1 extinction."})
    w.writerow({"object":"TC1_CONIC_F1","type":"INFINITE_RAW_TC1_Q1_ARCHITECTURE",
                "status":"INHERITED_R28_GLOBAL_SOURCE_ROOM_EMPTY",
                "exact_data":"1000P1+50P2+P3=151Q0; (A,W,u0,g1,n,delta,m,k,g)=(1,2,1,10,2,0,1,1,0)",
                "implication":"q1 forced scale itself is not a finite phenomenon; source room kills this entire fixed architecture."})

rec_fields=["object","N30_positive","reconstruction_triggered","stage_reached","failure","full_strict_A1"]
with (ROOT/"105-R32-reconstruction-registry.csv").open("w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=rec_fields); w.writeheader()
    for r in seven_rows:
        w.writerow({"object":f"({r['P1']},{r['P2']},{r['P3']},{r['Q0']})","N30_positive":"NO",
                    "reconstruction_triggered":"NO","stage_reached":"q1 denominator + raw TC1",
                    "failure":"SOURCE_ROOM_EMPTY","full_strict_A1":"NO"})
    w.writerow({"object":"(50,10,1,51) structural countermodel","N30_positive":"NO",
                "reconstruction_triggered":"NO","stage_reached":"digit/source/support pre-master",
                "failure":"TC1_MASTER_RESIDUAL_-4444","full_strict_A1":"NO"})

# Machine-readable saturation certificate.
cert = {
  "schema":"105-R32-unit-chamber-saturation-v1",
  "global_verdict":"R32_TERMINAL_ATTACK_FAILED",
  "unit_chamber_source_room_extinction":"NOT_PROVED_NOT_FALSIFIED",
  "strict_A1_unliftability":"NOT_PROVED",
  "global_N30_zero":"NOT_PROVED",
  "full_strict_A1_witness":"NOT_FOUND",
  "proved":{
    "exponent_difference":"(m3-m2)-(n3-n2)=2g+k",
    "packet_invariant":"R=P2/(10^(2g+k)*P3)",
    "double_interval_necessary_window":"10^-2 < R < 10^2",
    "unit_chamber_digit_determinization":"m2=digits(A*Lambda);m3=digits(W*Lambda);g=m3-n3;k=n2-m2-g",
    "scale_q_digit_determinization":"m2=digits(A*Lambda*q);m3=digits(W*Lambda*q);g=m3-n3;k=n2-m2-g",
    "seven_hit_face3_kill":"7/7 in complete R28 E27 Q0<=3000 q1 raw-TC1 hits",
    "seven_hit_face2_kill":"5/7",
    "seven_hit_integer_gap":"Ulo-Uhi=1 for all 7",
    "digit_only_countermodel":"(50,10,1,51), TC1 residual=-4444"
  },
  "bounded_search":{
    "restricted_q1_master_lane_exact_configurations":899910,
    "square_discriminants":0,
    "final_hits":0,
    "global_inference":False
  },
  "first_unresolved_object":"MASTER_CONDITIONED_UNIT_SOURCE_ROOM_COLLISION",
  "prime_branch":{
    "global_attack_triggered_by_unit_extinction":False,
    "exact_symbolic_reduction":"PROVED",
    "genuine_prime_survivor":"NOT_FOUND",
    "global_prime_extinction":"NOT_PROVED"
  }
}
(ROOT/"105-R32-unit-saturation-certificate.json").write_text(json.dumps(cert,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print("R32 exact unit-digit script: PASS")
print("SEVEN_Q1_HITS=7")
print("FACE3_ROOM_KILL=7")
print("FACE2_ROOM_KILL=5")
print("ALL_SEVEN_DELTA_U=1")
print("DIGIT_ONLY_COUNTERMODEL_TC1_RESIDUAL=-4444")
print("RESTRICTED_EXACT_CONFIGURATIONS=899910")
print("RESTRICTED_SQUARE_DISCRIMINANTS=0")
print("GLOBAL_Q1_EXTINCTION=UNDECIDED")
