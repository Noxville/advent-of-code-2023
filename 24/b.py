import z3

from a import Hail

with open('big') as fin:
    hail = [Hail(e.strip()) for e in fin.readlines()]

solver = z3.Solver()
starting_x, starting_y, starting_z = z3.Real("starting_x"), z3.Real("starting_y"), z3.Real("starting_z")
velocity_x, velocity_y, velocity_z = z3.Real("velocity_x"), z3.Real("velocity_y"), z3.Real("velocity_z")

for idx, h in enumerate(hail):
    t = z3.Real(f"t_for_hail_idx_{idx}")
    solver.add(t > 0)
    solver.add(starting_x + (t * velocity_x) == h.x + (h.dx * t))
    solver.add(starting_y + (t * velocity_y) == h.y + (h.dy * t))
    solver.add(starting_z + (t * velocity_z) == h.z + (h.dz * t))

assert z3.sat == solver.check()
model = solver.model()
x, y, z = model.eval(starting_x), model.eval(starting_y), model.eval(starting_z)
sm = x.as_long() + y.as_long() + z.as_long()
print(sm)
