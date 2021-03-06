
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftorxorleftandleft<>left+-left*/rightuminusand assign ellipsis else endfor endfun endif false for fun if not nr or say string then true var xor code : s  code : code ';' s  ciclo : for var '[' e ellipsis e ']' com_list ';' endfor  func : fun var '(' args ')' com_list ';' endfun  condicao : if e then com_list else com_list endif  comando : e\n                    | ciclo\n                    | condicao  comando : var assign e  comando : say e_list  s : func\n              | comando  e_list : e\n                   | e_list ',' e  n : nr\n              | '-' e  %prec uminus   n : e '+' e\n              | e '-' e\n              | e '*' e\n              | e '/' e\n              | e '<' e\n              | e '>' e  b : f\n              | e or e\n              | e and e\n              | e xor e  f : true  f : false  f : not f  e : var  e : '(' e ')'  e : b\n              | n\n              | string  e : var '(' e_list ')'\n              | var '(' ')'  com_list : comando\n                     | com_list ';' comando  var_list : var\n                     | var_list ',' var  args :\n                 | var_list "
    
_lr_action_items = {'fun':([0,23,],[5,5,]),'var':([0,5,7,11,15,16,19,23,25,26,29,30,31,32,33,34,35,36,37,45,59,60,61,70,71,72,73,74,80,81,85,],[6,24,28,28,40,28,28,6,28,28,28,28,28,28,28,28,28,28,28,62,28,28,6,6,76,28,6,6,6,6,6,]),'say':([0,23,61,70,73,74,80,81,85,],[11,11,11,11,11,11,11,11,11,]),'(':([0,6,7,11,16,19,23,24,25,26,28,29,30,31,32,33,34,35,36,37,59,60,61,70,72,73,74,80,81,85,],[7,26,7,7,7,7,7,45,7,7,26,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'string':([0,7,11,16,19,23,25,26,29,30,31,32,33,34,35,36,37,59,60,61,70,72,73,74,80,81,85,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'for':([0,23,61,70,73,74,80,81,85,],[15,15,15,15,15,15,15,15,15,]),'if':([0,23,61,70,73,74,80,81,85,],[16,16,16,16,16,16,16,16,16,]),'nr':([0,7,11,16,19,23,25,26,29,30,31,32,33,34,35,36,37,59,60,61,70,72,73,74,80,81,85,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'-':([0,6,7,8,11,12,13,14,16,17,18,19,20,21,23,25,26,27,28,29,30,31,32,33,34,35,36,37,39,41,42,43,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,65,66,67,70,72,73,74,77,80,81,85,],[19,-30,19,33,19,-32,-33,-34,19,-23,-15,19,-27,-28,19,19,19,33,-30,19,19,19,19,19,19,19,19,19,33,33,-16,-29,33,-36,-31,33,33,33,-17,-18,-19,-20,33,33,19,19,19,-35,33,33,19,19,19,19,33,19,19,19,]),'true':([0,7,11,16,19,22,23,25,26,29,30,31,32,33,34,35,36,37,59,60,61,70,72,73,74,80,81,85,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'false':([0,7,11,16,19,22,23,25,26,29,30,31,32,33,34,35,36,37,59,60,61,70,72,73,74,80,81,85,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'not':([0,7,11,16,19,22,23,25,26,29,30,31,32,33,34,35,36,37,59,60,61,70,72,73,74,80,81,85,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'$end':([1,2,3,4,6,8,9,10,12,13,14,17,18,20,21,28,38,39,42,43,44,46,48,49,50,51,52,53,54,55,56,57,58,65,66,82,83,86,],[0,-1,-11,-12,-30,-6,-7,-8,-32,-33,-34,-23,-15,-27,-28,-30,-10,-13,-16,-29,-2,-9,-36,-31,-24,-25,-26,-17,-18,-19,-20,-21,-22,-35,-14,-5,-4,-3,]),';':([1,2,3,4,6,8,9,10,12,13,14,17,18,20,21,28,38,39,42,43,44,46,48,49,50,51,52,53,54,55,56,57,58,65,66,68,69,75,78,79,82,83,84,86,],[23,-1,-11,-12,-30,-6,-7,-8,-32,-33,-34,-23,-15,-27,-28,-30,-10,-13,-16,-29,-2,-9,-36,-31,-24,-25,-26,-17,-18,-19,-20,-21,-22,-35,-14,74,-37,80,74,-38,-5,-4,85,-3,]),'assign':([6,],[25,]),'or':([6,8,12,13,14,17,18,20,21,27,28,39,41,42,43,46,48,49,50,51,52,53,54,55,56,57,58,65,66,67,77,],[-30,29,-32,-33,-34,-23,-15,-27,-28,29,-30,29,29,-16,-29,29,-36,-31,-24,-25,-26,-17,-18,-19,-20,-21,-22,-35,29,29,29,]),'and':([6,8,12,13,14,17,18,20,21,27,28,39,41,42,43,46,48,49,50,51,52,53,54,55,56,57,58,65,66,67,77,],[-30,30,-32,-33,-34,-23,-15,-27,-28,30,-30,30,30,-16,-29,30,-36,-31,30,-25,30,-17,-18,-19,-20,-21,-22,-35,30,30,30,]),'xor':([6,8,12,13,14,17,18,20,21,27,28,39,41,42,43,46,48,49,50,51,52,53,54,55,56,57,58,65,66,67,77,],[-30,31,-32,-33,-34,-23,-15,-27,-28,31,-30,31,31,-16,-29,31,-36,-31,-24,-25,-26,-17,-18,-19,-20,-21,-22,-35,31,31,31,]),'+':([6,8,12,13,14,17,18,20,21,27,28,39,41,42,43,46,48,49,50,51,52,53,54,55,56,57,58,65,66,67,77,],[-30,32,-32,-33,-34,-23,-15,-27,-28,32,-30,32,32,-16,-29,32,-36,-31,32,32,32,-17,-18,-19,-20,32,32,-35,32,32,32,]),'*':([6,8,12,13,14,17,18,20,21,27,28,39,41,42,43,46,48,49,50,51,52,53,54,55,56,57,58,65,66,67,77,],[-30,34,-32,-33,-34,-23,-15,-27,-28,34,-30,34,34,-16,-29,34,-36,-31,34,34,34,34,34,-19,-20,34,34,-35,34,34,34,]),'/':([6,8,12,13,14,17,18,20,21,27,28,39,41,42,43,46,48,49,50,51,52,53,54,55,56,57,58,65,66,67,77,],[-30,35,-32,-33,-34,-23,-15,-27,-28,35,-30,35,35,-16,-29,35,-36,-31,35,35,35,35,35,-19,-20,35,35,-35,35,35,35,]),'<':([6,8,12,13,14,17,18,20,21,27,28,39,41,42,43,46,48,49,50,51,52,53,54,55,56,57,58,65,66,67,77,],[-30,36,-32,-33,-34,-23,-15,-27,-28,36,-30,36,36,-16,-29,36,-36,-31,36,36,36,-17,-18,-19,-20,-21,-22,-35,36,36,36,]),'>':([6,8,12,13,14,17,18,20,21,27,28,39,41,42,43,46,48,49,50,51,52,53,54,55,56,57,58,65,66,67,77,],[-30,37,-32,-33,-34,-23,-15,-27,-28,37,-30,37,37,-16,-29,37,-36,-31,37,37,37,-17,-18,-19,-20,-21,-22,-35,37,37,37,]),'else':([6,8,9,10,12,13,14,17,18,20,21,28,38,39,42,43,46,48,49,50,51,52,53,54,55,56,57,58,65,66,68,69,79,82,86,],[-30,-6,-7,-8,-32,-33,-34,-23,-15,-27,-28,-30,-10,-13,-16,-29,-9,-36,-31,-24,-25,-26,-17,-18,-19,-20,-21,-22,-35,-14,73,-37,-38,-5,-3,]),'endif':([6,8,9,10,12,13,14,17,18,20,21,28,38,39,42,43,46,48,49,50,51,52,53,54,55,56,57,58,65,66,69,78,79,82,86,],[-30,-6,-7,-8,-32,-33,-34,-23,-15,-27,-28,-30,-10,-13,-16,-29,-9,-36,-31,-24,-25,-26,-17,-18,-19,-20,-21,-22,-35,-14,-37,82,-38,-5,-3,]),')':([12,13,14,17,18,20,21,26,27,28,39,42,43,45,47,48,49,50,51,52,53,54,55,56,57,58,62,63,64,65,66,76,],[-32,-33,-34,-23,-15,-27,-28,48,49,-30,-13,-16,-29,-41,65,-36,-31,-24,-25,-26,-17,-18,-19,-20,-21,-22,-39,70,-42,-35,-14,-40,]),',':([12,13,14,17,18,20,21,28,38,39,42,43,47,48,49,50,51,52,53,54,55,56,57,58,62,64,65,66,76,],[-32,-33,-34,-23,-15,-27,-28,-30,59,-13,-16,-29,59,-36,-31,-24,-25,-26,-17,-18,-19,-20,-21,-22,-39,71,-35,-14,-40,]),'then':([12,13,14,17,18,20,21,28,41,42,43,48,49,50,51,52,53,54,55,56,57,58,65,],[-32,-33,-34,-23,-15,-27,-28,-30,61,-16,-29,-36,-31,-24,-25,-26,-17,-18,-19,-20,-21,-22,-35,]),'ellipsis':([12,13,14,17,18,20,21,28,42,43,48,49,50,51,52,53,54,55,56,57,58,65,67,],[-32,-33,-34,-23,-15,-27,-28,-30,-16,-29,-36,-31,-24,-25,-26,-17,-18,-19,-20,-21,-22,-35,72,]),']':([12,13,14,17,18,20,21,28,42,43,48,49,50,51,52,53,54,55,56,57,58,65,77,],[-32,-33,-34,-23,-15,-27,-28,-30,-16,-29,-36,-31,-24,-25,-26,-17,-18,-19,-20,-21,-22,-35,81,]),'[':([40,],[60,]),'endfun':([80,],[83,]),'endfor':([85,],[86,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'code':([0,],[1,]),'s':([0,23,],[2,44,]),'func':([0,23,],[3,3,]),'comando':([0,23,61,70,73,74,80,81,85,],[4,4,69,69,69,79,79,69,79,]),'e':([0,7,11,16,19,23,25,26,29,30,31,32,33,34,35,36,37,59,60,61,70,72,73,74,80,81,85,],[8,27,39,41,42,8,46,39,50,51,52,53,54,55,56,57,58,66,67,8,8,77,8,8,8,8,8,]),'ciclo':([0,23,61,70,73,74,80,81,85,],[9,9,9,9,9,9,9,9,9,]),'condicao':([0,23,61,70,73,74,80,81,85,],[10,10,10,10,10,10,10,10,10,]),'b':([0,7,11,16,19,23,25,26,29,30,31,32,33,34,35,36,37,59,60,61,70,72,73,74,80,81,85,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'n':([0,7,11,16,19,23,25,26,29,30,31,32,33,34,35,36,37,59,60,61,70,72,73,74,80,81,85,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'f':([0,7,11,16,19,22,23,25,26,29,30,31,32,33,34,35,36,37,59,60,61,70,72,73,74,80,81,85,],[17,17,17,17,17,43,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'e_list':([11,26,],[38,47,]),'args':([45,],[63,]),'var_list':([45,],[64,]),'com_list':([61,70,73,81,],[68,75,78,84,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> code","S'",1,None,None,None),
  ('code -> s','code',1,'p_code1','logic_grammar.py',37),
  ('code -> code ; s','code',3,'p_code2','logic_grammar.py',41),
  ('ciclo -> for var [ e ellipsis e ] com_list ; endfor','ciclo',10,'p_ciclo','logic_grammar.py',46),
  ('func -> fun var ( args ) com_list ; endfun','func',8,'p_func','logic_grammar.py',54),
  ('condicao -> if e then com_list else com_list endif','condicao',7,'p_condicao','logic_grammar.py',62),
  ('comando -> e','comando',1,'p_comando1','logic_grammar.py',72),
  ('comando -> ciclo','comando',1,'p_comando1','logic_grammar.py',73),
  ('comando -> condicao','comando',1,'p_comando1','logic_grammar.py',74),
  ('comando -> var assign e','comando',3,'p_comando2','logic_grammar.py',78),
  ('comando -> say e_list','comando',2,'p_comando3','logic_grammar.py',82),
  ('s -> func','s',1,'p_s','logic_grammar.py',88),
  ('s -> comando','s',1,'p_s','logic_grammar.py',89),
  ('e_list -> e','e_list',1,'p_e_list','logic_grammar.py',95),
  ('e_list -> e_list , e','e_list',3,'p_e_list','logic_grammar.py',96),
  ('n -> nr','n',1,'p_n1','logic_grammar.py',104),
  ('n -> - e','n',2,'p_n1','logic_grammar.py',105),
  ('n -> e + e','n',3,'p_n2','logic_grammar.py',109),
  ('n -> e - e','n',3,'p_n2','logic_grammar.py',110),
  ('n -> e * e','n',3,'p_n2','logic_grammar.py',111),
  ('n -> e / e','n',3,'p_n2','logic_grammar.py',112),
  ('n -> e < e','n',3,'p_n2','logic_grammar.py',113),
  ('n -> e > e','n',3,'p_n2','logic_grammar.py',114),
  ('b -> f','b',1,'p_b1','logic_grammar.py',120),
  ('b -> e or e','b',3,'p_b1','logic_grammar.py',121),
  ('b -> e and e','b',3,'p_b1','logic_grammar.py',122),
  ('b -> e xor e','b',3,'p_b1','logic_grammar.py',123),
  ('f -> true','f',1,'p_f1','logic_grammar.py',132),
  ('f -> false','f',1,'p_f2','logic_grammar.py',136),
  ('f -> not f','f',2,'p_f3','logic_grammar.py',140),
  ('e -> var','e',1,'p_e1','logic_grammar.py',146),
  ('e -> ( e )','e',3,'p_e2','logic_grammar.py',150),
  ('e -> b','e',1,'p_e3','logic_grammar.py',154),
  ('e -> n','e',1,'p_e3','logic_grammar.py',155),
  ('e -> string','e',1,'p_e3','logic_grammar.py',156),
  ('e -> var ( e_list )','e',4,'p_e4','logic_grammar.py',160),
  ('e -> var ( )','e',3,'p_e4','logic_grammar.py',161),
  ('com_list -> comando','com_list',1,'p_com_list','logic_grammar.py',169),
  ('com_list -> com_list ; comando','com_list',3,'p_com_list','logic_grammar.py',170),
  ('var_list -> var','var_list',1,'p_var_list','logic_grammar.py',180),
  ('var_list -> var_list , var','var_list',3,'p_var_list','logic_grammar.py',181),
  ('args -> <empty>','args',0,'p_args','logic_grammar.py',191),
  ('args -> var_list','args',1,'p_args','logic_grammar.py',192),
]
