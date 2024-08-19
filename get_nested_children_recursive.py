stage_ref = omni.usd.get_context().get_stage()

def print_children_path(root_path):
    prim_ref = stage_ref.GetPrimAtPath(root_path)
    children_refs = prim_ref.GetChildren()

    if not children_refs:
        return
    
    for prim_ref in children_refs:
        print(prim_ref.GetPath())
        print_children_path(prim_ref.GetPath())

print_children_path('/World/Xform')


