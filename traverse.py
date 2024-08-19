stage_ref = omni.usd.get_context().get_stage()

prim_refs = stage_ref.Traverse()

for prim_ref in prim_refs:
    print(prim_ref.GetPath())
