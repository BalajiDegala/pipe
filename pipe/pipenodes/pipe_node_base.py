from qtpy.QtGui import QImage, QPixmap
from qtpy.QtCore import QRectF, Qt
from qtpy.QtWidgets import QLabel, QTextEdit, QVBoxLayout, QLineEdit, QFileDialog, QPushButton, QHBoxLayout

from nodeeditor.node_node import Node
from nodeeditor.node_content_widget import QDMNodeContentWidget
from nodeeditor.node_graphics_node import QDMGraphicsNode
from nodeeditor.node_socket import LEFT_CENTER, RIGHT_CENTER
from nodeeditor.utils import dumpException


class MainGraphicsNode(QDMGraphicsNode):
    def initSizes(self):
        super().initSizes()
        self.width = 400
        self.height = 80
        self.edge_roundness = 6
        self.edge_padding = 0
        self.title_horizontal_padding = 8
        self.title_vertical_padding = 10




class MainSmallGraphicsNode(QDMGraphicsNode):
    def initSizes(self):
        super().initSizes()
        self.width = 220
        self.height = 80
        self.edge_roundness = 6
        self.edge_padding = 0
        self.title_horizontal_padding = 8
        self.title_vertical_padding = 10





class MainNode(Node):
    icon = ""
    op_code = 0
    op_title = "Undefined"
    content_label = ""
    content_label_objname = "calc_node_bg"

    GraphicsNode_class = MainGraphicsNode

    def __init__(self, scene, inputs=[1], outputs=[1]):
        super().__init__(scene, self.__class__.op_title, inputs, outputs)

        self.value = None

        # it's really important to mark all nodes Dirty by default

    def initSettings(self):
        super().initSettings()
        self.socket_spacing = 26

        self.input_socket_position = LEFT_CENTER
        self.output_socket_position = RIGHT_CENTER


    def onInputChanged(self, socket=None):
        print("%s::__onInputChanged" % self.__class__.__name__)

    def serialize(self):
        res = super().serialize()
        res['op_code'] = self.__class__.op_code
        return res

    def deserialize(self, data, hashmap={}, restore_id=True):
        res = super().deserialize(data, hashmap, restore_id)
        print("Deserialized CalcNode '%s'" %
              self.__class__.__name__, "res:", res)
        return res


############################################################################

class DeptGraphicsNode(QDMGraphicsNode):
    def initSizes(self):
        super().initSizes()
        self.width = 200
        self.height = 300
        self.edge_roundness = 6
        self.edge_padding = 0
        self.title_horizontal_padding = 8
        self.title_vertical_padding = 10


class DeptContent(QDMNodeContentWidget):
    def initUI(self):
        box = QVBoxLayout(self)

        lbl1 = QLabel("Modeling", self)
        lbl2 = QLabel("Texturing", self)
        lbl3 = QLabel("Rigging", self)
        lbl4 = QLabel("Animation", self)
        lbl5 = QLabel("Layout", self)
        lbl6 = QLabel("lighting", self)
        lbl7 = QLabel("Integration", self)
        lbl8 = QLabel("Compositing", self)
        lbl9 = QLabel("Roto", self)
        lbl10 = QLabel("Paint", self)


        box.addWidget(lbl1)
        box.addWidget(lbl2)
        box.addWidget(lbl3)
        box.addWidget(lbl4)
        box.addWidget(lbl5)
        box.addWidget(lbl6)
        box.addWidget(lbl7)
        box.addWidget(lbl8)
        box.addWidget(lbl9)
        box.addWidget(lbl10)



class DeptNode(Node):
    icon = ""
    op_code = 0
    op_title = "Undefined"
    content_label = ""
    content_label_objname = "calc_node_bg"

    GraphicsNode_class = DeptGraphicsNode
    NodeContent_class = DeptContent

    def __init__(self, scene, inputs=[2], outputs=[1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1]):
        super().__init__(scene, self.__class__.op_title, inputs, outputs)

        self.value = None

        # it's really important to mark all nodes Dirty by default

    def initSettings(self):
        super().initSettings()
        self.socket_spacing = 26

        self.input_socket_position = LEFT_CENTER
        self.output_socket_position = RIGHT_CENTER

    def onInputChanged(self, socket=None):
        print("%s::__onInputChanged" % self.__class__.__name__)

    def serialize(self):
        res = super().serialize()
        res['op_code'] = self.__class__.op_code
        return res

    def deserialize(self, data, hashmap={}, restore_id=True):
        res = super().deserialize(data, hashmap, restore_id)
        print("Deserialized CalcNode '%s'" %
              self.__class__.__name__, "res:", res)
        return res


############################################################################


