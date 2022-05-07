import ProjectileDrop as pd

print("bez vjetra")
pd1 = pd.ProjectileDrop(2000, 200, 0.01)
pd1.meta(5000, 400)
print("s vjetrom")
pd2 = pd.ProjectileDrop(2000, 200, 0.01)
pd2.meta(5000, 400, -5)