# 105-R32 — Prime-Branch Immediate Derivation

The unit branch was **not** globally proved extinct in R32, so the campaign rule
does not authorize pretending that the prime branch is now the unique frontier.
Nevertheless the exact specialization is pushed as far as the unit analysis
allows.

## 1. Prescribed-q digit determinization

For any prescribed residual integer \(q\ge1\),

\[
z=\Lambda q.
\]

Therefore denominator digits force

\[
\boxed{
m_2=\operatorname{dig}(A\Lambda q),\qquad
m_3=\operatorname{dig}(W\Lambda q).
}
\]

The frozen exponent identities then force

\[
\boxed{
g=m_3-n_3,\qquad
k=n_2-m_2-g.
}
\]

Thus prescribed q, including prime q, deletes the same independent exponent
simplex that q=1 deletes.

```text
PRESCRIBED_Q_DIGIT_DETERMINIZATION_THEOREM=PROVED
```

## 2. Minimal prime branch

For minimal \(q=p\) prime, the inherited exact conditions are

\[
Q_-\le p\le Q_+,\qquad p\nmid FU,
\]

and R31 gives

\[
Q_+<10Q_-.
\]

No prime-distribution theorem is needed or used.

For a candidate source digit pair and packet/selectors, the exact order is now:

1. compute \(\Lambda(n_3)\);
2. choose/test prime p in the actual q-window;
3. recover \(m_2,m_3,g,k\) deterministically;
4. reject unless \(g\ge0,k\ge1\);
5. replay TC1/master;
6. replay source residue/completed-source;
7. test \(p\nmid FU\);
8. reconstruct Strict A1 if positive.

This is a strict reduction, not a global extinction theorem.

## 3. Bounded one-digit prime stress lane

For \(p\in\{2,3,5,7\}\), the same restricted lane used in the q1 search has
\(m_2=m_3=1\). Its TC1+sphere equation is independent of the one-digit q once
the recovered digit lengths are fixed. The 899,910 exact configurations contain
zero integer TC1-conic roots, hence zero prime survivors in that lane.

This result is recorded in `105-R32-prime-q-registry.csv` and is explicitly
bounded.

## 4. Honest prime verdict

```text
MINIMAL_PRIME_DENOMINATOR_EXTINCTION=NOT_PROVED
GENUINE_PRIME_Q_SURVIVOR_FOUND=NO
PRIME_BRANCH_EXACT_VARIABLE_REDUCTION=PROVED
PRIME_BRANCH_GLOBAL_EXISTENCE=UNDECIDED
```

Because q1 itself remains undecided, no claim is made that the remaining global
object has already collapsed to prime/composite only.
