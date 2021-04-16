# Copyright (c) Rusted Studio
# Licensed under APGL-3.0 license. Read LiCENSE.txt for more info
#Developers:
# CertifiedRice - Lead Developer
# Rusted Studio - Development Studio

class varAssignNode:
    def __init__(self, var_name_tok, value_node):
        self.var_name_tok = var_name_tok
        self.value_node = value_node

        self.pos_start = self.var_name_tok.pos_start
        self.pos_end = self.value_node.pos_end
