import randomwalk as rw
import matplotlib.pyplot as plt

particle_number = 1000
step_number = 1000
#------------------------
# Step 1 Testplt.ylim(-50,50)
# if you want to draw animation, input ani=True parameter in the last parameter
#------------------------
q1 = rw.RandomWalkDrawer(particle_number, step_number, ani=False)
q1.clear()
q1.action()
#------------------------
# For Report
#------------------------
# q1.drawStoredParticles()

# q2 = rw.RandomWalkAnalyzer(particle_number, step_number)
# q2.clear()
# q2.action()
# ------------------------
# Mean Std graph Test
# ------------------------
# q2.drawMeanVarGraph()
#------------------------
# Regresion Test
#------------------------
# q2.cal_reg_cor()
# q2.drawRegressionGraph()

#------------------------
# Step3 Test
#------------------------
# q3 = rw.RandomWalkDiffusionTester(particle_number, step_number)
# q3.action()
