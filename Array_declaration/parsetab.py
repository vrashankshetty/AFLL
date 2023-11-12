
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMA DTYPE ID LEFTBRACE RIGHTBRACE SEMICOLON\n    declaration : DTYPE LEFTBRACE multiple RIGHTBRACE list SEMICOLON     \n    \n     list : ID COMMA list \n          | ID\n     \n    multiple : COMMA multiple\n             | \n    '
    
_lr_action_items = {'DTYPE':([0,],[2,]),'$end':([1,10,],[0,-1,]),'LEFTBRACE':([2,],[3,]),'COMMA':([3,5,9,],[5,5,11,]),'RIGHTBRACE':([3,4,5,7,],[-5,6,-5,-4,]),'ID':([6,11,],[9,9,]),'SEMICOLON':([8,9,12,],[10,-3,-2,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'declaration':([0,],[1,]),'multiple':([3,5,],[4,7,]),'list':([6,11,],[8,12,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> declaration","S'",1,None,None,None),
  ('declaration -> DTYPE LEFTBRACE multiple RIGHTBRACE list SEMICOLON','declaration',6,'p_declaration','parser.py',9),
  ('list -> ID COMMA list','list',3,'p_list','parser.py',15),
  ('list -> ID','list',1,'p_list','parser.py',16),
  ('multiple -> COMMA multiple','multiple',2,'p_multiple','parser.py',25),
  ('multiple -> <empty>','multiple',0,'p_multiple','parser.py',26),
]