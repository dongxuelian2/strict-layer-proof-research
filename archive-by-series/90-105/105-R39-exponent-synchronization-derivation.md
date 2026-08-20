# 105-R39 — Exponent Synchronization Derivation

## 1. Decimal collapse

From

\[
n_2=m_2+g+k,\qquad m_3=n_3+g,
\]

\[
XYGK=10^{m_2+n_3+g+k}=10^{n_2+n_3}.
\]

Therefore

\[
L_N=aXYGK=\boxed{a10^{n_2+n_3}}.
\]

Similarly

\[
YG=10^{m_3},\qquad XYG=10^{m_2+m_3}.
\]

## 2. Global sign theorem

Let \(z=\Lambda q\). Since \(\mu\mid\Lambda\), \(\mu\le z\). The denominator digit conditions imply

\[
Az<10^{m_2},\qquad Wz<10^{m_3},
\]

hence

\[
\mu A<10^{m_2},\qquad \mu W<10^{m_3}.
\]

Therefore

\[
\mu(W+A10^{m_3})
<
10^{m_3}+10^{m_2+m_3}.
\]

Because \(m_2\ge1\),

\[
10^{m_3}\le10^{m_2+m_3-1},
\]

so

\[
B_{\rm src}
<
\left(a+\frac{11}{10}\right)10^{m_2+m_3}.
\]

On the other hand \(k\ge1\) gives

\[
L_{\rm src}
=
a10^{m_2+m_3+k}
\ge
10a\,10^{m_2+m_3}.
\]

For every \(a\ge1\),

\[
a+\frac{11}{10}<10a.
\]

Thus

\[
\boxed{B_{\rm src}<L_{\rm src}},
\qquad
\boxed{\mathcal A_N<0}.
\]

Consequences:

```text
SOURCE_NATIVE_LINEAR_BRANCH_EXTINCTION=PROVED
SOURCE_NATIVE_ROOTS_IF_ANY_ARE_STRICTLY_NEGATIVE_QUADRATIC=YES
```

## 3. Information-gain audit

On exact incidence,

\[
B_{\rm src}Q_0-C_{\rm src}=L_{\rm src}P_1.
\]

Thus PINT, QINT and the full decimal divisibility are exact NTC1 restatements after exponent collapse.

```text
PINT_INFORMATION_GAIN=0
QINT_INFORMATION_GAIN=0
SOURCE_NATIVE_DECIMAL_DIVISIBILITY_INFORMATION_GAIN=0
```
