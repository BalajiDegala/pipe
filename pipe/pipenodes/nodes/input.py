from qtpy.QtWidgets import QLineEdit,QVBoxLayout ,QHBoxLayout, QTextEdit, QLabel,QCheckBox
from qtpy.QtCore import Qt
from qtpy.QtGui import QPixmap,QTransform,QMovie

from pipe.pipenodes.pipe_conf import register_node,OP_NODE_LOGO,OP_NODE_SUBINPUT, OP_NODE_DUMMY, OP_NODE_DES, OP_NODE_VIDEO,OP_NODE_INPUT, OP_NODE_OBJECT,OP_NODE_DATA, OP_NODE_ENTITY, OP_NODE_IMAGE
from pipe.pipenodes.pipe_node_base import MainNode,MainSmallGraphicsNode, MainGraphicsNode,DataNode,DataGraphicsNode, EntityGraphicsNode, DescriptionGraphicsNode , EntityNode,  ImageGraphicsNode, ImageNode,LogoGraphicsNode, DummyGraphicsNode
from nodeeditor.node_content_widget import QDMNodeContentWidget
from nodeeditor.utils import dumpException


class CalcInputContent(QDMNodeContentWidget):
    def initUI(self):
        self.edit = QLineEdit("IN-PUT", self)
        self.edit.setMinimumWidth(390)
        self.edit.setAlignment(Qt.AlignCenter)
        self.edit.setObjectName(self.node.content_label_objname)

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


@register_node(OP_NODE_INPUT)
class CalcNode_Input(MainNode):
    icon = "regular/file.svg"
    op_code = OP_NODE_INPUT
    op_title = "T I T L E"
    content_label_objname = "calc_node_input"

    def __init__(self, scene):
        super().__init__(scene, inputs=[], outputs=[3])
        self.eval()

    def initInnerClasses(self):
        self.content = CalcInputContent(self)
        self.grNode = MainGraphicsNode(self)


#########################################################################################################

class SubInputContent(QDMNodeContentWidget):
    def initUI(self):
        self.edit = QLineEdit("", self)
        self.edit.setMinimumWidth(390)
        self.edit.setAlignment(Qt.AlignCenter)
        self.edit.setObjectName(self.node.content_label_objname)

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


@register_node(OP_NODE_SUBINPUT)
class SubNode_Input(MainNode):
    icon = "regular/file.svg"
    op_code = OP_NODE_SUBINPUT
    op_title = "S U B T I T L E"
    content_label_objname = "calc_node_input"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1], outputs=[3])
        self.eval()

    def initInnerClasses(self):
        self.content = SubInputContent(self)
        self.grNode = MainGraphicsNode(self)


#########################################################################################################


class ObjectInputContent(QDMNodeContentWidget):
    def initUI(self):
        self.edit = QLineEdit("IN-PUT", self)
        self.edit.setMinimumWidth(200)
        self.edit.setAlignment(Qt.AlignCenter)
        self.edit.setObjectName(self.node.content_label_objname)

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


@register_node(OP_NODE_OBJECT)
class Object(MainNode):
    icon = "regular/circle-stop.svg"
    op_code = OP_NODE_OBJECT
    op_title = "O B J E C T"
    content_label_objname = "calc_node_input"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1], outputs=[3])
        self.eval()

    def initInnerClasses(self):
        self.content = ObjectInputContent(self)
        self.grNode = MainSmallGraphicsNode(self)


#########################################################################################################


class DataInputContent(QDMNodeContentWidget):
    def initUI(self):
        self.box = QVBoxLayout(self)

        self.lbl1 = QLineEdit("", self)
        self.lbl2 = QTextEdit(self)

        self.box.addWidget(self.lbl1)
        self.box.addWidget(self.lbl2)
    def serialize(self):
        res = super().serialize()
        res['value1'] = self.lbl1.text()
        res['value2'] = self.lbl2.toPlainText()
        return res

    def deserialize(self, data, hashmap={}):
        res = super().deserialize(data, hashmap)
        try:
            value1 = data['value1']
            value2 = data['value2']

            self.lbl1.setText(value1)
            self.lbl2.setText(value2)

            return True & res
        except Exception as e:
            dumpException(e)
        return res


