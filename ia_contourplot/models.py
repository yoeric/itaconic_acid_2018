def second_order_model(x, y, X, Y, coefs, f_v):

    ite = f_v["ITE"]
    cad = f_v["CAD"]
    aco = f_v["ACO"]
    pyc = f_v["PYC"]
    csc = f_v["CSC"]
    acdh = f_v["ACDH"]

    if x is "log_ITE" :
        ite = X
    if x is "log_CAD" :
        cad = X
    if x is "log_ACO" :
        aco = X
    if x is "log_PYC" :
        pyc = X
    if x is "log_CSC" :
        csc = X
    if x is "log_ACDH":
        acdh = X
    if y is "log_ITE" :
        ite = Y
    if y is "log_CAD" :
        cad = Y
    if y is "log_ACO" :
        aco = Y
    if y is "log_PYC" :
        pyc = Y
    if y is "log_CSC" :
        csc = Y
    if y is "log_ACDH":
        acdh = Y


    coD = {'ite'    : coefs['coef']['log_ITE'],
           'cad'    : coefs['coef']['log_CAD'],
           'aco'    : coefs['coef']['log_ACO'],
           'pyc'    : coefs['coef']['log_PYC'],
           'csc'    : coefs['coef']['log_CSC'],
           'acdh'   : coefs['coef']['log_ACDH'],
           's_ite'  : coefs['coef']['np.power(log_ITE, 2)'],
           's_cad'  : coefs['coef']['np.power(log_CAD, 2)'],
           's_aco'  : coefs['coef']['np.power(log_ACO, 2)'],
           's_pyc'  : coefs['coef']['np.power(log_PYC, 2)'],
           's_csc'  : coefs['coef']['np.power(log_CSC, 2)'],
           's_acdh' : coefs['coef']['np.power(log_ACDH, 2)'],
           'i_cad'  : coefs['coef']['log_ITE:log_CAD'],
           'i_aco'  : coefs['coef']['log_ITE:log_ACO'],
           'i_pyc'  : coefs['coef']['log_ITE:log_PYC'],
           'i_csc'  : coefs['coef']['log_ITE:log_CSC'],    
           'i_acdh' : coefs['coef']['log_ITE:log_ACDH'],
           'c_aco'  : coefs['coef']['log_CAD:log_ACO'],
           'c_pyc'  : coefs['coef']['log_CAD:log_PYC'],
           'c_csc'  : coefs['coef']['log_CAD:log_CSC'],
           'c_acdh' : coefs['coef']['log_CAD:log_ACDH'],
           'a_pyc'  : coefs['coef']['log_ACO:log_PYC'],
           'a_csc'  : coefs['coef']['log_ACO:log_CSC'],
           'a_acdh' : coefs['coef']['log_ACO:log_ACDH'],
           'p_csc'  : coefs['coef']['log_PYC:log_CSC'],
           'p_acdh' : coefs['coef']['log_PYC:log_ACDH'],
           'cs_acdh': coefs['coef']['log_CSC:log_ACDH'],
           'intercept' : coefs['coef']['Intercept']}

    F1 = ite*coD['ite']+cad*coD['cad']+aco*coD['aco']
    F2 = pyc*coD['pyc']+csc*coD['csc']+acdh*coD['acdh']
    S1 = ite*ite*coD['s_ite']+cad*cad*coD['s_cad']+aco*aco*coD['s_aco']
    S2 = pyc*pyc*coD['s_pyc']+csc*csc*coD['s_csc']+acdh*acdh*coD['s_acdh']
    C1 = ite*cad*coD['i_cad']+ite*aco*coD['i_aco']+ite*pyc*coD['i_pyc']
    C2 = ite*csc*coD['i_csc']+ite*acdh*coD['i_acdh']+cad*aco*coD['c_aco']
    C3 = cad*pyc*coD['c_pyc']+cad*csc*coD['c_csc']+cad*acdh*coD['c_acdh']
    C4 = aco*pyc*coD['a_pyc']+aco*csc*coD['a_csc']+aco*acdh*coD['a_acdh']
    C5 = pyc*csc*coD['p_csc']+pyc*acdh*coD['p_acdh']+csc*acdh*coD['cs_acdh']

    Z =  coD['intercept'] + F1 + F2 + S1 + S2 + C1 + C2 + C3 + C4 + C5

    return Z

