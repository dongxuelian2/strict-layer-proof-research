# Fourth 85 · R6 — Gaussian Architecture Autopsy

## Central theorem

The standard affine conics

\[
x^2-A_2v^2=T_4
\]

and

\[
u^2+w^2=T_4
\]

are not isomorphic over \(F=\mathbf Q(G)\).

Their boundary degree-two schemes have quadratic algebras

\[
F(\sqrt{A_2})
\]

and

\[
F(i).
\]

An affine isomorphism would force these algebras to agree, hence

\[
-A_2\in F^{\times2}.
\]

But \(A_2\) is a nonconstant squarefree sextic. Contradiction.

Therefore any base-field projective conic equivalence must use a moving affine denominator.

## Consequences

- no fixed affine Gaussian source lattice;
- no intrinsic Gaussian SNF/circle-radius collision;
- no source-canonical integral Gaussian phase;
- no source-canonical finite split-prime orientation;
- no rigorous representation-count-to-source bridge.

The norm-one integralization torsor is

\[
\mathcal T_{\rm int}(z_{\rm src})
=
\{\varepsilon\in\mathbf Q(i)^1:
\varepsilon z_{\rm src}\in\mathbf Z[i]\}.
\]

It intervenes before a concrete integral Gaussian representation is selected.

## Verdict

```text
GAUSSIAN_SPLIT_SOURCE_ARCHITECTURE = DEAD
Q1_GAUSSIAN_PRIME_HUNTING_CONTINUE = NO
```

The remaining q=1 negative problem must return to a source-native formulation.
