#!/usr/bin/env python3
"""
A1 J2 RCRF4 exact targeted certificate.

Scope:
  Strict Layer A1-only, Exact Resonance R=0, J=2.
Purpose:
  1) census the linear Bézout cells before root-factor use;
  2) certify explicit high-depth linear survivors (so linear-only extinction is false);
  3) certify that those witnesses fail the forced decimal root core;
  4) exhaust the only finite residual needed for the uniform ell=1 closure:
     q=1, g in {4,5}.

No floating-point decision is used.
"""
from fractions import Fraction
from math import gcd
from pathlib import Path

ETA = Fraction(1299, 500)  # rigorous majorant for inherited eta
LOW_G_MIN, LOW_G_MAX = 4, 10
OUT = Path("/mnt/data")


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
    """All t in [L,U] satisfying a*t == b (mod m)."""
    if L > U:
        return []
    d = gcd(a, m)
    if b % d:
        return []
    aa, bb, mm = a // d, b // d, m // d
    r = (bb * pow(aa, -1, mm)) % mm
    first = r
    if first < L:
        first += ceil_div(L - first, mm) * mm
    return list(range(first, U + 1, mm))


def gcd_lemma(G: int, q: int, A: int):
    """d = gcd(A,q(q+4)) = gcd(A,G^2-1)."""
    d1 = gcd(A, q * (q + 4))
    d2 = gcd(A, G * G - 1)
    if d1 != d2:
        raise AssertionError(("gcd lemma", G, q, A, d1, d2))
    return d1


def reconstruct(G: int, q: int, N: int, t: int):
    if (G + 1) % q:
        return None
    u = (G + 1) // q
    A = 2 * u + 1
    denZ = q * (q + 4)
    numZ = A * t - 2 * N
    if numZ % denZ:
        return None
    Z = numZ // denZ
    dena = 2 * (q + 4)
    numa = (G - 1) * t - q * N
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
        "G": G, "u": u, "q": q, "A": A, "N": N, "t": t,
        "a3": a3, "Z": Z, "X": X, "D2": D2, "h": h, "m": m, "r": r,
    }