@register_node(OP_NODE_DATA)
class DATA(DataNode):
    icon = "regular/message.svg"
    op_code = OP_NODE_DATA
    op_title = "D A T A"
    content_label = ""
    content_label_objname = "calc_node_bg"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1], outputs=[2])
        self.eval()

    def initInnerClasses(self):
        self.content = DataInputContent(self)
        self.grNode = DataGraphicsNode(self)


#########################################################################################################


class EntityInputContent(QDMNodeContentWidget):
    def initUI(self):
        self.box = QVBoxLayout(self)

        self.lbl1 = QLineEdit("", self)
        lb1f = self.lbl1.font()  
        lb1f.setPointSize(14)
        self.lbl1.setFont(lb1f) 
        self.lbl2 = QTextEdit(self)
        lb2f = self.lbl2.font()  
        lb2f.setPointSize(12)
        self.lbl2.setFont(lb2f) 

        self.box.addWidget(self.lbl1)
        self.box.addWidget(self.lbl2)

    def serialize(self):
        res = super().serialize()
        res['value1'] = self.lbl1.text()
        res['value2'] = self.lbl2.toPlainText()
        return res

    def deserialize(self, data, hashmap={}):
        res = super().deserialize(data, hashmap)
        try:
            value1 = data['value1']
            value2 = data['value2']

            self.lbl1.setText(value1)
            self.lbl2.setText(value2)

            return True & res
        except Exception as e:
            dumpException(e)
        return res


@register_node(OP_NODE_ENTITY)
class ENTITY(EntityNode):
    icon = "regular/message.svg"
    op_code = OP_NODE_ENTITY
    op_title = "E N T I T Y"
    content_label = ""
    content_label_objname = "calc_node_mul"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1], outputs=[2])
        self.eval()

    def initInnerClasses(self):
        self.content = EntityInputContent(self)
        self.grNode = EntityGraphicsNode(self)

#########################################################################################################

@register_node(OP_NODE_DES)
class ENTITY_LARGE(EntityNode):
    icon = "regular/message.svg"
    op_code = OP_NODE_DES
    op_title = "D E S C R I P T I O N "
    content_label = ""
    content_label_objname = "calc_node_mul"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1], outputs=[2])
        self.eval()

    def initInnerClasses(self):
        self.content = EntityInputContent(self)
        self.grNode = DescriptionGraphicsNode(self)


#########################################################################################################

class ImageInputContent(QDMNodeContentWidget):
    def initUI(self):
        self.boxV = QVBoxLayout()
        self.boxH = QHBoxLayout()
        self.check = QCheckBox(self)
        self.lbl = QLabel(self)        
        self.lbl.setAlignment(Qt.AlignCenter)
        self.text = QLineEdit('Upload image', self)
        self.text.resize(1024,100)
        self.pixmap = QPixmap()
        self.text.textChanged.connect(self.get_image_file)
        self.boxV.addWidget(self.lbl)
        self.boxH.addWidget(self.text)
        self.boxH.addWidget(self.check)
        self.boxV.addLayout(self.boxH)
        self.setLayout(self.boxV)

    def get_image_file(self):
        filename = self.text.text()
        self.pixmap.load(filename)
        if self.check.isChecked():
            self.pixmap = self.pixmap.scaled(1024, 720, Qt.KeepAspectRatio)
        self.lbl.setPixmap(self.pixmap)

    def serialize(self):
        res = super().serialize()
        res['value'] = self.text.text()
        res['check'] = self.check.isChecked()
        return res

    def deserialize(self, data, hashmap={}):
        res = super().deserialize(data, hashmap)
        try:
            value = data['value']
            check = data['check']

            self.text.setText(value)
            self.check.setChecked(check)
            self.get_image_file()
            return True & res
        except Exception as e:
            dumpException(e)
        return res

@register_node(OP_NODE_IMAGE)
class IMAGE(ImageNode):
    icon = "regular/image.svg"
    op_code = OP_NODE_IMAGE
    op_title = "I M A G E"
    content_label = ""
    content_label_objname = "calc_node_bg"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1], outputs=[2])

    def initInnerClasses(self):
        self.content = ImageInputContent(self)
        self.grNode = ImageGraphicsNode(self)

#########################################################################################################

