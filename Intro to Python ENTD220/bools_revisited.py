# The following uses functions for simulating logical circuits. Just like PEMDAS/BEDMAS
# logical expressions also have an order of operations. Their precedence is as follows:
# 1. NOT (HIGHEST)
# 2. AND
# 3. OR  (LOWEST)

# the "and" operator, also known as conjunction, requires all operands to be true simultaneously.
def log_and(op1,op2):
    return op1 and op2 #logical order of operations, gives "and" the 2nd highest precedent.

# the "or" operator, also known as disjunction, requires at least one operand to be true.
def log_or(op1,op2):
    return op1 or op2

# NOTE: NOT is a unary operator which negates the logical value of a boolean expression.
def log_negation (op):
    return not op

# NOTE: Because NOT is a unary operator, surrounding parentheses are needed to ensure the
# appropriate outcome; otherwise the statement below would have been evaluated as:
#                          (not op1) and op2
def log_nand(op1,op2): # NAND negates the outcomes of AND.
    return not(op1 and op2) # logical order of operations, gives "not" the highest precedence.

def log_nor(op1,op2): # NOR negates the outcomes of OR.
    return not(op1 or op2) # logical order of operations, gives "not" the highest precedence.

def log_xor(op1,op2): # XOR is true when one of the 2 operands are true - BUT NOT BOTH!
    excl_or = (op1 and not op2) or (not op1 and op2)
    return excl_or

# XNOR is true when both operands have the same logical value; equivalent to biconditional (iff)
def log_xnor(op1,op2):# XNOR is XOR's exact opposite.
    excl_nor = (op1 and op2) or (not op1 and not op2)
    return excl_nor

print("Values for 'and' ...")
print(log_and(True, True))
print(log_and(True, False))
print(log_and(False,True))
print(log_and(False, False))

print("Values for 'or' ...")
print(log_or(True, True))
print(log_or(True, False))
print(log_or(False,True))
print(log_or(False, False))

print("Values for 'nand' ...")
print(log_nand(True, True))
print(log_nand(True, False))
print(log_nand(False,True))
print(log_nand(False, False))

print("Values for 'nor' ...")
print(log_nor(True, True))
print(log_nor(True, False))
print(log_nor(False,True))
print(log_nor(False, False))

print("Values for 'xor' ...")
print(log_xor(True, True))
print(log_xor(True, False))
print(log_xor(False,True))
print(log_xor(False, False))

print("Values for 'xnor' ...")
print(log_xnor(True, True))
print(log_xnor(True, False))
print(log_xnor(False,True))
print(log_xnor(False, False))

print("Values for 'not' ...")
print(log_negation(True))
print(log_negation(False))