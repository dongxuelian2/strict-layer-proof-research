# 105-R31 — Minimal-q Descent

**Status:** exact prime-stripping theorem proved; descent-to-one not proved.

## 1. Setup

Fix a legal post-support architecture \(\mathfrak a\) and a source candidate \(U\in\mathcal U_0\). Let

\[
M:=FU,
\]

and, if nonempty, define

\[
q_{\min}=\min\{q\in[Q_-,Q_+]\cap\mathbb Z_{>0}:(q,M)=1\}.
\]

Then \(N_{30}>0\) exactly when this minimum exists for at least one \(U\).

## 2. Prime-stripping lower-edge theorem

Let \(p\mid q_{\min}\). Since \((q_{\min},M)=1\), also

\[
(q_{\min}/p,M)=1.
\]

If \(q_{\min}/p\ge Q_-\), then

\[
Q_-\le q_{\min}/p<q_{\min}\le Q_+,
\]

contradicting minimality. Therefore, for **every** prime divisor \(p\mid q_{\min}\),

\[
\boxed{q_{\min}/p<Q_-.}
\tag{R31-STRIP}
\]

In the original scale \(Z=\Lambda q\),

\[
\boxed{Z/p<Z_-}
\]

because \(Q_-\) is the first integer q whose scale can reach the lower digit boundary. Thus every failed prime stripping exits only through the lower edge, never the upper edge.

Let \(p_{\min}=p_{\min}(q_{\min})\). Then

\[
\boxed{Q_-\le q_{\min}<p_{\min}Q_-.}
\tag{R31-EDGE}
\]

This is the exact minimal-q exceptional strip requested in R31.

## 3. Prime-or-quadratic-strip theorem

If \(q_{\min}\) is composite, then \(q_{\min}\ge p_{\min}^2\). Combining with (R31-EDGE),

\[
p_{\min}^2\le q_{\min}<p_{\min}Q_-,
\]

so

\[
p_{\min}<Q_-.
\]

Consequently

\[
\boxed{
q_{\min}\text{ is prime, or }q_{\min}<Q_-^2.
}
\tag{R31-PQ}
\]

This is a genuine descent compression. It does **not** say q is a prime power, and it does **not** imply q=1.

Examples obtained by exact enumeration of the necessary composite strip:

- \(Q_-=1\): \(q_{\min}=1\) automatically if the source set is nonempty;
- \(Q_-=2\): no composite satisfies the strip, hence \(q_{\min}\) must be prime;
- \(Q_-=3\): the only composite possibility is \(4\);
- \(Q_-=4\): composite possibilities are \(4,6,9\);
- \(Q_-=5\): composite possibilities are \(6,8,9\).

The full exact table for \(Q_-=1,\ldots,10\) is `105-R31-minimal-q-registry.csv`.

## 4. Unit / prime / finite-composite trichotomy

For one fixed U, existence of any compatible q is equivalent to one of:

1. **Unit branch:** \(Q_-=1\), in which case q=1 is automatically compatible;
2. **Prime branch:** a prime \(p\in[Q_-,Q_+]\) with \(p\nmid FU\);
3. **Finite composite strip:** a composite
   \[
   q\in[Q_-,\min(Q_+,Q_-^2-1)]
   \]
   with \((q,FU)=1\).

Proof: choose the minimal compatible q. If it is composite, (R31-PQ) applies; if prime, branch 2; if \(Q_-=1\), q=1 precedes everything. The converse directions are immediate.

Thus all composite q at or above \(Q_-^2\) are mathematically redundant for **existence testing**: if one were compatible, a smaller compatible q of branch 1, 2, or 3 would already exist.

## 5. Universal multiplicative q-window bound

From the decimal-window geometry,

\[
\boxed{Q_+<10Q_-}
\]

whenever the q-window is nonempty. Hence \(Q_+\le10Q_--1\).

This gives a universal multiplicative constant \(C=10\), but not the stronger \(C=2\) or \(3\) contemplated in the attack prompt.

## 6. Why descent-to-one is not proved

Prime stripping proves only that every proper prime quotient of a minimal q falls below the lower edge. It gives no legal operation that moves the lower edge itself. A prime minimal q can therefore survive the stripping argument untouched, and a composite minimal q can survive inside the explicit quadratic strip.

Accordingly R31 does **not** sign

```text
MINIMAL_Q_DESCENT_TO_ONE=YES
```

and it also does not sign it false by a genuine legal counterexample, because no genuine \(N_{30}>0\) architecture was found. The exact status is

```text
MINIMAL_Q_DESCENT_TO_ONE=NOT_PROVED
PRIME_STRIPPING_LOWER_EDGE_RIGIDITY=PROVED
MINIMAL_Q_PRIME_OR_QUADRATIC_STRIP=PROVED
Q_WINDOW_MULTIPLICATIVE_BOUND_LT_10=PROVED
```

The remaining nonunit difficulty is the prime branch plus the finite composite strip, evaluated with the actual architecture-specific support \(FU\).
