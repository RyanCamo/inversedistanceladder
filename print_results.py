import pandas as pd
from chainconsumer import ChainConsumer

c = ChainConsumer()

# Prints the results from Table 1 in 2406.05049. Note that the r_s constraint is just returning the prior.
q = 'chains/[Cosmographic_q_rd] DES5YR SN + desi BAO_chain.pkl'
qj = 'chains/[Cosmographic_qj_rd] DES5YR SN + desi BAO_chain.pkl'
qjs = 'chains/[Cosmographic_qjs_rd] DES5YR SN + desi BAO_chain.pkl'
qjsl = 'chains/[Cosmographic2_qjsl_rd] DES5YR SN + desi BAO_chain.pkl'

paths = [q, qj, qjs, qjsl]
names = ['2nd order', '3rd order', '4th order', '5th order']
params = ['$M_B$', '$r_s$', '$H_0$', '$q_0$', '$s_0$', '$j_0$', '$l_0$']

for i, path in enumerate(paths):
    pkl = pd.read_pickle(path)
    df = pd.DataFrame(pkl['chain'])
    df.columns = params[:len(df.columns)]
    c.add_chain(df, shade_alpha=0.5, weights=pkl["weights"], shade_gradient=0.1, posterior=pkl["posterior"], name=names[i])
    
c.configure(statistics="cumulative", kde=[0,0, 0, 0])
c.analysis.get_latex_table(filename="results.txt", transpose=False)