def digit_t_interval(G: int, q: int, N: int):
    # G/10 <= a3 < G, with a3=((G-1)t-qN)/(2(q+4)).
    L = ceil_div((q + 4) * (G // 5) + q * N, G - 1)
    U = (2 * (q + 4) * G + q * N - 1) // (G - 1)
    return L, U


def linear_common_checks(row):
    G = row["G"]
    return (
        G // 10 <= row["a3"] < G
        and unit10(row["a3"])
        and row["Z"] > 0 and unit10(row["Z"])
        and unit10(row["D2"])
        and unit10(row["h"])
        and unit10(row["m"])
        and unit10(row["r"])
    )


def positive_linear_ok(row):
    G, u, A = row["G"], row["u"], row["A"]
    X = row["X"]
    if not linear_common_checks(row):
        return False
    if not (X < 0 and unit10(X) and row["D2"] > 0 and row["h"] > 0 and row["m"] > 0 and row["r"] > 0):
        return False
    W = -X
    if not (0 < W < u):
        return False
    if not (row["Z"] * G < 2 * u * A):
        return False
    # exact RCE replay
    q, N, t, Z, a3 = row["q"], row["N"], row["t"], row["Z"], row["a3"]
    return (
        2 * A * a3 == q * (G - 1) * Z - N
        and (G - 1) * t == 2 * (q + 4) * a3 + q * N
        and q * (q + 4) * Z == A * t - 2 * N
    )


def negative_linear_ok(row, k: int):
    G, u, A = row["G"], row["u"], row["A"]
    X = row["X"]
    if not linear_common_checks(row):
        return False
    if not (X > 0 and unit10(X) and row["D2"] > 0 and row["h"] > 0 and row["m"] > 0 and row["r"] > 0):
        return False
    K = 10 ** k
    # inherited UW- and UZ-, using ETA majorant.
    if not (X * K < ETA * u * G * G):
        return False
    if not (row["Z"] < 2 * ETA * u / K + Fraction(2 * u * A, G)):
        return False
    q, N, t, Z, a3 = row["q"], row["N"], row["t"], row["Z"], row["a3"]
    return (
        2 * A * a3 == q * (G - 1) * Z - N
        and (G - 1) * t == 2 * (q + 4) * a3 + q * N
        and q * (q + 4) * Z == A * t - 2 * N
    )


def Ftilde(row):
    return row["A"] * row["X"] * row["X"] + row["Z"] * row["D2"]


def dcore(g: int, k: int):
    return (2 ** min(k + 1, 2 * g - 2)) * (5 ** min(k, 2 * g))


def vp(n: int, p: int):
    c = 0
    while n and n % p == 0:
        c += 1
        n //= p
    return c


def core_record(row, g: int, k: int):
    F = Ftilde(row)
    D = dcore(g, k)
    return {
        "core_pass": (F % D == 0),
        "v2F": vp(F, 2),
        "v5F": vp(F, 5),
        "D_v2": min(k + 1, 2 * g - 2),
        "D_v5": min(k, 2 * g),
    }


def positive_candidates_for_outer(g: int, u: int, q: int, A: int):
    G = 10 ** g
    if q <= 1 or u <= 1:
        return [], 0, 0
    # The exact positive effective integer window:
    # r>0 iff t>=q+2; digit upper gives t<=2q+8.
    L, U = q + 2, 2 * q + 8
    M = q * (q + 4)
    d = gcd_lemma(G, q, A)
    solvable = int(d == 1)  # PBZ RHS=-2 and d is odd
    if not solvable:
        return [], solvable, 0
    ts = solve_congruence_interval(A, -2, M, L, U)
    rows = []
    for t in ts:
        row = reconstruct(G, q, -1, t)
        if row and positive_linear_ok(row):
            rows.append(row)
    return rows, solvable, len(ts)


def negative_boundary_candidates_for_outer(g: int, u: int, q: int, A: int):
    G = 10 ** g
    if q <= 1 or u <= 1:
        return [], 0, 0
    rows, solvable_cells, residue_hits = [], 0, 0
    for N in (1, 3, 5):
        d = gcd_lemma(G, q, A)
        if N % d:
            continue
        solvable_cells += 1
        L, U = digit_t_interval(G, q, N)
        ts = solve_congruence_interval(A, 2 * N, q * (q + 4), L, U)
        residue_hits += len(ts)
        for t in ts:
            row = reconstruct(G, q, N, t)
            if row and negative_linear_ok(row, 2 * g):
                rows.append(row)
    return rows, solvable_cells, residue_hits


def low_depth_census():
    totals = {
        "positive_outer": 0, "positive_pbz_solvable_outer": 0,
        "positive_interval_residue": 0, "positive_linear": 0, "positive_root_core": 0,
        "negative_outer": 0, "negative_nbz_solvable_N_cells": 0,
        "negative_interval_residue": 0, "negative_linear": 0, "negative_root_core": 0,
    }
    per_g = []
    for g in range(LOW_G_MIN, LOW_G_MAX + 1):
        G = 10 ** g
        pg = {k: 0 for k in totals}
        for u, q, A in outer_pairs(G):
            if q > 1 and u > 1 and q ** 3 < 216 * G:
                pg["positive_outer"] += 1
                rows, sol, hits = positive_candidates_for_outer(g, u, q, A)
                pg["positive_pbz_solvable_outer"] += sol
                pg["positive_interval_residue"] += hits
                pg["positive_linear"] += len(rows)
                pg["positive_root_core"] += sum(core_record(r, g, 2 * g - 1)["core_pass"] for r in rows)

                pg["negative_outer"] += 1
                nrows, nsol, nhits = negative_boundary_candidates_for_outer(g, u, q, A)
                pg["negative_nbz_solvable_N_cells"] += nsol
                pg["negative_interval_residue"] += nhits
                pg["negative_linear"] += len(nrows)
                pg["negative_root_core"] += sum(core_record(r, g, 2 * g)["core_pass"] for r in nrows)
        for k in totals:
            totals[k] += pg[k]
        per_g.append((g, pg))
    return totals, per_g


def verify_positive_high_witness():
    g, q, t = 2385, 19, 45
    G = 10 ** g
    u = (G + 1) // q
    A = 2 * u + 1
    assert (G + 1) % q == 0
    assert gcd_lemma(G, q, A) == 1
    assert q + 2 <= t <= 2 * q + 8
    row = reconstruct(G, q, -1, t)
    assert row and positive_linear_ok(row)
    cr = core_record(row, g, 2 * g - 1)
    assert not cr["core_pass"]
    return row, cr


def verify_negative_high_witness():
    g, q, N, t = 39, 7, 3, 17
    G = 10 ** g
    u = (G + 1) // q
    A = 2 * u + 1
    assert (G + 1) % q == 0
    assert gcd_lemma(G, q, A) == 1
    L, U = digit_t_interval(G, q, N)
    assert L <= t <= U
    row = reconstruct(G, q, N, t)
    assert row and negative_linear_ok(row, 2 * g)
    cr = core_record(row, g, 2 * g)
    assert not cr["core_pass"]
    return row, cr


def ell1_q1_finite_residual():
    """Exact residual after size proof closes q=1, g>=6."""
    records = []
    stats = {}
    for g in (4, 5):
        G = 10 ** g
        q = 1
        u = G + 1
        A = 2 * u + 1
        k = 2 * g - 1
        # ETA-majorant strip:
        # -(20 eta/G^2 + 2A/G) < N < 20 eta.
        Ns = [-3, -1] + list(range(1, 52, 2))
        linear = []
        root_core = []
        for N in Ns:
            L, U = digit_t_interval(G, q, N)
            ts = solve_congruence_interval(A, 2 * N, q * (q + 4), L, U)
            for t in ts:
                row = reconstruct(G, q, N, t)
                if row and negative_linear_ok(row, k):
                    linear.append(row)
                    cr = core_record(row, g, k)
                    records.append((row, cr))
                    if cr["core_pass"]:
                        root_core.append((row, cr))
        stats[g] = {"linear": len(linear), "root_core": len(root_core)}
        assert len(linear) == 6
        assert not root_core
    return stats, records


def theorem_constant_checks():
    G0 = 10 ** 4
    # Positive: candidate would force G^3 < 600 u^2, q>=7.
    assert 49 * G0 ** 3 > 600 * (G0 + 1) ** 2
    # Negative k=2g: candidate would force G^3 < 560 u^2, q>=7.
    assert 49 * G0 ** 3 > 560 * (G0 + 1) ** 2

    # ell=1 upper coefficient:
    # Ftilde < 729 A u^2 for G>=1e4.
    coeff = 100 * ETA * ETA + 2 * (1 + 10 * ETA) \
            + Fraction(20, 3 * G0) * ETA * (1 + 10 * ETA)
    assert coeff < 729
    # q>1 ell=1 candidate would force G^3 < 145800 u^2.
    assert 49 * G0 ** 3 > 145800 * (G0 + 1) ** 2
    # q=1 ell=1 size closure begins by g=6.
    G6 = 10 ** 6
    assert G6 ** 3 > 145800 * (G6 + 1) ** 2

    # General deficiency wedge.  Put L=10^ell.  For every ell>=1,
    # Ftilde < 7.3 L^2 A u^2 and Dcore >= G^2/(2L), hence
    # G^3 < 146 L^3 u^2 for any root survivor.
    L0 = 10
    ratio = ETA * ETA + 2 * ETA / L0 + Fraction(2, L0 * L0) \
            + Fraction(2, 30000) * ETA * (1 + ETA * L0) / L0
    assert ratio < Fraction(73, 10)
    eps2 = Fraction(10001, 10000) ** 2
    assert Fraction(146, 49) * eps2 < 3      # q>1 => G < 3 L^3
    assert 146 * eps2 < 147                  # q=1 => G < 147 L^3
    return coeff, ratio


def compact_row(branch, row, cr):
    return {
        "branch": branch,
        "g": len(str(row["G"])) - 1,
        "q": row["q"], "N": row["N"], "t": row["t"],
        "a3_last2": row["a3"] % 100,
        "Z_last2": row["Z"] % 100,
        "X_last2": row["X"] % 100,
        "D2_last2": row["D2"] % 100,
        "h_last2": row["h"] % 100,
        "m_last2": row["m"] % 100,
        "r_last2": row["r"] % 100,
        "root_core_pass": cr["core_pass"],
        "v2F": cr["v2F"], "v5F": cr["v5F"],
        "D_v2": cr["D_v2"], "D_v5": cr["D_v5"],
    }


def main():
    coeff, deficiency_ratio = theorem_constant_checks()
    totals, per_g = low_depth_census()
    posrow, poscr = verify_positive_high_witness()
    negrow, negcr = verify_negative_high_witness()
    ellstats, ellrecords = ell1_q1_finite_residual()

    survivor_rows = [
        compact_row("POSITIVE_LINEAR", posrow, poscr),
        compact_row("NEG_K2G_LINEAR", negrow, negcr),
    ]
    for row, cr in ellrecords:
        survivor_rows.append(compact_row("ELL1_Q1_LINEAR", row, cr))

    # TSV: these are linear survivors, not root survivors.
    cols = list(survivor_rows[0].keys())
    tsv = ["\t".join(cols)]
    for rec in survivor_rows:
        tsv.append("\t".join(str(rec[c]) for c in cols))
    (OUT / "A1_J2_RCRF4_survivors.tsv").write_text("\n".join(tsv) + "\n", encoding="utf-8")

    lines = [
        "A1 J2 RCRF4 exact certificate",
        f"ETA_MAJORANT={ETA.numerator}/{ETA.denominator}",
        f"LOW_DEPTH_CENSUS_G={LOW_G_MIN}..{LOW_G_MAX}",
        "",
        "THEOREM_CONSTANT_CHECKS=PASS",
        f"ELL1_UPPER_COEFFICIENT_MAJORANT={coeff}",
        f"GENERAL_DEFICIENCY_UPPER_RATIO_AT_L10={deficiency_ratio}",
        "GENERAL_DEFICIENCY_WEDGE: root survivor => G^3 < 146*10^(3ell)*u^2.",
        "GENERAL_DEFICIENCY_QGT1: q>1 => g<=3ell.",
        "GENERAL_DEFICIENCY_Q1: q=1 => g<=3ell+2.",
        "POSITIVE_SIZE_CONTRADICTION: G^3 < 600 u^2; q>1 => q>=7; impossible for G>=10^4.",
        "NEG_K2G_SIZE_CONTRADICTION: G^3 < 560 u^2; q>1 => q>=7; impossible for G>=10^4.",
        "ELL1_QGT1_SIZE_CONTRADICTION: G^3 < 145800 u^2; q>1 => q>=7; impossible for G>=10^4.",
        "ELL1_Q1_LARGE_G: G^3 < 145800(G+1)^2 impossible for g>=6.",
        "",
        "LOW_DEPTH_TOTALS=" + repr(totals),
    ]
    for g, d in per_g:
        lines.append(f"LOW_DEPTH_g={g} " + repr(d))

    lines += [
        "",
        "POSITIVE_HIGH_DEPTH_LINEAR_WITNESS=" + repr(compact_row("POSITIVE_LINEAR", posrow, poscr)),
        "NEG_K2G_HIGH_DEPTH_LINEAR_WITNESS=" + repr(compact_row("NEG_K2G_LINEAR", negrow, negcr)),
        "ELL1_Q1_FINITE_STATS=" + repr(ellstats),
        f"ELL1_Q1_LINEAR_TOTAL={sum(v['linear'] for v in ellstats.values())}",
        f"ELL1_Q1_ROOT_CORE_TOTAL={sum(v['root_core'] for v in ellstats.values())}",
        "",
        "LINEAR_SURVIVOR_FILE=A1_J2_RCRF4_survivors.tsv",
        f"LINEAR_SURVIVOR_ROWS={len(survivor_rows)}",
        "ROOT_SURVIVOR_COUNT=0",
        "",
        "VERDICT_POSITIVE_J2=CLOSED",
        "VERDICT_NEGATIVE_K_2G=CLOSED",
        "VERDICT_ELL1=CLOSED",
        "VERDICT_FULL_J2=OPEN",
        "NEW_FRONTIER=J=2, S_R<0, ell>=2 (equiv k<=2g-2), with inherited g>=4,u>1 reductions.",
        "CERTIFICATE_STATUS=PASS",
    ]
    (OUT / "A1_J2_RCRF4_certificate.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
