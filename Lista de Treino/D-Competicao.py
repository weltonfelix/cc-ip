points_ph_A = int(input())
points_ph_L = int(input())
points_ph_P = int(input())
hours = int(input())

points_A = points_ph_A * hours
points_L = points_ph_L * hours
points_P = points_ph_P * hours

max_points_A_L = (points_A + points_L + abs(points_A - points_L)) / 2
max_points_AL_P = (max_points_A_L + points_P + abs(max_points_A_L - points_P)) / 2

print(int(max_points_AL_P))
