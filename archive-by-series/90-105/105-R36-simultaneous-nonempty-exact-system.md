# 105-R36 — Simultaneous-Nonempty Exact System

## 1. Frozen terminal predicate
For a fixed legal post-support architecture \(\mathfrak a\), R35 freezes
\[
\exists U\in\mathcal U_0(\mathfrak a),\qquad
\exists q\in[Q_-,Q_*]\cap\mathbf Z_{>0},\qquad(q,FU)=1,
\]
with
\[
Q_*=\min(Q_+,Q_{\rm master}),\qquad
Q_{\rm master}=\left\lfloor\frac{Q_0-1}{b_1D}\right\rfloor,
\]
and
\[
Q_{\rm master}<Q_-\iff Q_-b_1D\ge Q_0.
\]

## 2. R36 correction: simultaneous nonemptiness has two denominator gates
The denominator interval is nonempty iff
\[
Q_-\le Q_+\quad\text{and}\quad Q_-\le Q_{\rm master}.
\]
By the frozen CUT theorem, the second condition is exactly
\[
Q_-b_1D<Q_0.
\]
Therefore the exact simultaneous source/denominator locus is
\[
\boxed{\mathscr T=\{\mathfrak a:\mathcal U_0\ne\varnothing,\ Q_-\le Q_+,\ Q_-b_1D<Q_0\}.}
\]
The prompt's raw \(\mathscr S_1,\mathscr S_+\) omit \(Q_-\le Q_+\). They are exact only under an additional convention that the ambient word “legal architecture” already includes raw TC3 window nonemptiness. The frozen post-support architecture does not include that gate, so R36 uses the corrected loci below.

Define
\[
\mathscr T_1=\{\mathfrak a:\ Q_-=1,\ \mathcal U_0\ne\varnothing,\ Q_+\ge1\},
\]
and
\[
\mathscr T_+=\{\mathfrak a:\ Q_-\ge2,\ \mathcal U_0\ne\varnothing,\ Q_-\le Q_+,\ Q_-b_1D<Q_0\}.
\]
On \(Q_-=1\), R33/R35 give \(0<b_1D<Q_0\), so the MASTER inequality is automatic.

### Partition theorem
\[
\boxed{\mathscr T=\mathscr T_1\sqcup\mathscr T_+.}
\]
Proof: every positive integer \(Q_-\) is uniquely either 1 or at least 2; all remaining defining conditions are inherited unchanged. Disjointness follows from the mutually exclusive conditions \(Q_-=1\) and \(Q_-\ge2\). Exhaustiveness follows by the same dichotomy.

## 3. Relation to TP
A TP-positive architecture lies in \(\mathscr T\). Conversely \(\mathfrak a\in\mathscr T\) only guarantees a nonempty rectangle; one must still test \((q,FU)=1\). In the unit branch, \(q=1\) is present and automatically coprime, hence
\[
\boxed{\mathfrak a\in\mathscr T_1\Longrightarrow TP=PASS.}
\]
For \(\mathscr T_+\), exact finite gcd enumeration is still required.

## 4. R36 status
No genuine point of \(\mathscr T_1\) or \(\mathscr T_+\) was found in the frozen replay or the new bounded source-first shell. No global theorem that either locus is empty was proved.
