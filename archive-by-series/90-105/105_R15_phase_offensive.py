#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
from collections import Counter, defaultdict
from math import gcd, isqrt
from pathlib import Path

ROOT = Path('/mnt/data')


def ceildiv(a: int, b: int) -> int:
    return (a + b - 1) // b


def digits(n: int) -> int:
    return len(str(n))


def divisors(n: int) -> list[int]:
    ds = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            ds.append(d)
            if d * d != n:
                ds.append(n // d)
    return sorted(ds)


def square_scale_divisors(n: int) -> list[int]:
    return [c for c in range(1, isqrt(n) + 1) if n % (c * c) == 0]


def cf_factorizations(n: int):
    """All exact R14 CF factorizations c^2 X0 Y0=n with X0>Y0, gcd=1,
    and P1,Q0 integral. No floating point is used."""
    for c in square_scale_divisors(n):
        m = n // (c * c)
        for y0 in divisors(m):
            x0 = m // y0
            if x0 <= y0 or gcd(x0, y0) != 1:
                continue
            if (c * (x0 - y0)) % 2:
                continue
            p1 = c * (x0 - y0) // 2
            q0 = c * (x0 + y0) // 2
            yield c, x0, y0, p1, q0


def corridor_data(m0: int, p1: int, gstar: int):
    g0 = gcd(m0, p1)
    c1 = (gstar > 0 and gstar % g0 == 0)
    c2 = (gstar > 0 and p1 % gstar == 0)
    if c1 and c2:
        mu = gstar // g0
        r1 = p1 // gstar
    else:
        mu = None
        r1 = None
    return g0, c1, c2, mu, r1


def shell_normal_form_holds(m0: int, p1: int, gstar: int, z: int) -> bool:
    lhs = gcd(m0 * z, p1) == gstar
    g0, c1, c2, mu, r1 = corridor_data(m0, p1, gstar)
    rhs = False
    if c1 and c2:
        assert mu is not None and r1 is not None
        rhs = (z % mu == 0 and gcd(z // mu, r1) == 1)
    return lhs == rhs


def theorem_regression():
    cases = 0
    for m0 in range(1, 41):
        for p1 in range(1, 41):
            for gstar in range(1, p1 + 2):
                for z in range(1, 81):
                    if not shell_normal_form_holds(m0, p1, gstar, z):
                        raise AssertionError((m0, p1, gstar, z))
                    cases += 1
    return cases


def enumerate_core(u: int, c2: int, c3: int):
    """Exact replay of the R14 n2=2,n3=1,u0=1 over-approximation.
    The source Smith gcds gcd(b2,C2)=gcd(b3,C3)=1 are necessary and are
    applied before CF. All z|gcd(b2,b3) are retained, exactly matching R14.
    """
    cnt = Counter()
    master_integral_rows = []
    for b2 in range(1, 10):
        if gcd(b2, c2) != 1:
            continue
        for b3 in range(1, 10):
            if gcd(b3, c3) != 1:
                continue
            for z in divisors(gcd(b2, b3)):
                a = b2 // z
                w = b3 // z
                p2 = w * c2
                p3 = a * c3
                n = p2 * p2 + p3 * p3
                for c, x0, y0, p1, q0 in cf_factorizations(n):
                    cnt['CF'] += 1
                    if gcd(gcd(gcd(p1, p2), p3), q0) != 1:
                        continue
                    cnt['PRIMITIVE'] += 1
                    # This chamber has g=0,k=1,m2=m3=1, hence G=1,K=10,X=Y=10.
                    D = 10 * p1 - q0
                    t3 = q0 - p3
                    if D <= 0 or t3 <= 0:
                        continue
                    cnt['D_RATIO'] += 1
                    if (z * w * t3) % 10 != 0:
                        continue
                    cnt['TAIL'] += 1
                    omega = w * t3 - a * 10 * (p2 - q0)
                    nmaster = a * w * 100 * D
                    if omega <= 0 or nmaster % omega != 0:
                        cnt['MASTER_NONINTEGER_ROWS'] += 1
                        continue
                    gstar = nmaster // omega
                    if gstar <= 0:
                        cnt['MASTER_NONINTEGER_ROWS'] += 1
                        continue
                    cnt['MASTER_INTEGER_ROWS'] += 1
                    m0 = a * w
                    g0, g0_div, g_div_p1, mu, r1 = corridor_data(m0, p1, gstar)
                    if g0_div and g_div_p1:
                        cnt['CORRIDOR_PASS_ROWS'] += 1
                    else:
                        cnt['CORRIDOR_FAIL_ROWS'] += 1
                    master_integral_rows.append({
                        'U': u, 'U0': 1, 'MR': c2, 'NR': c3, 'N2': 2, 'N3': 1,
                        'C2': c2, 'C3': c3, 'b2': b2, 'b3': b3, 'z_R14': z,
                        'A': a, 'W': w, 'c': c, 'X0': x0, 'Y0': y0,
                        'P1': p1, 'P2': p2, 'P3': p3, 'Q0': q0,
                        'D': D, 'T3': t3, 'Omega': omega, 'Nmaster': nmaster,
                        'G1_STAR': gstar, 'M0': m0, 'G0': g0,
                        'G0_DIVIDES_G1_STAR': int(g0_div),
                        'G1_STAR_DIVIDES_P1': int(g_div_p1),
                        'MU': '' if mu is None else mu,
                        'R1_RESIDUAL': '' if r1 is None else r1,
                        'CORRIDOR_STATUS': 'PASS' if (g0_div and g_div_p1) else (
                            'FAIL_G0_DIVIDES_G1_STAR' if not g0_div else 'FAIL_G1_STAR_DIVIDES_P1'
                        ),
                    })
    if cnt['CF'] == 0:
        first = 'FAIL_CF'
    elif cnt['PRIMITIVE'] == 0:
        first = 'FAIL_PRIMITIVE'
    elif cnt['D_RATIO'] == 0:
        first = 'FAIL_D_RATIO'
    elif cnt['TAIL'] == 0:
        first = 'FAIL_TAIL'
    elif cnt['MASTER_INTEGER_ROWS'] == 0:
        first = 'FAIL_MASTER_NONINTEGER'
    elif cnt['CORRIDOR_PASS_ROWS'] == 0:
        first = 'FAIL_G1_CORRIDOR'
    else:
        first = 'POST_CORRIDOR'
    return cnt, master_integral_rows, first


def prescribed_core_ranges(u: int):
    # u*C2 has exactly 2 digits, u*C3 exactly 1 digit.
    return (
        range(ceildiv(10, u), 99 // u + 1),
        range(ceildiv(1, u), 9 // u + 1),
    )


def enumerate_chamber(us):
    registry = []
    masters = []
    by_u = defaultdict(Counter)
    for u in us:
        r2, r3 = prescribed_core_ranges(u)
        for c2 in r2:
            for c3 in r3:
                cnt, rows, first = enumerate_core(u, c2, c3)
                by_u[u][first] += 1
                masters.extend(rows)
                registry.append({
                    'U': u, 'U0': 1, 'MR': c2, 'NR': c3, 'N2': 2, 'N3': 1,
                    'C2': c2, 'C3': c3,
                    'CF_FACTOR_ROWS': cnt['CF'],
                    'PRIMITIVE_PASS_ROWS': cnt['PRIMITIVE'],
                    'D_T3_PASS_ROWS': cnt['D_RATIO'],
                    'TAIL_PASS_ROWS': cnt['TAIL'],
                    'MASTER_INTEGER_ROWS': cnt['MASTER_INTEGER_ROWS'],
                    'CORRIDOR_PASS_ROWS': cnt['CORRIDOR_PASS_ROWS'],
                    'FIRST_FAILURE': first,
                    'FULL_SOURCE_LIFT_COUNT': 0 if first != 'POST_CORRIDOR' else '',
                    'CERTIFICATION': 'EXACT_EMPTY_BY_NECESSARY_GATE' if first != 'POST_CORRIDOR' else 'REQUIRES_POST_CORRIDOR_RECONSTRUCTION',
                })
    return registry, masters, by_u


def write_csv(path: Path, rows, fieldnames):
    with path.open('w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        w.writeheader()
        for row in rows:
            w.writerow(row)


def targeted_construct_search():
    """Discovery-only canonical finite-shape search. It is not used as a theorem.
    Scope: u0=U=1, 10<=C2<=120, 1<=C3<=40, all exponent charts,
    A,W<=12, exact CF factorizations. Stops at corridor because none pass.
    """
    counts = Counter()
    cf_factor_rows = 0
    for c2 in range(10, 121):
        n2 = digits(c2)
        for c3 in range(1, 41):
            n3 = digits(c3)
            for ge in range(0, n2 - 1):
                for ke in range(1, n2 - ge):
                    m2 = n2 - ge - ke
                    m3 = n3 + ge
                    if m2 < 1:
                        continue
                    G = 10 ** ge
                    K = 10 ** ke
                    X = 10 ** m2
                    Y = 10 ** n3
                    for a in range(1, min(12, 10 ** m2 - 1) + 1):
                        if gcd(a, c2) != 1:
                            continue
                        for w in range(1, min(12, 10 ** m3 - 1) + 1):
                            if gcd(w, c3) != 1 or gcd(a, w) != 1:
                                continue
                            p2 = w * c2
                            p3 = a * c3
                            n = p2 * p2 + p3 * p3
                            for c, x0, y0, p1, q0 in cf_factorizations(n):
                                cf_factor_rows += 1
                                if gcd(gcd(gcd(p1, p2), p3), q0) != 1:
                                    continue
                                D = K * p1 - q0
                                t3 = q0 - p3
                                if D <= 0 or t3 <= 0:
                                    continue
                                omega = w * t3 - a * Y * (p2 - G * q0)
                                nmaster = a * w * X * Y * G * D
                                if omega <= 0 or nmaster % omega != 0:
                                    counts['MASTER_NONINTEGER'] += 1
                                    continue
                                gstar = nmaster // omega
                                if gstar <= 0:
                                    counts['MASTER_NONINTEGER'] += 1
                                    continue
                                m0 = a * w
                                g0, c1, c2ok, _, _ = corridor_data(m0, p1, gstar)
                                if not (c1 and c2ok):
                                    counts['CORRIDOR_FAIL'] += 1
                                    continue
                                counts['CORRIDOR_PASS'] += 1
    return cf_factor_rows, counts


def sha256(path: Path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def main():
    theorem_cases = theorem_regression()
    reg123, masters123, by_u123 = enumerate_chamber(range(1, 4))
    reg19, masters19, by_u19 = enumerate_chamber(range(1, 10))

    assert len(reg123) == 1080
    assert len(reg19) == 1191
    assert len(masters123) == 132
    assert all(r['CORRIDOR_STATUS'] == 'FAIL_G1_STAR_DIVIDES_P1' for r in masters123)
    assert sum(1 for r in masters123 if r['G1_STAR'] > r['P1']) == 126
    assert sum(1 for r in masters123 if r['G1_STAR'] <= r['P1']) == 6
    assert sum(1 for r in reg123 if r['FIRST_FAILURE'] == 'FAIL_PRIMITIVE') == 120
    assert sum(1 for r in reg123 if r['FIRST_FAILURE'] == 'FAIL_TAIL') == 378
    assert sum(1 for r in reg123 if r['FIRST_FAILURE'] == 'FAIL_MASTER_NONINTEGER') == 522
    assert sum(1 for r in reg123 if r['FIRST_FAILURE'] == 'FAIL_G1_CORRIDOR') == 60
    assert all(r['FIRST_FAILURE'] != 'POST_CORRIDOR' for r in reg19)

    # R14 assignment totals recovered exactly.
    tail_total = 0
    nonint_total = 0
    for row in reg123:
        # row doesn't store noninteger row count; recompute cheaply per core for exact log.
        cnt, _, _ = enumerate_core(row['U'], row['C2'], row['C3'])
        tail_total += cnt['TAIL']
        nonint_total += cnt['MASTER_NONINTEGER_ROWS']
    assert tail_total == 18581
    assert nonint_total == 18449

    cf_target, construct_counts = targeted_construct_search()
    assert construct_counts['CORRIDOR_PASS'] == 0

    # 1. Master corridor exact rows (R14 132)
    corridor_fields = list(masters123[0].keys())
    write_csv(ROOT / '105_R15_Master_G1_Corridor.csv', masters123, corridor_fields)
    write_csv(ROOT / '105_R15_R14_132_Reclassification.csv', masters123, corridor_fields)

    # 2. Algebraic theorem registry
    shell_rows = [
        {
            'THEOREM_ID': 'R15-GCD-EXISTENCE',
            'STATEMENT': 'exists z>0: gcd(M0*z,P1)=g iff gcd(M0,P1)|g|P1',
            'FORCED_SCALE': 'mu=g/g0',
            'RESIDUAL_FACTOR': 'R1=P1/g',
            'NORMAL_FORM': 'z=mu*q and gcd(q,R1)=1',
            'STATUS': 'PROVED_ALGEBRAICALLY',
            'REGRESSION_CASES': theorem_cases,
        },
        {
            'THEOREM_ID': 'R15-TAIL-FUSION',
            'STATEMENT': 'lambda_z|z with z=mu*q iff tau|q; tau=lambda_z/gcd(lambda_z,mu)',
            'FORCED_SCALE': 'Lambda=lcm(mu,lambda_z)=mu*tau',
            'RESIDUAL_FACTOR': 'requires gcd(tau,R1)=1',
            'NORMAL_FORM': 'z=Lambda*r and gcd(r,R1)=1',
            'STATUS': 'PROVED_ALGEBRAICALLY',
            'REGRESSION_CASES': '',
        },
        {
            'THEOREM_ID': 'R15-SMITH-FUSION',
            'STATEMENT': 'raw Smith+tail+g1 shell iff z=Lambda*q and gcd(q,F)=1 under shape compatibility',
            'FORCED_SCALE': 'Lambda=lcm(mu,lambda_z)',
            'RESIDUAL_FACTOR': 'F=rad((P1/g)*C2*C3)',
            'NORMAL_FORM': 'z=Lambda*q; gcd(q,F)=1',
            'STATUS': 'PROVED_ALGEBRAICALLY',
            'REGRESSION_CASES': '',
        },
    ]
    write_csv(ROOT / '105_R15_Z_Shell_Normalization.csv', shell_rows,
              ['THEOREM_ID','STATEMENT','FORCED_SCALE','RESIDUAL_FACTOR','NORMAL_FORM','STATUS','REGRESSION_CASES'])

    lambda_rows = [
        {
            'SCOPE': 'GENERAL_FIXED_FINITE_SHAPE',
            'MU': 'g1star/gcd(u0*A*W,P1)',
            'LAMBDA_Z': 'Y/gcd(Y,W*T3)',
            'TAU': 'LAMBDA_Z/gcd(LAMBDA_Z,MU)',
            'CANONICAL_LAMBDA': 'lcm(MU,LAMBDA_Z)=MU*TAU',
            'CANONICAL_FORBIDDEN_FACTOR': 'rad((P1/g1star)*C2*C3)',
            'TAIL_G1_COLLISION': 'gcd(TAU,P1/g1star)>1',
            'TAIL_SMITH_COLLISION': 'gcd(CANONICAL_LAMBDA,C2*C3)>1',
            'STATUS': 'PROVED_FORMULA_PACKAGE',
        },
        {
            'SCOPE': 'U1_TO_U9_CERTIFIED_CHAMBER',
            'MU': '', 'LAMBDA_Z': '', 'TAU': '', 'CANONICAL_LAMBDA': '',
            'CANONICAL_FORBIDDEN_FACTOR': '', 'TAIL_G1_COLLISION': '', 'TAIL_SMITH_COLLISION': '',
            'STATUS': 'NO_POST_CORRIDOR_SHAPES__LAMBDA_NOT_ACTIVATED',
        },
    ]
    write_csv(ROOT / '105_R15_Lambda_F_Registry.csv', lambda_rows,
              ['SCOPE','MU','LAMBDA_Z','TAU','CANONICAL_LAMBDA','CANONICAL_FORBIDDEN_FACTOR','TAIL_G1_COLLISION','TAIL_SMITH_COLLISION','STATUS'])

    q_rows = [
        {
            'SCOPE': 'GENERAL_FIXED_FINITE_SHAPE',
            'Z_LOWER': 'Z_-', 'Z_UPPER': 'Z_+',
            'Q_LOWER': 'ceil(Z_-/Lambda)', 'Q_UPPER': 'floor(Z_+/Lambda)',
            'SUCCESSOR': 'min q>=Q_LOWER with gcd(q,F)=1',
            'NONEMPTY_CRITERION': 'q_min<=Q_UPPER',
            'Z_MIN': 'Lambda*q_min',
            'STATUS': 'CANONICAL_TRANSVERSE_Z_SUCCESSOR_THEOREM_PROVED',
        },
        {
            'SCOPE': 'U1_TO_U9_CERTIFIED_CHAMBER',
            'Z_LOWER': '', 'Z_UPPER': '', 'Q_LOWER': '', 'Q_UPPER': '', 'SUCCESSOR': '',
            'NONEMPTY_CRITERION': 'NOT_REACHED', 'Z_MIN': '',
            'STATUS': '0_POST_CORRIDOR_ROWS',
        },
    ]
    write_csv(ROOT / '105_R15_Q_Successor_Registry.csv', q_rows,
              ['SCOPE','Z_LOWER','Z_UPPER','Q_LOWER','Q_UPPER','SUCCESSOR','NONEMPTY_CRITERION','Z_MIN','STATUS'])

    # 3. Core certification registries
    core_fields = list(reg123[0].keys())
    write_csv(ROOT / '105_R15_U123_Exact_Certification.csv', reg123, core_fields)
    write_csv(ROOT / '105_R15_U1_U9_Exact_Certification.csv', reg19, core_fields)

    # 4. Dominant failure registry
    dom_rows = []
    for label, reg, byu in [('U1_U3', reg123, by_u123), ('U1_U9', reg19, by_u19)]:
        total = len(reg)
        agg = Counter(r['FIRST_FAILURE'] for r in reg)
        for gate in ['FAIL_CF','FAIL_PRIMITIVE','FAIL_D_RATIO','FAIL_TAIL','FAIL_MASTER_NONINTEGER','FAIL_G1_CORRIDOR','POST_CORRIDOR']:
            dom_rows.append({'SCOPE': label, 'U': 'ALL', 'TOTAL_CORES': total, 'FAILURE_GATE': gate, 'COUNT': agg[gate], 'EVIDENCE_CLASS': 'EXACT_COMPLETE_CHAMBER'})
        for u, ctr in sorted(byu.items()):
            utotal = sum(ctr.values())
            for gate, count in sorted(ctr.items()):
                dom_rows.append({'SCOPE': label, 'U': u, 'TOTAL_CORES': utotal, 'FAILURE_GATE': gate, 'COUNT': count, 'EVIDENCE_CLASS': 'EXACT_COMPLETE_CHAMBER'})
    write_csv(ROOT / '105_R15_Dominant_Failure_Registry.csv', dom_rows,
              ['SCOPE','U','TOTAL_CORES','FAILURE_GATE','COUNT','EVIDENCE_CLASS'])

    # 5. Construct / lift / first-failure registries
    construct_rows = [{
        'SEARCH_ID': 'R15_TARGETED_CANONICAL_SHAPE_DISCOVERY',
        'SCOPE': 'u0=U=1;10<=C2<=120;1<=C3<=40;all exponent charts;A,W<=12;exact CF',
        'CF_FACTOR_ROWS': cf_target,
        'MASTER_NONINTEGER': construct_counts['MASTER_NONINTEGER'],
        'CORRIDOR_FAIL': construct_counts['CORRIDOR_FAIL'],
        'CORRIDOR_PASS': construct_counts['CORRIDOR_PASS'],
        'Z_SELECTOR_HITS': 0,
        'FULL_LIFT_HITS': 0,
        'EVIDENCE_CLASS': 'DISCOVERY_ONLY__NO_GLOBAL_INFERENCE',
    }]
    write_csv(ROOT / '105_R15_Construct_Hits.csv', construct_rows,
              ['SEARCH_ID','SCOPE','CF_FACTOR_ROWS','MASTER_NONINTEGER','CORRIDOR_FAIL','CORRIDOR_PASS','Z_SELECTOR_HITS','FULL_LIFT_HITS','EVIDENCE_CLASS'])

    write_csv(ROOT / '105_R15_Full_Lift_Witnesses.csv', [],
              ['WITNESS_ID','RADIAL_CORE','FINITE_SHAPE','Z','Q','SMITH_RECONSTRUCTION','PSDG_RECONSTRUCTION','FULL_POST_PSDG_REGRESSION','PLAIN_U','DOWNSTREAM_STATUS'])

    ff_rows = [
        {'SCOPE':'R14_INPUT','OLD_GATE':'POST_PSDG_FINITE_SHAPE_MASTER_G1_TAIL_GCD_Z_SELECTOR_NONEMPTINESS','NEW_GATE':'MASTER_G1_DIVISOR_CORRIDOR_ON_GENERAL_POSITIVE_FINITE_SHAPES','COUNT_OR_STATUS':'R15 NORMALIZED','THEOREM_OR_CERTIFICATE':'GCD shell existence iff g0|g1star|P1'},
        {'SCOPE':'U1_U3','OLD_GATE':'R14 over-approx no-hit','NEW_GATE':'EXACTLY_EMPTY','COUNT_OR_STATUS':'1080/1080 certified empty','THEOREM_OR_CERTIFICATE':'105_R15_U123_Exact_Certification.csv'},
        {'SCOPE':'U1_U9','OLD_GATE':'optional extension','NEW_GATE':'EXACTLY_EMPTY','COUNT_OR_STATUS':'1191/1191 prescribed cores certified empty','THEOREM_OR_CERTIFICATE':'105_R15_U1_U9_Exact_Certification.csv'},
        {'SCOPE':'GENERAL','OLD_GATE':'raw five-condition z selector','NEW_GATE':'corridor -> Lambda/F selector if corridor passes','COUNT_OR_STATUS':'GLOBAL OPEN BEFORE q activation','THEOREM_OR_CERTIFICATE':'MASTER_TAIL_SMITH_Z_SHELL_FACTORIZATION_PROVED'},
    ]
    write_csv(ROOT / '105_R15_First_Failure_Registry.csv', ff_rows,
              ['SCOPE','OLD_GATE','NEW_GATE','COUNT_OR_STATUS','THEOREM_OR_CERTIFICATE'])

    # Execution log
    agg123 = Counter(r['FIRST_FAILURE'] for r in reg123)
    agg19 = Counter(r['FIRST_FAILURE'] for r in reg19)
    with (ROOT / '105_R15_execution.log').open('w', encoding='utf-8') as f:
        f.write('105-R15 exact phase-offensive execution\n')
        f.write(f'GCD_NORMAL_FORM_REGRESSION_CASES={theorem_cases}\n')
        f.write('R14_REPLAY_TAIL_SURVIVING_ASSIGNMENTS=18581\n')
        f.write('R14_REPLAY_G1STAR_NONINTEGRAL=18449\n')
        f.write('R14_REPLAY_MASTER_INTEGRAL=132\n')
        f.write('R14_MASTER_INTEGRAL_132_FAIL_G1STAR_DIVIDES_P1=132\n')
        f.write('R14_MASTER_INTEGRAL_132_G1STAR_GT_P1=126\n')
        f.write('R14_MASTER_INTEGRAL_132_G1STAR_LE_P1_BUT_NONDIVISOR=6\n')
        f.write(f'U123_CORES={len(reg123)} FIRST_FAILURE={dict(sorted(agg123.items()))}\n')
        f.write(f'U1_U9_CORES={len(reg19)} FIRST_FAILURE={dict(sorted(agg19.items()))}\n')
        f.write('U123_POST_CORRIDOR=0\nU1_U9_POST_CORRIDOR=0\n')
        f.write(f'TARGETED_CONSTRUCT_CF_FACTOR_ROWS={cf_target}\n')
        f.write(f'TARGETED_CONSTRUCT_COUNTS={dict(sorted(construct_counts.items()))}\n')
        f.write('ALL_ASSERTIONS=PASS\n')

    # Manifest (main markdown will be added later by report builder, then manifest refreshed externally)
    generated = [
        ROOT / '105_R15_Master_G1_Corridor.csv', ROOT / '105_R15_Z_Shell_Normalization.csv',
        ROOT / '105_R15_Lambda_F_Registry.csv', ROOT / '105_R15_Q_Successor_Registry.csv',
        ROOT / '105_R15_R14_132_Reclassification.csv', ROOT / '105_R15_U123_Exact_Certification.csv',
        ROOT / '105_R15_U1_U9_Exact_Certification.csv', ROOT / '105_R15_Dominant_Failure_Registry.csv',
        ROOT / '105_R15_Construct_Hits.csv', ROOT / '105_R15_Full_Lift_Witnesses.csv',
        ROOT / '105_R15_First_Failure_Registry.csv', ROOT / '105_R15_execution.log', Path(__file__),
    ]
    manifest_rows=[]
    for p in generated:
        manifest_rows.append({'file': str(p.relative_to(ROOT)), 'bytes': p.stat().st_size, 'sha256': sha256(p)})
    write_csv(ROOT / '105_R15_SHA256_Manifest.csv', manifest_rows, ['file','bytes','sha256'])

    print('R15 exact phase offensive: PASS')
    print('U1-U3:', dict(sorted(agg123.items())))
    print('U1-U9:', dict(sorted(agg19.items())))
    print('Targeted construct:', cf_target, dict(sorted(construct_counts.items())))


if __name__ == '__main__':
    main()
