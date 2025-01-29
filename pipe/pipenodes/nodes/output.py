from qtpy.QtWidgets import QLabel, QHBoxLayout,QLineEdit
from qtpy.QtCore import Qt
from pipe.pipenodes.pipe_conf import register_node, OP_NODE_OUTPUT
from pipe.pipenodes.pipe_node_base import MainNode, MainGraphicsNode
from nodeeditor.node_content_widget import QDMNodeContentWidget
from nodeeditor.utils import dumpException


class CalcOutputContent(QDMNodeContentWidget):
    def initUI(self):
        self.box = QHBoxLayout(self)
        self.lbl = QLabel("PIPE", self)
        self.lbl.setAlignment(Qt.AlignCenter)
        self.edit = QLineEdit("OUT-PUT", self)
        self.edit.setAlignment(Qt.AlignCenter)
        self.edit.setObjectName(self.node.content_label_objname)

        self.box.addWidget(self.lbl)
        self.box.addWidget(self.edit)

    def serialize(self):
        res = super().serialize()
        res['value'] = self.edit.text()
        return res

    def deserialize(self, data, hashmap={}):
        res = super().deserialize(data, hashmap)
        try:
            value = data['value']
            self.edit.setText(value)
            return True & res
        except Exception as e:
            dumpException(e)
        return res

@register_node(OP_NODE_OUTPUT)
class CalcNode_Output(MainNode):
    icon = "regular/circle-check.svg"
    op_code = OP_NODE_OUTPUT
    op_title = "N O D E - E N D"
    content_label_objname = "calc_node_output"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1], outputs=[])

    def initInnerClasses(self):
        self.content = CalcOutputContent(self)
        self.grNode = MainGraphicsNode(self)

