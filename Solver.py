from gurobipy import *


def solver(a, b, c, t):
    m = Model('LP')
    m.setParam('OutputFlag', 0)
    for i in range(len(c)):
        m.addVar(vtype=GRB.CONTINUOUS, name='x' + str(i))
    m.update()
    variables = m.getVars()
    linear_exp = LinExpr()
    for i in range(len(c)):
        linear_exp += c[i] * variables[i]
    if t == -1:
        m.setObjective(linear_exp, GRB.MINIMIZE)
    else:
        m.setObjective(linear_exp, GRB.MAXIMIZE)
    for i in range(len(b)):
        linear_exp = LinExpr()
        for j in range(len(c)):
            linear_exp += a[i][j] * variables[j]
        if t == 1:
            m.addConstr(linear_exp, GRB.LESS_EQUAL, b[i])
        else:
            m.addConstr(linear_exp, GRB.GREATER_EQUAL, b[i])
    m.update()
    m.optimize()
    result = []
    if m.status == GRB.OPTIMAL:
        x = m.getAttr('x', variables)
        for tmp in x:
            result.append(tmp)
    elif m.status == GRB.INFEASIBLE:
        return 'infeasible'
    elif m.status == GRB.UNBOUNDED:
        return 'unbounded'
    elif m.status == GRB.INF_OR_UNBD:
        return ['infeasible', 'unbounded']
    return result, m.objVal