class DataGraphicsNode(QDMGraphicsNode):
    def initSizes(self):
        super().initSizes()
        self.width = 500
        self.height = 500
        self.edge_roundness = 6
        self.edge_padding = 0
        self.title_horizontal_padding = 8
        self.title_vertical_padding = 10


class DataNode(Node):
    icon = ""
    op_code = 0
    op_title = "Undefined"
    content_label = ""
    content_label_objname = "calc_node_input"

    GraphicsNode_class = DataGraphicsNode

    def __init__(self, scene, inputs=[1], outputs=[2,2]):
        super().__init__(scene, self.__class__.op_title, inputs, outputs)

        self.value = None

    def initSettings(self):
        super().initSettings()
        self.socket_spacing = 26

        self.input_socket_position = LEFT_CENTER
        self.output_socket_position = RIGHT_CENTER

    def onInputChanged(self, socket=None):
        print("%s::__onInputChanged" % self.__class__.__name__)

    def serialize(self):
        res = super().serialize()
        res['op_code'] = self.__class__.op_code
        return res

    def deserialize(self, data, hashmap={}, restore_id=True):
        res = super().deserialize(data, hashmap, restore_id)
        print("Deserialized CalcNode '%s'" %
              self.__class__.__name__, "res:", res)
        return res


############################################################################

class EntityGraphicsNode(QDMGraphicsNode):
    def initSizes(self):
        super().initSizes()
        self.width = 200
        self.height = 200
        self.edge_roundness = 6
        self.edge_padding = 0
        self.title_horizontal_padding = 8
        self.title_vertical_padding = 10




class DescriptionGraphicsNode(QDMGraphicsNode):
    def initSizes(self):
        super().initSizes()
        self.width = 400
        self.height = 210
        self.edge_roundness = 6
        self.edge_padding = 0
        self.title_horizontal_padding = 8
        self.title_vertical_padding = 10


class EntityNode(Node):
    icon = ""
    op_code = 0
    op_title = "Undefined"
    content_label = ""
    content_label_objname = "calc_node_bg"

    GraphicsNode_class = EntityGraphicsNode

    def __init__(self, scene, inputs=[1], outputs=[2,2]):
        super().__init__(scene, self.__class__.op_title, inputs, outputs)

        self.value = None

        # it's really important to mark all nodes Dirty by default

    def initSettings(self):
        super().initSettings()
        self.socket_spacing = 26

        self.input_socket_position = LEFT_CENTER
        self.output_socket_position = RIGHT_CENTER


    def onInputChanged(self, socket=None):
        print("%s::__onInputChanged" % self.__class__.__name__)

    def serialize(self):
        res = super().serialize()
        res['op_code'] = self.__class__.op_code
        return res

    def deserialize(self, data, hashmap={}, restore_id=True):
        res = super().deserialize(data, hashmap, restore_id)
        print("Deserialized CalcNode '%s'" %
              self.__class__.__name__, "res:", res)
        return res




############################################################################

class ImageGraphicsNode(QDMGraphicsNode):
    def initSizes(self):
        super().initSizes()
        self.width = 1150
        self.height = 850
        self.edge_roundness = 6
        self.edge_padding = 0
        self.title_horizontal_padding = 8
        self.title_vertical_padding = 10



class ImageNode(Node):
    icon = ""
    op_code = 0
    op_title = "Undefined"
    content_label = ""
    content_label_objname = "calc_node_bg"

    GraphicsNode_class = ImageGraphicsNode

    def __init__(self, scene, inputs=[1], outputs=[2,2]):
        super().__init__(scene, self.__class__.op_title, inputs, outputs)

        self.value = None

        # it's really important to mark all nodes Dirty by default

    def initSettings(self):
        super().initSettings()
        self.socket_spacing = 26

        self.input_socket_position = LEFT_CENTER
        self.output_socket_position = RIGHT_CENTER


    def onInputChanged(self, socket=None):
        print("%s::__onInputChanged" % self.__class__.__name__)

    def serialize(self):
        res = super().serialize()
        res['op_code'] = self.__class__.op_code
        return res

    def deserialize(self, data, hashmap={}, restore_id=True):
        res = super().deserialize(data, hashmap, restore_id)
        print("Deserialized CalcNode '%s'" %
              self.__class__.__name__, "res:", res)
        return res


############################################################################

class LogoGraphicsNode(QDMGraphicsNode):
    def initSizes(self):
        super().initSizes()
        self.width = 200
        self.height = 200
        self.edge_roundness = 6
        self.edge_padding = 0
        self.title_horizontal_padding = 8
        self.title_vertical_padding = 10

class DummyGraphicsNode(QDMGraphicsNode):
    def initSizes(self):
        super().initSizes()
        self.width = 100
        self.height = 20
        self.edge_roundness = 6
        self.edge_padding = 0
        self.title_horizontal_padding = 8
        self.title_vertical_padding = 10