def linear_model(x, y, X, Y, coefs, f_v):

    ite = f_v["ITE"]
    cad = f_v["CAD"]
    aco = f_v["ACO"]
    pyc = f_v["PYC"]
    csc = f_v["CSC"]
    acdh = f_v["ACDH"]

    if x is "log_ITE" :
        ite = X
    if x is "log_CAD" :
        cad = X
    if x is "log_ACO" :
        aco = X
    if x is "log_PYC" :
        pyc = X
    if x is "log_CSC" :
        csc = X
    if x is "log_ACDH":
        acdh = X
    if y is "log_ITE" :
        ite = Y
    if y is "log_CAD" :
        cad = Y
    if y is "log_ACO" :
        aco = Y
    if y is "log_PYC" :
        pyc = Y
    if y is "log_CSC" :
        csc = Y
    if y is "log_ACDH":
        acdh = Y

    coD = {'ite'    : coefs['coef']['log_ITE'],
           'cad'    : coefs['coef']['log_CAD'],
           'aco'    : coefs['coef']['log_ACO'],
           'pyc'    : coefs['coef']['log_PYC'],
           'csc'    : coefs['coef']['log_CSC'],
           'acdh'   : coefs['coef']['log_ACDH'],
           'intercept' : coefs['coef']['Intercept']}

    F1 = ite*coD['ite']+cad*coD['cad']+aco*coD['aco']
    F2 = pyc*coD['pyc']+csc*coD['csc']+acdh*coD['acdh']

    Z =  coD['intercept'] + F1 + F2

    return Z
    
def second_order_nosquare_model(x, y, X, Y, coefs, f_v):

    ite = f_v["ITE"]
    cad = f_v["CAD"]
    aco = f_v["ACO"]
    pyc = f_v["PYC"]
    csc = f_v["CSC"]
    acdh = f_v["ACDH"]

    if x is "log_ITE" :
        ite = X
    if x is "log_CAD" :
        cad = X
    if x is "log_ACO" :
        aco = X
    if x is "log_PYC" :
        pyc = X
    if x is "log_CSC" :
        csc = X
    if x is "log_ACDH":
        acdh = X
    if y is "log_ITE" :
        ite = Y
    if y is "log_CAD" :
        cad = Y
    if y is "log_ACO" :
        aco = Y
    if y is "log_PYC" :
        pyc = Y
    if y is "log_CSC" :
        csc = Y
    if y is "log_ACDH":
        acdh = Y


    coD = {'ite'    : coefs['coef']['log_ITE'],
           'cad'    : coefs['coef']['log_CAD'],
           'aco'    : coefs['coef']['log_ACO'],
           'pyc'    : coefs['coef']['log_PYC'],
           'csc'    : coefs['coef']['log_CSC'],
           'acdh'   : coefs['coef']['log_ACDH'],
           'i_cad'  : coefs['coef']['log_ITE:log_CAD'],
           'i_aco'  : coefs['coef']['log_ITE:log_ACO'],
           'i_pyc'  : coefs['coef']['log_ITE:log_PYC'],
           'i_csc'  : coefs['coef']['log_ITE:log_CSC'],    
           'i_acdh' : coefs['coef']['log_ITE:log_ACDH'],
           'c_aco'  : coefs['coef']['log_CAD:log_ACO'],
           'c_pyc'  : coefs['coef']['log_CAD:log_PYC'],
           'c_csc'  : coefs['coef']['log_CAD:log_CSC'],
           'c_acdh' : coefs['coef']['log_CAD:log_ACDH'],
           'a_pyc'  : coefs['coef']['log_ACO:log_PYC'],
           'a_csc'  : coefs['coef']['log_ACO:log_CSC'],
           'a_acdh' : coefs['coef']['log_ACO:log_ACDH'],
           'p_csc'  : coefs['coef']['log_PYC:log_CSC'],
           'p_acdh' : coefs['coef']['log_PYC:log_ACDH'],
           'cs_acdh': coefs['coef']['log_CSC:log_ACDH'],
           'intercept' : coefs['coef']['Intercept']}

    F1 = ite*coD['ite']+cad*coD['cad']+aco*coD['aco']
    F2 = pyc*coD['pyc']+csc*coD['csc']+acdh*coD['acdh']
    C1 = ite*cad*coD['i_cad']+ite*aco*coD['i_aco']+ite*pyc*coD['i_pyc']
    C2 = ite*csc*coD['i_csc']+ite*acdh*coD['i_acdh']+cad*aco*coD['c_aco']
    C3 = cad*pyc*coD['c_pyc']+cad*csc*coD['c_csc']+cad*acdh*coD['c_acdh']
    C4 = aco*pyc*coD['a_pyc']+aco*csc*coD['a_csc']+aco*acdh*coD['a_acdh']
    C5 = pyc*csc*coD['p_csc']+pyc*acdh*coD['p_acdh']+csc*acdh*coD['cs_acdh']

    Z =  coD['intercept'] + F1 + F2 + C1 + C2 + C3 + C4 + C5

    return Z