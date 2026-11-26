import importlib.util,os,sys
ep=sys.argv[1]; d=f"../output/photos/{ep}"
s=importlib.util.spec_from_file_location('e',f"episodes/{ep}.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
for i,sc in enumerate(m.S):
  for k,p in enumerate(sc.get('photos',[])):
    f=f"{d}/{i:02d}_{k}.png"
    if m.GO in p and os.path.exists(f): os.remove(f); print("del",f)