class VideoInputContent(QDMNodeContentWidget):
    def initUI(self):
        self.boxV = QVBoxLayout()
        self.boxH = QHBoxLayout()
        self.lbl = QLabel(self)        
        self.lbl.setAlignment(Qt.AlignCenter)
        self.text = QLineEdit('Upload Video', self)
        self.text.resize(1024,100)
        self.text.textChanged.connect(self.get_video_file)
        self.boxV.addWidget(self.lbl)
        self.boxH.addWidget(self.text)
        self.boxV.addLayout(self.boxH)
        self.setLayout(self.boxV)

    def get_video_file(self):
        filename = self.text.text()
        self.movie = QMovie(filename)
        self.lbl.setMovie(self.movie)
        self.movie.start() 

    def serialize(self):
        res = super().serialize()
        res['value'] = self.text.text()
        return res

    def deserialize(self, data, hashmap={}):
        res = super().deserialize(data, hashmap)
        try:
            value = data['value']
            self.text.setText(value)
            self.get_video_file()
            return True & res
        except Exception as e:
            dumpException(e)
        return res

@register_node(OP_NODE_VIDEO)
class video(ImageNode):
    icon = "regular/image.svg"
    op_code = OP_NODE_VIDEO
    op_title = "V I D E O"
    content_label = ""
    content_label_objname = "calc_node_bg"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1], outputs=[2])

    def initInnerClasses(self):
        self.content = VideoInputContent(self)
        self.grNode = ImageGraphicsNode(self)
#########################################################################################################

class LogoInputContent(QDMNodeContentWidget):
    def initUI(self):
        self.box = QVBoxLayout(self)

        self.lbl = QLabel(self)
        self.lbl.setAlignment(Qt.AlignCenter)
        
        self.text = QLineEdit('Upload image', self)
        self.text.resize(175,150)
        self.text.textChanged.connect(self.get_image_file)

        self.box.addWidget(self.lbl)
        self.box.addWidget(self.text)

    def get_image_file(self):
        filename = self.text.text()
        pixmap = QPixmap(filename)
        pixmap = pixmap.scaled(150, 100, Qt.KeepAspectRatio)
        self.lbl.setPixmap(pixmap)

    def serialize(self):
        res = super().serialize()
        res['value'] = self.text.text()
        return res

    def deserialize(self, data, hashmap={}):
        res = super().deserialize(data, hashmap)
        try:
            value = data['value']

            self.text.setText(value)

            return True & res
        except Exception as e:
            dumpException(e)
        return res

@register_node(OP_NODE_LOGO)
class IMAGE(ImageNode):
    icon = "regular/image.svg"
    op_code = OP_NODE_LOGO
    op_title = "L O G O"
    content_label = ""
    content_label_objname = "calc_node_bg"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1], outputs=[2])
        self.eval()

    def initInnerClasses(self):
        self.content = LogoInputContent(self)
        self.grNode = LogoGraphicsNode(self)

class DummyInputContent(QDMNodeContentWidget):
    def initUI(self):
        self.boxV = QVBoxLayout()
        self.boxH = QHBoxLayout()
        self.lbl = QLabel(self)        
        self.lbl.setAlignment(Qt.AlignCenter)
        self.text = QLineEdit('Upload Video', self)
        self.text.resize(1024,100)
        self.text.textChanged.connect(self.get_video_file)
        self.boxV.addWidget(self.lbl)
        self.boxH.addWidget(self.text)
        self.boxV.addLayout(self.boxH)
        self.setLayout(self.boxV)

    def get_video_file(self):
        filename = self.text.text()
        self.movie = QMovie(filename)
        self.lbl.setMovie(self.movie)
        self.movie.start() 

    def serialize(self):
        res = super().serialize()
        res['value'] = self.text.text()
        return res

    def deserialize(self, data, hashmap={}):
        res = super().deserialize(data, hashmap)
        try:
            value = data['value']
            self.text.setText(value)
            self.get_video_file()
            return True & res
        except Exception as e:
            dumpException(e)
        return res

@register_node(OP_NODE_DUMMY)
class DUMMY(ImageNode):
    icon = "regular/image.svg"
    op_code = OP_NODE_DUMMY
    op_title = "D U M M Y"
    content_label = ""
    content_label_objname = "calc_node_bg"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1], outputs=[2])
        self.eval()

    def initInnerClasses(self):
        self.content = DummyInputContent(self)
        self.grNode = DummyGraphicsNode(self)

