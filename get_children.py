stage_ref = omni.usd.get_context().get_stage()

prim_ref = stage_ref.GetPrimAtPath('/World/Xform')
children_refs = prim_ref.GetChildren()

for prim_ref in children_refs:
    print(prim_ref.GetPath())
