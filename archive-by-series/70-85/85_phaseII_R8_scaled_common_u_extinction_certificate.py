from math import gcd


def ceil_div(a,b):
    return (a+b-1)//b


def r7_deepest_control():
    g=5; G=10**g; k=3; K=10**k; u=11; q=9091; A=23; H=G//2
    B=2*G+q
    r0=1083
    c=2844241425759278313791310157183552723
    z=209677679429991676302394167849
    n=546955596371187859561484885716881905
    lam=1093911419823302541803955206926647590467
    C1=(B*z+A*lam)//(2*K)
    C2=A*c+H*lam
    w=G*H*z-u*A*c
    T=G*z+u*lam
    d2=u*c+G*w
    assert lam == r0*z + 2*K*n
    assert H*H*C1*C1 + w*w == T*d2
    assert gcd(c*z*lam,10)==1
    Ulo=max(ceil_div(G*G*K,10*C2),ceil_div(G,10*c),1)
    Uhi=min((G*G*K-1)//C2,(G-1)//c)
    assert (Ulo,Uhi)==(1,0)
    assert c>G and C2>G*G*K
    return {
        'name':'R7 deepest exact-root/source survivor',
        'Ulo':Ulo,'Uhi':Uhi,'c_gt_G':c>G,'C2_gt_G2K':C2>G*G*K,
        'root':'PASS','lattice':'PASS'
    }


def plcf_control():
    # t=0 member of the old 85 PLCF family.
    g=5; G=10**g; K=10; u=11; q=(G+1)//u; A=2*u+1; B=2*G+q; H=G//2
    r0=(-pow(A,-1,2*K)*B)%(2*K)
    c=z=1; lam=3
    assert r0==3
    n=(lam-r0*z)//(2*K)
    assert n==0
    C1=(B*z+A*lam)//(2*K)
    C2=A*c+H*lam
    w=G*H*z-u*A*c
    T=G*z+u*lam
    d2=u*c+G*w
    root_residual=H*H*C1*C1+w*w-T*d2
    U=G-1
    X=U*c; Z=U*z; N=U*n; L=U*lam; Y=U*C2
    assert gcd(U,u*G*H)==1
    assert G//10 <= X < G
    assert G*G*K//10 <= Y < G*G*K
    assert gcd(X,Z,N)==U
    assert L==r0*Z+2*K*N
    assert Y==A*X+H*L
    assert root_residual != 0
    return {
        'name':'PLCF t=0 double-box/root-independent control',
        'U':U,'X':X,'Y':Y,'N':N,
        'X_box':'PASS','Y_box':'PASS','content':'PASS','lattice':'PASS',
        'gcd(U,uGH)':gcd(U,u*G*H),'full_root':'FAIL',
        'root_residual':root_residual
    }


def scaled_equivalence_regression():
    # Scale the R7 deepest primitive root/source survivor by a harmless test scale.
    # This is NOT a genuine common-U realization because the decimal boxes fail;
    # it only checks algebraic scaling identities exactly.
    g=5; G=10**g; K=1000; u=11; q=9091; A=23; B=2*G+q; H=G//2
    r0=1083
    c=2844241425759278313791310157183552723
    z=209677679429991676302394167849
    n=546955596371187859561484885716881905
    lam=1093911419823302541803955206926647590467
    U=7
    X=U*c; Z=U*z; N=U*n; L=U*lam
    P=(B*Z+A*L)//(2*K)
    Y=A*X+H*L
    W=G*H*Z-u*A*X
    S=G*Z+u*L
    D2=u*X+G*W
    assert L==r0*Z+2*K*N
    assert 2*K*P==B*Z+A*L
    assert H*H*P*P+W*W==S*D2
    assert gcd(X,Z,N)==U
    assert gcd(X,Z,N,L,Y)==U
    # Deep section scales by U but gives no new independent information.
    Ms=u*A*A*X + u*(A*G-1)*L - G*Z
    assert Ms%(U*H*H)==0
    return {'scaled_exact_equivalence':'PASS','exact_content_all5':gcd(X,Z,N,L,Y)}


if __name__=='__main__':
    print('R8 SCALED COMMON-U CERTIFICATE')
    for block in (r7_deepest_control(), plcf_control(), scaled_equivalence_regression()):
        for k,v in block.items():
            print(f'{k}={v}')
        print('---')
