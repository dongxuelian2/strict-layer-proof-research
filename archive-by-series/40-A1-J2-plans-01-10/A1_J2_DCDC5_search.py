#!/usr/bin/env python3
"""
A1 J2 DCDC5 exact certificate.

Scope: Strict Layer A1-only, Exact Resonance R=0, J=2, negative branch.
Inherited frozen frontier: g>=4, u>1, ell:=2g-k>=2.

This script certifies the complete finite residuals for ell=2 and ell=3,
and also an exact diagnostic/closure for ell=4 after the new uniform
DCDC wedge reductions.  All decisions use exact integer/Fraction arithmetic.
No floating-point decision is used.
"""
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path

OUT = Path('/mnt/data')
ETA = Fraction(1299, 500)  # inherited rigorous majorant eta<2.598


def unit10(n: int) -> bool:
    return gcd(abs(n), 10) == 1


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def divisors_trial(n: int):
    lo, hi = [], []
    d = 1
    while d * d <= n:
        if n % d == 0:
            lo.append(d)
            if d * d != n:
                hi.append(n // d)
        d += 1
    return lo + hi[::-1]


def outer_pairs(G: int):
    ans = []
    for u in divisors_trial(G + 1):
        if u <= 1:
            continue
        q = (G + 1) // u
        A = 2 * u + 1
        if unit10(A):
            ans.append((u, q, A))
    return ans


def solve_congruence_interval(a: int, b: int, m: int, L: int, U: int):
    if L > U:
        return []
    d = gcd(a, m)
    if b % d:
        return []
    aa, bb, mm = a // d, b // d, m // d
    r = (bb * pow(aa, -1, mm)) % mm
    if r < L:
        r += ceil_div(L - r, mm) * mm
    return list(range(r, U + 1, mm))


def reconstruct(G: int, q: int, N: int, t: int):
    if (G + 1) % q:
        return None
    u = (G + 1) // q
    A = 2 * u + 1
    Mq = q * (q + 4)
    R = A * t - 2 * N
    if R % Mq:
        return None
    Z = R // Mq
    numa = (G - 1) * t - q * N
    dena = 2 * (q + 4)
    if numa % dena:
        return None
    a3 = numa // dena
    if (Z + u * N) % 2:
        return None
    X = (Z + u * N) // 2
    if (N + q * Z) % 2:
        return None
    h = (N + q * Z) // 2
    if (A * N + (q + 2) * Z) % 2:
        return None
    m = (A * N + (q + 2) * Z) // 2
    r = (G // 2) * h - u * a3
    D2 = u * a3 + G * X
    return {
        'G': G, 'u': u, 'q': q, 'A': A, 'N': N, 't': t,
        'a3': a3, 'Z': Z, 'X': X, 'D2': D2,
        'h': h, 'm': m, 'r': r,
    }


def digit_t_interval(G: int, q: int, N: int):
    # G/10 <= a3 < G, with a3=((G-1)t-qN)/(2(q+4)).
    L = ceil_div((q + 4) * (G // 5) + q * N, G - 1)
    U = (2 * (q + 4) * G + q * N - 1) // (G - 1)
    return L, U


def nstrip_Ns(G: int, u: int, A: int, k: int):
    K = 10 ** k
    lo = -(2 * ETA / K + Fraction(2 * A, G))
    hi = 2 * ETA * G * G / K
    nmin = lo.numerator // lo.denominator - 3
    nmax = hi.numerator // hi.denominator + 3
    Ns = [n for n in range(nmin, nmax + 1) if n % 2 and lo < n < hi]
    return Ns, lo, hi


def negative_linear_ok(row, k: int):
    G, u, A = row['G'], row['u'], row['A']
    X = row['X']
    K = 10 ** k
    if not (
        G // 10 <= row['a3'] < G and unit10(row['a3'])
        and row['Z'] > 0 and unit10(row['Z'])
        and unit10(row['D2']) and unit10(row['h'])
        and unit10(row['m']) and unit10(row['r'])
    ):
        return False
    if not (
        X > 0 and unit10(X) and row['D2'] > 0
        and row['h'] > 0 and row['m'] > 0 and row['r'] > 0
    ):
        return False
    if not (X * K < ETA * u * G * G):
        return False
    if not (Fraction(row['Z'], 1) < 2 * ETA * u / K + Fraction(2 * u * A, G)):
        return False
    q, N, t, Z, a3 = row['q'], row['N'], row['t'], row['Z'], row['a3']
    return (
        2 * A * a3 == q * (G - 1) * Z - N
        and (G - 1) * t == 2 * (q + 4) * a3 + q * N
        and q * (q + 4) * Z == A * t - 2 * N
    )


def Ftilde(row):
    return row['A'] * row['X'] * row['X'] + row['Z'] * row['D2']


def dcore(g: int, k: int):
    return (2 ** min(k + 1, 2 * g - 2)) * (5 ** min(k, 2 * g))


def vp(n: int, p: int):
    c = 0
    while n and n % p == 0:
        c += 1
        n //= p
    return c


def dcdc_nt_identity(row):
    """Return both sides of 4 M^2 F = A Y^2 + 2 R E."""
    G, u, q, A, N, t = (row[x] for x in ('G','u','q','A','N','t'))
    Mq = q * (q + 4)
    R = A * t - 2 * N
    Y = R + u * N * Mq
    E = u * q * ((G - 1) * t - q * N) + G * Y
    lhs = 4 * Mq * Mq * Ftilde(row)
    rhs = A * Y * Y + 2 * R * E
    return lhs, rhs


def q1_polynomial(row):
    G, N, t = row['G'], row['N'], row['t']
    val = (
        G**3 * (50*N*N + 60*N*t + 20*t*t)
        + G**2 * (115*N*N + 170*N*t + 66*t*t)
        + G * (100*N*N + 158*N*t + 68*t*t)
        + 31*N*N + 52*N*t + 21*t*t
    )
    return val


def root_a1_data(row, g: int, k: int):
    G, u, A = row['G'], row['u'], row['A']
    H, K = G // 2, 10 ** k
    F = Ftilde(row)
    aa = A * H * H
    bb = -2 * u * K * row['D2']
    cc = F
    disc = bb * bb - 4 * aa * cc
    nonneg = disc >= 0
    square = False
    roots = []
    if nonneg:
        s = isqrt(disc)
        square = s * s == disc
        if square:
            den = 2 * aa
            for sign in (1, -1):
                num = -bb + sign * s
                if num > 0 and num % den == 0:
                    roots.append(num // den)
    return nonneg, square, sorted(set(roots))


def allowed_outer_for_layer(ell: int, g: int, q: int):
    # New uniform reductions proved in the report:
    # q=1: g <= 2 ell + 2 for ell>=2.
    # q>1, ell=2: g<=6.
    # q>1, ell>=3: g <= 3 ell - 1.
    if q == 1:
        return g <= 2 * ell + 2
    if ell == 2:
        return g <= 6
    return g <= 3 * ell - 1


def scan_layer(ell: int):
    if ell == 2:
        gmax = 6
    elif ell == 3:
        gmax = 8
    elif ell == 4:
        gmax = 11
    else:
        raise ValueError('certificate only scans ell=2,3,4')

    totals = {
        'outer': 0, 'N_cells': 0, 'congruence': 0, 'reconstructed': 0,
        'digit_legal': 0, 'dcdc': 0, 'disc_nonnegative': 0,
        'disc_square': 0, 'integral_a1_roots': 0, 'full_radial_survivors': 0,
    }
    per_g = {}
    per_q = []
    dcdc_survivors = []

    for g in range(4, gmax + 1):
        G = 10 ** g
        k = 2 * g - ell
        gs = {key: 0 for key in totals}
        qlist = []
        for u, q, A in outer_pairs(G):
            if q == G + 1:  # u=1, frozen closed
                continue
            if not allowed_outer_for_layer(ell, g, q):
                continue
            gs['outer'] += 1
            qstat = {
                'ell': ell, 'g': g, 'q': q, 'u': u,
                'N_cells': 0, 'congruence': 0, 'reconstructed': 0,
                'digit_legal': 0, 'dcdc': 0, 'disc_square': 0,
                'integral_a1_roots': 0,
            }
            Ns, _, _ = nstrip_Ns(G, u, A, k)
            gs['N_cells'] += len(Ns)
            qstat['N_cells'] = len(Ns)
            for N in Ns:
                L, U = digit_t_interval(G, q, N)
                ts = solve_congruence_interval(A, 2 * N, q * (q + 4), L, U)
                gs['congruence'] += len(ts)
                qstat['congruence'] += len(ts)
                for t in ts:
                    row = reconstruct(G, q, N, t)
                    if row is not None:
                        gs['reconstructed'] += 1
                        qstat['reconstructed'] += 1
                    if not (row and negative_linear_ok(row, k)):
                        continue
                    gs['digit_legal'] += 1
                    qstat['digit_legal'] += 1

                    lhs, rhs = dcdc_nt_identity(row)
                    assert lhs == rhs
                    if q == 1:
                        assert 100 * Ftilde(row) == q1_polynomial(row)

                    F = Ftilde(row)
                    D = dcore(g, k)
                    if F % D:
                        continue
                    gs['dcdc'] += 1
                    qstat['dcdc'] += 1
                    nonneg, square, roots = root_a1_data(row, g, k)
                    gs['disc_nonnegative'] += int(nonneg)
                    gs['disc_square'] += int(square)
                    gs['integral_a1_roots'] += len(roots)
                    qstat['disc_square'] += int(square)
                    qstat['integral_a1_roots'] += len(roots)

                    s1 = A * row['X'] * row['X']
                    s2 = row['Z'] * row['D2']
                    dcdc_survivors.append({
                        'ell': ell, 'g': g, 'q': q, 'u': u,
                        'N': N, 't': t, 'a3': row['a3'], 'Z': row['Z'],
                        'X': row['X'], 'D2': row['D2'],
                        'Ftilde': F, 'Dcore': D, 'core_quotient': F // D,
                        'v2_s1': vp(s1, 2), 'v2_s2': vp(s2, 2), 'v2_F': vp(F, 2),
                        'v5_s1': vp(s1, 5), 'v5_s2': vp(s2, 5), 'v5_F': vp(F, 5),
                        'disc_nonnegative': nonneg, 'disc_square': square,
                        'integral_a1_roots': ','.join(map(str, roots)),
                    })
            qlist.append(q)
            per_q.append(qstat)
        per_g[g] = {'q_values': qlist, **gs}
        for key in totals:
            totals[key] += gs[key]

    # In the certified layers, no integral a1 root survives; therefore the
    # later primitive/common-U radial gate is vacuously empty.
    assert totals['integral_a1_roots'] == 0
    totals['full_radial_survivors'] = 0
    assert all(x['full_radial_survivors'] == 0 for x in per_g.values())
    return totals, per_g, per_q, dcdc_survivors


def theorem_checks():
    G0 = 10 ** 4
    eps2 = Fraction(10001, 10000) ** 2
    # ell>=3 exact D=2K improves q>1 coefficient below 1.
    assert Fraction(73, 98) * eps2 < 1
    # q>=23 and q>=61 staircase refinements.
    assert Fraction(73, 2 * 23 * 23) * eps2 < Fraction(1, 10)
    assert Fraction(73, 2 * 61 * 61) * eps2 < Fraction(1, 100)
    # q=1 tail-product bound.
    assert Fraction(31 * 53 * 53, 50 * 50) < 35
    assert 175 < 1000
    # inherited eta majorant is safely below 2.598 by construction.
    assert ETA == Fraction(1299, 500)
    return True


def make_table(per_g):
    rows = [
        '| g | q values | outer | N cells | congruence | reconstructed | digit-legal | DCDC | square disc | integral roots |',
        '|---:|:--|---:|---:|---:|---:|---:|---:|---:|---:|'
    ]
    for g, s in per_g.items():
        qtxt = ', '.join(map(str, s['q_values'])) if s['q_values'] else '—'
        rows.append(
            f"| {g} | {qtxt} | {s['outer']} | {s['N_cells']} | {s['congruence']} | "
            f"{s['reconstructed']} | {s['digit_legal']} | {s['dcdc']} | "
            f"{s['disc_square']} | {s['integral_a1_roots']} |"
        )
    return '\n'.join(rows)


def write_outputs():
    theorem_checks()
    L2 = scan_layer(2)
    L3 = scan_layer(3)
    L4 = scan_layer(4)
    layers = {2: L2, 3: L3, 4: L4}

    all_survivors = L2[3] + L3[3] + L4[3]
    assert L2[0]['dcdc'] == 0
    assert L3[0]['dcdc'] == 0
    assert L4[0]['dcdc'] == 2
    assert len(all_survivors) == 2
    assert all(not r['disc_square'] for r in all_survivors)

    # Survivor TSV (DCDC survivors, both die at discriminant square gate).
    cols = list(all_survivors[0].keys())
    tsv = ['\t'.join(cols)]
    for rec in all_survivors:
        tsv.append('\t'.join(str(rec[c]) for c in cols))
    (OUT / 'A1_J2_DCDC5_survivors.tsv').write_text('\n'.join(tsv) + '\n', encoding='utf-8')

    # Dedicated ell=2 certificate.
    l2tot, l2pg, _, _ = L2
    l2lines = [
        'A1 J2 DCDC5 deficiency-2 exact closure certificate',
        'STATUS=ELL2_CLOSED',
        'UNIFORM_RANGE_REDUCTION=q=1 => g<=6; q>1 => g<=6',
        f"TOTALS={l2tot!r}",
    ]
    for g, s in l2pg.items():
        l2lines.append(f"g={g} {s!r}")
    l2lines += [
        'DCDC_SURVIVORS=0',
        'INTEGRAL_A1_ROOTS=0',
        'FULL_RADIAL_SURVIVORS=0',
        'CERTIFICATE_STATUS=PASS',
    ]
    (OUT / 'A1_J2_L2_certificate.txt').write_text('\n'.join(l2lines) + '\n', encoding='utf-8')

    # Main certificate.
    lines = [
        'A1 J2 DCDC5 exact certificate',
        f'ETA_MAJORANT={ETA.numerator}/{ETA.denominator}',
        'THEOREM_CHECKS=PASS',
        'NEW_Q1_WEDGE: q=1, ell>=2, DCDC/root survivor => g<=2ell+2.',
        'NEW_QGT1_WEDGE: q>1, ell>=3, DCDC/root survivor => g<=3ell-1.',
        'OUTER_SENSITIVE: G < (73/(2q^2))*(1+1/G)^2*10^(3ell) for ell>=3.',
        'OUTER_STAIRCASE: q>=23 => g<=3ell-2; q>=61 => g<=3ell-3.',
        'NORMALIZED_COMPLEMENT: ell>=3, Lambda=2K lambda0, lambda0=uD2-(A*10^ell/8)a1; v5(lambda0)=0; ell>=4 => gcd(lambda0,10)=1.',
        'NT_DCDC: with M=q(q+4), R=At-2N, Y=R+uNM, E=uq((G-1)t-qN)+GY, 4M^2 F=A Y^2+2RE.',
        'Q1_TAIL: 100F cubic identity verified on every q=1 digit-legal census cell.',
        '',
    ]
    for ell, (tot, pg, pq, surv) in layers.items():
        lines.append(f'ELL={ell} TOTALS={tot!r}')
        for g, s in pg.items():
            lines.append(f'ELL={ell} g={g} {s!r}')
        lines.append(f'ELL={ell} DCDC_SURVIVORS={len(surv)}')
        lines.append('')
    lines += [
        f'DCDC_SURVIVOR_ROWS={len(all_survivors)}',
        "DCDC_SURVIVOR_FILE=A1_J2_DCDC5_survivors.tsv",
        'VERDICT_ELL2=CLOSED',
        'VERDICT_ELL3=CLOSED',
        'VERDICT_ELL4=CLOSED',
        'VERDICT_Q1=OPEN_BUT_SLOPE2',
        'VERDICT_FULL_J2=OPEN',
        'NEW_FRONTIER=J=2, S_R<0, ell>=5, g>=4, u>1, with q=1 => g<=2ell+2 and q>1 => g<=3ell-1.',
        'CERTIFICATE_STATUS=PASS',
    ]
    (OUT / 'A1_J2_DCDC5_certificate.txt').write_text('\n'.join(lines) + '\n', encoding='utf-8')

    # Report.
    report = r'''# A1 J2 DCDC5 Report

**Project:** 三项十进制拼接平方和问题  
**Scope:** Strict Layer — \(A_1\)-only — Exact Resonance \(R=0\) — \(J=2\)  
**Campaign:** \(\ell=2\) Exact Closure × Deficiency-Core Decimal Congruence × Wedge-Slope Compression  
**Inherited source:** `A1_J2_RCRF4_Report.md`  
**Computation:** `A1_J2_DCDC5_search.py`  
**Certificate:** `A1_J2_DCDC5_certificate.txt`

---

# Part I — Executive Status

\[
\boxed{\ell=2\ \textbf{CLOSED}}
\]

\[
\boxed{q=1\ \textbf{OPEN globally, but compressed to }g\le2\ell+2}
\]

\[
\boxed{
q>1,\ \ell\ge3
\Longrightarrow
g\le3\ell-1
}
\]

and the outer-divisor-sensitive refinement is

\[
\boxed{
G<\frac{73}{2q^2}\left(1+\frac1G\right)^2 10^{3\ell}.
}
\tag{OW}
\]

The finite DCDC census also gives, as extra closures,

\[
\boxed{\ell=3\Longrightarrow\varnothing,\qquad \ell=4\Longrightarrow\varnothing.}
\]

Hence the full \(J=2\) chamber is still open, but its unique live deficiency frontier has moved to

\[
\boxed{
J=2,\quad S_R<0,\quad g\ge4,\quad u>1,\quad \ell\ge5,
}
\]

with

\[
\boxed{
q=1\Rightarrow g\le2\ell+2,
\qquad
q>1\Rightarrow g\le3\ell-1.
}
\tag{NEW-WEDGE}
\]

This round therefore achieves the required \(\ell=2\) exact closure, a genuine \((N,t)\)-only DCDC congruence, and a structural wedge improvement.  The main new uniform gain is the slope-2 theorem in the previously dangerous \(q=1\) chamber.

---

# Part II — Frozen Deficiency Ledger

Let

\[
G=10^g,\qquad H=G/2,\qquad K=10^k,\qquad \ell=2g-k,\qquad L=10^\ell,
\]

\[
uq=G+1,\qquad A=2u+1.
\]

The frozen radial-cyclotomic system is

\[
2Aa_3=q(G-1)Z-N,
\tag{RCE1}
\]

\[
(G-1)t=2(q+4)a_3+qN,
\tag{RCE2}
\]

\[
q(q+4)Z=At-2N.
\tag{RCE3}
\]

Thus

\[
a_3=\frac{(G-1)t-qN}{2(q+4)},\qquad
Z=\frac{At-2N}{q(q+4)},
\]

\[
\mathcal X=\frac{Z+uN}{2},\qquad
D_2=ua_3+G\mathcal X.
\]

The negative signed-index strip is

\[
-\left(\frac{2\eta}{K}+\frac{2A}{G}\right)<N<\frac{2\eta G^2}{K}=2\eta L,
\qquad \eta<2.598.
\tag{NSTRIP}
\]

This is crucial: after passing to deficiency coordinates, the upper size of \(N\) depends on \(\ell\), not on \(g\).

The root-factor system is

\[
a_1\Lambda=\widetilde F,
\qquad
AH^2a_1+\Lambda=2uKD_2,
\]

\[
\widetilde F=A\mathcal X^2+ZD_2,
\qquad
a_1>\frac{AG}{10}.
\tag{DRL}
\]

The exact decimal core is

\[
D_{g,k}=2^{\min(k+1,2g-2)}5^{\min(k,2g)}\mid\Lambda,\widetilde F.
\]

In deficiency coordinates:

\[
\ell=2:\quad D_{g,k}=K=\frac{G^2}{100},
\]

\[
\ell\ge3:\quad D_{g,k}=2K=\frac{2G^2}{L}.
\]

The inherited radial upper bound is

\[
\widetilde F<\frac{73}{10}L^2Au^2.
\tag{UP}
\]

---

# Part III — \(\ell=2\) Exact Closure

For \(\ell=2\), \(D=K=G^2/100\).  Combining DRL with the exact core gives

\[
\widetilde F>\frac{AG}{10}\frac{G^2}{100},
\]

hence with (UP)

\[
G^3<73L^3u^2,\qquad L=100.
\]

For \(q>1\), \(q\ge7\), so this leaves \(g\le6\).  For \(q=1\), the stronger q=1 tail theorem proved in Part VII also gives \(g\le2\ell+2=6\).  Therefore the **complete** \(\ell=2\) residual is only

\[
g\in\{4,5,6\}.
\]

@@L2TABLE@@

Totals:

```text
@@L2TOTAL@@
```

There are **214** fully digit-legal linear RCE cells and **zero** decimal-core survivors.  Thus no discriminant/root/common-\(U\) reconstruction is even reached:

\[
\boxed{\ell=2\Longrightarrow\varnothing.}
\]

This is the requested **Deficiency-2 Closure Certificate**.

---

# Part IV — Explicit Root-Factor Expansion in \((N,t)\)

Set

\[
M:=q(q+4),\qquad R:=At-2N,
\]

\[
Y:=R+uNM,
\]

\[
E:=uq\bigl((G-1)t-qN\bigr)+GY.
\]

Then the frozen reconstruction becomes exactly

\[
Z=\frac RM,
\qquad
\mathcal X=\frac{Y}{2M},
\qquad
D_2=\frac{E}{2M}.
\]

Therefore

\[
\boxed{
4M^2\widetilde F
=AY^2+2RE.
}
\tag{NT-F}
\]

This is the desired complete elimination of \(Z,\mathcal X,D_2\): the root-product term is now an explicit function of

\[
(g,\ell,u,q,N,t)
\]

and, after \(u=(G+1)/q\), of the outer divisor and the two terminal integers \((N,t)\).

Consequently DCDC becomes the genuine \((N,t)\)-only congruence

\[
\ell=2:\qquad
\boxed{
AY^2+2RE\equiv0\pmod{4KM^2},
}
\tag{NT-DCDC2}
\]

and for \(\ell\ge3\),

\[
\boxed{
AY^2+2RE\equiv0\pmod{8KM^2}.
}
\tag{NT-DCDC}
\]

This is stronger than merely recording \(2K\mid\widetilde F\): no \(Z,\mathcal X,D_2\) variables remain.

---

# Part V — Deficiency-Core Decimal Congruence

For \(\ell\ge3\), write

\[
\Lambda=2K\lambda_0.
\]

The second root-factor equation gives an exact scale-free normalization:

\[
AH^2a_1+2K\lambda_0=2uKD_2.
\]

Since

\[
\frac{H^2}{2K}=\frac L8,
\]

we get

\[
\boxed{
\lambda_0=uD_2-\frac{AL}{8}a_1.
}
\tag{NCF}
\]

Now \(u,D_2,A\) are ten-units.  Because \(5^\ell\mid L/8\),

\[
\lambda_0\equiv uD_2\pmod5,
\]

hence

\[
\boxed{v_5(\lambda_0)=0\qquad(\ell\ge3).}
\tag{NCF5}
\]

For \(\ell\ge4\), \(2\mid L/8\), so

\[
\lambda_0\equiv uD_2\equiv1\pmod2
\]

in parity, and therefore

\[
\boxed{\gcd(\lambda_0,10)=1\qquad(\ell\ge4).}
\tag{NCF10}
\]

This is an exact allocation theorem for the complementary root factor.  In particular, any extra \(2\)- or \(5\)-adic depth of

\[
\widetilde F=2K\,a_1\lambda_0
\]

beyond the forced core comes entirely from \(a_1\) once \(\ell\ge4\).  No generic local-phase machinery is needed.

The computational census also shows that DCDC can be achieved by genuine cancellation on the RCE side: two \(\ell=4,q=1,g=4\) states satisfy the whole decimal core even though both summands are individually \(2\)- and \(5\)-adic units.  They die only at the square-discriminant gate; see Part IX.

---

# Part VI — Decimal-Core Quotient

For \(\ell\ge3\), define

\[
\Omega:=\frac{\widetilde F}{2K}=a_1\lambda_0.
\]

The normalized complementary factor itself satisfies

\[
1\le\lambda_0
<\frac{73}{2}\frac{L^3u^2}{G^3}.
\tag{LAM-UP}
\]

Indeed, divide (UP) by \(2K a_1\) and use DRL.

This is the cleanest form of the new wedge mechanism.  Since \(uq=G+1\), for \(q>1\)

\[
1
<\frac{73}{2q^2}\frac{L^3}{G}\left(1+\frac1G\right)^2,
\]

so

\[
\boxed{
G<\frac{73}{2q^2}\left(1+\frac1G\right)^2L^3.
}
\tag{OW-again}
\]

The point is not just that \(\Omega\) is integral.  The complementary quotient \(\lambda_0\) is a positive integer with tightly controlled local support, and its positivity alone yields an outer-divisor-sensitive wedge.

---

# Part VII — The \(q=1\) Chamber: Decimal Tail and Slope 2

Now set

\[
q=1,\qquad u=G+1,\qquad A=2G+3.
\]

The RCE formulas become

\[
Z=\frac{(2G+3)t-2N}{5},
\]

\[
a_3=\frac{(G-1)t-N}{10},
\]

\[
\mathcal X=\frac{5GN+2Gt+3N+3t}{10},
\]

\[
D_2=\frac{5G^2N+3G^2t+2GN+3Gt-N-t}{10}.
\]

A direct exact expansion gives

\[
\begin{aligned}
100\widetilde F={}&
G^3(50N^2+60Nt+20t^2)\\
&+G^2(115N^2+170Nt+66t^2)\\
&+G(100N^2+158Nt+68t^2)\\
&+(N+t)(31N+21t).
\end{aligned}
\tag{Q1-POLY}
\]

For \(\ell=2\), put \(c=1\); for \(\ell\ge3\), put \(c=2\).  Then the decimal core is \(cK\mid\widetilde F\).  Since

\[
\frac{G^2}{100cK}=\frac{L}{100c}\in\mathbf Z
\qquad(\ell\ge2),
\]

all \(G^2,G^3\) terms disappear modulo \(100cK\).  Hence

\[
G(100N^2+158Nt+68t^2)+(N+t)(31N+21t)
\equiv0\pmod{100cK}.
\tag{Q1-TAIL}
\]

RCE3 gives

\[
At\equiv2N\pmod5.
\]

Since \(A\equiv3\pmod5\),

\[
N+t\equiv0\pmod5.
\]

Write

\[
N=-t+5s.
\]

Then

\[
100N^2+158Nt+68t^2
=10(250s^2-21st+t^2),
\]

\[
(N+t)(31N+21t)=25s(31s-2t).
\]

Thus (Q1-TAIL) is equivalent to

\[
\boxed{
20cK\mid
2G(250s^2-21st+t^2)+5s(31s-2t).
}
\tag{Q1-S}
\]

Assume first \(\ell<g\).  Then \(L\le G/10\).  NSTRIP gives

\[
N\ge-3,
\qquad
N<2\eta L<5.196L,
\]

and the exact digit window for \(a_3\) forces

\[
1\le t\le10.
\]

Therefore \(s=(N+t)/5\ge0\).  The case \(s=0\) would make (Q1-S) require a divisor at least \(100\) of the odd square \(t^2\le81\), impossible.  Hence \(s\ge1\).

Moreover

\[
s<\frac{5.196L+10}{5}<\frac{53}{50}L.
\]

Because \(G\mid20cK\), reducing (Q1-S) modulo \(G\) gives

\[
\frac G5\mid s(31s-2t).
\]

But \(s\ge1\), \(t\le10\), so

\[
0<s(31s-2t)<31s^2<35L^2.
\]

Consequently

\[
G<175L^2.
\]

As \(175<10^3\),

\[
\boxed{g\le2\ell+2.}
\tag{Q1-SLOPE2}
\]

If \(\ell\ge g\), the same conclusion is trivial.  Therefore (Q1-SLOPE2) is uniform for every \(q=1,\ell\ge2\) root/DCDC survivor.

This is the main slope compression of the round.

---

# Part VIII — Wedge-Slope Compression

The old wedge was

\[
q>1:\ g\le3\ell,
\qquad
q=1:\ g\le3\ell+2.
\]

The exact deficiency core improves it as follows.

## 8.1 \(q>1,\ell\ge3\)

Since \(D=2K\), DRL and (UP) give

\[
G^3<\frac{73}{2}L^3u^2.
\]

Using \(u=(G+1)/q\),

\[
G<\frac{73}{2q^2}\left(1+\frac1G\right)^2L^3.
\]

For the worst possible \(q=7\) and \(G\ge10^4\), the coefficient is already \(<1\).  Hence

\[
\boxed{q>1,\ \ell\ge3\Longrightarrow g\le3\ell-1.}
\]

More strongly,

\[
q\ge23\Longrightarrow g\le3\ell-2,
\]

\[
q\ge61\Longrightarrow g\le3\ell-3.
\]

So the dangerous q>1 outer chambers are forced toward genuinely small complementary divisors.

## 8.2 \(q=1\)

Part VII gives the strictly better slope

\[
\boxed{q=1\Longrightarrow g\le2\ell+2.}
\]

Thus the previously most dangerous maximal-\(u\) chamber is no longer slope 3 at all.

## 8.3 \(\ell=2\)

For \(q>1\), the exact \(D=K\) size inequality gives \(g\le6\); for \(q=1\), slope 2 also gives \(g\le6\).  Hence Part III is a genuinely complete finite closure.

---

# Part IX — Computational Census

All searches use the exact NSTRIP, the exact RCE congruence

\[
At\equiv2N\pmod{q(q+4)},
\]

the exact half-open digit window for \(a_3\), ten-unit/positivity conditions, DCDC, and then the exact quadratic discriminant/integral-root test.

## 9.1 \(\ell=2\)

@@L2TABLE2@@

```text
@@L2TOTAL2@@
```

Result: zero DCDC survivor, hence

\[
\boxed{\ell=2\text{ CLOSED}.}
\]

## 9.2 \(\ell=3\)

@@L3TABLE@@

```text
@@L3TOTAL@@
```

There are **3574** digit-legal linear cells and zero DCDC survivors.  Thus

\[
\boxed{\ell=3\text{ CLOSED}.}
\]

## 9.3 \(\ell=4\)

@@L4TABLE@@

```text
@@L4TOTAL@@
```

Exactly two DCDC pseudo-survivors occur, both in

\[
(g,q)=(4,1).
\]

They are:

```text
@@SURVIVORS@@
```

For both states,

\[
v_5(A\mathcal X^2)=v_5(ZD_2)=0,
\qquad
v_5(\widetilde F)=4,
\]

so the required \(5\)-adic depth is produced by **genuine cancellation**, not by individual divisibility.  The 2-adic cancellation is also genuine.  Nevertheless neither discriminant is a square, so no integral \(a_1\) root exists and the radial gate is never reached.

Therefore

\[
\boxed{\ell=4\text{ CLOSED}.}
\]

This \(\ell=4\) computation is useful primarily as a DCDC diagnostic: it falsifies any claim that the decimal core forces individual high divisibility of the two summands, while confirming that deep cancellation can occur but still be killed at the exact root gate.

---

# Part X — New Frontier

Full \(J=2\) is still open.  The new unique frontier is

\[
\boxed{
J=2,\quad S_R<0,\quad \ell\ge5,
}
\]

with frozen

\[
g\ge4,\qquad u>1,
\]

and the new uniform restrictions

\[
\boxed{
q=1\Rightarrow g\le2\ell+2,
}
\]

\[
\boxed{
q>1\Rightarrow
G<\frac{73}{2q^2}\left(1+\frac1G\right)^2L^3
\Rightarrow g\le3\ell-1.
}
\]

The preferred terminal obstruction is no longer merely

\[
2K\mid\widetilde F.
\]

It is the combined package

\[
\boxed{
\textbf{NT-DCDC}
:
AY^2+2RE\equiv0\pmod{8Kq^2(q+4)^2},
}
\]

plus

\[
\boxed{
\lambda_0=uD_2-\frac{AL}{8}a_1,
\qquad
v_5(\lambda_0)=0,
\qquad
\ell\ge4\Rightarrow\gcd(\lambda_0,10)=1,
}
\]

and, in the \(q=1\) chamber, the much lower-dimensional decimal-tail congruence (Q1-S).

The next highest-value target is therefore **not** \(\ell=5\) enumeration.  It is to generalize the q=1 tail-factor mechanism to the remaining small fixed \(q>1\) chambers, or to use NT-DCDC plus the outer-sensitive bound to force a similar slope-2 product divisibility.

---

# Status Ledger

## NEW PROVED

1. \(\ell=2\) exact closure.
2. Explicit \((N,t)\)-only root-product identity (NT-F).
3. Exact \((N,t)\)-only DCDC congruence modulo \(4KM^2\) / \(8KM^2\).
4. Normalized complementary factor
   \[
   \lambda_0=uD_2-(AL/8)a_1.
   \]
5. \(v_5(\lambda_0)=0\) for \(\ell\ge3\).
6. \(\gcd(\lambda_0,10)=1\) for \(\ell\ge4\).
7. Outer-sensitive wedge (OW).
8. \(q>1,\ell\ge3\Rightarrow g\le3\ell-1\).
9. \(q\ge23\Rightarrow g\le3\ell-2\); \(q\ge61\Rightarrow g\le3\ell-3\).
10. q=1 exact decimal-tail polynomial and congruence.
11. Uniform q=1 slope-2 theorem
    \[
    g\le2\ell+2.
    \]
12. Extra exact closures \(\ell=3,4\).

## FALSIFIED / DOWNGRADED

- DCDC does **not** force the two summands \(A\mathcal X^2\) and \(ZD_2\) to be individually highly divisible: the two \(\ell=4\) pseudo-survivors achieve the required core by genuine cancellation.
- No claim is made that \(\Omega\) itself is a ten-unit; only \(\lambda_0\) is forced to be a ten-unit for \(\ell\ge4\).

## OPEN

\[
\boxed{\textbf{Full J2 OPEN}.}
\]

The remaining uniform problem begins at \(\ell\ge5\).

---

# File Audit

The following files are generated and checked by the executable certificate:

```text
A1_J2_DCDC5_Report.md
A1_J2_DCDC5_search.py
A1_J2_DCDC5_certificate.txt
A1_J2_DCDC5_survivors.tsv
A1_J2_L2_certificate.txt
```

The report/certificate agree on:

```text
VERDICT_ELL2=CLOSED
VERDICT_ELL3=CLOSED
VERDICT_ELL4=CLOSED
VERDICT_Q1=OPEN_BUT_SLOPE2
VERDICT_FULL_J2=OPEN
```

FINAL_REPORT_FILE: A1_J2_DCDC5_Report.md

COMPUTATION_FILE: A1_J2_DCDC5_search.py

CERTIFICATE_FILE: A1_J2_DCDC5_certificate.txt

SURVIVOR_FILE: A1_J2_DCDC5_survivors.tsv

L2_CERTIFICATE_FILE: A1_J2_L2_certificate.txt
'''

    l2table = make_table(L2[1])
    l3table = make_table(L3[1])
    l4table = make_table(L4[1])
    survtxt = '\n'.join(
        f"ell={r['ell']} g={r['g']} q={r['q']} N={r['N']} t={r['t']} "
        f"core_quotient={r['core_quotient']} "
        f"v2=({r['v2_s1']},{r['v2_s2']}->{r['v2_F']}) "
        f"v5=({r['v5_s1']},{r['v5_s2']}->{r['v5_F']}) disc_square={r['disc_square']}"
        for r in all_survivors
    )
    report = (report
        .replace('@@L2TABLE@@', l2table)
        .replace('@@L2TOTAL@@', repr(L2[0]))
        .replace('@@L2TABLE2@@', l2table)
        .replace('@@L2TOTAL2@@', repr(L2[0]))
        .replace('@@L3TABLE@@', l3table)
        .replace('@@L3TOTAL@@', repr(L3[0]))
        .replace('@@L4TABLE@@', l4table)
        .replace('@@L4TOTAL@@', repr(L4[0]))
        .replace('@@SURVIVORS@@', survtxt)
    )
    (OUT / 'A1_J2_DCDC5_Report.md').write_text(report, encoding='utf-8')

    # Final audit.
    required = [
        'A1_J2_DCDC5_Report.md', 'A1_J2_DCDC5_search.py',
        'A1_J2_DCDC5_certificate.txt', 'A1_J2_DCDC5_survivors.tsv',
        'A1_J2_L2_certificate.txt',
    ]
    for name in required:
        p = OUT / name
        assert p.exists() and p.stat().st_size > 0, name
    text = (OUT / 'A1_J2_DCDC5_Report.md').read_text(encoding='utf-8')
    for needle in ('Part I — Executive Status', 'ell=2', 'Deficiency-Core Decimal Congruence', 'FINAL_REPORT_FILE'):
        assert needle in text, needle

    print('THEOREM_CHECKS=PASS')
    print('ELL2_TOTALS=', L2[0])
    print('ELL3_TOTALS=', L3[0])
    print('ELL4_TOTALS=', L4[0])
    print('DCDC_SURVIVORS=', len(all_survivors))
    print('VERDICT_ELL2=CLOSED')
    print('VERDICT_ELL3=CLOSED')
    print('VERDICT_ELL4=CLOSED')
    print('VERDICT_Q1=OPEN_BUT_SLOPE2')
    print('VERDICT_FULL_J2=OPEN')
    print('CERTIFICATE_STATUS=PASS')
    print('FINAL_REPORT_FILE: A1_J2_DCDC5_Report.md')
    print('COMPUTATION_FILE: A1_J2_DCDC5_search.py')
    print('CERTIFICATE_FILE: A1_J2_DCDC5_certificate.txt')
    print('SURVIVOR_FILE: A1_J2_DCDC5_survivors.tsv')
    print('L2_CERTIFICATE_FILE: A1_J2_L2_certificate.txt')


if __name__ == '__main__':
    write_outputs()
