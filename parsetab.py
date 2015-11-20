
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = 'C456957C64B5A329F9A3F6E1FEABBF75'
    
_lr_action_items = {'FUNCTION':([0,2,7,8,9,10,11,13,16,19,20,25,26,27,28,29,30,31,32,33,35,54,57,58,59,60,64,67,],[-3,12,-8,12,-5,-6,-2,12,-4,12,-12,12,12,12,-7,12,12,12,12,12,-13,12,-10,-9,-3,-11,12,-14,]),'OP_DIVIDE':([3,4,14,15,17,21,22,24,34,39,42,43,44,45,46,47,48,49,56,61,67,],[-21,-23,-20,-24,27,27,-20,27,27,-22,27,27,-18,27,-17,27,27,27,-25,-30,-14,]),'RETURN':([0,2,7,9,10,11,16,20,28,35,57,58,59,60,64,67,],[-3,8,-8,-5,-6,-2,-4,-12,-7,-13,-10,-9,-3,-11,8,-14,]),'SEMICOLON':([3,4,8,14,15,17,21,22,39,43,44,45,46,47,48,49,56,61,67,],[-21,-23,20,-20,-24,28,35,-20,-22,57,-18,-16,-17,-19,-15,58,-25,-30,-14,]),'OP_MINUS':([3,4,14,15,17,21,22,24,34,39,42,43,44,45,46,47,48,49,56,61,67,],[-21,-23,-20,-24,29,29,-20,29,29,-22,29,29,-18,-16,-17,29,-15,29,-25,-30,-14,]),'OP_TIMES':([3,4,14,15,17,21,22,24,34,39,42,43,44,45,46,47,48,49,56,61,67,],[-21,-23,-20,-24,30,30,-20,30,30,-22,30,30,-18,30,-17,30,30,30,-25,-30,-14,]),'OP_GT':([3,4,14,15,17,21,22,24,34,39,42,43,44,45,46,47,48,49,56,61,67,],[-21,-23,-20,-24,31,31,-20,31,31,-22,31,31,-18,-16,-17,None,-15,31,-25,-30,-14,]),'NUMBER':([0,2,7,8,9,10,11,13,16,19,20,25,26,27,28,29,30,31,32,33,35,54,57,58,59,60,64,67,],[-3,3,-8,3,-5,-6,-2,3,-4,3,-12,3,3,3,-7,3,3,3,3,3,-13,3,-10,-9,-3,-11,3,-14,]),'OP_PLUS':([3,4,14,15,17,21,22,24,34,39,42,43,44,45,46,47,48,49,56,61,67,],[-21,-23,-20,-24,32,32,-20,32,32,-22,32,32,-18,-16,-17,32,-15,32,-25,-30,-14,]),'LBRACKET':([50,51,],[59,59,]),'OP_EQUAL':([14,18,],[26,33,]),'WHILE':([0,2,7,9,10,11,16,20,28,35,57,58,59,60,64,67,],[-3,6,-8,-5,-6,-2,-4,-12,-7,-13,-10,-9,-3,-11,6,-14,]),'COMMA':([3,4,15,22,37,38,39,40,42,44,45,46,47,48,56,61,62,63,67,],[-21,-23,-24,-20,52,-34,-22,54,-29,-18,-16,-17,-19,-15,-25,-30,52,54,-14,]),'LPAREN':([0,2,6,7,8,9,10,11,12,13,14,16,19,20,22,25,26,27,28,29,30,31,32,33,35,54,57,58,59,60,64,67,],[-3,13,19,-8,13,-5,-6,-2,23,13,25,-4,13,-12,25,13,13,13,-7,13,13,13,13,13,-13,13,-10,-9,-3,-11,13,-14,]),'VAR':([0,2,7,9,10,11,16,20,28,35,57,58,59,60,64,67,],[-3,5,-8,-5,-6,-2,-4,-12,-7,-13,-10,-9,-3,-11,5,-14,]),'RPAREN':([3,4,15,22,24,34,36,37,38,39,40,41,42,44,45,46,47,48,53,55,56,61,62,63,65,66,67,],[-21,-23,-24,-20,39,50,51,-33,-34,-22,-28,56,-29,-18,-16,-17,-19,-15,-31,-26,-25,-30,-33,-28,-32,-27,-14,]),'RBRACKET':([7,9,10,11,16,20,28,35,57,58,59,60,64,67,],[-8,-5,-6,-2,-4,-12,-7,-13,-10,-9,-3,-11,67,-14,]),'ID':([0,2,5,7,8,9,10,11,13,16,19,20,23,25,26,27,28,29,30,31,32,33,35,52,54,57,58,59,60,64,67,],[-3,14,18,-8,22,-5,-6,-2,22,-4,22,-12,38,22,22,22,-7,22,22,22,22,22,-13,38,22,-10,-9,-3,-11,14,-14,]),'$end':([0,1,2,7,9,10,11,16,20,28,35,57,58,60,67,],[-3,0,-1,-8,-5,-6,-2,-4,-12,-7,-13,-10,-9,-11,-14,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'function_decl':([2,8,13,19,25,26,27,29,30,31,32,33,54,64,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'statements':([0,59,],[2,64,]),'parameters':([23,],[36,]),'argument':([25,54,],[40,63,]),'parameter':([23,52,],[37,62,]),'define_stmt':([2,64,],[9,9,]),'function_call':([2,8,13,19,25,26,27,29,30,31,32,33,54,64,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'assign_stmt':([2,64,],[10,10,]),'while_stmt':([2,64,],[16,16,]),'program':([0,],[1,]),'return_stmt':([2,64,],[7,7,]),'arguments':([25,],[41,]),'statement':([2,64,],[11,11,]),'arguments_rest':([40,63,],[55,66,]),'expression':([2,8,13,19,25,26,27,29,30,31,32,33,54,64,],[17,21,24,34,42,43,44,45,46,47,48,49,42,17,]),'parameters_rest':([37,62,],[53,65,]),'compound_statements':([50,51,],[60,61,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statements','program',1,'p_program','parser.py',7),
  ('statements -> statements statement','statements',2,'p_statements','parser.py',11),
  ('statements -> <empty>','statements',0,'p_statements_empty','parser.py',16),
  ('statement -> while_stmt','statement',1,'p_statement','parser.py',20),
  ('statement -> define_stmt','statement',1,'p_statement','parser.py',21),
  ('statement -> assign_stmt','statement',1,'p_statement','parser.py',22),
  ('statement -> expression SEMICOLON','statement',2,'p_statement','parser.py',23),
  ('statement -> return_stmt','statement',1,'p_statement','parser.py',24),
  ('define_stmt -> VAR ID OP_EQUAL expression SEMICOLON','define_stmt',5,'p_define','parser.py',29),
  ('assign_stmt -> ID OP_EQUAL expression SEMICOLON','assign_stmt',4,'p_assign','parser.py',33),
  ('while_stmt -> WHILE LPAREN expression RPAREN compound_statements','while_stmt',5,'p_while','parser.py',37),
  ('return_stmt -> RETURN SEMICOLON','return_stmt',2,'p_return_none','parser.py',41),
  ('return_stmt -> RETURN expression SEMICOLON','return_stmt',3,'p_return','parser.py',45),
  ('compound_statements -> LBRACKET statements RBRACKET','compound_statements',3,'p_compound_statements','parser.py',49),
  ('expression -> expression OP_PLUS expression','expression',3,'p_expression_bin_op','parser.py',53),
  ('expression -> expression OP_MINUS expression','expression',3,'p_expression_bin_op','parser.py',54),
  ('expression -> expression OP_TIMES expression','expression',3,'p_expression_bin_op','parser.py',55),
  ('expression -> expression OP_DIVIDE expression','expression',3,'p_expression_bin_op','parser.py',56),
  ('expression -> expression OP_GT expression','expression',3,'p_expression_bin_op','parser.py',57),
  ('expression -> ID','expression',1,'p_expression_id','parser.py',62),
  ('expression -> NUMBER','expression',1,'p_term_factor','parser.py',66),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_expr','parser.py',70),
  ('expression -> function_call','expression',1,'p_expression_func_call','parser.py',74),
  ('expression -> function_decl','expression',1,'p_expression_func_call','parser.py',75),
  ('function_call -> ID LPAREN arguments RPAREN','function_call',4,'p_func_call','parser.py',80),
  ('arguments -> argument arguments_rest','arguments',2,'p_arguments','parser.py',84),
  ('arguments_rest -> COMMA argument arguments_rest','arguments_rest',3,'p_arguments_rest','parser.py',88),
  ('arguments_rest -> <empty>','arguments_rest',0,'p_arguments_rest_empty','parser.py',92),
  ('argument -> expression','argument',1,'p_argument','parser.py',96),
  ('function_decl -> FUNCTION LPAREN parameters RPAREN compound_statements','function_decl',5,'p_func_decl','parser.py',100),
  ('parameters -> parameter parameters_rest','parameters',2,'p_parameters','parser.py',104),
  ('parameters_rest -> COMMA parameter parameters_rest','parameters_rest',3,'p_parameters_rest','parser.py',108),
  ('parameters_rest -> <empty>','parameters_rest',0,'p_parameters_rest_empty','parser.py',112),
  ('parameter -> ID','parameter',1,'p_parameter','parser.py',116),
]
