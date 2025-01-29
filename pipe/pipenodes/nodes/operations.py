from pipe.pipenodes.pipe_conf import register_node, OP_NODE_IMAGE, OP_NODE_ENTITY, OP_NODE_OBJECT, OP_NODE_DEPT
from pipe.pipenodes.pipe_node_base import MainNode, DeptNode, EntityNode, DataNode, ImageNode


@register_node(OP_NODE_DEPT)
class DEPT(DeptNode):
    icon = "regular/map.svg"
    op_code = OP_NODE_DEPT
    op_title = "D E P T"
    content_label = ""
    content_label_objname = "calc_node_div"
